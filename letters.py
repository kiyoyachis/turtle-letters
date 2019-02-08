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
        tur.setheading(270)
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
        tur.fd(15)
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
        tur.setheading(0)
        tur.pd()
        tur.fd(20)
        tur.bk(10)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(14)
        tur.right(90)
        tur.fd(12)
        #fix
        tur.pu()
        tur.fd(18)
        tur.right(90)
        tur.fd(39)
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S": #10 20
        tur.setheading(0)
        tur.pd()
        tur.fd(20)
        tur.pu()
        tur.bk(20)
        tur.right(90)
        tur.pd()
        tur.fd(12)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(18)
        tur.right(90)
        tur.fd(22)
        #fixes
        tur.pu()
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(37)
    elif letter == "T":
        tur.setheading(0)
        tur.pd()
        tur.fd(20)
        tur.bk(10)
        tur.right(90)
        tur.fd(30)
        #fixes
        tur.pu()
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
    elif letter == "U":
        tur.setheading(270)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(30)
        #fixes
        tur.pu()
        tur.right(90)
        tur.fd(15)
    elif letter == "V":
        tur.setheading(300)
        tur.pd()
        tur.fd(35)
        tur.left(120)
        tur.fd(35)
        #fixes
        tur.pu()
        tur.right(60)
        tur.fd(15)
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
        tur.setheading(300)
        tur.fd(20)
        tur.right(30)
        tur.fd(12)
        tur.left(180)
        tur.fd(12)
        tur.right(30)
        tur.fd(20)
        #fixes
        tur.pu()
        tur.right(60)
        tur.fd(15)
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.fd(40)
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)

window.exitonclick()
