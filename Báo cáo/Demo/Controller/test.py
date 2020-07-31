
class test:
    def __init__(self):
        self.i=0
    def set(self,i):
        self.i=i
t=test()
t.set(5)
print(t.i)
class bao:
	def __init__(self):
		self.t=test()
	def inf(self,i):
		self.t.set(i)
		print(self.t.i)
b=bao()
b.inf(5)