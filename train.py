from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance system by face detection")
        
        title_lbl=Label(self.root, text="TRAIN DATA SET", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\facialrecognition.png")
        img_top=img_top.resize((1530,280))            
        self.Photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(self.root,image=self.Photoimg_top)
        f_lbl.place(x=0,y=48,width=1530,height=280)
         
         
        #button
        b1_btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white",cursor="hand2")
        b1_btn.place(x=0,y=300,width=1530,height=60)
         
        
        
        img_bottom=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\opencv_face_reco_more_data.jpg")
        img_bottom=img_bottom.resize((1530,440))            
        self.Photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        
        f_lbl=Label(self.root,image=self.Photoimg_bottom)
        f_lbl.place(x=0,y=360,width=1530,height=440)
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')    #Gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        
        
        # ==============================Train the classifier and save================================
        
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!",parent=self.root)
        
        





if __name__=="__main__" :  
  root=Tk()
  obj=Train(root)
  root.mainloop()