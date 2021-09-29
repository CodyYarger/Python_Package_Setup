#!/usr/bin/env python3
# 01/27/2021
# Dev: Cody Yarger
# Exercise 6.3: Mailroom Package

""" This module manages donors and their donations. Existing donor data is
read-in from a csv file. New donations are recorded by existing or new donors
and stored. Email objects are created thanking the donor for their donation.
Email text are written to .txt file objects. New donor data is stored to donor
file. """

from datetime import date
import sys
import os
import csv
# ===============================================================================
### GLOBAL ###
# ===============================================================================
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# read donor records csv file to donor dict object
with open((data_path + "/donor_csv.csv"), "r") as don_csv:
    donor = {}
    donor_readdict = csv.DictReader(don_csv)
    donor_l = list(donor_readdict)[0]
    # convert value string to list of floats
    for donor_names, dons in donor_l.items():
        donor[donor_names] = eval(dons)

TODAY = date.today()

# thank you email string
EMAIL = ("\n{}\n\nThank you, {} \n\n"
         "    Your ${:.2f} donation is really appreciated. It is donors like you that"
         " keep our services up and running.""\n\n    Your annual donation total to date "
         "is: ${:.2f}.\n\nSincerely, The Mailroom Team")

# current working directory to write letters to
cwd = os.getcwd()

# ===============================================================================
### Mailroom Functions ###
# ===============================================================================


def donor_list():
    """ produces indexed list of existing donors """
    email_menu_list = []
    for count, name in enumerate(sorted(donor)):
        email_menu_list.append("{:>5}{:>20}".format(count + 1, name))
    return email_menu_list


def print_list():
    """ prints the donor list to the console """
    for name in donor_list():
        print(name)


def get_email_string(total, *args):
    """ produces thank you email string object """
    # create email thank you message
    email_txt = EMAIL.format(TODAY, *args, total)
    return email_txt


def get_donor_data():
    """ records names and amount of new donors """
    # enter donor name and donor amount
    donor_name = input("Enter a donor name: ")

    while True:
        try:
            donor_amount = float(input("Enter a donation amount: "))
            break
        except ValueError:
            print("\n---- That is not a valid donation ---- \n")

    return (donor_name, donor_amount)


def add_donor_data(*args):
    """ adds new donor name and or donations to donor dict """
    # if entered donor_name in donor keys append donation else add new donor
    if args[0] in donor.keys():
        donor[args[0]].append(args[1])
    else:
        donor[args[0]] = [args[1]]

    # donor total for writing email files
    donor_total = sum(donor[args[0]])
    return donor_total


def print_donor_data():
    """ prints thankyou email for give donor data"""
    get_name_donation = get_donor_data()
    donor_total = add_donor_data(*get_name_donation)

    # print thank you email to terminal
    print(get_email_string(donor_total, *get_name_donation))


def get_report():
    """ tabulates the donor name, sum of all donations, number of donations and
    average donation, with formatting. returns report (list) of string objects """

    # initialize report list and define report categories
    report = []
    cat = ("Name", "Total ($)", "# Donations", "Average ($)")

    # report upper borders
    report.append("{:80}".format("-"*85))
    report.append("{:80}".format("-"*85))

    # report categories
    report.append("{0:>20}|{1:>20}|{2:>20}|{3:>20}".format(*cat))
    report.append("{:80}".format("-"*85))

    # define lists for sorting by total donation
    name = []
    don_totals = []
    num_don = []
    avg_don = []

    # for names and donations in donor compute, total, #donations, and average donation
    # and store to lists
    for names, donations in donor.items():
        name.append(names)
        don_totals.append(sum(donations))
        num_don.append(len(donations))
        avg_don.append(sum(donations)/len(donations))

    # unzip(sorted tuple of zipped (name, totals, num don, avg don))
    don_totals, name, num_don, avg_don = zip(*sorted(zip(don_totals, name, num_don, avg_don)))

    # for elem in don_totals append name, donor totals, #donations, and average donation
    for i, _ in enumerate(don_totals):
        # name, total, #donations, and average donation strings appended to report
        report.append("{:>20}|{:>20.2f}|{:>20}|{:>20.2f}".
                      format(name[-(i + 1)], don_totals[-(i + 1)], num_don[-(i + 1)], avg_don[-(i + 1)]))

    # report lower border
    report.append("{:80}".format("-"*85))
    return report


def print_report():
    """ print elements in get_report to console """
    # prints report (email string object) to terminal
    for row in get_report():
        print(row)


def exit_program():
    """Exits mailroom and saves state of donor dictionary to CSV """
    print("\n---     Saving Donor Records to CSV File     ---\n")
    try:
        with open((data_path + "/donor_csv.csv"), "w") as donor_csv:
            write = csv.DictWriter(donor_csv, donor.keys())
            write.writeheader()
            write.writerow(donor)
    except IOError:
        print("I/O error")
    print("--------------    Exiting Program    -------------- ")
    sys.exit(0)


def return_menu():
    """ exits sub-menu """
    print("Return to Main-Menu \n")
    return "exit menu"


def send_letters():
    """ writes thank you email.txt files for each donor in donor dictionary """
    # for names and donations write EMAIL to thankyou.txt
    for names, donations in donor.items():
        donor_total = sum(donor[names])
        with open((data_path + "/data/" + names + ".txt"), "w+t") as thankyou:
            thankyou.write(get_email_string(TODAY, *(names, donations[-1]), donor_total))


def menu_selection(prompt, dispatch_dict):
    """ dictionary switch function for main and sub menu """
    while True:
        while True:
            response = (input(prompt))
            try:
                _ = dispatch_dict[response]
                break
            except KeyError:
                print("\n---- That is not a valid selection ---- \n")

        # print(dispatch_dict[response]) # for testing
        if dispatch_dict[response]() == "exit menu":
            break


def email_menu():
    """ email_menu (is sub-menu) from main prompt """
    sub_prompt = """\nSub-Menu:
    Enter 'list' for a list of donors
    Enter 2 to enter a donor name
    Enter 3 to return to Main-Menu \n\nSelection: """

    sub_dispatch = {"list": print_list,
                    "2": print_donor_data,
                    "3": return_menu,
                    }

    menu_selection(sub_prompt, sub_dispatch)
