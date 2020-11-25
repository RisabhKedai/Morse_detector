# Importing all necessary libraries 
import cv2 
import PIL
from PIL import Image

# Read the video from specified path 
cam = cv2.VideoCapture("ilu.mp4") 

# frame 
currentframe = 0

# bdkbshdhfhjd
g=0


#the code chart

def check_vid(vid_loc):
	# frame 
	currentframe = 0

	# bdkbshdhfhjd
	g=0


	#the code chart
	cc={
	'.-':'a',
	'-...':'b',
	'-.-.':'c',
	'-..':'d',
	'.':'e',
	'..-.':'f',
	'--.':'g',
	'....':'h',
	'..':'i',
	'.---':'j',
	'-.-':'k',
	'.-..':'l',
	'--':'m',
	'-.':'n',
	'---':'o',
	'.--.':'p',
	'--.-':'q',
	'.-.':'r',
	'...':'s',
	'-':'t',
	'..-':'u',
	'...-':'v',
	'.--':'w',
	'-..-':'x',
	'-.--':'y',
	'--..':'z',
	'.----':'1',
	'..---':'2',
	'...--':'3',
	'....-':'4',
	'.....':'5',
	'-....':'6',
	'--...':'7',
	'---..':'8',
	'----.':'9',
	'-----':'0',
	'   ':' ',
	'':'',
	}

	cam=cv2.VideoCapture(vid_loc) 
	# defiing a fubction for checking white spots
	def check_spots(address):
		# list for the codes
		l=['']

		#check if it  is a single code or tge next character
		light=False
		dctr=0
		lctr=0
	
		# the string for code 
		sym=' '
	
		for img in address:
			print(img)
			image=cv2.imread(img,0)
			#creating a pil image from the frame
			pilimg=Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)).convert('L')
			ti=pilimg.load()
			found = False
			
			if img=='vidimg/278.jpg':
			#checking for a white spot
				for r in range(230,300): #was 630-700
					for c in range(201,300): #was 301-400
						#checking for dark and light spots
							ti[r,c]=0
				pilimg.show()
				g=1

			#  Checking for dark spots and light spots 
			for r in range(330,400): # original working with well lighted room 630 660 and not so well 630-700 and 530 700
				for c in range(201,300): # original working with well lighted room 401 440 and 401 500 and not so well 301 500
					#checking for dark and light spots
					if ti[r,c]>=250: #if light spot found
						found=True
						break
			if found:
				if light!=(ti[r,c]>=250): # if the spot volor changed from dark to light
					light=True
					# dctr=0
					lctr+=1
					sym=''  # symbol has been added so erasing the old one
				else:   #if light spots are cntinuing
					lctr+=1
			
			else:  #if dark is the spot
				if light!=(ti[r,c]>=200): #if the spot color changed from light to dark
					print("lctr"+str(lctr))
					#deciding the symbol
					if 3<=lctr and lctr<=20: #was 3-10
						sym='.'
					elif 20<=lctr and lctr<=40: #was 13-25
						sym='-'
					#adding the symbol
					print("dctr"+str(dctr))
					print("added a {}".format(sym))
					if 0<=dctr and dctr<=15:
						#symbol willbe added  the last string in the list
						# if not l:
						# 	l=['',]
						l[-1]+=sym
					elif 15<=dctr:#and dctr<=15: #was 10<=dctr
						#symbol will be added to the new string
						if dctr>=50: #was 25
							l.append('   ')
							l.append(sym)
						else:
							l.append(sym)
					dctr=0
					light=False
					lctr=0
					dctr+=1
					sym=''
				else:
					dctr+=1
		return l

	# creating a list of addresses 
	address=[]		
	while(True): 
		# reading from frame 
		ret,frame = cam.read() 
		if ret: 
			# if video is still left continue creating images 
			name = 'vidimg/'+ str(currentframe+1) + '.jpg'
			#print(l)
			print ('Creating...' + name)
			address.append(name) 
		
		# if currentframe==200:
		# #checking for a white spot
		# 	for r in range(630,660):
		# 		for c in range(380,430):
		# 			#checking for dark and light spots
		# 				ti[r,c]=0
		# 		pilimg.show()
		# 		g=1

		# writing the extracted images 
			cv2.imwrite(name, frame) 

		# increasing counter so that it will 
		# show how many frames are created 
			currentframe += 1
		else: 
			break

# Release all space and windows once done 
	cam.release() 
	cv2.destroyAllWindows() 

	ans=check_spots(address)
	tbp=''
	for a in ans:
		try:
			tbp+=cc[a].upper()
		except KeyError:
			tbp+=''
	print(tbp.strip())
	print(ans)
	return tbp.strip()


print(check_vid('ilu.mp4'))
#print(len(l))



'''===================================Explanation of lines 32 - 59===================================================================================================================================================================================='''
'''
line 44:  for loop for row pixels 
line 45:  for loop for column pixels
line 47: checking if  a pixel is light
line 48: if yes then we founfd that the image is light signal
line 49: breaking so it is no more needed to checkall pixels. if light is not found then it will check all.
line 50: if found  light image then do limes 51 to 58 else 59 to   83
line 51: if it was a transition from dark to light
line 52: since light has come so change light from False to True
line 54: Increase the light image counter
line 55: symbol is made null  because while coming from dark to light a new symbol has to be formed so cleaniing the old ones
line 56: if light ws already there then just increase the light image counter
line 59: if the image is dark
line 82: if the images were already dark increase he dark counter
line 60: if the image changed from light to dark. then we need to form te d=symbol from the light image count
line 63: if the light image count(lctr) is 5 to 10 implies a dot so sym is a dot
line 65: if it is a 15 to 20 then it is a dash
line 70: if the dctr tells there were a few only darks then the dot or dash is added to the existing morse string
line 75: if it was more then add to a new string
line 78: since we decidedand added the symbol make dctr 0 for a new symbol
line 79-81: normalprocedure for light to dark transition 

All in all we keep a track of the dark counter whenever it turns to light images e=we dinot make the counter 0 rather start the light counter alse and clean the sym variable.
Then when again turns to dark again then we change the add the symbol and make the dark 0 for counting the new dark screens also we may clean the symbol after adding it to the list.
The list variable l is defined with an empty string so that the initial dctr is compatible with both small and big values. if the value is big it will start with anither string else add it to the empty string we already gave.
'''
'''==================================================================================================================================================================================================================================================='''




# Importing all necessary libraries 
# import cv2 
# import os 

# # Read the video from specified path 
# cam = cv2.VideoCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 

# try: 
	
# 	# creating a folder named data 
# 	if not os.path.exists('data'): 
# 		os.makedirs('data') 

# # if not created then raise error 
# except OSError: 
# 	print ('Error: Creating directory of data') 

# # frame 
# currentframe = 0

# while(True): 
	
# 	# reading from frame 
# 	ret,frame = cam.read() 

# 	if ret: 
# 		# if video is still left continue creating images 
# 		name = './data/frame' + str(currentframe) + '.jpg'
# 		print ('Creating...' + name) 

# 		# writing the extracted images 
# 		cv2.imwrite(name, frame) 

# 		# increasing counter so that it will 
# 		# show how many frames are created 
# 		currentframe += 1
# 	else: 
# 		break

# # Release all space and windows once done 
# cam.release() 
# cv2.destroyAllWindows() 
