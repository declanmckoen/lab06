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
    print(encode(input()))

if __name__ == "__main__":
    main()