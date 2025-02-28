from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image

def home(request):
    return render(request, 'home.html')

def extract_text(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        file_path = fs.save(image.name, image)
        file_url = fs.url(file_path)

        # Open image and extract text
        img = Image.open(fs.path(file_path))
        extracted_text = pytesseract.image_to_string(img)

        return render(request, 'home.html', {'text': extracted_text, 'image_url': file_url})

    return render(request, 'home.html')
