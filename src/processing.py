def filter_by_state(list_transitions, state="EXECUTED"):
    new_list_transactions = []

    for transition in list_transitions:
        if transition["state"] == "":
            transition["state"] = "EXECUTED"

        if transition["state"] == "state":
            new_list_transactions.append(transition)

    return new_list_transactions


def sort_by_date(list_transitions, reverse=False):
    new_list_transactions = sorted(
        list_transitions, key=lambda x: x["date"], reverse=reverse
    )

    return new_list_transactions


# Пример списка транзакций
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-15T10:30:00.000",
        "amount": 5000
    },
    {
        "id": 2,
        "state": "CANCELED",
        "date": "2024-01-10T14:20:00.000",
        "amount": 1000
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2024-01-20T09:15:00.000",
        "amount": 7500
    },
    {
        "id": 4,
        "state": "CANCELED",
        "date": "2024-01-25T03:05:00.000",
        "amount": 6752
    },
    {
        "id": 5,
        "state": "",
        "date": "2024-01-05T05:10:00.000",
        "amount": 1337
    },
]

executed = filter_by_state(transactions)
canceled = filter_by_state(transactions, "CANCELED")

sorted_desc = sort_by_date(transactions)
sorted_asc = sort_by_date(transactions, reverse=False)

print("Фильтр EXECUTED:", executed)
print("Фильтр CANCELED:", canceled)
print("Сортировка (новые сверху):", sorted_desc)
print("Сортировка (старые сверху):", sorted_asc)
