#Rowen Dsa 17-Jun-2024
#This program is an exercise for list 3.4
guests = ['Pavan', 'Chethan', 'Shaun']
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[0].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[1].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[2].title()}?")

#Shaun unable to attend due to some commitments
print(f"{guests[2].title()} is unable to make it to the event.")
guests[2] = 'Umesh'

#2nd set of invites
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[0].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[1].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[2].title()}?")

#bigger dinner table available
print("We have got the main dinner table for the event. So we will invite 3 more guests.")

#adding guest at the first
guests.insert(0, 'Suresh')

#adding guest in the middle
guests.insert(2, 'Sankar')

#adding guest to the end of the list - append
guests.append('Lloyd')

#resending the invites to guests
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[0].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[1].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[2].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[3].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[4].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[5].title()}?")

#Message that dinner table will not arrive on time for the dinner
print("Unfortunately, the dinner table will not be available on time. So I will only be able to invite 2 guests")

#Popping Shrink_Guest
shrink_guest = guests.pop()
print(f"Sorry buddy. Your invite is cancelled Mr. {shrink_guest.title()}.")

shrink_guest = guests.pop()
print(f"Sorry buddy. Your invite is cancelled Mr. {shrink_guest.title()}.")

shrink_guest = guests.pop()
print(f"Sorry buddy. Your invite is cancelled Mr. {shrink_guest.title()}.")

shrink_guest = guests.pop()
print(f"Sorry buddy. Your invite is cancelled Mr. {shrink_guest.title()}.")

#resending the invites to guests
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[0].title()}?")
print(f"Would you like to join us for dinner on June 23, 2024 Mr. {guests[1].title()}?")

#deleting invitees from list
del guests[0]
del guests[0]

print(guests)

