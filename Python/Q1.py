d=int(input())  #No. of digits

primes=[2]

for n in range(3,10**((d+1)//2),2):
	for p in primes :
		if n%p==0 :
			break
		if p**2>n :
			primes+=[n]
			break	

def isPrime(n):
	if n==1:
		return False
	for p in primes :
		if n%p==0 :
			if(n==p) :
				return True
			else :
				return False
	return True

file = open("myFirstFile","w+")

for n in range(10**(d-1),10**d-1):
	if isPrime(n) and isPrime(n+2):
		file.write(str(n)+" "+str(n+2)+"\n")

file.close()
