def check_armstrong(num):
    str_num = str(num)
    power = len(str_num)
    final_val = 0 
    for i in range(len(str_num)):
        final_val += int(str_num[i]) ** power
    if final_val == int(str_num):
        return True
    return False

if check_armstrong(153):
    print("Its a Armstrong Number")
else:
    print("Not a Armstrong number")
