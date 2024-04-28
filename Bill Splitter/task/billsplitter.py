from random import choice

party_group = {}
lucky_flag = False


def calc_bill_split(size):
    bill_value = float(input("Enter the total bill value:\n"))
    bill_split = round(bill_value / size, 2)
    use_lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")
    if use_lucky.lower() == "yes":
        bill_split = round(bill_value / (size - 1), 2)
        lucky_guest = choice(list(party_group.keys()))
        print(f"\n{lucky_guest} is the lucky one!")
        for name in party_group.keys():
            if name == lucky_guest:
                party_group[lucky_guest] = 0
            else:
                party_group[name] = bill_split
        print(party_group)
    else:
        print("\nNo one is going to be lucky")
        for name in party_group.keys():
            party_group[name] = bill_split
        print(party_group)


def get_party_details():
    party_size = int(input("Enter the number of friends joining (including you):\n"))
    if party_size <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for _ in range(party_size):
            guest = input()
            party_group.update({guest: 0})
        calc_bill_split(party_size)


get_party_details()
