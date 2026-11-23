from datetime import date  # Bugünün tarihini almak için date sınıfını içe aktarır.

ad = input("Adın nedir? ").strip()  # Adı alır ve kenarlardaki boşlukları siler.
dogum_yili = int(input("Doğum yılın nedir? "))  # Girilen yılı tam sayıya dönüştürür.
bu_yil = date.today().year  # İçinde bulunduğumuz yılı alır.
if dogum_yili > bu_yil:



  print("Lütfen Geçerli Tarih Girin")
else:



  yas = bu_yil - dogum_yili
    print(f"Merhaba {ad}! Bu yıl {yas} yaşına giriyorsun.")

yas = bu_yil - dogum_yili  # Kullanıcının bu yıl dolduracağı yaşı hesaplar.
print(f"Merhaba {ad}! Bu yıl {yas} yaşına giriyorsun.")  # Kişiye özel mesajı gösterir.
