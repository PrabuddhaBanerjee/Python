import math

def main():
  print("This program is to calculate cost per square inch of a circular pizza")
  diameter = int(input("Please enter the diameter of Pizza:"))
  print("Cost per inch of Pizza is $2")
  radius = diameter / 2
  area = math.pi * (radius ** 2)
  price  = area * 2
  print("The price for the pizza is", price)

main()
