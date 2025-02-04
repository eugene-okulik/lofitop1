import datetime

easy_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(easy_date, "%b %d, %Y - %H:%M:%S")
month_name = python_date.strftime("%B")
print(month_name)
formatted_date = python_date.strftime("%d.%m.%Y, %H:%M")
print(formatted_date)
