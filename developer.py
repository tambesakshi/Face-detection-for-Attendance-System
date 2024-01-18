from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox 
import mysql.connector
import cv2

class Developer:
    def __init_(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\facialrecognition.png")
        img_top=img_top.resize((1530,280))            
        self.Photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(self.root,image=self.Photoimg_top)
        f_lbl.place(x=0,y=48,width=1530,height=280)

        #frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\facialrecognition.png")
        img_top1=img_top1.resize((1530,280))            
        self.Photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(main_frame,image=self.Photoimg_top)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Hello my name, sakshi",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a Developer",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=40)


         
        img3=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\iStock-182059956_18390_t12.jpg")
        img3=img3.resize((500,300))            
        self.Photoimg3=ImageTk.PhotoImage(img3)
    
        f_lbl=Label(main_frame,image=self.Photoimg3)
        f_lbl.place(x=0,y=210,width=500,height=300)










if __name__ == "_main_":
    root=Tk()
    obj=Developer(root)
    root.mainloop()