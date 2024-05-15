from src.utils import (load_operations, get_filter_state, sorts_date, change_date_format, change_card, change_account)

list_json = load_operations()

state_executed = get_filter_state(list_json)
the_last_five_date = sorts_date(state_executed)
for operation in the_last_five_date:
    to_ = operation.get('to')
    currency_ = operation.get('operationAmount')
    amount = currency_.get('amount')
    from_ = operation.get('from')
    currency_in = currency_.get('currency')
    currency_name = currency_in.get('name')
    if operation['description'] == "Открытие вклада":
        print(f"{change_date_format(operation['date'])} {operation["description"]}")
        print(f'-> {change_account(to_)}')
        print(amount, currency_name, end='\n\n')
    else:
        print(f"{change_date_format(operation['date'])} {operation["description"]}")
        if from_:
            if 'Счет' not in from_:
                print(f'{change_card(from_)} -> {change_account(to_)}')
            else:
                print(f'{change_account(from_)} -> {change_account(to_)}')
        print(amount, currency_name, end='\n\n')
