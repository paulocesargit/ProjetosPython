from datetime import time, timezone, timedelta

horario=time(hour=6,minute=30,second=10, microsecond=500)
print(horario)

horario_formato1=horario.replace(minutes=59)
print(horario_formato1)#valor alterado

horario_formato2=horario.isoformat('minutes')
print(horario_formato2)#exibir hora e minutos

hora=timedelta(hours=-21)
fuso=timezone(hora)
print(fuso)

