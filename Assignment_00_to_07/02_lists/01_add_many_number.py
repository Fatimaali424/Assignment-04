def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers_list = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    result = sum_of_numbers(numbers_list)
    print("List:", numbers_list)
    print("Sum of numbers:", result)

if __name__ == '__main__':
    main()