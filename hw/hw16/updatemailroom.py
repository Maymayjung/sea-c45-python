donors = {'Mom': [2, 25], 'Dad': [2, 30], 'John': [3, 45], 'Jane': [5, 500],
          'Bob Smith': [2, 20]}


def createreport():
    """Create a detailed report of donors and their history"""
    donorreport = []
    for name in donors:
        totaldonation = (donors[name][1])
        donationtimes = (donors[name][0])
        avgdonate = round((totaldonation / donationtimes), 2)
        donorreport.append((name, totaldonation, donationtimes,
                            avgdonate))
    donorreport.sort(key=lambda x: x[1], reverse=True)
    print("\n\n\n")
    print("{:20} {:30} {:40} {:40}\n".format(
          "Name", "Total Donations", "# of Donations",
          "Avg. Donation"))
    for i in donorreport:
        print("{:20} {:<30} {:<40} {:<40}".format(
              i[0], i[1], i[2], i[3]))
    print("\n\n\n")


def get_name():
    while True:
        print("\nEnter 'list' to see list of names.")
        print("Enter 'quit' to go back.")
        name = input("Please enter a name: ")
        if (name == 'list'):
            show_list()
        elif (name == 'quit'):
            break
        elif (len(name) > 25):
            print("\nPlease use a name that is 25 charachters or less.")
        else:
            donation_amount = get_amount()
            if (donation_amount == 'quit'):
                break
            if (name not in donors):
                donors[name] = [1, donation_amount]
            else:
                donors[name][0] = donors[name][0] + 1
                donors[name][1] = donors[name][1] + donation_amount
            print_letter(name, donation_amount)
            break


def show_list():
    print("\nDonor Names:")
    print("-" * 20)
    for name in donors:
        print(name)


def get_amount():
    while True:
        print("\nPlease enter donation amount. "
              "Enter 'quit' to return to main menu.")
        donation = input("$")
        if (donation == 'quit'):
            return donation
        try:
            donation = float(donation)
            return donation
        except:
            print("\nSorry.  '$%s' is not a valid amount." % donation)


def save_letter(letter, name, amount):
    '''
    Save a copy of a Thank You letter to the local disk when the letter is sent
    '''
    file_name = '{}_{}'.format(name.replace(' ', '_'),
                               amount.replace('.', '_'))
    f = open(file_name, 'w')
    f.write(letter)
    f.close()


def print_letter(name, donation_amount):
    message = ("\nDear {},\n\nThank you for your most recent donation of ${}. "
               "To date, you have donated\na total of ${} to the "
               "Woman Cancer.  Our company greatly appreciates the\ncontinued "
               "generosity from individiuals like you.\n\nMay Hansen\n"
               "The Woman Cancer\n'Money for Lady'")
    message = (message.format(name, donation_amount, donors[name][1]))
    print(message)
    return message


def save_all():
    for name in list(donors.keys()):
        amount = donors[name][0] * donors[name][1]
        message = print_letter(name, amount)
        save_letter(message, name, str(amount))


if (__name__ == '__main__'):
    while True:
        print("\nPlease choose a menu option below:")
        print("Send a (T)hank you")
        print("Create a (R)eport")
        print("(S)ave all letters to disk")
        print("quit")
        menu_option = input("> ")
        if (menu_option == "T"):
            get_name()
        if (menu_option == "R"):
            createreport()
        if (menu_option == "S"):
            save_all()
        elif (menu_option == "quit"):
            break
        else:
            print("Sorry. '%s' is not a valid menu option." % menu_option)
