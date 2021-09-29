#!/usr/bin/env python3
# 01/27/2021
# Dev: Cody Yarger
# Exercise 6.3: Mailroom Package

""" Entry point for mailroom package """

from mailroom.tools import mailroom_tools

# ===============================================================================
### main() ###
# ===============================================================================


def main():
    """ console_script entry point for mailroom package """

    main_prompt = """\nMain-Menu:
    Enter 1 to record a donation and send a Thank You
    Enter 2 to get a donor report
    Enter 3 to send letters to all donors
    Enter 4 to exit and save donor data \n\nSelection: """

    main_dispatch = {"1": mailroom_tools.email_menu,
                     "2": mailroom_tools.print_report,
                     "3": mailroom_tools.write_letters,
                     "4": mailroom_tools.exit_program,
                     }

    # header at program start
    print("_____________________________________________________")
    print("               Donor Management Tool                 ")
    print("{:30}".format("-"*53))

    # call menu selection to display prompt and get 'response'
    mailroom_tools.menu_selection(main_prompt, main_dispatch)

    print("{:30}".format("-"*53))
    print()


# ===============================================================================
if __name__ == "__main__":
    main()
