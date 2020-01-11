from PIL import Image
import os

print(""" 
-------------------------
$ Created by Ujikstark 
$ ig: @ujikpoi
-------------------------
                '-.
      .---._     \ .--'
    /       `-..__)  ,-'
   |    0           /
    --.__,   .__.,`
     `-.___'._\_.'

""")     
file_image = input("Image : ") #input user
pic = Image.open('./image/'+ file_image) #open file

if pic.mode in ("RGBA", "P"):
    pic = pic.convert("RGB")

print("Pixel Image : " + str(pic.size)) #pixel image
print('-'*28)

width = int(input('Width : '))
height = int(input('Height : '))
quality = int(input('Quality : '))
pic_resize = pic.resize((width, height)) #resize picture
print("Resize Pixel to : " + str(pic_resize.size)) #pixel with resize

def new_file(dir1): #make a dir
    try:
        if not os.path.exists(dir1):
            os.makedirs(dir1)
    except OSError:
        print('Error: Creating Directory. ' +  dir1)
        

new_file('./result/')

name_image = input("Name of new picture : ") #input new name of the picture
print("Success!!", name_image)

pic_result = './result/' + name_image

result = pic_resize.save(pic_result, quality=quality) #save file with quality
pic1 = Image.open(pic_result)
print("Format File : " + pic1.format)


bytes1 = int(len(pic1.fp.read())) 
hasil = bytes1 / 1000 #convert to KiloBytes
print("Size File :", hasil, 'KB') 



