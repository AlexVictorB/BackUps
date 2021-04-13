from datetime import date
import datetime


DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

dateToday = str(date.today())



data = date.today()
print(data)

week_index = data.weekday()


dia_da_semana = DIAS[week_index]
print(dia_da_semana)
