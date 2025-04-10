def average(a, b):
    sum = a + b
    return sum / 2

def main():
    avg_1 = float (input ("Enter first number: "))
    avg_2 = float (input ("Enter second number: "))
    
    final = average(avg_1, avg_2)
    print (f"The average of {avg_1} and {avg_2} is: {final}")


if __name__ == '__main__':
    main()