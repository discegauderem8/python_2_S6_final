from date_checker import check as ch
from sys import argv

if __name__ == "__main__":
    date = "00.00.0000"
    user_input = argv
    if len(user_input) >= 2:
        date = user_input[1]
    else:
        date = input("Введите дату в формате DD.MM.YYYY: ")

    print(ch(date))

