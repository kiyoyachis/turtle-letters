import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)#40
        tur.bk(15)#20
        tur.left(145)
        tur.fd(10)#20
        tur.bk(10)#20
        tur.right(110)
        tur.fd(20)#25
        tur.left(145)
        tur.pu()
        tur.fd(50)
        tur.right(90)
        tur.fd(15)
	    
    
    elif letter == "L":
	    pass
    elif letter == "M":
	tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.bk(30)
        tur.left(20)
        tur.fd(20)
        tur.left(135)
        tur.fd(20)
        tur.right(155)
        tur.fd(30)
        tur.bk(30)
        tur.pu()
        tur.bk(5)
        tur.left(90)
        tur.fd(15)
    elif letter == "N":
	tur.right(90)
        tur.fd(30)
        tur.bk(30)
        tur.left(45)
        tur.fd(45)
        tur.left(135)
        tur.fd(30)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(15)
           
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	tur.forward(30)
        tur.right(90)
        tur.forward(40)
        tur.left(30)
        tur.forward(10)
        tur.right(180)
        tur.forward(20)
        tur.left(180)
        tur.forward(10)
        tur.setheading(180)
        tur.forward(30)
        tur.right(90)
        tur.forward(40)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(50)
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
        tur.right(60)
        tur.forward(50)
        tur.left(130)
        tur.forward(50)
        tur.right(135)
        tur.forward(50)
        tur.left(130)
        tur.forward(50)
        tur.right(50)
    elif letter == "X":
	tur.pu()
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.pd()
        tur.left(45)
        tur.fd(20)
        tur.bk(60)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.bk(60)
        tur.left(45)
        tur.pu()
        tur.fd(55)
        tur.right(90)
        tur.fd(50)
        tur.fd(15)
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
