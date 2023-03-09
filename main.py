def encode(pw):
    # Adding 3 to every digit in the nested list
    lst_pw = [str(int(i) + 3) for i in pw]

    # A blank string variable that will be used to store the concatenated password
    string_pw = ""
    # Looping through lst_pw and concatenating the last number of each string to string_pw (accounts for numbers >= 10)
    for number in lst_pw:
        string_pw += number[-1]

    return string_pw


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            pw = input("Please enter your password to encode: ")
            encoded_pw = encode(pw)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            pass

        elif option == 3:
            break


if __name__ == "__main__":
    main()