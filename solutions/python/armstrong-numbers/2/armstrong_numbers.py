def is_armstrong_number(number):
    sum_val=0
    str_num = str(number)
    length_num = len(str(number))
    for digit in str_num:
        val = int(digit) ** int(length_num)
        sum_val += val
    if sum_val== int(number):
        return True
    else:
        return False

 
 