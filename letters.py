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
        #Oluschi: P, R, I, H, B, O, Z
    elif letter == "B":
	    tur.setheading(0)
	    tur.pd()
	    tur.right(90)
	    tur.fd(30)
	    tur.left(90)
	    tur.fd(20)
	    tur.left(90)
	    tur.fd(13)
	    tur.left(90)
	    tur.fd(20)
	    tur.right(90)
	    tur.fd(4)
	    tur.right(90)
	    tur.fd(20)
	    tur.left(90)
	    tur.fd(13)
	    tur.left(90)
	    tur.fd(20)
	    tur.right(180)
	    tur.pu()
	    tur.fd(35)
	    
    elif letter == "C":
	      tur.setheading(180)
        tur.pd()
        tur.fd(20)
        tur.setheading(270)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(20)
        tur.pu()
        tur.setheading(90)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(15)
    elif letter == "D":
	tur.setheading(270)
        tur.pd()
        tur.fd(30)
        tur.setheading(90)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(15)
        tur.setheading(315)
        tur.fd(3)
        tur.setheading(270)
        tur.fd(25)
        tur.setheading(235)
        tur.fd(3)
        tur.setheading(180)
        tur.fd(15)
        tur.pu()
        tur.setheading(90)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(35)
    elif letter == "E":
	      tur.pd()
        tur.fd(20)
        tur.pu()
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.pd()
        tur.fd(15)
        tur.setheading(0)
        tur.fd(20)
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.fd(15)
        tur.setheading(0)
        tur.fd(20)
        tur.pu()
        tur.right(180)
        tur.fd(15)
        tur.right(90)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(35)
    elif letter == "F":
	      tur.pd()
        tur.fd(20)
        tur.pu()
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.pd()
        tur.fd(15)
        tur.setheading(0)
        tur.fd(20)
        tur.setheading(180)
        tur.fd(20)
        tur.setheading(270)
        tur.fd(15)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(35)
    elif letter == "G":
	      tur.setheading(180)
        tur.pd()
        tur.fd(20)
        tur.setheading(270)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(20)
        tur.setheading(90)
        tur.fd(10)
        tur.left(90)
        tur.fd(10)
        tur.pu()
        tur.right(180)
        tur.fd(10)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(15)		
    elif letter == "H":
	    pass
    elif letter == "I":
        tur.setheading(0)
        tur.pd()
        tur.fd(20)
        tur.pu()
        tur.right(180)
        tur.fd(10)
        tur.left(90)
        tur.pd()
        tur.fd(30)
        tur.right(90)
        tur.fd(10)
        tur.pu()
        tur.right(180)
        tur.fd(10)
        tur.pd()
        tur.fd(10)
        tur.pu()
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)

        
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":

	      tur.right(90)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(20)
        tur.pu()
        tur.setheading(90)
        tur.fd(30)
        tur.setheading(0)
        tur.fd(15)

    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
        tur.setheading(0)
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.right(180)
        tur.fd(35)
    
    elif letter == "P":
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
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
        #tur.fd(15)
        #tur.left(90)
        #tur.fd(20)
        #tur.pu()
        #fixes
        #tur.right(90)
        #tur.fd(20)
        #tur.right(90)
        #tur.fd(35)
        #tur.right(180)
        #Oluschi: P, R, I, H, B, O, Z		
    elif letter == "Q":
	    pass
    elif letter == "R":
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
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        tur.left(145)
        tur.fd(28)
        tur.pu()
        tur.left(120)
        tur.fd(32)
        tur.right(90)
        tur.fd(13)

        
        
	    
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
        tur.setheading(0)
        tur.pd()
        tur.fd(20)
        tur.right(125)
        tur.fd(35)
        tur.left(125)
        tur.fd(20)
        tur.pu()
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        
        
        
	    		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
turtleLetter("box",tur)
turtleLetter("P",tur)
turtleLetter("R",tur)
turtleLetter("I",tur)
turtleLetter("H",tur)
turtleLetter("O",tur)
turtleLetter("Z",tur)
turtleLetter("H",tur)
turtleLetter("A",tur)

window.exitonclick()
