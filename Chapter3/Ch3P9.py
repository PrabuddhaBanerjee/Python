import math
def main():
  print("This program calculates area of a triangle")
  a, b, c = eval(input("Please enter 3 sides of triangle a, b, c:"))
  s = (a + b + c)/2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  print("Area of the triangle is ", area)

main()
