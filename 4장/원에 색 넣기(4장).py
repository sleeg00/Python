import turtle
t = turtle.Turtle()
t.shape("turtle")

color = [0] * 3
color[0] = input("색상 #1을 입력하시오: ")
color[1] = input("색상 #2을 입력하시오: ")
color[2] = input("색상 #3을 입력하시오: ")

t.fillcolor(color[0]) #채울 컬러
t.begin_fill()        #채운다 컬러
t.circle(50)          #반지름 50
t.end_fill()          #끝낸다 컬러

t.up()
t.fd(100)
t.down()

t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()

t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()
