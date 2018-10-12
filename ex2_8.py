from turtle import*
pensize(1)
pencolor("green")
i=1
while(i<=60):
    seth(90)
    fd(1)
    seth(180)
    fd(i+1)
    seth(-90)
    fd(i+2)
    seth(0)
    fd(i+3)
    i=i+4
