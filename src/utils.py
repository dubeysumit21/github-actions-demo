def is_even(n):
    return n % 2 == 0


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
