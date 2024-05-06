import bcrypt

def hash_password(password):
    # Hash a password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

print("\n -- Generate hashing using Bcrypt -- ")
password = input(" \n Enter your message : ")

# Hash the password
hashed_password = hash_password(password)

print(" \n Hashed Message :", hashed_password.decode('utf-8'))
