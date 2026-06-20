#Rowen Dsa 01-Jun-2026
#This program was written to understand if statements
current_users = ['jaden', 'michael', 'david', 'admin', 'simon']
new_users = ['sagar', 'gautham', 'chloe', 'david', 'simon', 'kim']

for a_user in new_users:
    if a_user.lower() in current_users:
        print(f"Sorry. The username {a_user.title()} is already taken. Please enter a new username.")
    else:
        print(f"The username {a_user.title()} is available.")

print("\nWe have checked all usernames.")