def comp(num):
    last_digit1 = num % 10
    last_digit2 = num % 100
    if last_digit2 >= 11 and last_digit2 <=20:
        return f'{num} компьютеров'
    elif last_digit1 == 1:
        return f'{num} компьютер'
    elif last_digit1 > 1 and last_digit1 <= 4:
        return f'{num} компьютера' 
    else: 
        return f'{num} компьютеров'

if __name__ == '__main__':
    print( comp(20))