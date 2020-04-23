def main():
    print("This program")
    x = eval(input("Enter num between 0 and 1:"))
    n = eval(input("Enter the number of iterations"))
    for i in range(n):
        x = 3.9 * (x - x * x)
        print( x )

main()
