from django.http import HttpResponse
import os
file_path=os.path.abspath(__file__)
pro_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro_dir_path)
def blue(request):
    return HttpResponse("<h3>WE ARE IN THE AN END OF THE EART ERA</h3>")
def fun(request):
    file_addr=os.path.join(dir_path,"sam.html")
    fp=open(file_addr,"r")
    data=fp.read()
    return HttpResponse(data)