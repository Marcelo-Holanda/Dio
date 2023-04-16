import datetime
import time

def countdown():
    data_str = input("Insira a data no formato YYYY-MM-DD HH:MM:SS: ")
    data_futura = datetime.datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
    while True:
        data_atual = datetime.datetime.now()
        dif_tempo = data_futura - data_atual
        if dif_tempo.total_seconds() < 0:
            print("Contagem finalizada!")
            break
        horas, resto = divmod(dif_tempo.seconds, 3600)
        minutos, segundos = divmod(resto, 60)
        print(f"Faltam {dif_tempo.days} dias e {horas:02d}:{minutos:02d}:{segundos:02d} para {data_str}")
        time.sleep(1)

countdown()
