from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_detection import Face_Detector
from attendance import Attendance
from developer import Developer

class Face_detection_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance system by face detection")
        
        img=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\viit.png")
        img=img.resize((500,130))            
        self.Photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.Photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        

        img2=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\facialrecognition.png")
        img2=img2.resize((500,130))            
        self.Photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.Photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        img3=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\u.jpg")
        img3=img3.resize((500,130))            
        self.Photoimg3=ImageTk.PhotoImage(img3)
    
        f_lbl=Label(self.root,image=self.Photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)
         
         #background image
        img4=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\bg.jpg")
        img4=img4.resize((1530,710))            
        self.Photoimg4=ImageTk.PhotoImage(img4)
    
        bg_img=Label(self.root,image=self.Photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #student button
        img5=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\gettyimages-1022573162.jpg")
        img5=img5.resize((220,220))            
        self.Photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.Photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=300,width=220,height=40)
        
        #Detect Face button
        img6=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\face_detector1.jpg")
        img6=img6.resize((220,220))            
        self.Photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.Photoimg6,cursor="hand2",command=self.face_detection)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_detection,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=300,width=220,height=40)
        
        #Attendance button
        img7=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\report.jpg")
        img7=img7.resize((220,220))            
        self.Photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.Photoimg7,cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=300,width=220,height=40)
        
        #help button
        img8=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\chat.jpg")
        img8=img8.resize((220,220))            
        self.Photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.Photoimg8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=300,width=220,height=40)
        
        #Train data button
        img9=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\Train.jpg")
        img9=img9.resize((220,220))            
        self.Photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.Photoimg9,cursor="hand2",command=self.train_data,)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=580,width=220,height=40)
        
        #photos button
        img10=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\opencv_face_reco_more_data.jpg")
        img10=img10.resize((220,220))            
        self.Photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.Photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=580,width=220,height=40)
        
        #Developer button
        img11=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\dev.jpg")
        img11=img11.resize((220,220))            
        self.Photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.Photoimg11,cursor="hand2",command=self.developer)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=580,width=220,height=40)
        
        #Exit button
        img12=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\exit.jpg")
        img12=img12.resize((220,220))            
        self.Photoimg12=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.Photoimg12,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")
    
        
 #========================functions buttons====================
  

    def student_details(self):          #function name
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)       #declaring class
    
    
    def train_data(self):          #function name
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)       #declaring class
 
    
    def face_detection(self):             #function name
        self.new_window=Toplevel(self.root)
        self.app=Face_Detector(self.new_window)       #declaring class
        
        
    def attendance(self):             #function name
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)       #declaring class
          
    def developer(self):             #function name
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)       #declaring class
                
    
    
 
 
 
 
 
 
 
 
 
 
 
if __name__=="__main__" :  
  root=Tk()
  obj=Face_detection_System(root)
 
  root.mainloop()



 