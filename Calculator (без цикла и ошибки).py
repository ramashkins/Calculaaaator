n = '''
\033[32m████████████████████████████████████████████████████
      
\033[36m█──█─████───██─█────█──█─█─█───██─████─███─████─████
\033[36m█─█──█──█──█─█─█────█─█──█─█──█─█─█──█──█──█──█─█──█
\033[36m██───████─█──█─████─██───███─█──█─████──█──█──█─████
\033[36m█─█──█──█─█──█─█──█─█─█────█─█──█──█─█──█──█──█─█───
\033[36m█──█─█──█─█──█─████─█──█─███─█──█──█─█──█──████─█───
      
\033[32m████████████████████████████████████████████████████
'''
print(n)
import math
predislovie = '''Пожалуйста
            Указывайте данные для градусных мер в радианах
   при логарифме вас будут спрашивать 2 цифры пишите только вторую
   при степени или корня 1 цифра для первого аргумента, вторая для второго''' 
print(predislovie)                   
a = int(input("Введите первое число > "))
b =int(input("Введите второе число > "))
c = input("""
ВЫБЕРИТЕ ОДИН ИЗ ПРЕДЛОЖЕННЫХ ЗНАКОВ
[1]-ДЕЛЕНИЕ
[2]-УМНОЖЕНИЕ
[3]-СЛОЖЕНИЕ
[4]-ВЫЧИТАНИЕ
[5]-СТЕПЕНЬ
[6]-КОРЕНЬ
[7]-СИНУС
[8]-КОСИНУС
[9]-ЛОГАРИФМ
[10]-ФАКТОРИАЛ
""")
g = 0
if c == "1":
    g = a / b
    
elif c == "2":
    g = a * b
elif c == "3":
    g = a + b
elif c == "4":
    g = a- b
elif c == "5":
    g=math.pow(a, b)
elif c == "6":
    g=math.sqrt(a, b)
elif c == "7":
    g=math.sin(math.radians(b))
elif c == "8":
    g=math.cos(math.radians(b))
    
elif c == "9":
    g=math.log(a, b)
elif c == "10":
    g=math.factorial(b)
else:
    print("ошибкаа")
h = '''
\033[32m████████████████████████████████████████████████████

\033[36m████─███─████──███─████──\                       
\033[36m█──█──█──█──██─█────█───█|                        
\033[36m█──█──█──████──███──█────|           ██████████    ██
\033[36m█──█──█──█──██─█────█───█|                    ██   ██ 
\033[36m████──█──████──███──█────/                      ██ ██   
                                          ███████████
                                                  
\033[32m████████████████████████████████████████████████████'''
print(h, g)
while True:
    user=input("хоч еще")

    if user == "да":
        continue
    else:
        break