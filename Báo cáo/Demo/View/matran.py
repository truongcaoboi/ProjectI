from numpy import * 
class Matran:
	#ham khoi tao
	def __init__(self):
		self.listArray=0
		self.n=0
		self.m=0
	#setgiatri
	def setMaTran(self,listArray,n,m):
		self.listArray=array(listArray)
		self.n=n
		self.m=m
	#cong ma tran
	def congMaTran(self,A,B):
		C=add(A,B)
		return C
	#nhan ma tran
	def nhanMaTran(self,A,B):
		C=dot(A,B)
		return C
	def phanBuDaiSo(self,A,i,j):
		A=delete(A,[j],0)
		A=A.transpose()
		A=delete(A,[i],0)
		A=A.transpose()
		return A
	#tinh det cua mot ma tran
	def det(self,A,n):
		i=0
		detA=0
		if n==1:
			return A[0][0]
		B=A[0];
		while i<n:
			if(i%2==0):
				detA=detA+B[i]*self.det(self.phanBuDaiSo(A,i,0),n-1)
			else:
				detA=detA+(-1)*B[i]*self.det(self.phanBuDaiSo(A,i,0),n-1)
			i+=1
			pass
		return detA
	#tim ma tran nghich dao
	def nghichDaoMaTran(sefl,A,n):
		mt=Matran()
		if(mt.det(A,n)==0):
			return 0,0
		else:
			return 1,linalg.inv(A)