def main():
    print("This program is used to convert the Celsius to Fahrenheit ")
    celsius = eval (input ("What is the Celsius temperature? ") )
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")

def check():
  for i in range (5):
    main ()

check()
