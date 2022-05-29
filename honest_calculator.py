msg_ = ["Enter an equation",  # msg_0
"Do you even know what numbers are? Stay focused!",  # msg_1
"Yes ... an interesting math operation. You've slept through all classes, haven't you?",  # msg_2
"Yeah... division by zero. Smart move...",  # msg_3
"Do you want to store the result? (y / n):",  # msg_4
"Do you want to continue calculations? (y / n):",  # msg_5
" ... lazy",  # msg_6
" ... very lazy",  # msg_7
" ... very, very lazy",  # msg_8
"You are",  # msg_9
"Are you sure? It is only one digit! (y / n)",  # msg_10
"Don't be silly! It's just one number! Add to the memory? (y / n)",  # msg_11
"Last chance! Do you really want to embarrass yourself? (y / n)",]  # msg_12

def calc(x, y, oper):
    if oper == "+":
        answer = x + y
    elif oper == "-":
        answer = x - y
    elif oper == "*":
        answer = x * y
    elif oper == "/":
        answer = x / y
    return answer
    
def is_one_digit(v):
    return (-10 < v < 10) and v.is_integer() 
    
def check(v1, v2, v3):
    global msg_
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_[7]
    if (v1 == 0 or v2 == 0) and v3 in "+-*":
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)
        
memory = float(0)

while True:
    x, oper, y = input(msg_[0]).split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        
        if oper in '+-*/':
            check(x, y, oper)
        else:
            raise TypeError
        
        result = calc(x, y, oper)
        print(result)

        flag_0 = True
        while flag_0:
            resp_0 = input(msg_[4])
            if resp_0 == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    flag_1 = True
                    while True:
                        resp_1 = input(msg_[msg_index])
                        if  resp_1 == 'y' and msg_index < 12:
                            msg_index += 1
                        elif resp_1 == 'y' and msg_index <= 12:
                            memory = result
                            flag_0 = False
                            break
                        elif resp_1 == 'n':
                            flag_0 = False
                            break
                else:
                    memory = result
                    break
            elif resp_0 == 'n':
                break
                
        
        if input(msg_[5]) == 'n':
            break
            
    except ValueError:
        print(msg_[1])
    except TypeError:
        print(msg_[2])
    except ZeroDivisionError:
        print(msg_[3])
