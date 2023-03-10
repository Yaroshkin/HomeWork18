# Реализуйте класс стека для работы со строками (стек строк). 
# Стек должен иметь фиксированный размер. Реализуйте набор операций для работы со стеком: 
# ■ помещение строки в стек; 
# ■ выталкивание строки из стека; 
# ■ подсчет количества строк в стеке; 
# ■ проверку пустой ли стек; 
# ■ проверку полный ли стек; 
# ■ очистку стека; 
# ■ получение значения без выталкивания верхней строки из стека. 
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию.

n = int(input("Введите ограничение стека: "))


class Stack:
    def __init__(self, n):
        self.__li = []
        self.n = n

    # ■ помещение строки в стек
    def push(self, value):
        if len(self.__li) < self.n:
            self.__li.append(value)
        else:
            print("Много ")
    
    # ■ выталкивание строки из стека
    def pop(self):
        if len(self.__li):
            return self.__li.pop()

    # ■ подсчет количества строк в стеке
    def count(self):
        print(f"Кол-во строк в стеке {len(self.__li)}")

    # ■ проверку пустой ли стек
    def zero(self):
        if self.__li == []:
            print("Стек пустой ")
        else:
            print("Что-то есть ")

    # ■ проверку полный ли стек
    def full(self):
        if len(self.__li) == self.n :
            print(f"Стек заполнен {self.__li}")
        else:
            print("Error")
    
    # ■ очистку стека
    def clean(self):
        self.__li.clear()

    # ■ получение значения без выталкивания верхней строки из стека.
    def no_up(self):
        print(self.__li[-1])

    def pr(self):
        print(self.__li)


stack = Stack(n)
# stack.push(4)   
# stack.push(2)
# stack.push(3)
# stack.push(5)
# print(stack.clean())   
# print(stack.zero())
# print(stack.no_up())
# print(stack.full())

while True:
    enter = str(input("Введите что сделать: a - добавление в стек, d - віталкивание, b - подсчет кол-ва строк,\n c - очистка стека, f - проверка полний , x - пустой, v - получение значения без выталкивания верхней строки из стека\n e - віход "))
   
    if enter == "c":
        stack.clean()
        print("Стек очищен ")
    elif enter == 'a':
        stack.push(input("Введите чем наполнить "))
        print(stack.pr())
    elif enter == 'd':
        stack.pop()
    elif enter == 'b':
        stack.count()
    elif enter == 'f':
        stack.full()
    elif enter == 'x':
        stack.zero()
    elif enter == 'v':
        stack.no_up()
    elif enter == 'e':
        break