PETERIOUS_AGE: int = 18
STANLEOUS_AGE: int = 25
MANYIOUS_AGE: int = 35


def main():

# This script checks if a user can vote in three different countries based on their age.
    user_age = int(input("Enter your age: "))

    if user_age >= PETERIOUS_AGE:
         print("✅ You can vote in Peterious where the voting age is " + str(PETERIOUS_AGE) + ".")

    else:
         print("❌ You cannot vote in Peterious where the voting age is " + str(PETERIOUS_AGE) + ".")


    if user_age >= STANLEOUS_AGE:
         print("✅ You can vote in Stanleous where the voting age is " + str(STANLEOUS_AGE) + ".")

    else:
         print("❌ You cannot vote in Stanleous where the voting age is " + str(STANLEOUS_AGE) + ".")

    
    if user_age >= MANYIOUS_AGE:
         print("✅You can vote in Manyious where the voting age is " + str(MANYIOUS_AGE) + ".")

    else:
        print("❌ You cannot vote in Manyious where the voting age is " + str(MANYIOUS_AGE) + ".")


if __name__ == "__main__":
    main()
