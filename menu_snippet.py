def user_menu(menu_items):
    # presents an indented menu to user to make selections
    # menu_items is a list of dicts
    # either {"level": x, "descr": some words} for headers
    # or w the addition of "selection": for selectable menu items
    # it returns the integer menu item selected, or "invalid" if bad input
    # SHOULD allow the selections to be strings like "pf1"

    l_acceptable_inputs = []

    #print the menu
    for x in menu_items:
        # set indent at 5 spaces per level
        padding = " " * 5 * x["level"]
        if "selection" in x:
            # it is not a header, print selection row format
            print(padding, "{:<3} {:60}".format(x["selection"], x["descr"]))
            # append to list of known valid inputs -- convert to string so comparisons are valid
            l_acceptable_inputs.append(str(x["selection"]))
        else:
            # it is a header, print header row format
            print(padding, x["descr"])
    print()

    # process user input
    user_selection = "invalid"
    while user_selection == "invalid":
        user_input = str(input("enter your selection number: "))
        if user_input in l_acceptable_inputs:
            user_selection = user_input
        else:
            print("that is not a valid entry")

    # user confirm their entry
    confirmed = False
    for x in menu_items:
        if "selection" in x:
            if user_selection == str(x["selection"]):
                print("you selected: ", x["descr"])
                input_yn = input("Enter y to proceed, anything else to cancel: ")
                if input_yn == "y":
                    confirmed = True
                else:
                    print("stopping")
                break

    if confirmed:
        print("let's go!")
    else:
        print("no match found")
        user_selection = "invalid"
    return(user_selection)


menu_items = [{"level": 0, "descr": "this is a header"},
              {"level": 1, "descr": "preflight selections"},
              {"level": 2, "selection": 1, "descr": "menu item 2"},
              {"level": 2, "selection": 2, "descr": "menu item 3"},
              {"level": 2, "descr": "submenu item 4000"},
              {"level": 3, "selection": 5, "descr": "menu item 5"},
              {"level": 3, "selection": 6, "descr": "menu item 6"},
              {"level": 0, "descr": "second main header"},
              {"level": 1, "selection": 7, "descr": "menu item 7"},
              {"level": 1, "selection": 8, "descr": "menu item 8"}
              ]

user_choice = user_menu(menu_items)

print("function returned", user_choice)