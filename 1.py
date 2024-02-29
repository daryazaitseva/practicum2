# Зайцева Дарья Практическая работа №2

silveramount = 96
goldamount = silveramount // 16
silverprice = 48
revenue = int(input('Введите общую` сумму выручки '))
goldprice = (revenue - silveramount*silverprice) // goldamount
print(goldprice)
