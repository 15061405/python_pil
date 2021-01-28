from PIL import Image
file = open("2.txt", 'w')
for i in range(1920):
	for j in range(1080):
		img_src = Image.open("test.png")
	    	img_src = img_src.convert('RGBA')
    		str_strlist = img_src.load()
    		data = str_strlist[i,j]
		file.write(str(data))
		file.write(",")
	file.write('\r\n')
img_src.close()


