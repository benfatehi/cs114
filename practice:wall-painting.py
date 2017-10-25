print("What is the width of the wall?")
width=int(input())
print("What is the height of the wall?")
height=int(input())
print("How much does a gallon of paint cost?")
cost=float(input())
squarefoot=width*height
paint=squarefoot/400
total=paint*cost
print("It will cost you ",total, "dollars.")
