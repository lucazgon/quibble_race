def menu(list):

    '''
    |---player--|
    |   -racers
            -a 2:1
            -b 1:1
            -c 3:1 *        |           
    |   -bet amount        |
    |-----------|
    '''


    # print options to screen
    if len(list) <= 0:
        raise Exception("Menu needs to have at least 1 item")
    for obj in list:
        #print(type(obj))
        if (type(obj).__name__ == "str" or type(obj).__name__ == "int"):
            print(f"{list.index(obj)}) {obj}")
        elif type(obj).__name__ == "Racer":
            print(f"{list.index(obj)}) {obj.name}")

    error_message = f'please enter a number between 0 - {len(list)-1}'
    user_input = 0
    
    while True:
        # check if user enters ctrl + c to quit
        try:
            user_input = input(">")
        except KeyboardInterrupt:
            print('\nSIGINT detected: Quitting Program')
            quit()
        # check if the user input can be converted to a integer, if not repeat
        try:
            user_input = int(user_input)
        except:
            print(error_message)
            continue
        # check if the user input fits within the bounds of the menu list
        if user_input >= 0 and user_input <= len(list)-1:
            break
        else: 
            print(error_message) 
    
    #print(list[user_input])
    return list[user_input]

def input_validation():
    while True:
        # check if user enters ctrl + c to quit
        try:
            user_input = input(">")
        except KeyboardInterrupt:
            print('\nSIGINT detected: Quitting Program')
            quit()
        if len(user_input) > 15:
            print("please enter a name UNDER 15 characters")
            continue
        else:
            break
    return user_input

if __name__ == "__main__":
    test_list = ['a','b','c','d']
    menu(test_list)