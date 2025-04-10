def main():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

    remainder = num % 2  
    return remainder == 1


if __name__ == '__main__':
    main()