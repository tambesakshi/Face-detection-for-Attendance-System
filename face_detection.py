from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Detector:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance system by face detection")
        
        title_lbl=Label(self.root, text="FACE DETECTOR", font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_right=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\face_detector1.jpg")
        img_right=img_right.resize((650,700))            
        self.Photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(self.root,image=self.Photoimg_right)
        f_lbl.place(x=0,y=55,width=650,height=700)
         
         
        img_top=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_top=img_top.resize((950,700))            
        self.Photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.Photoimg_top)
        f_lbl.place(x=600,y=55,width=950,height=700)
        
        
        #button
        b1_btn=Button(f_lbl,text="Detect Face",command=self.face_recog,font=("times new roman",18,"bold"),bg="dark green",fg="white",cursor="hand2")
        b1_btn.place(x=365,y=620,width=200,height=40)
        
        
        # ===============attendance============================
    
    def mark_attendance(self,i,r,n,d):
        with open ("Sakshi.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
               
            
                
                
             
            
        
        # ================Face Detection====================
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                
            coord=[]    #list
                
            for(x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))   
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Sakshi@47",database="facerecogniser")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i is not None else ""

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r is not None else ""

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n is not None else ""

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d is not None else ""
                
                
                
                if confidence>88:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                    
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   
                
                coord=[x,y,w,h]
                
            return coord
        
           
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
       
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0)
        
        while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Detector",img)
            
                if cv2.waitKey(1) == 13:

                    break 
        video_cap.release()
        cv2.destroyAllWindows()
                   
        



if __name__=="__main__" :  
  root=Tk()
  obj=Face_Detector(root)
  root.mainloop()
         
         