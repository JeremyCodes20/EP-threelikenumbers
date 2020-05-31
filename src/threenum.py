def three_num(value):
    total = 0  # total substrings
    str_value = str(value)

    for start_index in range(len(str_value)):
        for end_index in range(start_index + 1, len(str_value) + 1):
            sub_value = int(str_value[start_index:end_index])

            if sub_value % 3 == 0:
                total += 1

    return total


def is_three_like(value):
    if three_num(value) % 3 == 0:
        return True
    else:
        return False
