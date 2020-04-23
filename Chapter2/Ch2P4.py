def main(num):
    print("This program is used to convert the Celsius to Fahrenheit ")
    # celsius = eval (input ("What is the Celsius temperature? ") )
    celsius = num
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")

def check():
  for i in range (0,110,10):
    print("for celsius:", i)
    main (i)

check()
