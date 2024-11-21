# Labarotory work 2.2

# exercise 1
print("exercise 1")

def write_to_file(file):
    with open(file, 'w') as file:
        print(f"Введите текст, который хотите сохранить в файл: ")
        while True:
            line = input()
            if line == "":
                break
            file.write(line + "\n")
    
    print(f"Файл {file} сохранен")

file = input("Введите имя файла: ")

write_to_file(file)

# exercise 2
print("exercise 2")


def count_string_in_file():
    while True:
        try:
            filename = input("Введите имя файла: ")
            
            with open(filename, 'r') as file:
                search_string = input("Введите строку для поиска: ")
                text = file.read()
                count = text.count(search_string)
              
                return filename, search_string, count

        except FileNotFoundError:
            print(f"Файл '{filename}' не был найден, повторите попытку: ")

file, string, counts = count_string_in_file()
print(f"Строка {string} появляется {counts} раз в {file}")


# option 1

print("option 1")

def sum_integers_in_file():
    try:
        with open("file_int", 'r') as file_int:
            text = file_int.read()
            numbers = text.split()
            integers = [int(num) for num in numbers]
            sum_ints = sum(integers)
            
            with open("output", 'w') as output:
                output.write(str(sum_ints))
    except FileNotFoundError as fn:
        print(fn)
    except ValueError as ve:
        print(ve)
    
print("сумма чисел в файле равна сохранена в файл")                
        