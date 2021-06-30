import pyodbc
from tkinter.scrolledtext import ScrolledText
import smtplib
import openpyxl
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from tkinter import *
import pandas as pd
import tkinter as tk
from playsound import playsound
import pyrebase
from PIL import Image, ImageTk
import numpy as np
from tkinter import ttk
from tkinter import filedialog
import sqlite3
import cv2
from PIL import Image
import os
import xlsxwriter
from datetime import date
from datetime import datetime
from tkinter import messagebox
import sys
import random
import socket
from time import sleep
#=====================Create Database=============================================
def createdb():
    conn = sqlite3.connect('saveddata.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS present_record(Employe_name TEXT,Emp_department TEXT,Employee_id TEXT,Attendance_Status TEXT,Date_of_Mark TEXT,Time_of_Mark TEXT)");
    c.execute("CREATE TABLE IF NOT EXISTS employee(id integer unique primary key autoincrement, name TEXT, dept TEXT, Emailaddress TEXT, employee_id TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS all_record(id integer unique primary key autoincrement, employee_name TEXT, employee_id TEXT, employee_department, employee_status TEXT, attendance_date TEXT, attendance_time TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT , passs TEXT,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    c.execute("CREATE TABLE IF NOT EXISTS adminpassword (nameadmin TEXT , passadmin TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS absent_emp (Employee_Name TEXT, Employee_id TEXT,Emp_department TEXT, Emp_Status TEXT, Attendence_date TEXT,Attendence_time TEXT)")
    conn.commit()
    conn.close()
createdb()
#======================Adding new admin in database===============================
def saveadmin():
	name_err = name_entry.get()
	pass_err = pass_entry.get()
	if name_err == "":
		messagebox.showinfo("Invalid input","Username can't be Empty")
	elif pass_err == "":
		messagebox.showinfo("Invalid input","Password can't be Empty")
	else:
		conn=sqlite3.connect("saveddata.db")
		c=conn.cursor()
		c.execute("INSERT INTO adminpassword(nameadmin,passadmin) VALUES(?,?) ",(name_entry.get(),pass_entry.get()))
		conn.commit()
		messagebox.showinfo("Information","New User has been Added")
#========================FetchingdataofAdminfromdatabase==========================
def loggin():
	while True:
		a=name2_entry.get()
		b=pass2_entry.get()
		with sqlite3.connect("saveddata.db") as db:
			cursor=db.cursor()
		find_user= ("SELECT * FROM adminpassword WHERE nameadmin = ? AND passadmin = ?")
		cursor.execute(find_user,[(a),(b)])
		results=cursor.fetchall()
		if results:
			for i in results:
				window.destroy()
#==================Window2+CreateFrame+f1============Animation also================================================
				window2=Tk()
				window2.title('Admin Panel')
				f1=Frame(window2,bg="black")
				f2=Frame(window2,bg="grey12")
				f3=Frame(window2,bg="grey12")
				f4=Frame(window2,bg="grey12")
				f5=Frame(window2,bg="grey12")
				f6=Frame(window2,bg="grey12")
				f7=Frame(window2,bg="black")


				def swap(frame):
					frame.tkraise()
				for frame in(f1,f2,f3,f4,f5,f6,f7):
					frame.place(x=0,y=0,width=600,height=600)
				window2.geometry("600x600+350+120")
				window2.resizable(False, False)
				label3=Label(f1,text="Admin Panel",font=("arial",20,"bold"),bg="grey16",fg="white",relief=SUNKEN)
				label3.pack(side=TOP,fill=X)

				label4=Label(f2,text="Facial Recognition Attendance System",font=("arial",10,"bold"),bg="gold3",fg="black")
				label4.pack(side=BOTTOM,fill=X)
				statusbar=Label(f1,text="Facial Recognition Attendance System",font=("arial",8,"bold"),bg="grey16",fg="white",relief=SUNKEN,anchor=W)
				statusbar.pack(side=BOTTOM,fill=X)

				class AnimatedGIF(Label, object):
					def __init__(self, master, path, forever=True):
						self._master = master
						self._loc = 0
						self._forever = forever
						self._is_running = False
						im = Image.open(path)
						self._frames = []
						i = 0
						try:
							while True:
								photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
								self._frames.append(photoframe)
								i += 1
								im.seek(i)
						except EOFError: pass
						self._last_index = len(self._frames) - 1
						try:
							self._delay = im.info['duration']
						except:
							self._delay = 100
						self._callback_id = None
						super(AnimatedGIF, self).__init__(master, image=self._frames[0])
					def start_animation(self, frame=None):
						if self._is_running: return
						if frame is not None:
							self._loc = 0
							self.configure(image=self._frames[frame])
						self._master.after(self._delay, self._animate_GIF)
						self._is_running = True
					def stop_animation(self):
						if not self._is_running: return
						if self._callback_id is not None:
							self.after_cancel(self._callback_id)
							self._callback_id = None
						self._is_running = False
					def _animate_GIF(self):
						self._loc += 1
						self.configure(image=self._frames[self._loc])
						if self._loc == self._last_index:
							if self._forever:
								self._loc = 0
								self._callback_id = self._master.after(self._delay, self._animate_GIF)
							else:
								self._callback_id = None
								self._is_running = False
						else:
							self._callback_id = self._master.after(self._delay, self._animate_GIF)
					def pack(self, start_animation=True, **kwargs):
						if start_animation:
							self.start_animation()
						super(AnimatedGIF, self).pack(**kwargs)
					def grid(self, start_animation=True, **kwargs):
						if start_animation:
							self.start_animation()
						super(AnimatedGIF, self).grid(**kwargs)
					def place(self, start_animation=True, **kwargs):
						if start_animation:
							self.start_animation()
						super(AnimatedGIF, self).place(**kwargs)
					def pack_forget(self, **kwargs):
						self.stop_animation()
						super(AnimatedGIF, self).pack_forget(**kwargs)
					def grid_forget(self, **kwargs):
						self.stop_animation()
						super(AnimatedGIF, self).grid_forget(**kwargs)
					def place_forget(self, **kwargs):
						self.stop_animation()
						super(AnimatedGIF, self).place_forget(**kwargs)
				if __name__ == "__main__":
					l = AnimatedGIF(f1, "./Resources/8.gif")
					l.pack()
				
				label4=Label(f3,text="Facial Recognition Attendance System",font=("arial",10,"bold"),bg="gold3",fg="black")
				label4.pack(side=BOTTOM,fill=X)
				label3=Label(f6,text="Email Section",font=("arial",20,"bold"),bg="grey16",fg="white",relief=SUNKEN)
				label3.pack(side=TOP,fill=X)
				label4=Label(f6,text="Facial Recognition Attendance System",font=("arial",10,"bold"),bg="gold3",fg="black")
				label4.pack(side=BOTTOM,fill=X)
#================================Trian System===========================================================


				def trainsystem():
					recognizer = cv2.face.LBPHFaceRecognizer_create()
					path = 'dataset'
					if not os.path.exists('./recognizer'):
						os.makedirs('./recognizer')
					def getImagesWithID(path):
						imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
						faces = []
						IDs = []
						for imagePath in imagePaths:
							faceImg = Image.open(imagePath).convert('L')
							faceNp = np.array(faceImg,'uint8')
							ID = int(os.path.split(imagePath)[-1].split('.')[1])
							faces.append(faceNp)
							IDs.append(ID)
							cv2.imshow("training",faceNp)
							cv2.waitKey(10)
						return np.array(IDs), faces
					Ids, faces = getImagesWithID(path)
					recognizer.train(faces,Ids)
					recognizer.save('recognizer/trainingData.yml')
					statusbar['text']='System Trained....'
					cv2.destroyAllWindows()
#==============================Detector/Attendence======================================================

				def markattendance():
					if not os.path.exists('./Attendance'):
							os.makedirs('./Attendance')
					statusbar['text']='Attendance Marked....'
					conn = sqlite3.connect('saveddata.db')
					c = conn.cursor()
					fname = "recognizer/trainingData.yml"
					if not os.path.isfile(fname):
					  print("Please train the data first")
					  exit(0)
					face_cascade = cv2.CascadeClassifier('./Resources/haarcascade_frontalface_default.xml')
					cap = cv2.VideoCapture(0)
					recognizer = cv2.face.LBPHFaceRecognizer_create()
					recognizer.read(fname)
					while True: 
					  ret, img = cap.read()
					  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
					  for (x,y,w,h) in faces:
					    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
					    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
					    c.execute("select * from employee where id = (?);", (ids,))
					    result = c.fetchall()
					    name = result[0][1]
					    print(name)
					    rname=str(name)
					    if conf < 50:
					      cv2.putText(img, rname, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
					      cv2.putText(img,'Hit Enter if you are '+name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
					    else:
					      cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
					  cv2.imshow('Face Recognizer',img)
					  k = cv2.waitKey(30) & 0xff
					  if k == 13:
					  	id_new   = result[0][0]
					  	name_new = result[0][1]
					  	dept_new = result[0][2]
					  	cont_new = result[0][3]
					  	eid_new  = result[0][4]
					  	statos="Present"
					  	emp_record = [id_new, name_new,eid_new, dept_new]
					  	date_obj=datetime.now()
					  	date_now=date_obj.strftime("%Y-%m-%d")
					  	time_now=date_obj.strftime("%H:%M:%S")
					  	c.execute("CREATE TABLE IF NOT EXISTS present_record(Employe_name,Emp_department,Employee_id,Attendance_Status,Date_of_Mark TEXT, Time_of_Mark TEXT)");
					  	

					  	c.execute("SELECT * from present_record where Employe_name = (?) AND Date_of_Mark = CURRENT_DATE ;", (name_new,))
					  	rzlt = c.fetchall()
					  	print(rzlt)

					  	if len(rzlt) > 0:
					  		messagebox.showerror("Error", "Attendance Already Marked!")
					  	else:
						  	c.execute("SELECT attendance_date FROM all_record ORDER BY id DESC LIMIT 1;")
						  	last_record = c.fetchall()
						  	c.execute("SELECT * FROM all_record")
						  	i = c.fetchall()
						  	if len(i) == 0:
						  		c.execute("INSERT INTO all_record(employee_name, employee_id, employee_department) SELECT name, employee_id, dept FROM employee")
						  		c.execute("UPDATE all_record SET attendance_date = :attend_date WHERE attendance_date IS NULL", {'attend_date': date_now})
						  		conn.commit()
						  	elif last_record[0][0] == None or len(i) >0:
					  			try:
					  				last_record_dat = last_record[0][0]
					  				date_record = datetime.strptime(str(last_record_dat), '%Y-%m-%d').date()
					  			except ValueError as e:
					  				pass
						  		current_date = datetime.strptime(date_now, '%Y-%m-%d').date()									
					  			if date_record != current_date:
					  				c.execute("INSERT INTO all_record(employee_name, employee_id, employee_department) SELECT name, employee_id, dept FROM employee")

					  			if len(i) > 0:
					  				c.execute("SELECT * FROM all_record WHERE employee_id = (?)", (eid_new,))
					  				x = c.fetchall()
					  				if len(x) == 0:
					  					c.execute("INSERT INTO all_record(employee_name, employee_id, employee_department, attendance_date) VALUES (?,?,?,?)", (name_new, eid_new, dept_new,date_now))
					  			c.execute("INSERT INTO present_record(Employe_name,Emp_department,Employee_id,Attendance_Status,Date_of_Mark,Time_of_Mark) VALUES(?,?,?,?,?,?)",(name_new,dept_new,eid_new,statos,date_now,time_now))
					  			c.execute("UPDATE all_record SET employee_status = 'ABSENT' WHERE NOT employee_id = :emp_rec_id AND employee_status IS NULL", {'emp_rec_id': eid_new})
					  			c.execute("UPDATE all_record SET attendance_time  = 'N/A' WHERE NOT employee_id = :emp_rec_id AND attendance_time  IS NULL", {'emp_rec_id': eid_new})
					  			c.execute("UPDATE all_record SET attendance_date = :attend_date WHERE attendance_date IS NULL", {'attend_date': date_now})
					  			# c.execute("UPDATE all_record SET employee_status = 'PRESENT' WHERE employee_id = :emp_rec_id AND employee_status = 'ABSENT' OR employee_status IS NULL", {'emp_rec_id': id_emp})
					  			c.execute("UPDATE all_record SET employee_status = 'PRESENT' WHERE (employee_id = :emp_rec_id AND attendance_date = :attend_date) AND ((employee_status = 'ABSENT') OR (employee_status IS NULL))", {'emp_rec_id': eid_new, 'attend_date': date_now})
					  			# c.execute("UPDATE all_record SET employee_status = 'PRESENT' WHERE employee_id = :emp_rec_id AND attendance_date = :attend_time AND employee_status = 'ABSENT'", {'emp_rec_id': id_emp, 'attend_time': time_now})
					  			c.execute("UPDATE all_record SET attendance_time  = :attend_time WHERE employee_id = :emp_rec_id AND attendance_time = 'N/A' OR attendance_time IS NULL", {'emp_rec_id': eid_new, 'attend_time': time_now})
						  		messagebox.showinfo("Success", "Attendance of employee "+name_new+" is Marked Successfully!")
					  		
					  			try:
					  				date_object = datetime.now()
					  				date_now = date_object.strftime("%Y-%m-%d")
					  				time_now = date_object.strftime("%H:%M:%S")
					  				c.execute("SELECT Emailaddress from employee WHERE id =(?);", (ids,))
					  				receiver_email= c.fetchall()[0][0]
					  				c.execute("SELECT name from employee WHERE id =(?);", (ids,))
					  				receiver_name= c.fetchall()[0][0]
					  				sender_email = 'pydeveloper000@gmail.com'
					  				sender_password = 'fypproject'
					  				server = smtplib.SMTP('smtp.gmail.com', 587)
					  				server.ehlo()
					  				server.starttls()
					  				server.login(sender_email, sender_password)
					  				attendance_mail = "Hello There "+receiver_name+", Your Attendance is marked Successfully of the date "+date_now+" ."
					  				message = 'Subject: Attendance Marked \n{}'.format(attendance_mail)
					  				server.sendmail(sender_email,receiver_email,message)
					  				server.quit()
					  				messagebox.showinfo("Success", "Attendance Marked And Mail is Successfully Sent To The Employee")
					  			except:
					  				messagebox.showerror("Error", "Attendance Marked But Email Doesn't Sent Because Something Went Wrong")
					  	
					  	c.execute("SELECT * FROM present_record WHERE Date_of_Mark=CURRENT_DATE")
					  	final_result=c.fetchall()
					  	print(final_result)
					  	
					  	try :
					  		timee=str(date.today())
					  		df=pd.DataFrame(final_result, columns=['Name', 'Department', 'Employee_id','status','Date','Time'])
					  		datatoexcel = pd.ExcelWriter("./Attendance/Employee Attendance"+timee+".xlsx", engine='xlsxwriter')
					  		df.to_excel(datatoexcel, index= False, sheet_name = "Sheet1")
					  		worksheet = datatoexcel.sheets['Sheet1']
					  		worksheet.set_column('A:A', 20)
					  		worksheet.set_column('B:B', 20)
					  		worksheet.set_column('C:C', 25)
					  		worksheet.set_column('D:D', 20)
					  		worksheet.set_column('E:E', 20)
					  		worksheet.set_column('F:F', 20)
					  		#df.loc[stat, 'Status'] = 'present'
					  		datatoexcel.save()
					  	except Exception as e:
					  		messagebox.showerror("Error","Please Close the Excel File to save Record")
					  	playsound('./Resources/sound.mp3')
					  	break
					cap.release()
					conn.commit()
					conn.close()
					cv2.destroyAllWindows()

#================================Frame2 Add new employee=================================================================

				label5=Label(f2,text="Employee Management",font=("arial",20,"bold"),bg="gold3",fg="black")
				label5.pack(side=TOP,fill=X)

				label6=Label(f2,text="Name",font=("arial",13,"bold"),bg='grey12',fg='white')
				label6.place(x=170,y=90)
				entry6=StringVar()
				entry6=ttk.Entry(f2,textvariable=entry6)
				entry6.place(x=290,y=90)
				entry6.focus()

				label7=Label(f2,text="Department",font=("arial",13,"bold"),bg='grey12',fg='white')
				label7.place(x=170,y=120)
				entry7=StringVar()
				combo=ttk.Combobox(f2,textvariable=entry7,width=15,font=("arial",10,"bold"),state='readonly')
				combo['values']=("BSInformationTech","BSChemistry","BSPhysics","BSMathematics","B.EDHons","MAEnglish","BBA")
				combo.place(x=290,y=120)
				label8=Label(f2,text="Email address",font=("arial",13,"bold"),bg='grey12',fg='white')
				label8.place(x=170,y=170)
				entry8=StringVar()
				entry8=ttk.Entry(f2,textvariable=entry8)
				entry8.place(x=290,y=170)
				label8=Label(f2,text="Employee_id",font=("arial",13,"bold"),bg='grey12',fg='white')
				label8.place(x=170,y=210)
				entry9=ttk.Entry(f2,textvariable=entry8)
				entry9.place(x=290,y=210)
#===================Buttons in window2===========================================
				btn1w2=ttk.Button(f1,text="Manage Employee",command=lambda:swap(f2))
				btn1w2.place(x=440, y=60,width=150,height=30)

				btn2w2=ttk.Button(f1,text="Trian System",command=trainsystem)
				btn2w2.place(x=440, y=115,width=150,height=30)

				btn3w2=ttk.Button(f1,text="Mark Attendance",command=markattendance)
				btn3w2.place(x=440, y=170,width=150,height=30)
				def quit():
					window2.destroy()
				btn9w2=ttk.Button(f1,text="Exit",command=quit)
				btn9w2.place(x=440, y=500,width=150,height=30)
				btn11w2=ttk.Button(f1,text="Record",command=lambda:swap(f7))
				btn11w2.place(x=440, y=225,width=150,height=30)

				Label(f7, text="Employee Attendance", font=("Times New Roman", 20, 'bold'), bg="gold3", fg="black").pack(fill=X)
				Label(f7, text="Seach Employee By Entering Employee ID", font=("arial", 10, 'bold'), bg="black", fg="white").place(x=50, y=90)
	
				search_id = StringVar()
				search_box1 = ttk.Entry(f7, width=20, textvariable= search_id)
				search_box1.focus()
				search_box1.place(x=300, y=90)
				search_btn = ttk.Button(f7, text="Search By Id", command= lambda:search_by_id())
				search_btn.place(x=470, y=90, width=140, height=30)

				Label(f7, text="Seach Employee By Entering Date as YYYY-MM-DD", font=("Times New Roman", 10, 'bold'), bg="black", fg="white").place(x=5, y=150)
				search_date = StringVar()
				search_box2 = ttk.Entry(f7, width=20, textvariable= search_date)
				search_box2.focus()
				search_box2.place(x=300, y=150)
				search_btn_date = ttk.Button(f7, width=20, text="Search By Date", command= lambda:search_by_date())
				search_btn_date.place(x=470, y=150, width=140, height=30)

				tree_3rd = ttk.Treeview(f7)
				tree_3rd["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
				tree_3rd.column("#0", width=0, minwidth=0, stretch=tk.NO)
				tree_3rd.column("one", width=20, minwidth=20, stretch= tk.NO)
				tree_3rd.column("two", width=110, minwidth=110, stretch= tk.NO)
				tree_3rd.column("three", width=70, minwidth=70, stretch=tk.NO)
				tree_3rd.column("four", width=100, minwidth=100, stretch=tk.NO)
				tree_3rd.column("five", width=75, minwidth= 75, stretch=tk.NO)
				tree_3rd.column("six", width=100, minwidth=100, stretch=tk.NO)
				tree_3rd.column("seven", width=110, minwidth=110, stretch=tk.NO)

				tree_3rd.heading("#0",text="index", anchor= tk.W)
				tree_3rd.heading("one", text="ID", anchor=tk.W)
				tree_3rd.heading("two", text=" Name", anchor=tk.W)
				tree_3rd.heading("three", text=" ID", anchor=tk.W)
				tree_3rd.heading("four", text=" Department", anchor=tk.W)
				tree_3rd.heading("five", text=" Status", anchor=tk.W)
				tree_3rd.heading("six", text="Attendance Date", anchor=tk.W)
				tree_3rd.heading("seven", text="Attendance Time", anchor=tk.W)

				tree_3rd.place(x=0, y=200)
				
				xl_btn = ttk.Button(f7, width=20, text="Save to Xlsx", command= lambda:xlsx())
				xl_btn.place(x=25, y=450, width=130, height=30)

				pdf_btn = ttk.Button(f7, width=20, text="Save to PDF", command= lambda:pdf())
				pdf_btn.place(x=165, y=450, width=130, height=30)

				clear_btn = ttk.Button(f7, width=20, text="Clear All", command= lambda:clear())
				clear_btn.place(x=305, y=450, width=130, height=30)

				percent_btn = ttk.Button(f7, width=20, text="Calculate Percentage", command= lambda:percent())
				percent_btn.place(x=445, y=450, width=130, height=30)

				btn_back = ttk.Button(f7, text="Back", width=15, command = lambda:swap(f1))
				btn_back.place(x=5, y=50)
				label4=Label(f7,text="Facial Recognition Attendance System",font=("arial",10,"bold"),bg="gold3",fg="black")
				label4.pack(side=BOTTOM,fill=X)
				def xlsx():
					i = random.randint(0,1000)
					conn = sqlite3.connect("saveddata.db")
					c = conn.cursor()
					counter_data = len(tree_3rd.get_children())
					today = str(date.today())
					id_error = search_id.get()
					date_error = search_date.get()
					date_another_error = str(date_error)
					if counter_data != 0:
						if str(id_error) == '' and str(date_error) == '':
							messagebox.showerror("Error", "Please Insert Date Or Id")
						elif id_error !=0 or date_error !=0:
							if id_error !=0:
								id_search = str(search_id.get())
								c.execute("SELECT * FROM all_record WHERE employee_id = (?)", (id_search,))
								resultss_id=c.fetchall()
								if not os.path.exists('./Saved Employee Attendance Excel'):
									os.makedirs('./Saved Employee Attendance Excel')
								if len(resultss_id) !=0:
									try:
										j = str(i)
										data = pd.DataFrame(resultss_id, columns= ['ID','Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time'])
										datatoexcel = pd.ExcelWriter("Saved Employee Attendance Excel/Employee List "+today+"("+j+").xlsx", engine='xlsxwriter')
										data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
										worksheet = datatoexcel.sheets['Sheet']
										worksheet.set_column('A:A', 15)
										worksheet.set_column('B:B', 20)
										worksheet.set_column('C:C', 25)
										worksheet.set_column('D:D', 20)
										worksheet.set_column('E:E', 20)
										worksheet.set_column('F:F', 20)
										worksheet.set_column('G:G', 20)
										datatoexcel.save()
										messagebox.showinfo("Success", "Excel File is Generated Successfully Employee List "+today+"("+j+").xlsx")
									except:
										messagebox.showerror("Error", "Invalid Id Or Record Does Not Exists")
						
							if date_another_error == '':
								pass
							else:
								date_search = str(search_date.get()) 
								try:
									try:
										searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
									except UnboundLocalError as e:
										pass
								except ValueError as e:
									pass
								c.execute("SELECT * FROM all_record WHERE attendance_date = (?)", (searched_date,))
								results_data=c.fetchall()

								if not os.path.exists('./Saved Employee Attendance Excel'):
									os.makedirs('./Saved Employee Attendance Excel')
								if len(results_data) !=0:
									try:
										data = pd.DataFrame(results_data, columns= ['ID','Employee Name','Employee ID', 'Employee Department', 'Attendance', 'Date', 'Time'])
										datatoexcel = pd.ExcelWriter("Saved Employee Attendance Excel/Employee List "+today+"("+str(i)+").xlsx", engine='xlsxwriter')
										data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
										worksheet = datatoexcel.sheets['Sheet']
										worksheet.set_column('A:A', 15)
										worksheet.set_column('B:B', 20)
										worksheet.set_column('C:C', 25)
										worksheet.set_column('D:D', 20)
										worksheet.set_column('E:E', 20)
										worksheet.set_column('F:F', 20)
										worksheet.set_column('G:G', 20)
										datatoexcel.save()
										messagebox.showinfo("Success", "Excel File is Generated Successfully Employee List "+today+"("+str(i)+").xlsx")
									except:
										messagebox.showerror("Error", "Invalid Date Or Record Does Not Exists")

					else:
						messagebox.showerror("Error", "No Data Availble In Treeview")
								

				def pdf():
					i = random.randint(0,1000)
					conn = sqlite3.connect("saveddata.db")
					counter_data = len(tree_3rd.get_children())
					c = conn.cursor()
					today = str(date.today())
					id_error = search_id.get()
					date_error = search_date.get()
					date_another_error = str(date_error)
					if counter_data !=0:
						if str(id_error) == '' and str(date_error) == '':
							messagebox.showerror("Error", "Please Insert Date Or Id")
						elif id_error !=0 or date_error !=0:
							if id_error !=0:
								id_search = str(search_id.get())
								c.execute("SELECT * FROM all_record WHERE employee_id = (?)", (id_search,))
								resultss_id=c.fetchall()
								if not os.path.exists('./Saved Employee Attendance PDF'):
									os.makedirs('./Saved Employee Attendance PDF')
								if len(resultss_id) !=0:
									try:
										pdf = SimpleDocTemplate("./Saved Employee Attendance PDF/Employee List "+today+"("+str(i)+").pdf")
										flow_obj = []
										td = [['ID','Employee Name','Employee ID', "Employee Department", "Employee Status", "Attendance Date", "Attendance Time"]]
										for j in resultss_id:
											td.append(j)
										table = Table(td)
										flow_obj.append(table)
										pdf.build(flow_obj)
										messagebox.showinfo("Success", "PDF generated Successfully With This Name Employee List "+today+"("+str(i)+").pdf")
									except:
										messagebox.showerror("Error", "Invalid Id Or Record Does Not Exists")
						
							if date_error =='':
								pass
							else:
								date_search = str(search_date.get()) 
								try:
									try:
										searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
									except UnboundLocalError as e:
										pass
								except ValueError as e:
									pass
								c.execute("SELECT * FROM all_record WHERE attendance_date = (?)", (searched_date,))
								results_data=c.fetchall()

								if not os.path.exists('./Saved Employee Attendance PDF'):
									os.makedirs('./Saved Employee Attendance PDF')
								if len(results_data) !=0:
									try:
										pdf = SimpleDocTemplate("./Saved Employee Attendance PDF/Employee List "+today+"("+str(i)+").pdf")
										flow_obj = []
										td = [['ID','Employee Name','Employee ID', "Employee Department", "Employee Status", "Attendance Date", "Attendance Time"]]
										for j in results_data:
											td.append(j)
										table = Table(td)
										flow_obj.append(table)
										pdf.build(flow_obj)
										messagebox.showinfo("Success", "PDF generated Successfully With This Name Employee List "+today+"("+str(i)+").pdf")
									except:
										messagebox.showerror("Error", "Invalid Id Or Record Does Not Exists")
					else:
						messagebox.showerror("Error", "No Data Availble In Treeview")
								

				def percent():
					try:
						rand = random.randint(0,1000)
						conn = sqlite3.connect("saveddata.db")
						c = conn.cursor()
						id = tree_3rd.item(tree_3rd.selection())['values']
						emp_id = id[2]
						c.execute("SELECT * FROM all_record WHERE employee_id = (?)", (emp_id,))
						total_rec = c.fetchall()
						c.execute("SELECT * FROM all_record WHERE employee_status = 'PRESENT' AND employee_id = (?)", (emp_id,))
						present_rec = c.fetchall()
						c.execute("SELECT * FROM all_record WHERE employee_status = 'ABSENT' AND employee_id = (?)", (emp_id,))
						absent_rec = c.fetchall()
						
						i = int(len(total_rec))
						j = int(len(present_rec))
						k = int(len(absent_rec))
						
						present_percentage = j/i *100
						absnet_percentage = k/i * 100
						
						c.execute("SELECT attendance_date FROM all_record WHERE employee_id = (?) ORDER BY attendance_date ASC LIMIT 1", (emp_id,))
						f_date = c.fetchall()
						from_date = f_date[0][0]

						c.execute("SELECT attendance_date FROM all_record WHERE employee_id = (?) ORDER BY attendance_date DESC LIMIT 1", (emp_id,))
						t_date = c.fetchall()
						to_date = t_date[0][0]

						c.execute("SELECT * FROM all_record WHERE employee_id =(?)", (emp_id,))
						emp_recd = c.fetchall()
						emp_name = emp_recd[0][1]
						emp_id_ = emp_recd[0][2]
						emp_dpt = emp_recd[0][3]
						data_of_employee = [emp_name, emp_id_, emp_dpt, present_percentage, absnet_percentage, from_date, to_date]
						if not os.path.exists('./Employee Attendance Percentage'):
							os.makedirs('./Employee Attendance Percentage')
						data = pd.DataFrame([data_of_employee], columns= ['Employee Name','Employee ID', 'Employee Department', 'Present Percentage', 'Absent Percentage', 'From This Date', 'To This Date'])
						datatoexcel = pd.ExcelWriter("Employee Attendance Percentage/Employee "+str(emp_name)+"("+str(rand)+").xlsx", engine='xlsxwriter')
						data.to_excel(datatoexcel, index=False, sheet_name = "Sheet")
						worksheet = datatoexcel.sheets['Sheet']
						worksheet.set_column('A:A', 25)
						worksheet.set_column('B:B', 25)
						worksheet.set_column('C:C', 25)
						worksheet.set_column('D:D', 25)
						worksheet.set_column('E:E', 25)
						worksheet.set_column('F:F', 25)
						worksheet.set_column('G:G', 25)
						datatoexcel.save()
						messagebox.showinfo("Success", "Excel File is Generated Successfully Employee "+str(emp_name)+"("+str(rand)+").xlsx")

					except IndexError as e:
						messagebox.showerror("Error", "Please Select A Rrcord.")

				def search_by_id():
					for i in tree_3rd.get_children():
						tree_3rd.delete(i)
					id_error = search_id.get()

					conn = sqlite3.connect("saveddata.db")
					c = conn.cursor()
					id_search = str(search_id.get())
					find_data= ("SELECT * FROM all_record WHERE employee_id = ?")
					c.execute(find_data,[(id_search)])
					resultss=c.fetchall()
					print(resultss)
					counter_data = len(tree_3rd.get_children())

					if id_error == "":
						messagebox.showerror("Error", "Please Enter Employee ID")
					
					elif len(resultss) ==0:
						messagebox.showerror("Error", "Invalid ID or Record Does Not Exists")

					elif counter_data == 0:
						for r in resultss:
							tree_3rd.insert("", tk.END, values=r)

				def clear():
					for i in tree_3rd.get_children():
						tree_3rd.delete(i)

				def search_by_date():
					for i in tree_3rd.get_children():
						tree_3rd.delete(i)
					date_error = search_date.get()

					conn = sqlite3.connect("saveddata.db")
					c = conn.cursor()
					date_search = str(search_date.get())
					if date_search == "":
						messagebox.showerror("Error", "Please Enter Date")
					else:
						try:
							searched_date = datetime.strptime(date_search, '%Y-%m-%d').date()
						except ValueError as e:
							# messagebox.showerror("Error", "Incorrect Date Format")
							pass
						find_data= ("SELECT * FROM all_record WHERE attendance_date = ?")
						try:
							c.execute(find_data,[(searched_date)])
						except UnboundLocalError as e:
							pass
						results_data=c.fetchall()

						counter_date = len(tree_3rd.get_children())
					
					
						if len(results_data) == 0:
							messagebox.showerror("Error", "Please Enter a Valid Date or Record Does not Exists")
						if counter_date == 0:
							for r in results_data:
								tree_3rd.insert("", tk.END, values=r)


#===============================SendCustomEmail======================================
				conn=sqlite3.connect('saveddata.db')
				c=conn.cursor()
				find_data=("SELECT Emailaddress FROM employee")
				c.execute(find_data)
				resultss=c.fetchall()
				email_address_var= StringVar()
				email_address=ttk.Combobox(f6,width=30,textvariable=email_address_var)
				email_address['values']=resultss
				email_address.place(x=200,y=70)
				l3=Label(f6,text="Email List",font=("arial",13,"bold"),bg='grey12',fg='white')
				l3.place(x=110,y=70)

				email_box=Text(f6,font=("arial",25,"bold"),wrap="word")
				email_box.place(x=50,y=100,width=500,height=300)
				def send():
					email_error=str(email_box.get(1.0,END))
					email_address_error=email_address_var.get()
					if len(email_address_error) == 0:
						messagebox.showerror("Error", "Please Select Email Of An Employee From List.")
					else:
						try:
							sender_email = 'pydeveloper000@gmail.com'
							sender_password = 'fypproject'
							server = smtplib.SMTP('smtp.gmail.com', 587)
							message = 'Subject: Facial Recoginition Attendance System \n{}'.format(email_error)
							server.ehlo()
							server.starttls()
							server.login(sender_email, sender_password)
							server.sendmail(sender_email,email_address_error,message)
							server.quit()
							messagebox.showinfo("Success", "Email Is Successfully Sent To The Employee.")
						except:
							messagebox.showerror("Error", "Email Didn't Sent Connection Problem Or Something Went Wrong")


				btn=ttk.Button(f6,text='Send Email',command=send)
				btn.place(x=200,y=410)

				def refresh_list():
					email_list = email_address.get()
					conn = sqlite3.connect("saveddata.db")
					c = conn.cursor()
					find_data= ("SELECT Emailaddress FROM employee")
					c.execute(find_data)
					resultss=c.fetchall()
					email_address['values'] = resultss
				btn=ttk.Button(f6,text='Refresh',command=refresh_list)
				btn.place(x=350,y=410)






				btn9w2=ttk.Button(f1,text="Send Email",command=lambda:swap(f6))
				btn9w2.place(x=440, y=445,width=150,height=30)

				def upload():
					try:
						s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect(('www.google.com',80))
						s.close()
						filename=filedialog.askopenfilename(initialdir ='./Attendance',title='Select a file',filetype=(("csv","*.xlsx"),("All files","*.*")))
						config ={
						"apiKey": "AIzaSyAS9d2AeHKQqDs983iuV3jC-QroblkXsNM",
						"authDomain": "fir-36de9.firebaseapp.com",
						"databaseURL": "https://fir-36de9.firebaseio.com",
						"projectId": "fir-36de9",
						"storageBucket": "fir-36de9.appspot.com",
						"messagingSenderId": "217031050296",
						"appId": "1:217031050296:web:cc8bd5cb5a4fdb021952cd",
						"measurementId": "G-T3ZYJZ4J9M"
						}
						if len(filename) > 0:

							firebase=pyrebase.initialize_app(config)
							storage = firebase.storage()
							path_on_cloud= "Attendance/"+os.path.basename(filename)
							storage.child(path_on_cloud).put(filename)
							messagebox.showinfo("Success","Successfully uploaded to Firebase")
						else:
							messagebox.showerror("Error","No file Selected")
					except Exception:
						messagebox.showerror('Error',"You are not connected to internet")
						sleep(1)
						
					#storage.child(path_on_cloud).download('myimage.png')

				btn9w2=ttk.Button(f1,text="Upload to Firebase",command=upload)
				btn9w2.place(x=440, y=390,width=150,height=30)
#======================Record_images_with_database======================================

				def capture_images():
					'''
					conn = sqlite3.connect('saveddata.db')
					c = conn.cursor()
					sql = """;
					CREATE TABLE IF NOT EXISTS employee (
								id integer unique primary key autoincrement,
								name text,dept text,Emailaddress text,employee_id
					);
					"""
					
					c.executescript(sql)'''
					if not os.path.exists('./dataset'):
						os.makedirs('./dataset')
					uname=entry6.get()
					up1=uname.upper()
					dep=entry7.get()
					cont=entry8.get()
					email=str(cont)
					match=re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b',email,re.I)
					eid=entry9.get()
					if uname=="":
						messagebox.showerror("Error","Please Enter Employee Name")
					elif dep=="":
						messagebox.showerror("Error","Please Select Department")
					elif cont=="":
						messagebox.showerror("Error","Please Enter Emailaddress")
					elif match==None:
						messagebox.showerror("Error","Invalid Email address")
					elif eid=="":
						messagebox.showerror("Error","Please Enter Employee ID")
					else:
						conn=sqlite3.connect("saveddata.db")
						c=conn.cursor()
						c.execute('INSERT INTO employee (name,dept,Emailaddress,employee_id) VALUES (?,?,?,?)', (up1,dep,cont,eid))
						uid = c.lastrowid
						face_classifier=cv2.CascadeClassifier("./Resources/haarcascade_frontalface_default.xml")

						def face_extractor(img):
							gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
							faces=face_classifier.detectMultiScale(gray,1.2,7)
							if faces is():
								return None
							for(x,y,w,h) in faces:
								cropped_face=img[y:y+h,x:x+w]
							return cropped_face
						cap=cv2.VideoCapture(0)
						count=0
						while True:
							ret,frame=cap.read()
							if face_extractor(frame) is not None:
								count+=1
								face=cv2.resize(face_extractor(frame),(400,400))
								face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
								file_name_path="dataset/"+up1+"."+str(uid)+"."+str(count)+".jpg"
								cv2.imwrite(file_name_path,face)
								cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
								cv2.imshow("Face Cropper",face)
							else:
								print("face not found")
								pass
							if cv2.waitKey(1)==13 or count==70:
								break
						cap.release()
						conn.commit()
						conn.close()
						statusbar['text']='Employee has been Added....'
						cv2.destroyAllWindows
						messagebox.showinfo("Information","Images has been collected")


				btn5w2=ttk.Button(f2,text="Capture and Save",command=capture_images)
				btn5w2.place(x=290, y=260,width=130,height=30)

				btn4w2=ttk.Button(f2,text="Back	",command=lambda:swap(f1))
				btn4w2.place(x=3, y=40,width=50,height=30)
				def swap2(frame):
					frame.tkraise()

				btn7w2=ttk.Button(f3,text="Back",command=lambda:swap(f1))
				btn7w2.place(x=3, y=40,width=50,height=30)

				#btn6w2=ttk.Button(f1,text="View Employee's Data",command=lambda:swap2(f3))
				#btn6w2.place(x=440, y=225,width=150,height=30)

				btn8w2=ttk.Button(f6,text="Back",command=lambda:swap(f1))
				btn8w2.place(x=3, y=40,width=50,height=30)

#==========================Develoeprs Page===============================================

				label10=Label(f5,text="Develoeprs",font=("arial",20,"bold"),bg="gold3",fg="black")
				label10.pack(side=TOP,fill=X)
				label11=Label(f5,text="A Project By Code Eater's",font=("arial",10,"bold"),bg="gold3",fg="black")
				label11.pack(side=BOTTOM,fill=X)
				canvas5 =Canvas(f5,width=600,height=500)
				path4="./Resources/3.jpg"
				image5=ImageTk.PhotoImage(Image.open(path4))
				canvas5.create_image(0,0,anchor=NW,image=image5)
				canvas5.pack()

				btn9w2=ttk.Button(f1,text="Developers",command=lambda:swap2(f5))
				btn9w2.place(x=440, y=335,width=150,height=30)
				btn4w2=ttk.Button(f5,text="Back	",command=lambda:swap4(f1))
				btn4w2.place(x=3, y=40,width=50,height=30)

#=========================Window2Frame4searchPage=========================================

				label10=Label(f4,text="Search Employee",font=("arial",20,"bold"),bg="gold3",fg="black")
				label10.pack(side=TOP,fill=X)
				label11=Label(f4,text="A Project By Code Eater's",font=("arial",10,"bold"),bg="gold3",fg="black")
				label11.pack(side=BOTTOM,fill=X)

				def swap4(frame):
					frame.tkraise()
					statusbar['text']='Facial Recognition Attendance System'

				btn4w2=ttk.Button(f4,text="Back	",command=lambda:swap4(f1))
				btn4w2.place(x=3, y=40,width=50,height=30)
				def swap3(frame):
					frame.tkraise()	
				btn9w2=ttk.Button(f1,text="Search Employee",command=lambda:swap3(f4))
				btn9w2.place(x=440, y=280,width=150,height=30)

#===========================FETCHDATABASEINLISTVIEW=========================================	

				def fetch():
					conn = sqlite3.connect("saveddata.db")
					cur = conn.cursor()
					cur.execute("SELECT * FROM employee")
					rows = cur.fetchall()
					counter= len(List_Table.get_children())
					if counter==0:
						for row in rows:
							List_Table.insert("", tk.END, values=row)
						conn.close()
					else:
						messagebox.showerror("Error","Already Visible")

				def search():
					for t in tree_scnd.get_children():
						tree_scnd.delete(t)
					conn = sqlite3.connect("saveddata.db")
					id_data_find = s_entry.get()
					data_obj=conn.cursor()
					find_data_by_id = ("SELECT * FROM present_record WHERE Employee_id= ?;")
					data_obj.execute(find_data_by_id,[(id_data_find)] )
					data_row=data_obj.fetchall()
					print(data_row)
					counter = len(tree_scnd.get_children())
					if id_data_find == "":
						messagebox.showerror("Error", "Please Enter Employee ID")
					elif len(data_row) == 0:
						messagebox.showerror("Error", "Invalid ID or Employee Does Not Exists")
					elif counter == 0:
						for i in data_row:
							tree_scnd.insert("", tk.END, values=i)

				s_button=ttk.Button(f4, text='Search by ID',command=search)
				s_button.place(x=100,y=40)
				s_entry=StringVar()
				pdd=str(s_entry)
				s_entry=ttk.Entry(f4,textvariable=s_entry)
				s_entry.place(x=200,y=42)

				def search_by_date():
					for t in tree_scnd.get_children():
						tree_scnd.delete(t)
					conn = sqlite3.connect("saveddata.db")
					date_data_find = d_entry.get()
					data_obj=conn.cursor()
					find_data_by_id = ("SELECT * FROM present_record WHERE Date_of_Mark= ?;")
					data_obj.execute(find_data_by_id,[(date_data_find)] )
					date_data=data_obj.fetchall()
					print(date_data)
					counter = len(tree_scnd.get_children())
					if date_data_find == "":
						messagebox.showerror("Error", "Please Enter Date")
					elif len(date_data) == 0:
						messagebox.showerror("Error", "Invalid ID or Employee Does Not Exists")
					elif counter == 0:
						for i in date_data:
							tree_scnd.insert("", tk.END, values=i)

				d_button=ttk.Button(f4, text='Search by Date',command=search_by_date)
				d_button.place(x=100,y=80)
				d_entry=StringVar()
				d_entry=ttk.Entry(f4,textvariable=d_entry)
				d_entry.place(x=200,y=82)


				d_label=Label(f4,text="YYYY-MM-DD")
				d_label.place(x=350,y=80)

				def pdfgen():
				    if not os.path.exists('./PDF'):	
					    os.makedirs('./PDF')
				    b=str(s_entry)
				    if s_entry == "":
					    messagebox.showerror("Error","Please Enter Employee_id")
				    else:
					    time=str(date.today())
					    a=s_entry.get()
					    pdf= SimpleDocTemplate("./PDF/Employee id "+a+time+".pdf")
					    flow_obj=[]
					    td=[['Employee_Name','Department','Employee_id','Status','Date','Time']]
					    conn=sqlite3.connect("saveddata.db")
					    data_obj=conn.cursor()
					    data_obj.execute("SELECT * FROM `present_record` WHERE `Employee_id` LIKE ?", ('%'+str(a)+'%',))
					    data_row=data_obj.fetchall()
					    for row in data_row:
						    td.append(row)
					    table=Table(td)
					    flow_obj.append(table)
					    pdf.build(flow_obj)
					    messagebox.showinfo("Success","PDF has been Generated")
					    s_entry.delete(0,END)

				pdf_button=ttk.Button(f4, text='Generate PDF',command=pdfgen)
				pdf_button.place(x=350,y=40)
				label=Label(f4,text='Enter only Employee id')
				label.place(x=450,y=40)


				tree_scnd = ttk.Treeview(f4)
				tree_scnd["columns"] = ("one", "two", "three", "four", "five", "six")
				tree_scnd.column("#0", width=0, minwidth=0, stretch=tk.NO)
				tree_scnd.column("one", width=120, minwidth=100, stretch= tk.NO)
				tree_scnd.column("two", width=100, minwidth=100, stretch=tk.NO)
				tree_scnd.column("three", width=100, minwidth=100, stretch=tk.NO)
				tree_scnd.column("four", width=100, minwidth= 100, stretch=tk.NO)
				tree_scnd.column("five", width=100, minwidth=100, stretch=tk.NO)
				tree_scnd.column("six", width=100, minwidth=100, stretch=tk.NO)

				tree_scnd.heading("#0",text="index", anchor= tk.W)
				tree_scnd.heading("one", text="Employee Name", anchor=tk.W)
				tree_scnd.heading("two", text="Department", anchor=tk.W)
				tree_scnd.heading("three", text="Employee ID", anchor=tk.W)
				tree_scnd.heading("four", text=" Status", anchor=tk.W)
				tree_scnd.heading("five", text=" Date", anchor=tk.W)
				tree_scnd.heading("six", text=" Time", anchor=tk.W)
				tree_scnd.place(x=0,y=140)
#==========================DeleteRecordfromDatabase=========================================
				def dell():
					conn = sqlite3.connect("saveddata.db")
					c = conn.cursor()
					try:
						id=List_Table.item(List_Table.selection())['values']
						dlt_id=id[4]
						print(id)
						print(dlt_id)
						c.execute("DELETE FROM employee WHERE employee_id=?;", ([dlt_id]))
						messagebox.showinfo("Success","Record Deleted Successfully please refresh")
						conn.commit()
						conn.close()
					except IndexError as e:
						messagebox.showerror("Error","Pleease Select a Record")
						return
				btn8w2=ttk.Button(f3,text="View Record",command=fetch)
				btn8w2.place(x=25, y=420,width=130,height=30)

				def refresh():
					for i in List_Table.get_children():
						List_Table.delete(i)
					conn=sqlite3.connect("saveddata.db")
					c=conn.cursor()
					c.execute("SELECT * FROM employee")
					data_employee= c.fetchall()
					counter= len(List_Table.get_children())
					if counter ==0:
						for emp in data_employee:
							List_Table.insert("",tk.END,values=emp)
						conn.close()

				btn10w2=ttk.Button(f3,text="Refresh",command=refresh)
				btn10w2.place(x=225, y=420,width=130,height=30)

				btn9w2=ttk.Button(f3,text="Delete Selected",command=dell)
				btn9w2.place(x=455, y=420,width=130,height=30)
#================================Frame3LISTVIEW==========================================


				label8=Label(f3,text="Employee Records",font=("arial",20,"bold"),bg="gold3",fg="black")
				label8.pack(side=TOP,fill=X)

				Detail_Frame=Frame(f3,bd=4,relief=RIDGE,bg="purple")
				Detail_Frame.place(x=8,y=100,width=590,height=300)
				scroll_x=Scrollbar(Detail_Frame,orient=HORIZONTAL)
				scroll_y=Scrollbar(Detail_Frame,orient=VERTICAL)
				List_Table=ttk.Treeview(Detail_Frame,columns=("1","2","3","4","5"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
				scroll_x.pack(side=BOTTOM,fill=X)
				scroll_y.pack(side=RIGHT,fill=Y)
				scroll_x.config(command=List_Table.xview)
				scroll_y.config(command=List_Table.yview)
				List_Table.heading("1",text="ID")
				List_Table.heading("2",text="Name")
				List_Table.heading("3",text="Department")
				List_Table.heading("4",text="Email address")
				List_Table.heading("5",text="Employee_id")
				List_Table['show']='headings'
				List_Table.column("1",width=20)
				List_Table.column("2",width=100)
				List_Table.column("3",width=100)
				List_Table.column("4",width=100)
				List_Table.column("5",width=100)
				List_Table.pack(fill=BOTH,expand=1)

				f1.tkraise()
				window2.mainloop()

			break
		else:
			messagebox.showerror("Error","invalid username or password")
			break
#======================MainLoginScreen============================================
window=Tk()

#====================LoginSCREEN====================================

p1=Frame(window,bg='black')
p2=Frame(window,bg="grey12")
p3=Frame(window,bg="grey12")

def swap(frame):
	frame.tkraise()
for frame in(p1,p2,p3):
	frame.place(x=0,y=0,width=500,height=500)
window.title("Login Panel")
p1.tkraise()
label3=Label(p1,text="Login Panel",font=("arial",20,"bold"),bg="grey25",fg="white",relief=RAISED)
label3.pack(side=TOP,fill=X)
label3=Label(p1,text="Project By Code Eaters",font=("arial",12,"bold"),bg="grey25",fg="white",relief=RAISED)
label3.pack(side=BOTTOM,fill=X)


#==============itemsinframe1(p2)=================================
label3=Label(p2,text="Login as Admin",font=("arial",20,"bold"),bg="grey25",fg="white",relief=FLAT)
label3.pack(side=TOP,fill=X)
label3=Label(p2,text="Project By Code Eaters",font=("arial",12,"bold"),bg="grey25",fg="white",relief=FLAT)
label3.pack(side=BOTTOM,fill=X)


canvas2 =Canvas(p2,width=500,height=500)
path2="./Resources/2.jpg"
image2=ImageTk.PhotoImage(Image.open(path2))
canvas2.create_image(0,0,anchor=NW,image=image2)
canvas2.pack()

name2_label=Label(p2,text="Name",font=("arial",15,"bold"),bg='chartreuse3',fg='white')
name2_label.place(x=100,y=100)
name2_entry=StringVar()
name2_entry=ttk.Entry(p2,textvariable=name2_entry)
name2_entry.place(x=230,y=98,height=25)
name2_entry.focus()

pass2_label=Label(p2,text="Password",font=("arial",15,"bold"),bg='chartreuse3',fg='white')
pass2_label.place(x=100,y=150)
pass2_entry=StringVar()
pass2_entry=ttk.Entry(p2,textvariable=pass2_entry,show="*")
pass2_entry.place(x=230,y=148,height=25)

btn3=ttk.Button(p2,text="Login",command=loggin)
btn3.place(x=150,y=200,width=210,height=35)

#==================items in frame3 Add new user (p3)===================================
label3=Label(p3,text="Add new User",font=("arial",20,"bold"),bg="grey25",fg="white",relief=FLAT)
label3.pack(side=TOP,fill=X)
label3=Label(p3,text="Project By Code Eaters",font=("arial",12,"bold"),bg="grey25",fg="white",relief=FLAT)
label3.pack(side=BOTTOM,fill=X)

canvas3 =Canvas(p3,width=500,height=500)
path="./Resources/2.jpg"
image3=ImageTk.PhotoImage(Image.open(path))
canvas3.create_image(0,0,anchor=NW,image=image3)
canvas3.pack()

name_label=Label(p3,text="Name",font=("arial",13,"bold"),bg='chartreuse3',fg='white')
name_label.place(x=150,y=100)
name_entry=StringVar()
name_entry=ttk.Entry(p3,textvariable=name_entry)
name_entry.place(x=240,y=100)
name_entry.focus()
pass_label=Label(p3,text="Password",font=("arial",13,"bold"),bg='chartreuse3',fg='white')
pass_label.place(x=150,y=148)
pass_entry=StringVar()
pass_entry=ttk.Entry(p3,textvariable=pass_entry,show="*")
pass_entry.place(x=240,y=148)

btn1=ttk.Button(p3,text="Add User",command=saveadmin)
btn1.place(x=180,y=190)
def clear():
	name_entry.delete(0,END)
	pass_entry.delete(0,END)
btn2=ttk.Button(p3,text="Clear",command=clear)
btn2.place(x=290,y=190)
#==================BACKGROUNDiMAGEformainframe============================
canvas =Canvas(p1,width=500,height=500)
path3="./Resources/1.jpg"
image=ImageTk.PhotoImage(Image.open(path3))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
#=================BUTTONSINLOGINSCREEN====================================
btn3=ttk.Button(p1,text="Login as Admin",command=lambda:swap(p2))
btn3.place(x=285,y=100,width=210,height=35)
btn4=ttk.Button(p1,text="Add new User",command=lambda:swap(p3))
btn4.place(x=285,y=180,width=210,height=35)
#============BackButtons===================================================
backf2=Button(p2,text="Back	",bg='red',fg='white',command=lambda:swap(p1))
backf2.place(x=3, y=40,width=60,height=30)
backf2=Button(p3,text="Back	",bg='red',fg='white',command=lambda:swap(p1))
backf2.place(x=3, y=40,width=60,height=30)

window.geometry("500x500+420+170")
window.resizable(False, False)
window.mainloop()