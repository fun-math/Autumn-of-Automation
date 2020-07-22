n=int(input())
prices=input().split(" ")

temp_buy_date=0
buy_price=(1<<31)-1
buy_date=0
profit=0

for i in range(n) :
	p=int(prices[i])
	if p<buy_price :
		buy_price=p
		temp_buy_date=i+1
		sell_price=0
	elif p-buy_price>profit :
		buy_date=temp_buy_date
		profit=p-buy_date

print(str(profit)+"\n"+str(buy_date))

