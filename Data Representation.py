letters = {
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F",
    16:"G"

}

while True:
    a = []
    for x in (input()):
        for keys, value in letters.items():
            if x == value:
                x = keys
        a.append(int(x))
    from_base = int(input("From Base "))
    raise_power = 0
    a = reversed(a)
    result = 0
    for y in a:
        result += y * from_base**raise_power
        print(f"{y} * {from_base} ** {raise_power} = {result}")
        raise_power += 1
    list_remainder = ""
    to_base = int(input("To Base "))
    while result != 0:
        divisor = result/to_base
        remainder = ((divisor - int(divisor)) * to_base)
        print(f"{result} / {to_base} = {divisor} - {int(divisor)} == {divisor - int(divisor)} * {to_base} = {remainder}")
        remainder = round(remainder)
        if remainder in letters:
            remainder = letters.get(remainder)
        list_remainder += (str(remainder))
        result = int(divisor)
    print(list_remainder[::-1])
