from django.shortcuts import render, redirect
from .models import File
from .form import Form
import os
from PIL import Image as pil_image
from pytesseract import pytesseract
from PyPDF2 import PdfReader 

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def index(request):
    form=Form()
    if request.method=='POST':
        form=Form(data=request.POST, files=request.FILES)
        current_directory = os.getcwd()
        if form.is_valid():
            form.save()
            obj=form.instance
            file=current_directory+str(obj.file.url).replace('/',"\\")
            prompt=obj.prompt
            if ".pdf" in file:
                reader = PdfReader(file)
                t_p=int(len(reader.pages))
                text=""
                for i in range(t_p):
                    page = reader.pages[i]
                    text = text+"\n"+page.extract_text()
                prompt=text+"\nfrom the above\n"+prompt
            else:
                img = pil_image.open(file)
                text = pytesseract.image_to_string(img) 
                prompt=text+"\n\nfrom the above\n"+prompt
            File.objects.all().delete()
            os.remove(file)
            return render(request,"index.html",{'form':form,"prompt":prompt})
    return render(request,'index.html',{'form':form})
        
