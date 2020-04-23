import math
def main():
  print("This program calculates distance between two points")
  x1, y1 = eval(input("Please enter x, y coordinates for point 1:"))
  x2, y2 = eval(input("Please enter x, y coordinates for point 2:"))
  distance = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
  print("Distance between two points is ", distance)

main()
