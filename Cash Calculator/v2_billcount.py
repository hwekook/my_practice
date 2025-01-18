money_list=[50000,10000,5000,1000,500,100,50,10]

money=int(input("금액을 입력하세요:"))

count_50000=money//50000
money%=50000

count_10000=money//10000
money%=10000

count_5000=money//5000
money%=5000

count_1000=money//1000
money%=1000

count_500=money//500
money%=500

count_100=money//100
money%=100

count_50=money//50
money%=50

count_10=money//10
money%=10

print(f"오만원권:",count_50000)
print(f"만원권:",count_10000)
print(f"오천원권:",count_5000)
print(f"천원권:",count_1000)
print(f"오백원:",count_500)
print(f"백원:",count_100)
print(f"오십원:",count_50)
print(f"십원:",count_10)