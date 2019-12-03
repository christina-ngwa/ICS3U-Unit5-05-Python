#!/usr/bin/env python3

# Created by : Christina Ngwa
# Created on : November 2019
# This program formats mailing addresses according to Canada Post


def canada_post(name, street, city, province, postal, apt_num=None):
    # This program formats mailing addresses according to canada post

    # process
    if apt_num is not None:
        formatted = name + "\n" + apt_num + "-" + street + "\n" + city + \
                    " " + province + "  " + postal
    else:
        formatted = name + "\n" + street + "\n" + city + " " + \
                    province + "  " + postal
    return formatted


def main():
    # Gets user's details to format for mailing
    user_apt_num = None

    # Output
    print("Welcome to the Canada Post address formatter.")
    print("For validity, please input with precision (upper case is ideal).")
    print("")

    # Input
    user_name = input("Enter full name: ")
    question = input("Does recipient live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        user_apt_num = input("Enter apartment number: ")
    user_street = input("Enter street name and number: ")
    user_city = input("Enter city: ")
    user_province = input("Enter province/territory: ")
    user_postal = input("Enter postal code: ")

    # call function
    if user_apt_num is not None:
        formatted_address = canada_post(user_name, user_street, user_city,
                                        user_province, user_postal,
                                        user_apt_num)
    else:
        formatted_address = canada_post(user_name, user_street, user_city,
                                        user_province, user_postal)
    print("")
    print("Formatted:")
    print(formatted_address)


if __name__ == "__main__":
    main()
