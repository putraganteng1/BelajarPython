def hitung_parkir(durasi):
    if durasi == 1:
        tarif=3500
    elif durasi == 2:
        tarif=5500
    elif durasi == 3:
        tarif = 7500
    else:
        tarif = 7500 + (durasi -3) * 2000
    return tarif

durasi_parkir = int(input())
total_tarif = hitung_parkir(durasi_parkir)

print(total_tarif)
