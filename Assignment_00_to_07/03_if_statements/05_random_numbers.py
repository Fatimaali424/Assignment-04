import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
   
    # This script generates and prints 10 random numbers between 1 and 100.
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(N_NUMBERS)]
    print("Random Numbers: ", random_numbers)

if __name__ == '__main__':
    main()