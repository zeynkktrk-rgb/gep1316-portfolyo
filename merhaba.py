from datetime import date  # Bugünün tarihini almak için date sınıfını içe aktarır.

ad = input("Adın nedir? ").strip()  # Adı alır ve kenarlardaki boşlukları siler.
dogum_yili = int(input("Doğum yılın nedir? "))  # Girilen yılı tam sayıya dönüştürür.
bu_yil = date.today().year  # İçinde bulunduğumuz yılı alır.

if dogum_yili > bu_yil:  # Doğum yılının gelecekte olup olmadığını kontrol eder.
    print("Lütfen Geçerli Tarih Girin")  # Gelecek bir yıl girildiyse uyarır.
else:  # Diğer yıllarda yaş hesabını yapar.
    yas = bu_yil - dogum_yili  # Bu yıl doldurulacak yaşı hesaplar.
    print(f"Merhaba {ad}! Bu yıl {yas} yaşına giriyorsun.")  # Karşılama mesajını gösterir.
