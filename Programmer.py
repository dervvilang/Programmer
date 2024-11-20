class Programmer:
    def __init__(self, name, position):
        # проверка на корректность должности
        if position not in ['Junior', 'Middle', 'Senior']:
            raise ValueError("Должность должна быть Junior, Middle или Senior")

        self.__name = name
        self.__position = position
        self.__hours_worked = 0
        self.__accumulated_salary = 0
        self.__senior_rate_increment = 0
        self.__history = [f"{self.__name} принят на должность {self.__position}"]

    def __get_hourly_rate(self):
        """
        метод для получения текущего оклада программиста за час
        """
        if self.__position == 'Junior':
            return 10
        elif self.__position == 'Middle':
            return 15
        elif self.__position == 'Senior':
            return 20 + self.__senior_rate_increment
        else:
            raise ValueError("Некорректная должность.")

    def work(self, time):
        """
        отмечает новую отработку в количестве часов time;
        """
        if not isinstance(time, (int, float)) or time <= 0:
            raise ValueError("Количество отработанных часов должно быть положительным числом.")

        hourly_rate = self.__get_hourly_rate()
        self.__hours_worked += time
        earned = time * self.__get_hourly_rate()
        self.__accumulated_salary += earned

        self.__history.append(f"{self.__name} отработал {time}ч, начислено {hourly_rate * time} тгр")

    def bonus(self, amount):
        """
        выдача программисту бонуса
        """
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Сумма бонуса должна быть неотрицательным числом.")

        self.__accumulated_salary += amount
        self.__history.append(f"{self.__name} получил бонус {amount} тгр")

    def rise(self):
        """
        повышает программиста (изменяет должность или добавляет к зарплате +1 для senior);
        """
        previous_position = self.__position

        if self.__position == 'Junior':
            self.__position = 'Middle'
            self.__history.append(f"Повышен с {previous_position} до {self.__position}")
        elif self.__position == 'Middle':
            self.__position = 'Senior'
            self.__history.append(f"Повышен с {previous_position} до {self.__position}")
        elif self.__position == 'Senior':
            self.__senior_rate_increment += 1
            self.__history.append(f"Получил повышение, оклад увеличен на 1 тгр.")
        else:
            raise ValueError("Некорректная должность.")

    def info(self):
        """
        возвращает строку для бухгалтерии
        """
        return f"{self.__name} {self.__hours_worked}ч. {self.__accumulated_salary} тгр."

    def salary(self):
        """
        выдача зарплаты. Возвращает сколько надо выдать зарплаты и обнуляет накопленную зарплату
        """
        amount_to_pay = self.__accumulated_salary
        self.__accumulated_salary = 0
        self.__history.append(f"Получил зарплату: {amount_to_pay} тгр.")
        return amount_to_pay

    def stat(self):
        """
        выводит статистику и все шаги с момента приема на работу в формате
        """
        return "\n".join(self.__history)


programmer = Programmer('Васильев Иван', 'Junior')

programmer.work(750)
print(programmer.info())

programmer.rise()
programmer.work(500)
print(programmer.info())

programmer.rise()
programmer.work(250)
print(programmer.info())

programmer.rise()
programmer.work(250)
print(programmer.info())

print("\n--- Статистика ---")
print(programmer.stat())
