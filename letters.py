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
	tur.setheading(150)
        tur.pd()
        tur.circle(20,250)
        tur.pu()
        tur.setheading(180)
        tur.fd(40)
        tur.setheading(90)
        tur.fd(50)
        tur.setheading(0)
        tur.fd(40)
    elif letter == "D":
	tur.setheading(270)
        tur.pd()
        tur.fd(40)
        tur.setheading(0)
        tur.circle(20,180)
        tur.pu()
        tur.setheading(0)
        tur.fd(20)
    elif letter == "E":
	tur.pd()
        tur.fd(20)
        tur.pu()
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.pd()
        tur.fd(30)
        tur.setheading(0)
        tur.fd(20)
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.pd()
        tur.fd(30)
        tur.setheading(0)
        tur.fd(20)
        tur.pu()
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(60)
        tur.setheading(0)
        tur.fd(40)
    elif letter == "F":
	tur.pd()
        tur.fd(20)
        tur.pu()
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.pd()
        tur.fd(30)
        tur.setheading(0)
        tur.fd(20)
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.pd()
        tur.fd(30)
    elif letter == "G":
	tur.setheading(150)
        tur.pd()
        tur.circle(20,270)
        tur.setheading(90)
        tur.fd(5)
        tur.setheading(180)
        tur.fd(20)
        tur.pu()
        tur.setheading(180)
        tur.fd(30)
        tur.setheading(90)
        tur.fd(40)
        tur.setheading(0)
        tur.fd(50)			
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	tur.right(90)
        tur.fd(50)
        tur.setheading(0)
        tur.fd(30)
        tur.pu()
        tur.setheading(90)
        tur.fd(50)
        tur.setheading(0)
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
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
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
