import math
def main():
  print("This program is used to figure out the date of Easter")
  year = eval(input("Please enter an year:"))
  c = year // 100
  epact= (8 + (C // 4) - C + ((80+13) // 25) + 11( year % 19)) % 30
  print("Value of epact is ", epact)

main()
