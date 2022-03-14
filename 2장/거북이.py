import turtle
t=turtle.Turtle()
t.shape("turtle")

t.fd(100)  #0,0에서 100 전진
t.up()      #그리지 않기
t.goto(0,200) #0,200으로 가기
t.down()      #그리기
t.fd(100)     #(0,200)에서 그리기 (100,200)
