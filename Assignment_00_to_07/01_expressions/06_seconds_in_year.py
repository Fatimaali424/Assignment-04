DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # This program calculates the number of seconds in a year.
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    print(f"There are {total_seconds} seconds in a year!")

# Call the main function
if __name__ == '__main__':
    main()