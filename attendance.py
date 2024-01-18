from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1530x790+0+0")
    self.root.title("Attendance system by face detection")

    img=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\smart-attendance.jpg")
    img=img.resize((800,200))            
    self.Photoimg=ImageTk.PhotoImage(img)
    
    f_lbl=Label(self.root,image=self.Photoimg)
    f_lbl.place(x=0,y=0,width=800,height=200)
        

    img2=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\iStock-182059956_18390_t12.jpg")
    img2=img2.resize((800,200))            
    self.Photoimg2=ImageTk.PhotoImage(img2)
    
    f_lbl=Label(self.root,image=self.Photoimg2)
    f_lbl.place(x=800,y=0,width=800,height=200)
        
    img4=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\bg.jpg")
    img4=img4.resize((1530,700))            
    self.Photoimg4=ImageTk.PhotoImage(img4)
    
    bg_img=Label(self.root,image=self.Photoimg4)
    bg_img.place(x=0,y=200,width=1530,height=700)
        
    title_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="green")
    title_lbl.place(x=0,y=0,width=1530,height=45)
        
    main_frame=Frame(bg_img,bd=2,bg="white")
    main_frame.place(x=5,y=55,width=1510,height=650)
        
    #left label frame
    Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("time new roman",12,"bold"))
    Left_frame.place(x=10,y=5,width=760,height=580)
        
    img_left=Image.open(r"C:\Users\madhu\Desktop\Attendance system\college_images\face-recognition.png")
    img_left=img_left.resize((760,130))            
    self.Photoimg_left=ImageTk.PhotoImage(img_left)
    
    f_lbl=Label(Left_frame,image=self.Photoimg_left)
    f_lbl.place(x=0,y=0,width=760,height=120)
        
    left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
    left_inside_frame.place(x=8,y=135,width=740,height=350)
        
    # Label and Entry
    #AttendanceID
    attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
    attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)
        
    attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
    attendanceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
    #roll
    rolllabel=Label(left_inside_frame,text="StudentID:",font=("comicsansns",13,"bold"),bg="white")
    rolllabel.grid(row=0,column=2,padx=10,sticky=W)
        
    atten_roll=ttk.Entry(left_inside_frame,width=20,font=("comicsansns",13,"bold"))
    atten_roll.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
        
    #name
    namelabel=Label(left_inside_frame,text="Name:",font=("comicsansns",13,"bold"),bg="white")
    namelabel.grid(row=1,column=0,padx=10,sticky=W)
        
    atten_name=ttk.Entry(left_inside_frame,width=20,font=("comicsansns",13,"bold"))
    atten_name.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        
    #department
    deplabel=Label(left_inside_frame,text="Department:",font=("comicsansns",13,"bold"),bg="white")
    deplabel.grid(row=1,column=2,padx=10,sticky=W)
        
    atten_dep=ttk.Entry(left_inside_frame,width=20,font=("comicsansns",13,"bold"))
    atten_dep.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        
    #time
    timelabel=Label(left_inside_frame,text="Time:",font=("comicsansns",13,"bold"),bg="white")
    timelabel.grid(row=2,column=0,padx=10,sticky=W)
        
    atten_time=ttk.Entry(left_inside_frame,width=20,font=("comicsansns",13,"bold"))
    atten_time.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
    #date
    datelabel=Label(left_inside_frame,text="Date:",font=("comicsansns",13,"bold"),bg="white")
    datelabel.grid(row=2,column=2,padx=10,sticky=W)
        
    atten_date=ttk.Entry(left_inside_frame,width=20,font=("comicsansns",13,"bold"))
    atten_date.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        
    #atttendance
    attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
    attendanceLabel.grid(row=3, column=0)
        
    self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold", state="readonly") 
    self.atten_status["values"]=("Status", "Present", "Absent")
    self.atten_status.grid (row=3, column=1, pady=8)
    self.atten_status.current(0)
        
    # button
    btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
    btn_frame.place(x=10,y=300,width=700,height=40)
        
    importcsv_btn=Button(btn_frame,text="Import csv",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17,cursor="hand2")
    importcsv_btn.grid(row=0,column=0)
        
    exportcsv_btn=Button(btn_frame,text="Export csv",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17,cursor="hand2")
    exportcsv_btn.grid(row=0,column=1)
        
    update_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17,cursor="hand2")
    update_btn.grid(row=0,column=2)
        
    Reset_btn=Button(btn_frame,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17,cursor="hand2")
    Reset_btn.grid(row=0,column=3)
        
        
        
        
        
        
        
        
    #right label frame
    Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
    Right_frame.place(x=780,y=5,width=750,height=580)
        
    table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
    table_frame.place(x=5,y=5,width=700,height=470)
        
        
        
        
     # scroll bar
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
    self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
      
    scroll_x.config(command=self.AttendanceReportTable.xview)
    scroll_y.config(command=self.AttendanceReportTable.yview)
      
    self.AttendanceReportTable.heading("id",text="Attendance ID")
    self.AttendanceReportTable.heading("roll",text="Roll")
    self.AttendanceReportTable.heading("name",text="Name")
    self.AttendanceReportTable.heading("department",text="Department")
    self.AttendanceReportTable.heading("time",text="Time")
    self.AttendanceReportTable.heading("date",text="Date")
    self.AttendanceReportTable.heading("attendance",text="Attendance")
      
    self.AttendanceReportTable["show"]="headings"
      
    self.AttendanceReportTable.column("id",width=100)
    self.AttendanceReportTable.column("roll",width=100)
    self.AttendanceReportTable.column("name",width=100)
    self.AttendanceReportTable.column("department",width=100)
    self.AttendanceReportTable.column("time",width=100)
    self.AttendanceReportTable.column("date",width=100)
    self.AttendanceReportTable.column("attendance",width=100)
      
    self.AttendanceReportTable.pack(fill=BOTH,expand=1)
    
    # =================fetch data=========================
    
    def fetchData(self,rows)
    
        
      
        
        
        
        





 
if __name__=="__main__" :  
  root=Tk()
  obj=Attendance(root)
  root.mainloop()       