def num_in_stock(fruit):
    inventory = {
        "apple": 750,
        "banana": 800,
        "pear": 1800,
        "orange": 1500,
        "mango": 900
    }
    return inventory.get(fruit.lower(), 0)  

def main():
    fruit = input("Enter a fruit: ")

    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()