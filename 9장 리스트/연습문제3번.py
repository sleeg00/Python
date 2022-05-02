list={}
k=0
while True:
    name=input("(입력모드)이름을 입력하시오: ")
    if not name:
        break;
    tel = input("전화번호를 입력하시오: ")
    list[name]=tel
k=input("(검색모드)이름을 입력하시오: ")
print(k,"의 전화번호는 ",list[k]+" 입니다")
