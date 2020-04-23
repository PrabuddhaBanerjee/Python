def main():
  print("This program calculates slope between two points")
  x1, y1 = eval(input("Please enter x, y coordinates for point 1:"))
  x2, y2 = eval(input("Please enter x, y coordinates for point 2:"))
  slope = (y2 - y1)/ (x2 - x1)
  print("Slope of the line is ", slope)

main()
