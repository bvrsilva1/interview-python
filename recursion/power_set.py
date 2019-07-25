
def calculate_power_set(set_string):
    result = []
    result.append('')

    if len(set_string) > 0:
        for current in range(0, len(set_string)):
            wall = len(result)
            for in_result in range(0, wall):
                result.append(result[in_result] + '' + set_string[current])

    return result


set_string = "abc"
print(calculate_power_set(set_string))
