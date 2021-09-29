#!/usr/bin/env python3
# 01/27/2021
# Dev: Cody Yarger
# Exercise 6.3: Mailroom Package

"""unit tests for mailroom.py functions"""
from datetime import date
from mailroom.tools import mailroom_tools

# date for test_get_email_string
TODAY = date.today()


def test_donor_list():
    expected = '    1         Average Joe'
    assert mailroom_tools.donor_list()[0] == expected


def test_get_email_string():
    assert ("Thank you, Test") in mailroom_tools.get_email_string(TODAY, "Test", 111, 1111)


def test_add_donor_data():
    assert mailroom_tools.add_donor_data("Test 1", 111) == 111


def test_get_report():
    test = ""
    report = mailroom_tools.get_report()
    test_l = [letter for elem in report for letter in elem if letter.isalpha()]
    test = "".join(test_l)
    assert "NameTotalDonationsAverage" in test
