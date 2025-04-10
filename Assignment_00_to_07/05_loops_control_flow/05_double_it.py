def main():
    # Prompt the user for a number
    curr_value = int(input("Enter a number: "))

    
    while curr_value < 100:
        curr_value *= 2  
        print(curr_value, end=" ")  


if __name__ == '__main__':
    main()