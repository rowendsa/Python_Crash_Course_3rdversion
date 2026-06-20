#Rowen Dsa 01-Jun-2026
#This program was written to understand if statements
current_users = ['jaden', 'michael', 'david', 'admin', 'simon']

if current_users:
    for a_user in current_users:
        if a_user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {a_user.title()}, thank you for logging in again")
else:
    print("We need to find some users!")