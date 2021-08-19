def calculate_missing_ranges(array: list, lower: int, upper: int):
    ranges = []

    for i in range(0, len(array)-1):
        if array[i + 1] > array[i] >= lower and array[i]+1 != array[i+1] and array[i] < upper:
            lower_limit = array[i] + 1
            upper_limit = array[i + 1] - 1
            if lower_limit != upper_limit:
                ranges.append(f"{lower_limit}->{upper_limit}")
            else:
                ranges.append(f"{lower_limit}")
        i += 1
    if array[-1] <= upper:
        ranges.append(f"{array[-1] + 1}->{upper}")
    return ranges


if __name__ == "__main__":
    # case 1
    array = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    missing_ranges = calculate_missing_ranges(array, lower, upper)
    print(missing_ranges)

    # case 2
    array = [0, 1, 3, 50, 75]
    lower = 2
    upper = 50
    missing_ranges = calculate_missing_ranges(array, lower, upper)
    print(missing_ranges)
