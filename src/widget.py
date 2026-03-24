from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card):
    num = "1234567890"
    i_test = 0
    for i in name_card:
        if i in num:
            print(f"{name_card[0:i_test-1]} {name_card[i_test:i_test+4]} {name_card[i_test+4:i_test+6]}** **** {name_card[-4:]}")
            break
        i_test += 1

input_card_number = input("Введите номер своей банковской карты: ")
input_mask_account = input("Введите номер своего счета: ")

get_mask_card_number(input_card_number)
get_mask_account(input_mask_account)
