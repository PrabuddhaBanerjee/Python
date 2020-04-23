def main():
  print("This program is Find the nth term of Fibonacci Series")
  num = int(input("Please enter the term of Fibonacci:"))
  print("The value at",num,"position is",fib(num))

def fib(num):
  if num<=0:
    print("Incorrect Input")
  elif num == 1 :
    return 1
  elif num == 2 :
    return 1
  else :
    return fib( num-1 ) + fib(num-2)

main()
