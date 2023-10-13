#банкомат!!
from num2words import num2words

def translate_summ(summ):

    if summ < 1 or summ > 100000:
        return "Банкомат принимает сумму от 1 до 100 000"
    
    words = num2words(summ, lang='ru')

    last_digit = summ % 10

    if last_digit == 1 and summ % 100 != 11:
        currency = "рубль"
    elif 2 <= last_digit <= 4 and (summ % 100 < 10 or summ % 100 >= 20):
        currency = "рубля"
    else:
        currency = "рублей"

    result = words.capitalize() + " " + currency

    return result
    return result

summ = int(input("Введите сумму от 1 до 100000: "))
result = translate_summ(summ)

print(result)