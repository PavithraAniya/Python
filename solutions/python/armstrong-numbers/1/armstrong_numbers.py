def is_armstrong_number(number):
    Sum_val=0
    str_num = str(number)
    length_num = len(str(number))
    for digit in str_num:
        val = int(digit) ** int(length_num)
        Sum_val += val
    if Sum_val== int(number):
        return True
    else:
        return False

 
 