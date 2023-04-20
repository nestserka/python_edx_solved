def is_a_before_b(string):
    count_a = 0
    count_b = 0
    for char in string:
        if char == 'a':
            count_a += 1
        elif char == 'b':
            count_b += 1
            if count_b <= count_a:
                return False
    return True
