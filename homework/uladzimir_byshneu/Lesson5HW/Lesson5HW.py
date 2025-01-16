# task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
# task 2
line1 = "результат операции: 42"
line2 = "результат операции: 514"
line3 = "результат работы программы: 9"
# Обработка первой строки
colon_index1 = line1.index(':')
number1 = int(line1[colon_index1 + 1:])
result1 = number1 + 10
print(result1)
# Обработка второй строки
colon_index2 = line2.index(':')
number2 = int(line2[colon_index2 + 1:])
result2 = number2 + 10
print(result2)
# Обработка третьей строки
colon_index3 = line3.index(':')
number3 = int(line3[colon_index3 + 1:])
result3 = number3 + 10
print(result3)
# task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print(f'Students {', '.join(students)} study these subjects: {', '.join(subjects)}')
