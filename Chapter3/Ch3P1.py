import math

def main():
  print("This program is to calculate the volume and surface area of a sphere")
  radius = int(input("Please enter the radius for sphere:"))
  vol = (4 / 3)* math.pi * (radius ** 3)
  area = 4 * math.pi * (radius ** 2)
  print("The area of the sphere is",area," and the volume is ",vol)

main()
