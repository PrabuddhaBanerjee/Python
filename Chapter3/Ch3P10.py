import math
def main():
  print("This program is to determine the length of a ladder required"
          + " to reach a given height when leaned against a house")
  height, angle = eval(input("Please enter height and angle:"))
  radians = (math.pi / 180) * angle
  length = height / math.sin(radians)
  print("Length of ladder should be ", length)

main()
