from PIL import Image,ImageDraw,ImageFont
from home.models import ImageModel
import os 
from django.core.files import File


def fix_pos(photo,c_text,w,h):
    pos = w,h
    photo.paste(c_text,pos,c_text)

dev = lambda x :int(x/2)

def watermark_image(input_path,text,img_name,opacity,no_watermark,size,quality) -> str:
    print('2 ------------------------------------*****-----------------')
    
    photo = Image.open(input_path)
    print('2 ==================error================')
    
    w,h = photo.size
    drawing = ImageDraw.Draw(photo)
    
    font = ImageFont.truetype('arial.ttf',int(h*0.01*size))
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
    
    path = f'static/media/temp/{img_name}'
    if photo.mode in ("RGBA", "P"):
       photo =photo.convert("RGB")
    photo.save(path,quality=quality)
    return path

def get_data(request):
    url = request.META['HTTP_HOST']
    url = f'http://{url}/' 
    
    text = request.POST.get('watermarkText')
    no_watermark = int(request.POST.get('noOfWatermark'))
    size = int(request.POST.get('size'))
    quality = int(request.POST.get('quality'))
    images = request.FILES.getlist('images')
    opacity = int(float(request.POST.get('opacity')))
    paths=[]
    for i in images:    
        print('1 ------------------------------------*****-----------------')
        image_model= ImageModel.objects.create(image=i,watermark_text=text)
        print('1 ==================error================')
        path = watermark_image(f'static/media/{image_model.image}',text,f'{image_model.uuid}.jpg',opacity,no_watermark,size,quality)
        filename = path.split('/')[-1]
        with open(path,'rb') as f:
            print('3 ------------------------------------*****-----------------')
            
            image_model.watermraked_image.save(filename,File(f))
            print('3 ==================error================')
            
        if request.user.is_authenticated:
            image_model.user =  request.user
        
        image_model.save()
        print('4 ------------------------------------*****-----------------')
        
        os.remove(f'static/media/temp/{filename}')
        print('4 ==================error================')
        path = f'{url}static/media/output/{filename}'
        paths.append(path)
    return paths