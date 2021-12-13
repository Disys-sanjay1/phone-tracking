photos = {"cam":8,"whatsappimages":36,"canva":1,"screenshots":67}
photos["B612"]=14
photos["snapchat"]=9
photos["snapseed"]=7      
photos["handcamera"]=6
photos["potrait camera"]=12

print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)
