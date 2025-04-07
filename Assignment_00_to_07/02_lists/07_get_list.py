def main():
    lst = []  
    
    while True:
        value = input("Enter a value: ")  
        
        if value == "": # Check for empty input to stop the loop
            break
        
        lst.append(value)  
    print("Here's the list:", lst) 


if __name__ == '__main__':
    main()