#Conversor de tempo
segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos2 = resto % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos2} segundo(s)")