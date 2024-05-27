from src.utils import (load_operations, get_filter_state, sorts_date, get_operation_info)


def main():
    list_json = load_operations()
    state_executed = get_filter_state(list_json)
    the_last_five_date = sorts_date(state_executed)[:5]

    for operation in the_last_five_date:
        get_operation_info(operation)


if __name__ == '__main__':
    main()
