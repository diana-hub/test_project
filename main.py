def return_slice_from_the_beginning(text, n):
    return text[:n]


def get_even_numbers(number):
    x = []
    for i in range(0, number):
        if i % 2 == 0:
            x.append(i)
    return x


def get_upper_case_if_even(text):
    list_of_words = text.split(' ')
    list_result = []
    count = 0
    for u in list_of_words:
        print(count)
        if count % 2 == 0:
            word = u.upper()
        else:
            word = u.lower()
        list_result.append(word)
        count = count + 1
    return ' '.join(list_result)


def get_letters_up_low(text):
    list_of_symbols = []
    count = 0
    for i in text:
        print(count)
        if i == ' ':
            list_of_symbols.append(i)
            continue
        if count % 2 == 0:
            symbol = i.lower()
        else:
            symbol = i.upper()
        list_of_symbols.append(symbol)
        count = count + 1
    return ''.join(list_of_symbols)


def is_even_number(number):
    if number % 2 == 0 and number % 3 == 0:
        return 'Диана молодец!'
    if number % 4 == 0:
        return 'Паша молодец!'

    return False

def factorial(number):
    x = 1
    for item in range(1,number+1):
        x = x*item
    return x



if __name__== '__main__':
    print(factorial(10))

