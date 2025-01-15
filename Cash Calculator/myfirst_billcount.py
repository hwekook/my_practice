result=input("금액을 만원 이상 입력하세요:")

h=int(result)/50000
a=(int(result)-int(h)*50000)/10000
b=(int(result)-int(h)*50000-int(a)*10000)/5000
c=(int(result)-int(h)*50000-int(a)*10000-int(b)*5000)/1000
d=(int(result)-int(h)*50000-int(a)*10000-int(b)*5000-int(c)*1000)/500
e=(int(result)-int(h)*50000-int(a)*10000-int(b)*5000-int(c)*1000-int(d)*500)/100
f=(int(result)-int(h)*50000-int(a)*10000-int(b)*5000-int(c)*1000-int(d)*500-int(e)*100)/50
g=(int(result)-int(h)*50000-int(a)*10000-int(b)*5000-int(c)*1000-int(d)*500-int(e)*100-int(f)*50)/10

print(f"오만원권 :",int(h))
print(f"만원권 :",int(a))
print(f"오천원권 :",int(b))
print(f"천원권 :",int(c))
print(f"오백원 :",int(d))
print(f"백원 :",int(e))
print(f"오십원 :",int(f))
print(f"십원 :",int(g))