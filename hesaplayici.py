from math import ceil, isfinite

# Sahne adını metin olarak al ve kenar boşluklarını temizle.
sahne_adi = input("Sahne adı: ").strip()

try:
    # Süreyi ondalıklı sayıya, FPS değerini tam sayıya dönüştür.
    sure = float(input("Sahne süresi (saniye): ").replace(",", "."))
    fps = int(input("FPS (tam sayı): "))

    # Sıfır süre geçerlidir. FPS pozitif ve sahne adı dolu olmalıdır.
    gecerli = bool(sahne_adi) and isfinite(sure) and sure >= 0 and fps > 0

    if gecerli:
        # Süre ile FPS'yi çarp ve sonucu yukarı yuvarla.
        ham_kare_sayisi = sure * fps
        kare_sayisi = ceil(ham_kare_sayisi)
        print(f"{sahne_adi} | Gereken kare sayısı: {kare_sayisi}")
    else:
        print("Hata: Sahne adı, süre veya FPS geçersiz.")
except (ValueError, OverflowError):
    # Sayıya dönüşmeyen veya hesaplama sınırını aşan girdiyi bildir.
    print("Hata: Süre sayı, FPS tam sayı olmalı ve değerler hesaplanabilir olmalı.")
