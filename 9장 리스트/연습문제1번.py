list=[]
hap=0
for i in range(5):
    i=int(input("점수를 입력해주세요: "))
    list.append(i)
    hap+=i
print("평균=",hap/5)
