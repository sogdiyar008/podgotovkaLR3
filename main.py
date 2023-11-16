# class Cars:
#     def go(self):
#         pass
# my_car=Cars()
# my_car.go() #переменная май кар отсылается и использует метод го() у которого нет аргументов

###############
#2222222222222#
###############

# class Book:
#     def __init__(self, book, author, publisher):
#         self.book=book
#         self.author=author
#         self.publisher=publisher
#
#     def get_book(self):
#         return self.book
#
#     def set_book(self, book):
#         self.book = book
#
#     def get_author(self):
#         return self.author
#
#     def set_author(self, new_author):
#         self.author = new_author
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_publisher(self, new_publisher):
#         self.publisher = new_publisher
#
#     def __str__(self):
#         return f"Book: {self.book}\nAuthor: {self.author}\nPublisher: {self.publisher}\n"
#
# #
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner")
# print(book1)
# book1.set_publisher("Vintage Classics")
# print(book1)


#########
#3333333#
#########
# class Pet:
#     def __init__(self):
#         self._name = ""
#         self._animal_type = ""
#         self._age = 0
#
#     def set_name(self, name):
#         self._name = name
#
#     def set_animal_type(self, animal_type):
#         self._animal_type = animal_type
#
#     def set_age(self, age):
#         self._age = age
#
#     def get_name(self):
#         return self._name
#
#     def get_animal_type(self):
#         return self._animal_type
#
#     def get_age(self):
#         return self._age
#
#
# pet = Pet()
#
# name = input("Введите имя вашего домашнего животного: ")
# pet.set_name(name)
#
# animal_type = input("Введите тип вашего домашнего животного: ")
# pet.set_animal_type(animal_type)
#
# age = input("Введите возраст вашего домашнего животного: ")
# pet.set_age(age)
#
# print("Информация о вашем домашнем животном:")
# print("Имя:", pet.get_name())
# print("Тип:", pet.get_animal_type())
# print("Возраст:", pet.get_age())

########
#444444#
########

# class Car:
#     def __init__(self, year_model, make):
#         self._year_model = year_model
#         self._make = make
#         self._speed = 0
#
#     def accelerate(self):
#         self._speed += 5
#
#     def brake(self):
#         self._speed -= 5
#
#     def get_speed(self):
#         return self._speed
#
#
# car = Car("2022", "Toyota")
#
# print("\nПри ускорении:")
# for i in range(5):
#     car.accelerate()
#     print("Текущая скорость:", car.get_speed())
#
# print("\nПри торможении:")
# for i in range(5):
#     car.brake()
#     print("Текущая скорость:", car.get_speed())


############
#5555555555#
############

# class Information:
#     def __init__(self, name, address, age, phone):
#         self._name = name
#         self._address = address
#         self._age = age
#         self._phone = phone
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name
#
#     def get_address(self):
#         return self._address
#
#     def set_address(self, address):
#         self._address = address
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, age):
#         self._age = age
#
#     def get_phone(self):
#         return self._phone
#
#     def set_phone(self, phone):
#         self._phone = phone
#
#     def get_all_info(self):
#         return f'''имя: {self._name}
# адрес: {self._address}
# возраст: {self._age}
# телефонный номер: {self._phone}
# '''
#
#
# my_info = Information("Сaгдияр", "2-я улица 27а г.Бишкек", 15, "+996 706 79 11 25")
# friend1_info = Information("Артем", "да фиг его, уже непомню :_)", 16, "+996 705 34 43 **")
# friend2_info = Information("Мама", "2-я улица 27а г.Бишкек", 42, "+996 706 01 06 **")
#
# print("Ваши данные:")
# print(my_info.get_all_info())
#
# my_info.set_name("Согдияр")
# my_info.set_address("ЮП30 КВ41")
# my_info.set_age(16)
# my_info.set_phone("+7 950 321 98 69")
#
# print("Обновленные данные о вас:")
# print(my_info.get_all_info())
#
#
# print("Данные друга 1:")
# print(friend1_info.get_all_info())
#
# print("Данные друга 2:")
# print(friend2_info.get_all_info())

########
#666666#
########

