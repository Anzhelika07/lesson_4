class Person:
    MIN_AGE = 15

    def __init__(self, name, middle_name, family_name, age):
        self.__name = name
        self.__middle_name = middle_name
        self.__family_name = family_name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) != 0:
            self.__name = name
            print("Имя было изменено")
        else:
            print("Имя не было изменено, передано пустое значение")

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, middle_mane):
        if len(middle_mane) != 0:
            self.__middle_name = middle_mane
            print("Отчество было изменено")
        else:
            print("Отчество не было изменено, передано пустое значение")

    @property
    def family_name(self):
        return self.__family_name

    @family_name.setter
    def family_name(self, family_mane):
        if len(family_mane) != 0:
            self.__family_name = family_mane
            print("Фамилия была изменена")
        else:
            print("Фамилия не была изменена, передано пустое значение")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < Person.MIN_AGE:
            print("Минимальный возраст 15 лет")
        else:
            self.__age = age
            print("Возраст был изменен")


    def __repr__(self):
        return f"{self.__family_name} {self.__name} {self.__middle_name}"

    def get_age(self):
        return self.__age
