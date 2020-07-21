given=str(input())  #Given number

d=len(given)  # No. of digits 
 
i=(d-1)//2                
while i>=0 :             
	if given[i]!="9" :
		break
	i-=1

if i>=0 :
	new_dig=str(int(given[i])+1)
	if i==d-i-1:
		given=given[:i]+new_dig+given[i+1:]
	else :
		given=given[:i]+new_dig+given[i+1:d-i-1]+new_dig+given[d-i:]
	print(given)
else :
	print(10**d+1)