# class Employee:
#     def __init__(self, name, ID_number, department,position):
#         self.name=name
#         self.ID_number=ID_number
#         self.department=department
#         self.position=position
#
#     def get_all_info(self):
#         print(f'''имя: {self.name}
# идентификационный номер: {self.ID_number}
# отдел: {self.department}
# должность: {self.position}
# ''')
#
# employee1=Employee('Сьюзан Мейерс',47899,"Бухгалтерия",'Вице-Президент')
# employee2=Employee("Марк Джоунс",39119,"ИТ",'Программист')
# employee3=Employee("Джой Роджерс",81774,"Производственный","Инженер")
#
# employee1.get_all_info()
# employee2.get_all_info()
# employee3.get_all_info()

###########
#777777777#
###########


# class Retailitem:
#     def __init__(self, name, kol_vo,price):
#         self.name=name
#         self.kol_vo=kol_vo
#         self.price=price
#
#     def get_all_info(self):
#         print(f'''название: {self.name}
# количество: {self.kol_vo}
# цена: {self.price}
# ''')
#
# employee1=Retailitem('Пиджак',12,59.95)
# employee2=Retailitem("джинсы",40,34.95)
# employee3=Retailitem("рубашка",20 ,24.95)
#
# employee1.get_all_info()
# employee2.get_all_info()
# employee3.get_all_info()

###########
#888888888#
###########

# class Patient:
#     def __init__(self, first_name, middle_name, last_name, address, city, region, postal_code, phone, emergency_contact_name, emergency_contact_phone):
#         self._first_name = first_name
#         self._middle_name = middle_name
#         self._last_name = last_name
#         self._address = address
#         self._city = city
#         self._region = region
#         self._postal_code = postal_code
#         self._phone = phone
#         self._emergency_contact_name = emergency_contact_name
#         self._emergency_contact_phone = emergency_contact_phone
#
#     def get_first_name(self):
#         return self._first_name
#
#     def set_first_name(self, first_name):
#         self._first_name = first_name
#
#     def get_middle_name(self):
#         return self._middle_name
#
#     def set_middle_name(self, middle_name):
#         self._middle_name = middle_name
#
#     def get_last_name(self):
#         return self._last_name
#
#     def set_last_name(self, last_name):
#         self._last_name = last_name
#
#     def get_address(self):
#         return self._address
#
#     def set_address(self, address):
#         self._address = address
#
#     def get_city(self):
#         return self._city
#
#     def set_city(self, city):
#         self._city = city
#
#     def get_region(self):
#         return self._region
#
#     def set_region(self, region):
#         self._region = region
#
#     def get_postal_code(self):
#         return self._postal_code
#
#     def set_postal_code(self, postal_code):
#         self._postal_code = postal_code
#
#     def get_phone(self):
#         return self._phone
#
#     def set_phone(self, phone):
#         self._phone = phone
#
#     def get_emergency_contact_name(self):
#         return self._emergency_contact_name
#
#     def set_emergency_contact_name(self, emergency_contact_name):
#         self._emergency_contact_name = emergency_contact_name
#
#     def get_emergency_contact_phone(self):
#         return self._emergency_contact_phone
#
#     def set_emergency_contact_phone(self, emergency_contact_phone):
#         self._emergency_contact_phone = emergency_contact_phone
#
# patient = Patient("саша", "сашович", "сашов", "сашинская 12", "сашгород", "сашово", "сшсшсшшсшшсш",
#                   "2312313123123", "сашилий", "саававаа")
#
# print("Данные пациента:")
# print("Имя:", patient.get_first_name())
# print("Отчество:", patient.get_middle_name())
# print("Фамилия:", patient.get_last_name())
# print("Адрес:", patient.get_address())
# print("Город:", patient.get_city())
# print("Область:", patient.get_region())
# print("Почтовый индекс:", patient.get_postal_code())
# print("Телефонный номер:", patient.get_phone())
# print("Имя контактного лица для экстренной связи:", patient.get_emergency_contact_name())
# print("Телефон контактного лица для экстренной связи:", patient.get_emergency_contact_phone())
#
# patient.set_first_name("паша")
# patient.set_address("пашов 433")
# patient.set_phone("пшпшпшшпшп")
#
# print("Обновленные данные пациента:")
# print("Имя:", patient.get_first_name())
# print("Адрес:", patient.get_address())
# print("Телефонный номер:", patient.get_phone())




