#Created BY UJIKSTARK

#!/usr/bin/env/ python3
from PIL import Image
import os, sys
from termcolor import colored

print(colored(""" 
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
""","red"))     

os.chdir(os.path.expanduser("~"))

file_image = input("Folder Image : ") #input file image from user
wanna_size = int(input("Pixel Resolution : "))

print("You can type Quality from 1-100") 
quality = int(input("Quality : ")) 

for i in os.listdir(file_image):
	pic = Image.open(os.path.join(file_image, i)) #open file


def new_file(dir1): #make a dir
    try:
        if not os.path.exists(dir1):
            os.makedirs(dir1)
    except OSError:
        print('Error: Creating Directory. ' +  dir1)

 
list_dir = os.listdir(file_image)
new_file(file_image + '/result/')

def start():
	global pic
	count_image = 0
	for i in list_dir:
		if os.path.isfile(file_image+i):
			pic = Image.open(file_image+i)
			x, y = os.path.splitext(file_image + 'result/' + i)

			size = pic.size
							
			if size[0] > size[1]:
				print(colored("Horizontal","blue"))
				wei_ave = (wanna_size / float(size[0]))
				hei_size = int((float(pic.size[1]) * float(wei_ave)))
				ratio = float(wanna_size) / max(size)
				round_image= tuple([int(wanna_size) for a in size])
					
				pic = pic.resize((wanna_size, hei_size), Image.ANTIALIAS)
				result = Image.new("RGB", (wanna_size, hei_size))
				result.paste(pic, ((wanna_size - round_image[0]) // 2, (wanna_size - round_image[1]) // 2))	
				show = result.save(x + 'ujik.jpg', quality=quality)
				count_image += 1
				print(colored(f"Success!! {x+'ujik.jpg'}","green"))
			else:
				print(colored("Vertical","blue"))
				hei_ave = (wanna_size / float(size[1]))
				wei_size = int((float(pic.size[0]) * float(hei_ave)))
				ratio = float(wanna_size) / max(size)
				
				round_image= tuple([int(wanna_size) for a in size])
				pic = pic.resize((wei_size, wanna_size), Image.ANTIALIAS)
				result = Image.new("RGB", (wei_size, wanna_size))
				
				result.paste(pic, ((wanna_size - round_image[0]) // 2, (wanna_size - round_image[1]) // 2))	
				show = result.save(x + 'ujik.jpg', quality=quality)
				print(colored(f"Success!! {x+'ujik.jpg'}","green"))
				count_image += 1
	print(colored(f"\n{count_image} IMAGE RESIZED!!!\n","yellow"))		

if __name__ == "__main__":
	start()
