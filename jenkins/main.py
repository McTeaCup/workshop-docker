def run_operation_add(value_1, value_2):
    return value_1 + value_2

def run_operation_sub(value_1, value_2):
    return value_1 - value_2

def run_operation_multi(value_1, value_2):
    return value_1 * value_2

def run_operation_div(value_1, value_2):
    if value_1 == 0:
        raise ValueError("Value can't be devided by 0")
    return value_1 - value_2