# class Procedure:
#     def __init__(self, name, date, doctor, cost):
#         self.name = name
#         self.date = date
#         self.doctor = doctor
#         self.cost = cost
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_date(self):
#         return self.date
#
#     def set_date(self, date):
#         self.date = date
#
#     def get_doctor(self):
#         return self.doctor
#
#     def set_doctor(self, doctor):
#         self.doctor = doctor
#
#     def get_cost(self):
#         return self.cost
#
#     def set_cost(self, cost):
#         self.cost = cost
#
#     def get_all(self):
#         print(f'''имя: {self.name}
# дата: {self.date}
# доктор: {self.doctor}
# стоимость: {self.cost}
# ''')
#
#
# class Patient:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# patient = Patient("Иванов", 30)
#
# procedure1 = Procedure("врачебный осмотр", "сегодня", "ирвин", 250)
# procedure2 = Procedure("рентгеноскопия", "сегодня", "Джемисон", 500)
# procedure3 = Procedure("анализ крови", "сегодня", "Смит", 200)
#
# procedure1.get_all()
# procedure2.get_all()
# procedure3.get_all()



##################
#9999999999999999#
##################

# class Employee:
#     def __init__(self, employee_id, name, department, position):
#         self.employee_id = employee_id
#         self.name = name
#         self.department = department
#         self.position = position
#
#     def display_info(self):
#         print(f"ID: {self.employee_id}, Имя: {self.name}, Отдел: {self.department}, Должность: {self.position}")
#
# employees_dict = {}
#
# def find_employee(employee_id):
#     if employee_id in employees_dict:
#         employees_dict[employee_id].display_info()
#     else:
#         print("Сотрудник не найден.")
#
# def add_employee(employee_id, name, department, position):
#     new_employee = Employee(employee_id, name, department, position)
#     employees_dict[employee_id] = new_employee
#     print("Сотрудник добавлен.")
#
# def update_employee(employee_id, name, department, position):
#     if employee_id in employees_dict:
#         employees_dict[employee_id].name = name
#         employees_dict[employee_id].department = department
#         employees_dict[employee_id].position = position
#         print("Информация о сотруднике обновлена.")
#     else:
#         print("Сотрудник не найден.")
#
# def delete_employee(employee_id):
#     if employee_id in employees_dict:
#         del employees_dict[employee_id]
#         print("Сотрудник удален.")
#     else:
#         print("Сотрудник не найден.")
#
# while True:
#     print("\nМеню:")
#     print("1. Найти сотрудника")
#     print("2. Добавить нового сотрудника")
#     print("3. Изменить информацию о сотруднике")
#     print("4. Удалить сотрудника")
#     print("5. Выйти из программы")
#
#     choice = input("Выберите действие (1-5): ")
#
#     if choice == "1":
#         employee_id = input("Введите ID сотрудника: ")
#         find_employee(employee_id)
#     elif choice == "2":
#         employee_id = input("Введите ID нового сотрудника: ")
#         name = input("Введите имя: ")
#         department = input("Введите отдел: ")
#         position = input("Введите должность: ")
#         add_employee(employee_id, name, department, position)
#     elif choice == "3":
#         employee_id = input("Введите ID сотрудника для изменения: ")
#         name = input("Введите новое имя: ")
#         department = input("Введите новый отдел: ")
#         position = input("Введите новую должность: ")
#         update_employee(employee_id, name, department, position)
#     elif choice == "4":
#         employee_id = input("Введите ID сотрудника для удаления: ")
#         delete_employee(employee_id)
#     elif choice == "5":
#         print("Программа завершена.")
#         break
#     else:
#         print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")


######################
#10#10#10#10#10#10#10#
######################

