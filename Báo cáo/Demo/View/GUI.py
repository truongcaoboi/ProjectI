from matran import *
from tkinter.ttk import Frame, Button, Label,Entry
from tkinter import Tk, BOTH
from tkinter import *
import numpy
import tkinter.messagebox as mbox
class GUI(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.frame1=LabelFrame(self.parent)
		self.frame1.pack(fill=X)
		self.frame2=LabelFrame(self.parent)
		self.frame2.pack(fill=BOTH,expand=True)
		self.matranA=Matran()
		self.matranB=Matran()
		self.lb1=Label(self.frame2)
		self.lb2=Label(self.frame2)
		self.lb3=Label(self.frame2)
		self.t1=Entry(self.frame2)
		self.t2=Entry(self.frame2)
		self.initUI()

	def initUI(self):
		self.parent.title("Demo")
		self.pack(fill=BOTH,expand=True)

		

		button1=Button(self.frame1,text="nhập ma trận A",command=self.nhapmatran1)
		button1.pack(side=LEFT,padx=5)
		button2=Button(self.frame1,text="nhập ma trận B",command=self.nhapmatran2)
		button2.pack(side=LEFT,padx=5)
		button3=Button(self.frame1,text="A+B",command=self.congMatran)
		button3.pack(side=LEFT,padx=5)
		button4=Button(self.frame1,text="AxB",command=self.nhanMatran)
		button4.pack(side=LEFT,padx=5)
		button5=Button(self.frame1,text="det(A)&det(B)",command=self.tinhdinhthuc)
		button5.pack(side=LEFT,padx=5)
		button6=Button(self.frame1,text="A^-1&B^-1",command=self.nghichDao)
		button6.pack(side=LEFT,padx=5)

		

	def congMatran(self):
		self.clear()
		self.clear()
		matran=Matran()
		nA=self.matranA.n
		mA=self.matranA.m
		nB=self.matranB.n
		mB=self.matranB.m
		if nA==nB and nA>0 and mA==mB and mA>0:
			A=numpy.array(self.matranA.listArray)
			B=numpy.array(self.matranB.listArray)
			C=matran.congMaTran(A,B)
			lb=Label(self.frame2,text="Kết quả phép cộng")
			lb.pack()
			text=Text(self.frame2)
			for hang in C:
				for cot in hang:
					text.insert(INSERT,(str(cot)+" "))
				text.insert(INSERT,"\n")
			text.insert(END,"\n")
			text.pack()
		else:
			mbox.showwarning("Warning","Thiếu dữ liệu đầu vào hoặc hai ma trận không khả cộng")
			return
		pass
	def nhanMatran(self):
		self.clear()
		nA=self.matranA.n
		mA=self.matranA.m
		nB=self.matranB.n
		mB=self.matranB.m
		if (nA>0 and nB>0 and mA>0 and mB>0):
			if(self.matranA.m==self.matranB.n):
				matran=Matran()
				A=self.matranA.listArray
				B=self.matranB.listArray
				C=matran.nhanMaTran(A,B)
				lb=Label(self.frame2,text="Kết quả phép nhân")
				lb.pack()
				text=Text(self.frame2)
				for hang in C:
					for cot in hang:
						text.insert(INSERT,(str(cot)+" "))
					text.insert(INSERT,"\n")
				text.insert(END,"\n")
				text.pack()
				pass
			else:
				mbox.showwarning("Warning","Hai ma trận không hợp lệ")
		else:
			mbox.showwarning("Warning","Thiếu dữ liệu đầu vào")
		pass

	def nghichDao(self):
		self.clear()
		nA=self.matranA.n
		mA=self.matranA.m
		nB=self.matranB.n
		mB=self.matranB.m
		text=Text(self.frame2)
		if(mA>0):
			if(mA==nA):
				matran=Matran()
				k,B=matran.nghichDaoMaTran(self.matranA.listArray,nA)
				if(k!=0):
					text.insert(INSERT,"ma trận nghịch đảo của A:\n")
					for hang in B:
						for cot in hang:
							text.insert(INSERT,(str(cot)+" "))
						text.insert(INSERT,"\n")
					text.insert(INSERT,"\n")
				else:
					text.insert(INSERT,"ma trận A không có ma trận nghịch đảo\n")
			else:
				text.insert(INSERT,"ma trận A không phải là ma trận vuông\n")
		else:
			text.insert(INSERT,"ma trận A thiếu dữ liệu\n")
		if(mB>0):
			if(mB==nB):
				matran=Matran()
				k,B=matran.nghichDaoMaTran(self.matranB.listArray,nB)
				if(k!=0):
					text.insert(INSERT,"ma trận nghich đảo của B:\n")
					for hang in B:
						for cot in hang:
							text.insert(INSERT,(str(cot)+" "))
						text.insert(INSERT,"\n")
					text.insert(INSERT,"\n")
				else:
					text.insert(INSERT,"ma trận B không có ma trận nghịch đảo\n")
			else:
				text.insert(INSERT,"ma trận B không phải là ma trận vuông\n")
		else:
			text.insert(INSERT,"ma trận B thiếu dữ liệu\n")
		text.insert(END,"\n")
		text.pack()
		pass

	def clear(self):
		for i in self.frame2.pack_slaves():
			i.destroy()
		for i in self.frame2.grid_slaves():
			i.destroy()

	def nhapmatran1(self):
		self.clear()
		self.lb3=Label(self.frame2,text="cập nhập ma trận A")
		self.lb1=Label(self.frame2,text="nhập kích thước ma trận (nxm)")
		self.lb2=Label(self.frame2,text="nhập các phần tử của ma trận")
		self.t1=Entry(self.frame2)
		self.t2=Entry(self.frame2)
		but=Button(self.frame2,text="OK",command=self.nhapA)
		self.lb3.grid(row=0)
		self.lb1.grid(row=1,column=0)
		self.lb2.grid(row=3,column=0)
		self.t1.grid(row=1,column=1)
		self.t2.grid(row=3,column=1)
		but.grid(row=4)
		pass
	def nhapmatran2(self):
		self.lb3=Label(self.frame2,text="cập nhập ma trận B")
		self.clear()
		self.lb1=Label(self.frame2,text="nhập kích thước ma trận (nxm)")
		self.lb2=Label(self.frame2,text="nhập các phần tử của ma trận")
		self.t1=Entry(self.frame2)
		self.t2=Entry(self.frame2)
		but=Button(self.frame2,text="OK",command=self.nhapB)
		self.lb3.grid(row=0)
		self.lb1.grid(row=1,column=0)
		self.lb2.grid(row=3,column=0)
		self.t1.grid(row=1,column=1)
		self.t2.grid(row=3,column=1)
		but.grid(row=4)
		pass
	def nhapA(self):
		try:
			str1=self.t1.get()
			str2=self.t2.get()
			str1=str1.split("x")
			n=int(str1[0])
			m=int(str1[1])
			str2=str2.split(",")
			j=0
			for i in str2:
				str2[j]=float(i)
				j=j+1
			str2=array(str2)
			#str2=array(reshape(str2,n,m))
			str2=array(str2.reshape(n,m))
			self.matranA.setMaTran(str2,n,m)
			mbox.showinfo("Information","cập nhật thành công")
		except Exception as e:
			mbox.showwarning("Warning","Có lỗi xảy ra")
			return
			raise

	def nhapB(self):
		try:
			str1=self.t1.get()
			str2=self.t2.get()
			str1=str1.split("x")
			n=int(str1[0])
			m=int(str1[1])
			str2=str2.split(",")
			j=0
			for i in str2:
				str2[j]=float(i)
				j=j+1
			str2=array(str2)
			#str2=array(reshape(str2,n,m))
			str2=array(str2.reshape(n,m))
			self.matranB.setMaTran(str2,n,m)
			mbox.showinfo("Information","cập nhật thành công")
		except Exception as e:
			mbox.showwarning("Warning","Có lỗi xảy ra")
			return
			raise
	def tinhdinhthuc(self):
		self.clear()
		nA=self.matranA.n
		mA=self.matranA.m
		nB=self.matranB.n
		mB=self.matranB.m
		t=Text(self.frame2)
		if(mA>0 and nA>0):
			if(mA==nA):
				matran=Matran()
				k=matran.det(self.matranA.listArray,nA)
				t.insert(INSERT,("det(A)= "+str(k)+"\n"))
			else:
				t.insert(INSERT,"ma trận A không phải là ma trận vuông\n")
		else:
			t.insert(INSERT,"ma trận A thiếu dữ liệu\n")

		if(mB>0 and nB>0):
			if(mB==nB):
				matran=Matran()
				k=matran.det(self.matranB.listArray,nB)
				t.insert(INSERT,("det(B)= "+str(k)+"\n"))
			else:
				t.insert(INSERT,"ma trận B không phải là ma trận vuông\n")
		else:
			t.insert(INSERT,"ma trận B thiếu dữ liệu\n")
		t.insert(END,"\n")
		t.pack()

root=Tk()
app=GUI(root)
root.geometry("600x500")
root.mainloop()

