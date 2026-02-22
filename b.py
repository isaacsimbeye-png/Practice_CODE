#Guestlist for 3
#I used a loop because it is much easier and cleaner to use it send a repeated invitation
guest_List = ['Jane','Martha','Liz','Diana']

for invitation in guest_List:
        print(f"\nHey {invitation} I am inviting you for dinner")

#sending out new invitations
print("It seems that Jane will be unable to attend")
#Replaces an element
guest_List[0] = 'Magaret'

for invitation in guest_List:
        print(f"\nHello {invitation} I am inviting you for dinner")
#invite 3 more guests
#Bigger dinner table has been found
print(f"\nA LARGER DINNER TABLE HAS BEEN FOUND!!!!!")

#add a guest at the begining of the list
guest_List.insert(0,'Jake')
#add a guest in the middle of the list
guest_List.insert(2,'Zuki')
#add guest at the end of the last
guest_List.append('Daniel')

#print list
print(f'\nNAMES ON GUESTLIST')
for names in guest_List:

        print(f"\n {names}")