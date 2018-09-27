import sys, os, pexpect
menu_actions  = {} 

def main_menu():
    os.system('clear')
       
    print "Welcome"
    print "Choose from menu:"
    print "1. Status & Rules"
    print "2. Add Firewall Rules from Any"
    print "3. Add Firewall Rules from IP"
    print "4. Add Subnet to allow on a single port"
    print "5. Add single port to deny from ANY"
    print "6. Add single port to deny from specific IP"
    print "7. Add Subnet to deny on a single port"
    print "8. Delete Rule"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
 
    return

def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again."
            menu_actions['main_menu']()
# Status
def UFW1():
    print "UFW Status!"
    p = pexpect.spawn('/bin/bash -c "ufw status"')
    p.expect(pexpect.EOF)
    print(p.before)
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


# Add from Any
def UFW2():
    port = raw_input("Enter the port you want to open : ")
    p = pexpect.spawn('/bin/bash -c "ufw allow "' + port)
    p.expect(pexpect.EOF)
    print(p.before)
    print "1. Status & Rules"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()

# Add single IP to port
def UFW3():
    port = raw_input("Enter the port you want to open for : ")
    IP = raw_input("Enter the IP Address : ")
    p = pexpect.spawn('/bin/bash -c "ufw allow from '+ IP + " to " "any port "+ port)
    p.expect(pexpect.EOF)
    print(p.before)
    print "1. Status & Rules"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Add a subnet CIDR to UFW Allow
def UFW4():
    port = raw_input("Enter the port you want to open for : ")
    iprange = raw_input("Enter your subnet i.e. 1.1.1.0 : ")
    subnet = raw_input("Please enter your subnet i.e. /24 : ")
    p = pexpect.spawn('/bin/bash -c "ufw allow from ' + iprange + "/" + subnet + " to " + " any port " + port)
    p.expect(pexpect.EOF)
    print(p.before)
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    menu_actions['main_menu']()

# Deny port from Any
def UFW5():
    port = raw_input("Enter the port you want to block : ")
    p = pexpect.spawn('/bin/bash -c "ufw deny "' + port)
    p.expect(pexpect.EOF)
    print(p.before)
    print "1. Status & Rules"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

    # Deny port from single IP
def UFW6():
    port = raw_input("Enter the port you want to block : ")
    IP = raw_input("Enter the IP you want to block : ")
    p = pexpect.spawn('/bin/bash -c "ufw deny from '+ IP + " to " "any port "+ port)
    p.expect(pexpect.EOF)
    print(p.before)
    print "1. Status & Rules"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
     # Add a subnet CIDR to UFW Deny single port
def UFW7():
    port = raw_input("Enter the port you want to open for : ")
    iprange = raw_input("Enter your subnet i.e. 1.1.1.0 : ")
    subnet = raw_input("Please enter your subnet i.e. /24 : ")
    p = pexpect.spawn('/bin/bash -c "ufw deny from ' + iprange + "/" + subnet + " to " + " any port " + port)
    p.expect(pexpect.EOF)
    print(p.before)
    print "1. Status & Rules"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

     # List Rules numbered and delete
def UFW8():
    p = pexpect.spawn('/bin/bash -c "ufw status numbered"')
    p.expect(pexpect.EOF)
    print(p.before)
    rule = raw_input("Enter the rule number to delete : ")
    p = pexpect.spawn('/bin/bash -c "yes | ufw delete "' + rule)
    p.expect(pexpect.EOF)
    print(p.before)
    print "1. Status & Rules"
    print "8. Delete another rule"
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

#Exit
def exit():
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    '1': UFW1,
    '2': UFW2,
    '3': UFW3,
    '4': UFW4,
    '5': UFW5,
    '6': UFW6,
    '7': UFW7,
    '8': UFW8,
    '9': back,
    '0': exit,
}
 
if __name__ == "__main__":
    main_menu()
