from tkinter import *
import tkinter.font as font
import cv2
import PIL
import turtle
from PIL import ImageTk
from vid_ext import check_vid
#import time

#class to capture and play videos
class vid_cap:
	def __init__(self,scr):
		#the tkinter screen 
		self.scr=scr

		self.ok=False
		# the video capture variable(video controller)
		self.video=cv2.VideoCapture(0)
		self.width=700
		self.height=500
		
		#create the video in thge storage
		self.fourcc=cv2.VideoWriter_fourcc(*'XVID')
		self.out=cv2.VideoWriter('output.avi',self.fourcc,10,(640,480))

		#create a canvas that can fit the camera feed
		self.canvas=Canvas(scr,width=self.width,height=self.height)
		self.canvas.grid(row=3,columnspan=2,padx=30)
		# self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)
		self.delay=1
		self.update()

	def update(self):
		ret,frame=self.video.read()
		if self.ok:
			self.out.write(frame)
		if ret:
			self.photo=ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
			self.canvas.create_image(0,0,image=self.photo,anchor=NW)
	
		self.scr.after(self.delay,self.update)

	def open_camera(self):
		self.ok=True
		print('camera open')
		print(self.ok)

	def close_cam(self):
		print('camera_close')
		self.ok=False
		self.video.release()
		self.out.release()





def main():
	#declaring screen
	scr=Tk()
	scr.geometry('900x634')
	scr.title('Morse Detector')

	#minute and second 
	minu='00'
	secu='00'

	#declaring font
	myf=font.Font(family='Courier',size=20,weight='bold')

	# #make increase true
	# def true(si):
	# 	print('true called')
	# 	si=True

	#make increase false
	

	#function for timer
	def incr(secu='00',minu='00'):
		with open('tf.txt','r') as tf:
			d=tf.read()
			print(d)
			#d=not d
		if not d=='kim':
			return None
		#time.sleep(0.1)
		if d=='kim':
			with open('tf.txt','r') as tf:
				d=tf.read()
			k=int(secu)
			secu=str(k+1)
			if secu=='60':
				secu='00'
				k=int(minu)
				minu=str(k+1)
			timer['text']=str(minu)+':'+secu
			scr.after(1000,lambda: incr(secu,minu))
		else:
			return 0

	def change():
		print('change called')
		with open('tf.txt','r') as tf:
			d=tf.read()
		if d=='jon':
			d='kim'
		with open('tf.txt','w') as tf:
			tf.write(str(d))
			vc.open_camera()
		print(d)
		incr()

	def ochange():
		print('change called')
		with open('tf.txt','r') as tf:
			d=tf.read()
			if d=='kim':
				d='jon'
		with open('tf.txt','w') as tf:
			tf.write(str(d))
		vc.close_cam()
		ans=check_vid('output.avi')
		print(ans)
		resu['text']=ans



	#start and stop button
	start=Button(scr,text='START',font=myf,width=5,height=1,bg='green',fg='white',command=change)
	#scr.bind('<Enter>',change)
	start.grid(row=0,column=0,padx=80,sticky='W',pady=40)
	end=Button(scr,text='END',font=myf,width=5,height=1,bg='red',fg='white',command=ochange)
	#scr.bind('<q>',ochange)
	end.grid(row=0,column=1,padx=80,pady=40,sticky='E')

	#the timer
	timer=Label(scr,text=minu+':'+secu,font=myf,fg='blue')
	timer.grid(row=1,columnspan=2)

	#the result
	resu=Label(scr,text="Keep the flashlight at the center for readable results" ,font=myf,fg='blue',width=55)
	resu.grid(row=2, columnspan=2,padx=10)

	# #the canvas for red box
	# redbox=Canvas(scr,width=300,height=300)
	# redbox.grid(row=4, columnspan=2)
	# #draw a turtle
	# draw=turtle.RawTurtle(redbox)
	# draw.pensize(10)
	# draw.penup()
	# #draw.goto(0,0)
	# draw.pendown()
	# draw.pencolor('red')
	# draw.fd(100)
	# draw.right(90)
	# draw.fd(100)
	# draw.right(90)
	# draw.fd(100)
	# draw.right(90)
	# draw.fd(100)

	#camera label
	vc=vid_cap(scr)
	cam=Label(scr,text=' ',height=10,width=30,bg='black')
	cam.grid(row=4,columnspan=2,padx=30,pady=100)

	#incr()
	
	scr.mainloop()


if __name__=='__main__':
	main()

