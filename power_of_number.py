def power_of_number(base, exp):
    assert exp >= 0 and int(exp), "The exponent must be a positive integer only!"
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * power_of_number(base, exp-1)


print(power_of_number(3, 3))