# class RetailItem:
#     def __init__(self, description, units_in_stock, price):
#         self.description = description
#         self.units_in_stock = units_in_stock
#         self.price = price
#
#     def display_info(self):
#         print(f"Описание товара: {self.description}")
#         print(f"Количество на складе: {self.units_in_stock}")
#         print(f"Цена: ${self.price}")
#         print()
#
#
# class CashRegister:
#     def __init__(self):
#         self.items = []
#
#     def purchase_item(self, retail_item):
#         self.items.append(retail_item)
#
#     def get_total(self):
#         total_cost = sum(item.price for item in self.items)
#         return total_cost
#
#     def show_items(self):
#         for item in self.items:
#             item.display_info()
#
#     def clear(self):
#         self.items = []
#
#
# cash_register = CashRegister()
#
# item1 = RetailItem("Пиджак", 12, 59.95)
# item2 = RetailItem("Дизайнерские джинсы", 40, 34.95)
# item3 = RetailItem("Рубашка", 20, 24.95)
#
# cash_register.purchase_item(item1)
# cash_register.purchase_item(item2)
# cash_register.purchase_item(item3)
#
# print("Выбранные товары:")
# cash_register.show_items()
#
# total_cost = cash_register.get_total()
# print(f"\nОбщая стоимость: ${total_cost:.2f}")
#
# cash_register.clear()

###################
#11#11#11#11#11#11#
###################


# class Question:
#     def __init__(self, question, option1, option2, option3, option4, correct_answer):
#         self.question = question
#         self.option1 = option1
#         self.option2 = option2
#         self.option3 = option3
#         self.option4 = option4
#         self.correct_answer = correct_answer
#
#     def display_question(self):
#         print(self.question)
#         print(f"1. {self.option1}")
#         print(f"2. {self.option2}")
#         print(f"3. {self.option3}")
#         print(f"4. {self.option4}")
#
#     def set_correct_answer(self, correct_answer):
#         self.correct_answer = correct_answer
#
#     def get_correct_answer(self):
#         return self.correct_answer
#
#
# question1 = Question("Вопрос 1: сколько пород котов в Бизнес Кэтс?",  "1","4", "2","3", 2)
# question2 = Question("Вопрос 2: национальная еда Кыргызстана?","устрицы", "бешбармак","плов","борщ",2)
# question3 = Question("Вопрос 3: национальный головной убор Кыргызстана?","калпак","шапка","тюбитейка","шлем",1 )
# question4 = Question("Вопрос 4: лучший язык программирования?","питон","js","html :)","1С", 1)
# question5 = Question("Вопрос 5: сколько колес у машины?","4","3","34","32", 1)
# question6 = Question("Вопрос 6: сколько лап у кролика?","2","4","3","1", 2)
# question7 = Question("Вопрос 7: сколько сторон у квадрата?","3","2","4","5", 3)
# question8 = Question("Вопрос 8: число пи?","3","21.2","6.43","3.14", 4)
# question9 = Question("Вопрос 9: Кто написал 'Ромео и Джульетту'?","Леонардо ДА Винчи","Шекспир","Бахтияров","мияги",2)
# question10 = Question("Вопрос 10: питон это?","язык","животное","еда","игра", 1)
#
# quiz_questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
#
# def run_quiz():
#     player1_score = 0
#     player2_score = 0
#
#     for i in range(5):
#         print(f"\nВопрос {i + 1} для игрока 1:")
#         quiz_questions[i].display_question()
#         player1_answer = int(input("Введите номер правильного ответа (1-4): "))
#         if player1_answer == quiz_questions[i].get_correct_answer():
#             player1_score += 1
#
#         print(f"\nВопрос {i + 1} для игрока 2:")
#         quiz_questions[i + 5].display_question()
#         player2_answer = int(input("Введите номер правильного ответа (1-4): "))
#         if player2_answer == quiz_questions[i + 5].get_correct_answer():
#             player2_score += 1
#
#     print("\nРезультаты:")
#     print(f"Игрок 1: {player1_score} очков")
#     print(f"Игрок 2: {player2_score} очков")
#
#     if player1_score > player2_score:
#         print("Игрок 1 победил!")
#     elif player1_score < player2_score:
#         print("Игрок 2 победил!")
#     else:
#         print("Ничья!")
#
# run_quiz()