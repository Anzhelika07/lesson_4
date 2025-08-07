from person import Person

name = input("Введите ваше имя: ")
middle_name = input("Введите ваше отчество: ")
family_name = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

person = Person(name, middle_name, family_name, age)

birth_year = person.get_birth_year()
print(f"{person} год рождения: {birth_year}")
