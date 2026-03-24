from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card):
    pass


input_card_number = input("Введите номер своей банковской карты: ")
input_mask_account = input("Введите номер своего счета: ")

get_mask_card_number(input_card_number)
get_mask_account(input_mask_account)
