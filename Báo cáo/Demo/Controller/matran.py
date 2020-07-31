from numpy import * 
class Matran:
	#ham khoi tao
	def setMaTran(self,listArray):
		self.listArray=array(listArray)
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
			return 0
		else:
			return linalg.inv(A)
#a=array([[1,2],[3,4]])
#b=array([[1,2],[3,4]])
#mt1=Matran()
#mt1.setMaTran(a)
##k=mt.det(a,2)
#print(mt1.listArray)
#print(mt1.nghichDaoMaTran(mt1.listArray,2))