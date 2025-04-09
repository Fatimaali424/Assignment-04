MINIMUM_HEIGHT : int = 60 

def main():
    # This script checks if a user is tall enough to ride a roller coaster.
    height = float(input("How tall are you in inches ❓"))

    if height >= MINIMUM_HEIGHT:
        print("🙂 You're tall enough to ride!")
    else:
        print("☹️  You're not tall enough to ride, but maybe next year!")



if __name__ == '__main__':
    main()