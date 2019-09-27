# Напишите программу,которая вычисляет сколько денег жители Лапландии тратят на сигареты маркок: "Parlament","Senator","Belomor canal",
# в неделю ,в месяц ,в год в стране, c населением 42, и сколько впоследствии никотина потребляет житель в год.
#Известно, что 13 курят "Parlament", 18 - "Senator", 1 - "Belomor canal", а остальное население не курит вообще.
# Причем ,каждый выкуривает не менее 1 сигареты в день(из курящих).
#Также есть информация, что люди,курящие "Parlament", курят x сигарет в день, люди,курящие "Senator",
# курят y сигарет в день,люди,курящие "Belomor canal", курят z сигарет в день.
#Параметры x, y, z ввдятся пользователем. Стоимость сигарет :"Parlament"- 189 тугриков,"Senator"- 150,
#'Belomor canal'- 73. В пачке 20 сигарет.
#Программа должна выводить самый дешевый вариант в долгосрочном периоде,количество полученного за этот
#период никтоина в неделю, месяц,год,количество потраченных тугриков за неделю,месяц,год, и общую сумму расходов
#на сигареты за день, месяц, год.
import math
print('Enter the number of cigarettes which are consumed by the person how is smoking " Parlament": ')
x = int(input())
print('Enter the number of cigarettes which are consumed by the person how is smoking "Senator": ')
y = int(input())
print('Enter the number of cigarettes which are consumed by the person how is smoking "Belomor canal": ')
z = int(input())
x7 = math.ceil((x * 7) / 20) * 189
y7 = math.ceil((y * 7) / 20) * 150
z7 = math.ceil((z * 7) / 20) * 73
summ1 = (x7 * 13) + (y7 * 18) + z7
xsmolw = int(7 * x * 4)
ysmolw = int(7 * x * 0.7)
zsmolw = int(7 * x * 30)
x30 = math.ceil((x * 30) / 20) * 189
y30 = math.ceil((y * 30) / 20) * 150
z30 = math.ceil((z * 30) / 20) * 73
summ2 = (x30 * 13) + (y30 * 18) + z30
xsmol1 = int(30 * x * 4)
ysmol2 = int(30 * x * 0.7)
zsmol3 = int(30 * x * 30)
x365 = math.ceil((x * 365) / 20) * 189
y365 = math.ceil((y * 365) / 20) * 150
z365 = math.ceil((z * 356) / 20) * 73
summ = (x365 * 13) + (y365 * 18) + z365
xsmol = int(365 * x * 4)
ysmol = int(365 * x * 0.7)
zsmol = int(365 * x * 30)
if (x365 < y365) and (x365 < z365):
    print('Smoking "Parliament" is cheaper in the long term.')
    print(x7,'-tugriky in a week people spend on Smoking "Parlament". Consumed in this case the amount of small (mg) is equal to:',xsmolw)
    print(x30,'-tugriky in a month people spend on Smoking "Parlament". Consumed in this case the amount of small (mg) is equal to:',xsmol1)
    print(x365, '-tugriky in a year people spend on Smoking "Parlament". Consumed in this case the amount of small (mg) is equal to:',xsmol)
if (y365 < x365) and (y365 < z365):
    print('Smoking "Senator" is cheaper in the long term.')
    print(y7,'-tugriky in a week people spend Smoking "Senator". Consumed in this case the amount of small (mg) is equal to:',ysmolw)
    print(y30, '-tugriky in a month people spend Smoking "Senator". Consumed in this case the amount of small (mg) is equal to:',ysmol2)
    print(y365, '-tugriky in a year people spend Smoking "Senator". Consumed in this case the amount of small (mg) is equal to:',ysmol)
if (z365 < y365) and (z365 < x365):
    print('Smoking "Belomor canal" is cheaper in the long term.')
    print(z7,'-tugriky in a week people spend Smoking "Belomor canal". Consumed in this case the amount of small (mg) is equal to:',zsmolw)
    print(z30,'-tugriky in a month people spend Smoking "Belomor canal". Consumed in this case the amount of small (mg) is equal to:',zsmol3)
    print(z365, '-tugriky in a year people spend Smoking "Belomor canal". Consumed in this case the amount of small (mg) is equal to:',zsmol)
print('Total cost of cigarettes per week:',summ1)
print('Total cost of cigarettes per month:',summ2)
print('Total cost of cigarettes per year:',summ)
print('SMOKING IS BAD FOR YOUR HEALTH(18+)')




