class Complex :
	def __init__(self, x, y) :
		self.x=x
		self.y=y

	def add(self,other) :
		return Complex(self.x+other.x,self.y+other.y)

	def subtract(self,other) :
		return Complex(self.x-other.x,self.y-other.y)

	def multiply(self,other) :
		return Complex(self.x*other.x-self.x*other.y,
					   self.x*other.y-self.y*other.x)

	def mod(self) :
		return (self.x**2+self.y**2)**(0.5)

	def conjugate(self) :
		return Complex(self.x,-self.y)

	def inverse(self) :
		return Complex(self.x/(self.mod()**2),
					   -self.y/(self.mod()**2))

	def display(self) :
		if self.y>=0:
			print("{}+{}i".format(self.x,self.y))
		else :
			print("{}-{}i".format(self.x,-self.y))



a=Complex(2,1)
print(a.mod())