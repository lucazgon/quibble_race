def menu(list):
    # print options to screen
    for obj in list:
        print(f"{list.index(obj)}) {obj}")

    # hold user until they input an acceptable input (which is a int)
    active = True
    while active == True:
        try:
            user_input = int(input(">"))
            if user_input >= 0 and user_input <= len(list):
                active = False
            else:
                print(f'please enter a number between 0 - {len(list)-1}')
        except:
            print(f'please enter a number between 0 - {len(list)-1}')
        
    return list[user_input]

if __name__ == "__main__":
    test_list = ["a","b","c","d"]
    menu(test_list)