n=int(input("수 입력 :"))
tri=0
while n>0:
    n=n//10
    tri=tri+1
    
print("자릿수:",int(tri))
