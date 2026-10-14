# Hastalık Belirtileri · Python Masaüstü Prototipi

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Yerel_veritabanı-003B57?logo=sqlite&logoColor=white)

Tkinter arayüzü ve SQLite ile bölüm bazlı örnek hastalık kayıtlarını listeleyen, ad ve belirti üzerinden filtreleyen eğitim amaçlı masaüstü uygulaması.

## Özellikler

- Bölüm seçimi ve kayıt sayılarının gösterimi.
- Hastalık adı araması, belirtiler için seçim kutuları ve kayıt detayları.
- Yeni kayıt ekleme ve yerel SQLite veritabanına kaydetme.
- İlk çalıştırmada kod içinde tanımlı örnek kayıtları oluşturma.

## Kurulum ve çalıştırma

Python 3 ve Tkinter destekli masaüstü ortamı gerekir. `sqlite3`, `tkinter` ve diğer kullanılan modüller Python standart kütüphanesindedir; üçüncü taraf Python paket kurulumu yoktur.

```sh
git clone https://github.com/Erkan54/Hastal-k-Belirtileri.git
cd Hastal-k-Belirtileri
python "HASTALIK BELİRTİLERİ.py"
```

Tkinter'ın bulunup bulunmadığını `python -m tkinter` ile kontrol edebilirsiniz. Linux dağıtımlarında Tkinter işletim sistemi paketi olarak ayrıca kurulabilir; başsız sunucuda pencere açılması için grafik oturumu gerekir.

## Dosyalar ve veri

[`HASTALIK BELİRTİLERİ.py`](HASTALIK%20BEL%C4%B0RT%C4%B0LER%C4%B0.py) veritabanı hazırlığı, sorgular ve arayüzü aynı dosyada içerir. Çalıştırıldığı klasörde `chest_diseases.db` oluşturulur; eklenen kayıtlar bu yerel dosyada tutulur.

Kodda iki `DiseaseListWindow` tanımı vardır; Python son tanımı kullanır. Örnek hastalık/belirti listesi gömülü veridir ve klinik doğrulama yapılmış bir veri seti olarak sunulmaz. Uygulama bir tanı motoru veya tıbbi karar aracı değildir; filtreleme sonucu bir hastalığı doğrulamaz.

## Geliştirme

Kodun veri, sorgu ve arayüz katmanlarına ayrılması; veri doğrulama ve arama testlerinin eklenmesi geliştirme alanlarıdır. Mevcut `.github/` kurs otomasyonları uygulamaya ait test paketi değildir. Bu README güncellemesinde program çalıştırılmadı.

Lisans: [MIT](LICENSE).
