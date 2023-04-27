from PIL import Image,ImageDraw,ImageFont
from home.models import ImageModel
import os 
from django.core.files import File
from django.conf import settings


def fix_pos(photo,c_text,w,h):
    pos = w,h
    photo.paste(c_text,pos,c_text)

dev = lambda x :int(x/2)

def watermark_image(input_path,text,img_name,opacity,no_watermark,size,quality) -> str:
    photo = Image.open(input_path)
    w,h = photo.size
    drawing = ImageDraw.Draw(photo)
    print(f'------------------{settings.STATIC_ROOT}/fonts/arial.ttf')
    try:
        path = f'{settings.STATIC_ROOT}/fonts/arial.ttf'
        print('run suceessfully')
        font = ImageFont.truetype(path, int(h * 0.01 * size))
    except:
        font = ImageFont.load_default()
        print('Error font not loaded')
    text_w , text_h = drawing.textsize(text,font)
    c_text = Image.new('RGB',(text_w,text_h),color="#000000")
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0,0),text,file='#ffff',font=font)
    c_text.putalpha(opacity)
    fix_pos(photo,c_text,w-text_w-20,h-text_h-20)
    if no_watermark >=2:
        fix_pos(photo,c_text,20,20)
    if no_watermark >=3:
        fix_pos(photo,c_text,w-text_w-20,20)
    if no_watermark >=4:
        fix_pos(photo,c_text,20,h-text_h-20)
    if no_watermark >=5:
        fix_pos(photo,c_text,dev(w)-dev(text_w),dev(h)-dev(text_h))

    path = f'media/temp/{img_name}'
    if photo.mode in ("RGBA", "P"):
       photo =photo.convert("RGB")
    photo.save(path,quality=quality)
    return path

def get_data(request):
    url = request.META['HTTP_HOST']
    url = f'https://{url}/' 
    
    text = request.POST.get('watermarkText')
    no_watermark = int(request.POST.get('noOfWatermark'))
    size = int(request.POST.get('size'))
    quality = int(request.POST.get('quality'))
    images = request.FILES.getlist('images')
    opacity = int(float(request.POST.get('opacity')))
    paths=[]
    for i in images:    

        image_model= ImageModel.objects.create(image=i,watermark_text=text)
  
        path = watermark_image(f'media/{image_model.image}',text,f'{image_model.uuid}.jpg',opacity,no_watermark,size,quality)
        filename = path.split('/')[-1]
        with open(path,'rb') as f:

            image_model.watermraked_image.save(filename,File(f))

            
        if request.user.is_authenticated:
            image_model.user =  request.user
        
        image_model.save()

        
        os.remove(f'media/temp/{filename}')

        path = f'{url}media/output/{filename}'
        paths.append(path)
    return paths