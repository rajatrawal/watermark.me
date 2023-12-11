# Watermark-Me: Django Image Watermarking Project

🌊 Welcome to Watermark-Me, a Django-based project that empowers users to effortlessly add watermarks to their images through a simple and interactive web interface. Dive in and make your images uniquely yours!

## Live Demo 🚀
Explore the live demo: [Watermark-Me Live Demo](https://watermark-me.onrender.com/)

## Preview
![index page](https://github.com/rajatrawal/watermark.me/assets/72153827/df8f0f6b-756c-4de0-826d-cfc33c50be3d)

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [API Documentation](#api-documentation)
- [Support](#support)

## Features 🎨
- **User-friendly Interface:** Intuitive web interface for adding watermarks to your images, designed with simplicity in mind.
- **Customization Options:** Tailor your watermarks with options like text, size, quality, opacity, and the number of watermarks.
- **Modern Frontend:** A visually appealing frontend crafted using HTML, CSS, JS, and Bootstrap for a seamless and responsive experience.
- **API Integration:** Seamlessly integrate the API for programmatically watermarking images.

### Tech Icons
![Django](https://img.shields.io/badge/Django-3.0-green.svg)
![HTML](https://img.shields.io/badge/HTML-5-blue.svg)
![CSS](https://img.shields.io/badge/CSS-3-orange.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4-purple.svg)

## Installation 🛠️

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rajatrawal/video-call-django.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd video-call-django
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access Watermark-Me:**
   Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to begin your watermarking journey!

## Usage 🖼️
1. **Access the Web Interface:** Open the user-friendly web interface.
2. **Choose Your Image:** Select the image file you want to watermark.
3. **Customize Your Watermark:** Personalize your watermark with options like text, size, quality, opacity, and the number of watermarks.
4. **Click "Watermark":** Effortlessly process your image by clicking the "Watermark" button.

## Contributing 🤝
🌟 We welcome contributions! Feel free to open issues or submit pull requests to help enhance the Watermark-Me experience.

## API Documentation 📘
To programmatically watermark images using the Watermark-Me API, refer to the Python example below:

```python
import requests
import urllib

# Example values
values = {
    "username": "YOUR_USERNAME",
    "key": "YOUR_API_KEY",
    "watermarkText": "WATERMARK_TEXT",
    "noOfWatermark": NO_OF_WATERMARK,
    "size": SIZE_OF_WATERMARK,
    "opacity": OPACITY_OF_WATERMARK,
    "quality": QUALITY_OF_IMAGE
}

url = "https://watermark-me.onrender.com/api/watermarkImage/"

files = {'images': open(r'YOUR_IMAGE_PATH', 'rb')}

# API request
r = requests.post(url, files=files, data=values)
data = r.json()

# Download watermarked images
for i in data:
    name = i.split('/')[-1]
    urllib.request.urlretrieve(i, name)
```

### Explanation of Fields

- **username:** Your username is `example@gmail.com` (Mandatory Field).
- **key:** Your API key is `ed9f7f84-0d2f-41ed-b1f5-4gc20e65c025`[Demo] (Mandatory Field).
- **watermarkText:** The watermark text will be printed on the image (Default = "watermark.me").
- **noOfWatermark:** The number of watermark texts on the image (An integer field, Default = 1, Min = 1, and Max = 5).
- **size:** Size of the watermark in % of height (An integer field, Default = 5, Min = 1, and Max = 100).
- **opacity:** Opacity of the watermark (An integer field, Default = 100, Min = 1, and Max = 100).
- **quality:** Quality of the watermarked image (An integer field, Default = 100, Min = 1, and Max = 100).

#### API Responses
- **200 Response [POST]:** List of file URLs (`['FILE_URL_1', 'FILE_URL_2', ...]`).
- **404 Response [GET]:** {'message': 'invalid request type'}.
- **404 Response [Invalid username or key]:** {'message': 'invalid user or API key'}.

To send multiple files, use the following format:
```python
files = [
    ('images', open(r'YOUR_IMAGE_PATH_1', 'rb')),
    ('images', open(r'YOUR_IMAGE_PATH_2', 'rb'))
]
```

## Support 🤔
If you encounter any issues or have questions, feel free to reach out to us through the [GitHub Issues](https://github.com/rajatrawal/video-call-django/issues) page.

Thank you for choosing Watermark-Me! 🌊 Happy watermarking!