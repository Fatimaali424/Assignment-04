from hashlib import sha256

def hash_password(password):
    """
    Hashes a password using SHA-256 and returns the hexadecimal digest.
    """
    return sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):

    if email in stored_logins:  
        stored_hash = stored_logins[email] 
        return stored_hash == hash_password(password_to_check)  
    return False 

def main():
    
    stored_logins = {
        "user@example.com": hash_password("password123"),
        "fatima.ali424@gmail.com": hash_password("fatimaali368"),
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    
    if login(email, password, stored_logins):
        print("✅ Login successful! ")
    else:
        print("❌ Login failed!  Incorrect email or password.")

if __name__ == '__main__':
    main()