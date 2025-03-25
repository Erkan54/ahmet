import os
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# ----------------------------------------------------------------------
# AŞAMA 1: VERİTABANINI OLUŞTUR VE GEREKEN KAYITLARI EKLE
# ----------------------------------------------------------------------
def create_db():
    """
    Eğer veritabanı yoksa veya bazı bölümlere ait kayıt eksikse,
    'diseases' tablosunu oluşturur ve her bölüm için 5 örnek kayıt ekler.
    """
    db_file = "chest_diseases.db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS diseases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            symptoms TEXT,
            description TEXT,
            department TEXT
        )
    """)
    # Örnek kayıtlar (her biri 5 kayıt içeriyor)
    chest_diseases = [
        ("Bronşit", "öksürük, nefes darlığı, göğüs ağrısı", "Bronşların iltihaplanması sonucu ortaya çıkar.", "Göğüs Hastalıkları"),
("Zatürre", "ateş, öksürük, titreme, göğüs ağrısı", "Akciğer dokusunun enfeksiyonu.", "Göğüs Hastalıkları"),
("Astım", "nefes darlığı, öksürük, hırıltı", "Hava yollarında daralma ve inflamasyon.", "Göğüs Hastalıkları"),
("KOAH", "öksürük, nefes darlığı, balgam çıkarma, yorgunluk", "Kronik obstrüktif akciğer hastalığı; çevresel etkenlerle ilişkilidir.", "Göğüs Hastalıkları"),
("Akciğer Kanseri", "öksürük, kanlı balgam, nefes darlığı, göğüs ağrısı", "Akciğer dokusunda oluşan malign tümörler.", "Göğüs Hastalıkları"),
("Bronşiektazi", "kronik öksürük, yoğun balgam, tekrarlayan enfeksiyonlar", "Bronş duvarlarının kalıcı genişlemesi sonucu oluşur.", "Göğüs Hastalıkları"),
("Pnömotoraks", "ani nefes darlığı, göğüs ağrısı, solunum güçlüğü", "Akciğer zarı yırtılarak hava sızıntısı oluşmasıyla meydana gelir.", "Göğüs Hastalıkları"),
("Pulmoner Emboli", "ani nefes darlığı, göğüs ağrısı, çarpıntı, bayılma", "Akciğer arterlerine kan pıhtısının tıkanması sonucu ortaya çıkar.", "Göğüs Hastalıkları"),
("Sarkoidoz", "öksürük, nefes darlığı, yorgunluk, kilo kaybı", "Vücudun çeşitli organlarında granülom oluşumu, akciğerleri sıkça tutar.", "Göğüs Hastalıkları"),
("Silikozis", "nefes darlığı, kronik öksürük, göğüs ağrısı", "Uzun süreli silica tozu maruziyetiyle akciğer dokusunda fibrozis gelişir.", "Göğüs Hastalıkları"),
("Mesotelyoma", "nefes darlığı, göğüs ağrısı, kilo kaybı", "Azbest maruziyetine bağlı mezotelyal hücrelerden malign tümör oluşumu.", "Göğüs Hastalıkları"),
("İnterstisyel Akciğer Hastalıkları", "nöbetleyen öksürük, kronik nefes darlığı", "Akciğer interstisyumunun inflamasyonu ve fibrozisi nedeniyle akciğer fonksiyonları bozulur.", "Göğüs Hastalıkları"),
("Bronchiolitis Obliterans", "kalıcı öksürük, kronik nefes darlığı, hırıltı", "Küçük hava yollarının inflamasyonu ve fibrozisi sonucu hava akımı kısıtlanır.", "Göğüs Hastalıkları"),
("Pulmoner Fibroz", "kronik öksürük, nefes darlığı, yorgunluk", "Akciğer dokusunda skar dokusu oluşumu, elastikiyet kaybına yol açar.", "Göğüs Hastalıkları"),
("Pulmoner Hipertansiyon", "nefes darlığı, çarpıntı, yorgunluk, ayak ödemi", "Akciğer damarlarında basıncın artması kalbin sağ tarafını zorlar.", "Göğüs Hastalıkları"),
("Akut Respiratuar Distres Sendromu", "şiddetli nefes darlığı, hızlı solunum, hipoksi", "Ciddi inflamasyon ve sıvı birikimi nedeniyle akciğerlerin oksijen alışverişi bozulur.", "Göğüs Hastalıkları"),
("Tüberküloz", "gece terlemesi, kronik öksürük, kilo kaybı, ateş", "Mycobacterium tuberculosis enfeksiyonuna bağlı akciğer iltihabı.", "Göğüs Hastalıkları"),
("Kistik Fibroz", "kalın balgam, tekrar eden enfeksiyonlar, solunum güçlüğü", "Genetik temelli mukus üretiminde anormallik nedeniyle hava yolları tıkanır.", "Göğüs Hastalıkları"),
("Non-Tüberkülos Mykobakteryal Enfeksiyon", "kronik öksürük, düşük dereceli ateş, yorgunluk", "Tüberküloza benzer bulgular gösteren, ancak farklı mikobakterilerden kaynaklanan enfeksiyonlar.", "Göğüs Hastalıkları"),
("Pulmoner Emfizem", "nefes darlığı, kronik öksürük, hırıltı", "Alveolar duvarların yıkılmasıyla hava keselerinin aşırı genişlemesi sonucu gaz değişiminde bozulma.", "Göğüs Hastalıkları")
    ]
    nephro_diseases = [
        ("Kronik Böbrek Yetmezliği", "yorgunluk, ödem, tansiyon yüksekliği", "Böbrek fonksiyonlarının azalması.", "Nefroloji"),
("Akut Böbrek Yetmezliği", "bulantı, idrar azlığı, ödem", "Böbreklerin ani işlev kaybı.", "Nefroloji"),
("Nefrit", "idrarda kan, ağrı, yüksek tansiyon", "Böbrek iltihabı; immün sistem etkisi.", "Nefroloji"),
("Böbrek Taşı", "şiddetli ağrı, idrar yaparken yanma", "Mineral ve tuzların böbreklerde birikmesiyle oluşan taşlar.", "Nefroloji"),
("Polikistik Böbrek Hastalığı", "karın ağrısı, yüksek tansiyon, böbrek kistleri", "Genetik nedenlere bağlı kist oluşumu.", "Nefroloji"),
("Glomerülonefrit", "proteinüri, ödem, hipertansiyon", "Glomerüllerin inflamasyonu; enfeksiyon veya otoimmün tepkilerle gelişebilir.", "Nefroloji"),
("Lupus Nephriti", "kanlı idrar, ödem, yorgunluk", "Sistemik lupus eritematozusun böbrekleri etkilemesi sonucu oluşur.", "Nefroloji"),
("IgA Nefropati", "kanlı idrar, hafif proteinüri, hipertansiyon", "IgA komplekslerinin glomerüllerde birikmesiyle ortaya çıkar.", "Nefroloji"),
("Post-Enfeksiyöz Glomerülonefrit", "ödem, hipertansiyon, idrarda kan", "Üst solunum yolu enfeksiyonu sonrası bağışıklık komplekslerinin glomerüllerde birikmesi.", "Nefroloji"),
("Minimal Change Hastalığı", "nefrotik sendrom, ödem, proteinüri", "Mikroskopik düzeyde değişikliklerle karakterize, özellikle çocuklarda görülür.", "Nefroloji"),
("Fokal Segmental Glomeruloskleroz", "proteinüri, ödem, hipertansiyon", "Glomerüllerin kısmi skarlaşması sonucu ilerleyici hasar.", "Nefroloji"),
("Membranöz Glomerülonefrit", "ağır proteinüri, ödem, nefrotik sendrom", "Glomeruler bazal membranda bağışıklık komplekslerinin birikmesiyle inflamasyon.", "Nefroloji"),
("Renal Arterstenozu", "hipertansiyon, böbrek fonksiyonlarında azalma", "Böbrek arterlerinde daralma sonucu azalan kan akımı.", "Nefroloji"),
("Renal Infarktüs", "ani yanma, şiddetli ağrı, fonksiyon kaybı", "Böbrek dokusunda ani kan akışının kesilmesiyle ölü bölge oluşumu.", "Nefroloji"),
("Akut İnterstisyel Nefrit", "idrarda anormallikler, hafif ateş, deri döküntüleri", "İlaç veya enfeksiyon sonrası böbrek interstisyumunun inflamasyonu.", "Nefroloji"),
("Renal Papiller Nekroz", "şiddetli ağrı, idrarda kan, böbrek fonksiyon kaybı", "Böbrek papiller bölgede iskemik hasar; özellikle diyabetik hastalarda görülür.", "Nefroloji"),
("Nutcracker Sendromu", "karın ağrısı, baskı hissi, mikroskobik hematuri", "Sol renal venin sıkışması nedeniyle oluşan damar sıkışıklığı.", "Nefroloji"),
("Basit Böbrek Kisti", "genellikle asemptomatik, zaman zaman bel ağrısı", "Böbrek dokusunda oluşan iyi huylu sıvı dolu kistler.", "Nefroloji"),
("Hemolitik Üremik Sendrom", "idrarda kan, ödem, trombositopeni", "Mikroanjiyopatik süreçlerin neden olduğu, özellikle çocuklarda rastlanan böbrek hasarı.", "Nefroloji"),
("Diabetik Nefropati", "proteinüri, ödem, hipertansiyon", "Diyabetin uzun süreli etkisiyle böbrek damarlarında ve glomerüllerde meydana gelen hasar.", "Nefroloji")
]
    cardio_diseases = [
        ("Koroner Arter Hastalığı", "göğüs ağrısı, nefes darlığı", "Kalbe giden kan akışının azalması.", "Kardiyoloji"),
("Kalp Yetmezliği", "nefes darlığı, ayak şişmesi", "Kalbin yeterince kan pompalayamaması.", "Kardiyoloji"),
("Aritmi", "düzensiz kalp atışı, çarpıntı", "Kalp ritminde bozukluk.", "Kardiyoloji"),
("Miyokard Enfarktüsü", "şiddetli göğüs ağrısı, terleme, bulantı", "Kalp kasının hasar görmesi (kalp krizi).", "Kardiyoloji"),
("Perikardit", "göğüs ağrısı, ateş, yutkunmada ağrı", "Kalp zarı iltihabı.", "Kardiyoloji"),
("Genişleyici Kardiyomiyopati", "nefes darlığı, yorgunluk, ödem", "Kalp kasının dilatasyonu ve zayıflaması.", "Kardiyoloji"),
("Restriktif Kardiyomiyopati", "nefes darlığı, ödem, anksiyete", "Kalp kasının elastikiyet kaybı ve dolumunun kısıtlanması.", "Kardiyoloji"),
("Kardiyak Arrest", "ani bilinç kaybı, solunum durması", "Kalp ritminin tamamen durmasıyla hayati fonksiyonların kesilmesi.", "Kardiyoloji"),
("Endokardit", "ateş, yorgunluk, kalp üfürümü, embolik olaylar", "Kalbin iç zarının enfeksiyonu.", "Kardiyoloji"),
("Aort Diseksiyonu", "ani şiddetli sırt veya göğüs ağrısı, bayılma", "Aort duvarında yırtılma ve kanın ayrı bir kanal oluşturması.", "Kardiyoloji"),
("Hipertansif Kalp Hastalığı", "baş ağrısı, göğüs ağrısı, nefes darlığı", "Uzun süre yüksek tansiyon nedeniyle kalpte yapısal değişiklikler.", "Kardiyoloji"),
("Aort Stenozu", "göğüs ağrısı, çarpıntı, senkop", "Aort kapak daralması sonucu sol ventrikülden çıkan kan akımında azalma.", "Kardiyoloji"),
("Mitral Kapak Yetmezliği", "nefes darlığı, yorgunluk, çarpıntı", "Mitral kapakta yetersiz kapanma sonucu kanın geriye akışı.", "Kardiyoloji"),
("Triküspid Kapak Yetmezliği", "ödem, karın şişliği, yorgunluk", "Triküspid kapak fonksiyon bozukluğu nedeniyle sağ kalp yetmezliği.", "Kardiyoloji"),
("Kardiyojenik Şok", "şiddetli hipotansiyon, soğuk terleme, bilinç kaybı", "Kalbin ani ve ciddi şekilde pompalanamaması sonucu hayati tehlike.", "Kardiyoloji"),
("Sinüs Takikardisi", "hızlı kalp atışı, çarpıntı", "Sinüs düğümünün hızlanması sonucu ortaya çıkan normalden yüksek kalp atım hızı.", "Kardiyoloji"),
("Ventriküler Fibrilasyon", "ani bilinç kaybı, düzensiz ve hızlı kalp atışı", "Ventriküllerde elektriksel aktivitenin düzensizleşmesiyle pompa işlevinin bozulması.", "Kardiyoloji"),
("Ventriküler Taşikardi", "hızlı kalp atışı, baş dönmesi", "Ventriküllerin anormal elektrik impulslarıyla hızlı atması.", "Kardiyoloji"),
("Romatizmal Kalp Hastalığı", "ateş, eklem ağrısı, kalp üfürümü", "Romatizmal ateş sonrası kalp kapaklarında skar oluşumu.", "Kardiyoloji"),
("Hipertrofik Kardiyomiyopati", "nefes darlığı, göğüs ağrısı, bayılma", "Kalp kasının anormal kalınlaşması sonucu sol ventrikül dolumunun kısıtlanması.", "Kardiyoloji")
    ]
    neuro_diseases = [
        ("İnme", "konuşma bozukluğu, vücut zayıflığı", "Beyin kan akışının kesilmesi sonucu felç.", "Nöroloji"),
("Migren", "şiddetli baş ağrısı, bulantı, ışığa duyarlılık", "Ağır migren atağı.", "Nöroloji"),
("Epilepsi", "nöbet, bilinç kaybı, kas seğirmeleri", "Beyinde anormal elektriksel aktivite.", "Nöroloji"),
("Parkinson Hastalığı", "titreme, kas sertliği, denge kaybı", "Sinir sisteminde dejeneratif bozukluk.", "Nöroloji"),
("Multiple Skleroz", "görme problemleri, güç kaybı, koordinasyon bozukluğu", "Bağışıklık sisteminin sinir sistemine saldırması.", "Nöroloji"),
("Alzheimer Hastalığı", "hafıza kaybı, kafa karışıklığı, davranış değişiklikleri", "Beyinde progressif dejeneratif süreç.", "Nöroloji"),
("Amyotrofik Lateral Skleroz (ALS)", "kas güçsüzlüğü, konuşma bozuklukları, yutma zorluğu", "Motor nöronların dejenerasyonu.", "Nöroloji"),
("Guillain-Barre Sendromu", "kas güçsüzlüğü, refleks kaybı, parestezi", "Periferal sinirlerin inflamatuar demyelinizasyonu.", "Nöroloji"),
("Myastenia Gravis", "kaslarda çabuk yorulma, çift görme, titreme", "Otoimmün asetilkolin reseptörlerine saldırı.", "Nöroloji"),
("Trigeminal Nevralji", "şiddetli yüz ağrısı, yanak ve çene bölgesinde ağrı", "Trigeminal sinirin anormal aktivitesi.", "Nöroloji"),
("Subaraknoid Kanama", "ani şiddetli baş ağrısı, bilinç kaybı, boyun sertliği", "Beynin zarları arasında kanama.", "Nöroloji"),
("Beyin Tümörü", "baş ağrısı, nörolojik defisit, nöbetler", "Beyin dokusunda anormal hücre büyümesi.", "Nöroloji"),
("Hidrosefali", "baş ağrısı, bulantı, bilişsel bozukluk", "Beyin omurilik sıvısının anormal birikimi.", "Nöroloji"),
("Bell Paralizisi", "tek taraflı yüz felci, çift görme, koku kaybı", "Facial sinirin inflamasyonu veya sıkışması.", "Nöroloji"),
("Diyabetik Nöropati", "ayaklarda uyuşma, karıncalanma, ağrılar", "Diyabet sonucu sinir hasarı.", "Nöroloji"),
("Normal Basınçlı Hidrosefali", "yürüyüş bozukluğu, idrar inkontinansı, bilişsel gerileme", "Beyin omurilik sıvısı dolaşımında anormallik.", "Nöroloji"),
("Temporal Lob Epilepsisi", "duygusal dalgalanmalar, hafıza kaybı, duyu bozuklukları", "Temporal lobda odaklanmış epileptik aktivite.", "Nöroloji"),
("Serebral Palsi", "kas tonusu bozuklukları, koordinasyon eksikliği, gelişimsel gecikme", "Beyin gelişimi sırasında oluşan hasar veya anormallikler.", "Nöroloji"),
("Hemifasiyal Spazm", "yüz kaslarında istemsiz kasılmalar, titremeler", "Facial sinirin dejenerasyonu veya sıkışması.", "Nöroloji"),
("Ensefalit", "ateş, konfüzyon, nöbetler", "Beyin dokusunun inflamasyonu; sıklıkla viral enfeksiyona bağlı.", "Nöroloji")
    ]
    ortho_diseases = [
        ("Osteoartrit", "eklem ağrısı, sertlik, şişlik", "Eklem kıkırdağının bozulması.", "Ortopedi"),
("Romatoid Artrit", "eklem şişliği, ağrı, sabah tutukluğu", "İmmün sistemin eklemlere saldırması.", "Ortopedi"),
("Kırık", "şiddetli ağrı, hareket kısıtlılığı, şişlik", "Kemiklerde kırık oluşumu.", "Ortopedi"),
("Skolyoz", "sırt eğriliği, postür bozukluğu, bel ağrısı", "Omurganın yanal eğriliği.", "Ortopedi"),
("Bursit", "eklem ağrısı, şişlik, hassasiyet", "Eklem çevresindeki bursaların iltihabı.", "Ortopedi"),
("Osteoporoz", "kemik ağrısı, kırıklık riski, boy kısalması", "Kemik yoğunluğunun azalması ve kırılganlık artışı.", "Ortopedi"),
("Menisküs Yırtığı", "dizde ağrı, kilitlenme, şişlik", "Diz menisküsünün yırtılması sonucu oluşan hasar.", "Ortopedi"),
("Anterior Çapraz Bağ Yırtığı", "dizde ani ağrı, şişlik, istikrar kaybı", "Diz ekleminde ön çapraz bağın yırtılması.", "Ortopedi"),
("Tendinit", "eklem çevresinde ağrı, hassasiyet, hareketle artan ağrı", "Tendon iltihabı; aşırı kullanım veya yaralanma sonucu.", "Ortopedi"),
("Spondilolistezis", "bel ağrısı, bacak ağrısı, kas spazmları", "Omurlar arasında kayma; omurga dengesi bozukluğu.", "Ortopedi"),
("Kalça Kırığı", "şiddetli ağrı, hareket kısıtlılığı, morarma", "Kalça kemiklerinde oluşan kırık.", "Ortopedi"),
("Rotator Manşet Tendiniti", "omuz ağrısı, hareket kısıtlılığı, güç kaybı", "Omuz çevresindeki tendonların iltihabı.", "Ortopedi"),
("Dupuytren Kontraktürü", "el parmaklarında kıvrılma, işlev kaybı", "Elde fibrotik dokunun kalınlaşması sonucu parmak bükülmesi.", "Ortopedi"),
("Karpal Tünel Sendromu", "el ve bilek ağrısı, uyuşma, karıncalanma", "Median sinirin sıkışması sonucu oluşan sinir iletim bozukluğu.", "Ortopedi"),
("Plantar Fasiit", "ayak tabanında ağrı, sabahları yoğunlaşan ağrı", "Plantar fasya iltihabı; ayak destek dokusunun zorlanması.", "Ortopedi"),
("Disk Hernisi", "bel veya boyun ağrısı, sinir sıkışması, uyuşma", "Omurga diskinin yerinden kayması veya fıtıklaşması.", "Ortopedi"),
("Tibial Stress Fraktürü", "alt bacak ağrısı, şişlik, hareket sırasında artan ağrı", "Tekrarlayan zorlanma sonucu tibia kemiğinde mikro kırık oluşumu.", "Ortopedi"),
("Non-Union Kırık", "kırık bölgesinde sürekli ağrı, iyileşmede gecikme", "Kemik kırığının uygun şekilde iyileşmemesi.", "Ortopedi"),
("Osteomiyelit", "ateş, kemik ağrısı, şişlik", "Kemikte enfeksiyonun oluşması.", "Ortopedi"),
("Skolyoz (İleri Evre)", "şiddetli sırt ağrısı, postür bozukluğu, solunum problemleri", "Omurgada ciddi eğrilik ve yapısal bozukluk.", "Ortopedi")
    ]
    hema_diseases = [
        ("Anemi", "yorgunluk, solgunluk, baş dönmesi", "Kanda yeterli sağlıklı kırmızı hücre olmaması.", "Hematoloji"),
("Lökositoz", "ateş, yorgunluk, enfeksiyonlar", "Beyaz kan hücresi sayısında artış.", "Hematoloji"),
("Lökopeni", "tekrarlayan enfeksiyonlar, halsizlik", "Beyaz kan hücresi sayısında azalma.", "Hematoloji"),
("Trombositoz", "ateş, baş ağrısı, kalp krizi riski", "Platelet sayısında artış.", "Hematoloji"),
("Pıhtılaşma Bozukluğu", "kanamalarda uzun süre durmama", "Kanın pıhtılaşma mekanizmasında sorun.", "Hematoloji"),

("Hemolitik Anemi", "yorgunluk, solgunluk, sarılık, koyu idrar", "Kırmızı kan hücrelerinin aşırı yıkımı.", "Hematoloji"),
("Demir Eksikliği Anemisi", "yorgunluk, solgunluk, baş dönmesi", "Demir eksikliği nedeniyle hemoglobin üretiminin azalması.", "Hematoloji"),
("Aplastik Anemi", "yorgunluk, enfeksiyon riski, kanama", "Kemik iliğinin yeterli kan hücresi üretmemesi.", "Hematoloji"),
("Orak Hücreli Anemi", "ağrı, anemi, enfeksiyon riski", "Genetik mutasyon sonucu orak şeklini alan kırmızı hücreler.", "Hematoloji"),
("Talasemi", "yorgunluk, büyüme geriliği, kemik deformiteleri", "Genetik olarak hemoglobin üretim bozukluğuna yol açar.", "Hematoloji"),

("Von Willebrand Hastalığı", "kanama, burun kanamaları, diş eti kanaması", "Von Willebrand faktörünün eksikliği nedeniyle pıhtılaşma bozukluğu.", "Hematoloji"),
("Myelofibrosis", "yorgunluk, anemi, splenomegali", "Kemik iliğinde fibrozis gelişmesi sonucu kan üretiminin bozulması.", "Hematoloji"),
("Akut Lenfoblastik Lösemi", "yorgunluk, enfeksiyon riski, kolay morarma", "Kemik iliğinde kontrolsüz lenfoblast üretimi.", "Hematoloji"),
("Akut Miyeloid Lösemi", "halsizlik, enfeksiyon, kanama", "Miyeloid hücrelerin hızlı proliferasyonu.", "Hematoloji"),
("Kronik Lenfositik Lösemi", "yorgunluk, lenfadenopati, enfeksiyon riski", "Olgun lenfositlerin birikmesiyle yavaş ilerleyen lösemi.", "Hematoloji"),

("Kronik Miyeloid Lösemi", "yorgunluk, gece terlemesi, kilo kaybı", "Miyeloid hücrelerin anormal proliferasyonu ile seyreden lösemi.", "Hematoloji"),
("İmmün Trombositopenik Purpura (ITP)", "kanama, cilt döküntüleri, morarmalar", "Otoimmün mekanizmalarla trombositlerin tahrip edilmesi.", "Hematoloji"),
("Hemofili", "uzun süreli kanama, eklem kanamaları, morluklar", "Faktör VIII veya IX eksikliği nedeniyle pıhtılaşma bozukluğu.", "Hematoloji"),
("Miyelodisplastik Sendrom", "anemi, enfeksiyon, kanama", "Kemik iliğinde displastik hücre üretimi ve ilerleyici kan hücresi eksikliği.", "Hematoloji"),
("Paroksismal Nokturnal Hemoglobinüri", "anemi, koyu renkli idrar, karın ağrısı", "Kırmızı kan hücrelerinin gece patlamalarla yıkımı.", "Hematoloji")
    ]
    onco_diseases = [
        ("Meme Kanseri", "yumru, cilt değişimi, ağrı", "Memede oluşan malign tümör.", "Onkoloji"),
("Prostat Kanseri", "işeme zorluğu, idrarda kan", "Prostat bezinde malign oluşum.", "Onkoloji"),
("Kolorektal Kanser", "karın ağrısı, kanama, kilo kaybı", "Kalın bağırsakta oluşan malign tümör.", "Onkoloji"),
("Akciğer Kanseri", "öksürük, kanlı balgam, kilo kaybı", "Akciğer dokusunda oluşan malign tümör.", "Onkoloji"),
("Lenfoma", "şişmiş lenf düğümleri, ateş, kilo kaybı", "Lenfatik sistemde malign tümör.", "Onkoloji"),
("Mide Kanseri", "bulantı, kilo kaybı, yutma güçlüğü", "Mide mukozasında oluşan malign tümör.", "Onkoloji"),
("Karaciğer Kanseri", "karın ağrısı, sarılık, kilo kaybı", "Karaciğer dokusunda gelişen malign tümör.", "Onkoloji"),
("Tiroid Kanseri", "boyun şişliği, yutma güçlüğü, ses kısıklığı", "Tiroid bezinde oluşan malign tümör.", "Onkoloji"),
("Böbrek Kanseri", "kanlı idrar, bel ağrısı, kilo kaybı", "Böbrek dokusunda oluşan malign tümör.", "Onkoloji"),
("Over Kanseri", "karın şişliği, pelvik ağrı, idrar değişiklikleri", "Over dokusunda oluşan malign tümör.", "Onkoloji"),
("Melanom", "deride asimetrik lezyon, renk değişikliği, düzensiz kenarlar", "Cilt melan hücrelerinde malign dönüşüm.", "Onkoloji"),
("Özofagus Kanseri", "yutma güçlüğü, kilo kaybı, ağızda tat değişikliği", "Özofagus duvarında oluşan malign tümör.", "Onkoloji"),
("Laringeal Kanser", "ses kısıklığı, boğaz ağrısı, yutma güçlüğü", "Gırtlak dokusunda oluşan malign tümör.", "Onkoloji"),
("Endometrial Kanser", "adet düzensizlikleri, pelvik ağrı, anormal kanama", "Endometrium hücrelerinde malign dönüşüm.", "Onkoloji"),
("Bazal Hücre Karsinomu", "yavaş büyüyen lezyon, cilt döküntüsü, lokal doku hasarı", "Derinin bazal hücrelerinde malign tümör oluşumu.", "Onkoloji"),
("Nasofarengeal Kanser", "burun tıkanıklığı, kulak ağrısı, yüz felci", "Nazofarenks bölgesinde oluşan malign tümör.", "Onkoloji"),
("Gastrointestinal Stromal Tümör (GIST)", "karın ağrısı, kitle hissi, hazımsızlık", "Mide veya bağırsak duvarında gelişen nadir malign tümör.", "Onkoloji"),
("Osteosarkom", "kemik ağrısı, şişlik, kırık riski", "Kemik dokusunda gelişen agresif malign tümör.", "Onkoloji"),
("Wilms Tümörü", "karın kitle, kanama, iştah kaybı", "Böbreklerde çocukluk çağına özgü malign tümör.", "Onkoloji"),
("Glioblastoma Multiforme", "baş ağrısı, nörolojik defisitler, bulantı", "Beyinde agresif malign tümör.", "Onkoloji")
    ]
    dahiliye_diseases = [
        ("Hiperlipidemi", "yüksek kolesterol, yorgunluk", "Kanda yüksek yağ/kolesterol düzeyi.", "Dahiliye"),
("Hipertansiyon", "baş ağrısı, çarpıntı, yorgunluk", "Yüksek kan basıncı.", "Dahiliye"),
("Diyabet", "sık idrara çıkma, aşırı susuzluk", "Yüksek kan şekeri.", "Dahiliye"),
("Tiroid Bozukluğu", "kilo değişimi, üşüme, yorgunluk", "Tiroid hormon dengesizliği.", "Dahiliye"),
("Gut Hastalığı", "eklem ağrısı, ani ağrılı ataklar", "Ürik asit birikimi.", "Dahiliye"),
("Gastroözofageal Reflü Hastalığı", "mide yanması, ekşime, boğaz tahrişi", "Mide asidinin özofagusa kaçması sonucu oluşan kronik durum.", "Dahiliye"),
("Peptik Ülser", "karın ağrısı, mide ekşimesi, hazımsızlık", "Mide veya duodenum duvarındaki asit etkisiyle yara oluşumu.", "Dahiliye"),
("İrritabl Bağırsak Sendromu", "kronik karın ağrısı, şişkinlik, ishal/kabızlık", "Bağırsak hareketlerindeki düzensizlik sonucu ortaya çıkan fonksiyonel bozukluk.", "Dahiliye"),
("Osteoporoz", "kemik kırılganlığı, boy kısalması, sırt ağrısı", "Kemik mineral yoğunluğunun azalması ve kırık riskinin artması.", "Dahiliye"),
("Sistemik Lupus Eritematozus (SLE)", "deri döküntüleri, eklem ağrısı, yorgunluk", "Bağışıklık sisteminin organlara saldırdığı otoimmün hastalık.", "Dahiliye"),
("Cushing Sendromu", "kilo artışı, yüz yuvarlaşması, deri incelmesi", "Yüksek kortizol seviyesine bağlı klinik durum.", "Dahiliye"),
("Addison Hastalığı", "yorgunluk, kilo kaybı, hiperpigmentasyon", "Adrenal bezlerin yetersiz kortizol ve aldosteron üretimi.", "Dahiliye"),
("Metabolik Sendrom", "obezite, hipertansiyon, hiperglisemi", "Bir dizi metabolik bozukluğun beraber görülmesi durumu.", "Dahiliye"),
("Non-Alkolik Yağlı Karaciğer Hastalığı", "yorgunluk, karın sağ üst ağrısı, hafif kilo değişimi", "Karaciğerde, alkol dışı nedenlerle yağ birikimi.", "Dahiliye"),
("Akut Pankreatit", "şiddetli karın ağrısı, bulantı, kusma", "Pankreasın ani inflamasyonu ve sindirim enzimlerinin aktivasyonu.", "Dahiliye"),
("Kronik Pankreatit", "sürekli karın ağrısı, yağlı dışkı, kilo kaybı", "Pankreas dokusunda tekrarlayan inflamasyon ve fibrozis.", "Dahiliye"),
("Ülseratif Kolit", "ishal, karın ağrısı, kanlı dışkı", "Kolon mukozasında kronik inflamasyonla karakterize inflamatuar bağırsak hastalığı.", "Dahiliye"),
("Crohn Hastalığı", "karın ağrısı, ishal, kilo kaybı", "Sindirim sisteminde geçişli inflamasyon ve tıkanıklık.", "Dahiliye"),
("Obezite", "aşırı kilo, yorgunluk, eklem ağrısı", "Vücutta aşırı yağ birikimi; metabolik ve kardiyovasküler riskler.", "Dahiliye"),
("Fibromiyalji", "yaygın kas ağrısı, yorgunluk, uyku bozukluğu", "Kronik yaygın ağrı sendromu; merkezi duyarlılığın artması.", "Dahiliye")
    ]
    gastro_diseases = [
        ("Gastrit", "karın ağrısı, mide bulantısı", "Mide mukozasının iltihabı.", "Gastroenteroloji"),
("Peptik Ülser", "karın ağrısı, hazımsızlık", "Mide veya onikiparmak bağırsağında yaralar.", "Gastroenteroloji"),
("Reflü", "yanma hissi, ekşime", "Mide asidinin yemek borusuna kaçması.", "Gastroenteroloji"),
("Crohn Hastalığı", "karın ağrısı, ishal, kilo kaybı", "İnflamatuvar barsak hastalığı.", "Gastroenteroloji"),
("İrritabl Barsak Sendromu", "karın krampları, ishal veya kabızlık", "Bağırsak fonksiyon bozukluğu.", "Gastroenteroloji"),

("Ulseratif Kolit", "kanlı ishal, karın ağrısı, ateş", "Kolon mukozasının kronik inflamasyonu.", "Gastroenteroloji"),
("Divertikülit", "karın ağrısı, ateş, hassasiyet", "Divertiküllerin iltihaplanması.", "Gastroenteroloji"),
("Pankreatit", "şiddetli karın ağrısı, bulantı, kusma", "Pankreasın ani inflamasyonu.", "Gastroenteroloji"),
("Safra Kesesi Taşı", "sağ üst karın ağrısı, bulantı, kusma", "Safra kesesinde taş oluşumu.", "Gastroenteroloji"),
("Celiac Hastalığı", "karın şişkinliği, ishal, kilo kaybı", "Gluten intoleransı nedeniyle ince bağırsak zarar görmesi.", "Gastroenteroloji"),
("Helicobacter pylori Enfeksiyonu", "mide ağrısı, hazımsızlık, şişkinlik", "Helicobacter pylori bakterisinin neden olduğu mide iltihabı.", "Gastroenteroloji"),
("Gastroparezi", "bulantı, erken doyma, karın ağrısı", "Midenin geç boşalması.", "Gastroenteroloji"),
("Esophagitis", "yutma güçlüğü, göğüs ağrısı, yanma", "Özofagus mukozasının iltihabı.", "Gastroenteroloji"),
("Barrett Özofagus", "asit reflü, yutma güçlüğü, hafif yanma", "Özofagus mukozasında metaplastik değişiklik.", "Gastroenteroloji"),
("Kolon Polipleri", "genellikle asemptomatik, zaman zaman rektal kanama", "Kolon mukozasında iyi huylu büyümeler.", "Gastroenteroloji"),
("Achalasia", "yutma güçlüğü, regürjitasyon, kilo kaybı", "Yemek borusu motilite bozukluğu.", "Gastroenteroloji"),
("Hemoroidler", "rektal ağrı, kanama, kaşıntı", "Anorektal bölgede damarların şişmesi.", "Gastroenteroloji"),
("Fonksiyonel Dispepsi", "karın ağrısı, hazımsızlık, şişkinlik", "Organik neden bulunmayan dispeptik semptomlar.", "Gastroenteroloji"),
("Gastrointestinal Stromal Tümör (GIST)", "karın ağrısı, kitle hissi, hazımsızlık", "Mide veya bağırsakta stromal tümör oluşumu.", "Gastroenteroloji"),
("Intestinal Obstrüksiyon", "karın ağrısı, kusma, şişlik", "Bağırsak tıkanıklığı sonucu ortaya çıkan akut durum.", "Gastroenteroloji")
    ]
    kulak_burun_bogaz_diseases = [
        ("Sinüzit", "burun tıkanıklığı, baş ağrısı, yüz ağrısı", "Sinüslerin iltihabı.", "Kulak Burun Boğaz"),
("Tonsillit", "boğaz ağrısı, yutma güçlüğü, ateş", "Bademciklerin iltihaplanması.", "Kulak Burun Boğaz"),
("Orta Kulak Enfeksiyonu", "kulak ağrısı, ateş, işitme kaybı", "Orta kulakta enfeksiyon.", "Kulak Burun Boğaz"),
("Laringit", "ses kısıklığı, boğaz ağrısı, yutma güçlüğü", "Ses tellerinin iltihabı.", "Kulak Burun Boğaz"),
("Öksürüklü Rinit", "burun akıntısı, hapşırma, hafif ateş", "Soğuk algınlığına bağlı rinit.", "Kulak Burun Boğaz"),
("Nazal Polipler", "burun tıkanıklığı, koku kaybı, yüz basıncı", "Nazal mukozada iyi huylu büyümeler.", "Kulak Burun Boğaz"),
("Septum Deviasyonu", "tek taraflı burun tıkanıklığı, tekrarlayan burun kanamaları, baş ağrısı", "Nazal septumun eğrilmesi.", "Kulak Burun Boğaz"),
("Akut Otitis Eksterna", "kulak ağrısı, kaşıntı, çevrede hassasiyet", "Dış kulak kanalının enfeksiyonu.", "Kulak Burun Boğaz"),
("Kronik Otitis Media", "uzun süreli kulak akıntısı, işitme kaybı, tekrarlayan enfeksiyonlar", "Orta kulakta kronik inflamasyon ve zar hasarı.", "Kulak Burun Boğaz"),
("Tinnitus", "kulak çınlaması, işitme kaybı, rahatsızlık", "Kulakta sürekli veya aralıklı istenmeyen ses algılanması.", "Kulak Burun Boğaz"),
("Meniere Hastalığı", "baş dönmesi, tinnitus, işitme kaybı, kulak dolgunluğu", "İç kulakta sıvı dengesinin bozulması.", "Kulak Burun Boğaz"),
("Presbikusis", "yaşla birlikte artan işitme zorluğu, konuşmaları anlama güçlüğü", "Yaşlanma sürecine bağlı işitme kaybı.", "Kulak Burun Boğaz"),
("Farenjit", "boğaz ağrısı, yutma güçlüğü, hafif ateş", "Farenksin iltihaplanması.", "Kulak Burun Boğaz"),
("Kronik Farenjit", "devam eden boğaz tahrişi, kuru öksürük, ses kısıklığı", "Farenksin uzun süreli inflamasyonu.", "Kulak Burun Boğaz"),
("Glossite", "dil ağrısı, şişlik, tat kaybı", "Dil mukozasının iltihaplanması veya irritasyonu.", "Kulak Burun Boğaz"),
("Laryngeal Papillomatosis", "ses kısıklığı, nefes almada güçlük, tekrarlayan lezyonlar", "Laringde papillomavirüs kaynaklı benign tümör oluşumu.", "Kulak Burun Boğaz"),
("Rhinophyma", "burun deformasyonu, kalınlaşmış cilt, kırmızımsı görünüm", "Burun derisinin aşırı yağ üretimi ve fibrozis sonucu oluşan deformasyon.", "Kulak Burun Boğaz"),
("Akustik Neuroma", "tek taraflı işitme kaybı, kulak çınlaması, denge bozukluğu", "Vestibulocochlear sinirin benign tümörü.", "Kulak Burun Boğaz"),
("Otoskleroz", "yavaş ilerleyen işitme kaybı, tinnitus", "İç kulakta iskelet yapının anormal kemik büyümesi.", "Kulak Burun Boğaz"),
("Peritonsiller Abseks", "şiddetli boğaz ağrısı, ağız açıklığında kısıtlılık, ateş", "Tonsiller çevresinde irin birikimi.", "Kulak Burun Boğaz")
    ]
    pediatri_diseases = [
        ("Bronşiolit", "öksürük, hırıltılı solunum, ateş", "Bebeklerde alt solunum yolu enfeksiyonu.", "Pediatri"),
("Çocuk Enfeksiyonu", "ateş, huzursuzluk, iştahsızlık", "Genel çocuk enfeksiyonu.", "Pediatri"),
("Dizanteri", "ishal, karın ağrısı, dehidratasyon", "Bağırsak enfeksiyonu.", "Pediatri"),
("Bebek Astımı", "nefes darlığı, hırıltı, öksürük", "Bebeklerde görülen astım atağı.", "Pediatri"),
("Otitis Media", "kulak ağrısı, hafif ateş, huzursuzluk", "Bebeklerde orta kulak enfeksiyonu.", "Pediatri"),
("Bebek Kolik", "uzun süreli ağlama, huzursuzluk, uyku bozuklukları", "Yeni doğan bebeklerde sebebi tam olarak anlaşılamayan aşırı ağlama atakları.", "Pediatri"),
("Neonatal Sarılık", "cilt ve gözlerin sararması", "Yenidoğanlarda bilirubin metabolizması bozukluğuna bağlı oluşan durum.", "Pediatri"),
("Neonatal Sepsis", "ateş, düşük aktivite, beslenme güçlüğü", "Yenidoğanlarda sistemik enfeksiyon.", "Pediatri"),
("El, Ayak ve Ağız Hastalığı", "ateş, ağızda yara, döküntü", "Coxsackievirus enfeksiyonu nedeniyle ortaya çıkan hastalık.", "Pediatri"),
("Gastroenterit", "ishal, kusma, ateş", "Bağırsak enfeksiyonu; genellikle viral nedenli.", "Pediatri"),
("Kızamık", "yüksek ateş, cilt döküntüsü, burun akıntısı", "Rubeola virüsü enfeksiyonuna bağlı çocuk hastalığı.", "Pediatri"),
("Suçiçeği", "döküntü, hafif ateş, kaşıntı", "Varicella zoster virüsü kaynaklı enfeksiyon.", "Pediatri"),
("Kabakulak", "tükürük bezlerinde şişme, ateş, kas ağrıları", "Mumps virüsü enfeksiyonu.", "Pediatri"),
("Pediatrik Pnömoni", "yüksek ateş, öksürük, nefes darlığı", "Bebeklerde alt solunum yolu enfeksiyonu ve inflamasyonu.", "Pediatri"),
("Atopik Dermatit", "kurdeşem, kaşıntı, cilt kuruluğu", "Çocuklarda sık görülen alerjik cilt inflamasyonu.", "Pediatri"),
("Bebek Gastroözofageal Reflü", "kusma, huzursuzluk, beslenme güçlüğü", "Bebeklerde mideden yemek borusuna asit kaçması.", "Pediatri"),
("Febril Konvülziyon", "ateşle birlikte kasılmalar, bilinç kaybı", "Yüksek ateş nedeniyle geçici nöbet atakları.", "Pediatri"),
("Pediatrik İdrar Yolu Enfeksiyonu", "ateş, huzursuzluk, idrar yaparken yanma", "Bebeklerde üste veya alt idrar yolu enfeksiyonu.", "Pediatri"),
("Ağız Pamukçuğu", "beyaz plaqlar, ağrı, beslenme güçlüğü", "Candida mantarının neden olduğu ağız enfeksiyonu.", "Pediatri"),
("Konjenital Hipotiroidizm", "yorgunluk, kilo artışı, gelişim geriliği", "Doğuştan tiroid hormon üretiminin yetersizliği.", "Pediatri")
    ]
    uroloji_diseases = [
        ("Benign Prostat Hiperplazisi", "zor idrara çıkma, sık idrara çıkma", "Prostatın normalden büyük olması.", "Üroloji"),
("Üriner Sistem Enfeksiyonu", "yanma, sık idrara çıkma, idrarda kan", "İdrar yolu enfeksiyonu.", "Üroloji"),
("Üreter Tıkanıklığı", "böbrek ağrısı, idrar akışında azalma", "Üreterde obstrüksiyon.", "Üroloji"),
("Kronik Prostatit", "kalıcı pelvis ağrısı, idrar sorunları", "Prostatın kronik iltihabı.", "Üroloji"),
("İdrar Kaçırma", "kontrolsüz idrar kaçırma, sık idrara çıkma", "Yaşlanma veya sinir problemleri nedeniyle.", "Üroloji"),
("Böbrek Taşı", "şiddetli bel ve yan ağrısı, idrarda kan, bulantı", "Böbreklerde veya üreterde mineral kristallerin birikmesiyle taş oluşumu.", "Üroloji"),
("Erektil Disfonksiyon", "sertleşme zorluğu, düşük cinsel performans", "Cinsel uyarıya rağmen yeterli kan akışının sağlanamaması.", "Üroloji"),
("İnterstisyel Mesane Sendromu", "sık idrara çıkma, mesane ağrısı, karın bölgesinde rahatsızlık", "Mesane mukozasında kronik inflamasyon ve ağrı.", "Üroloji"),
("Priapizm", "uzun süreli ağrılı ereksiyon", "Normalden uzun süren, ağrılı ve istenmeyen ereksiyon durumu.", "Üroloji"),
("Varikokel", "skrotal ağrı, testis küçülmesi, şişlik", "Testis etrafındaki venöz yapıların genişlemesi.", "Üroloji"),
("Hidrosel", "skrotumda şişlik, yumuşak doku hissi", "Testis çevresinde sıvı birikimi.", "Üroloji"),
("Testis Torsiyonu", "ani şiddetli testis ağrısı, şişlik, bulantı", "Testislerin kendi ekseni etrafında dönmesi sonucu kan akışının kesilmesi.", "Üroloji"),
("Epididimit", "testis arkasında ağrı, şişlik, ateş", "Epididimin inflamasyonu.", "Üroloji"),
("Fimosis", "zor idrara çıkma, ağrı, cinsel ilişki güçlüğü", "Penis başının daralması.", "Üroloji"),
("Balanitis", "penis başında kızarıklık, kaşıntı, ağrı", "Penis başında inflamasyon.", "Üroloji"),
("Üretral Darlık", "zayıf idrar akışı, idrar yaparken ağrı, tekrarlayan enfeksiyonlar", "Üretra içindeki daralma.", "Üroloji"),
("Neurojenik Mesane", "sık idrara çıkma, idrar yaparken zorlanma, inkontinans", "Sinir sistemi bozukluklarına bağlı mesane kontrol problemleri.", "Üroloji"),
("Kronik İdrar Retansiyonu", "tam boşalamama hissi, zayıf idrar akışı", "Mesane boşaltımında kronik zorluk.", "Üroloji"),
("Mesane Kanseri", "kanlı idrar, boşalma sırasında ağrı, pelvik ağrı", "Mesane duvarında malign hücre dönüşümü.", "Üroloji"),
("Vesikoureteral Reflü", "tekrarlayan üriner sistem enfeksiyonları, idrarda kan, idrar kaçırma", "İdrarın mesaneden üreterlere geri akışı.", "Üroloji")
    ]
    kadin_dogum_diseases = [
        ("Preeklampsi", "yüksek tansiyon, şişlik, baş ağrısı", "Gebelikte gelişen tehlikeli durum.", "Kadın Doğum"),
("Ektopik Gebelik", "karın ağrısı, düzensiz kanama", "Rahim dışı gebelik.", "Kadın Doğum"),
("Endometriozis", "ağrılı adet, kronik karın ağrısı", "Rahim içi dokunun rahim dışında yerleşmesi.", "Kadın Doğum"),
("Polikistik Over Sendromu", "düzensiz adet, tüylenme, kilo artışı", "Hormonal dengesizlikten dolayı yumurtalık kistleri.", "Kadın Doğum"),
("Doğum Komplikasyonu", "prematüre doğum, doğum travması", "Gebelik sırasında beklenmeyen komplikasyonlar.", "Kadın Doğum"),
("Gestasyonel Diyabet", "aşırı susuzluk, sık idrara çıkma, yorgunluk", "Gebelik sırasında ortaya çıkan glukoz intoleransı.", "Kadın Doğum"),
("Postpartum Hemoraji", "şiddetli lohusa kanaması, hipotansiyon, baş dönmesi", "Doğum sonrası aşırı kan kaybı.", "Kadın Doğum"),
("İntrauterin Büyüme Geriliği", "düşük doğum ağırlığı, gelişim geriliği", "Bebeğin rahim içindeki büyümesinin yetersiz olması.", "Kadın Doğum"),
("Oligohidramnios", "küçük karın çevresi, rahim sessizliği, fetal distres", "Amniyotik sıvı miktarının normalin altında olması.", "Kadın Doğum"),
("Polyhydramnios", "rahim genişlemesi, sık idrara çıkma, solunum zorluğu", "Amniyotik sıvı miktarının normalden fazla olması.", "Kadın Doğum"),
("Placenta Previa", "ağrısız vajinal kanama, rahim büyüklüğünde düzensizlik", "Plasentanın rahim ağzını kısmen veya tamamen kapatması.", "Kadın Doğum"),
("Plasental Abrupsi", "ani şiddetli vajinal kanama, karın ağrısı, uterin tonus artışı", "Plasentanın erken ayrılması.", "Kadın Doğum"),
("Hyperemesis Gravidarum", "aşırı kusma, dehidrasyon, kilo kaybı", "Gebeliğin ilk dönemlerinde görülen şiddetli bulantı ve kusma durumu.", "Kadın Doğum"),
("Uterin Myom", "ağrılı adet, pelvik basınç, kanama", "Rahimdeki benign kas tümörleri.", "Kadın Doğum"),
("Molar Gebelik", "ağrısız vajinal kanama, aşırı bulantı, uterusun anormal büyümesi", "Anormal plasenta gelişimi sonucu oluşan gestasyonel trophoblastic hastalık.", "Kadın Doğum"),
("Servikal Yetmezlik", "tekrarlayan erken düşük, erken doğum", "Rahim ağzının yapısal zayıflığı nedeniyle erken açılması.", "Kadın Doğum"),
("Endometritis", "ateş, karın ağrısı, kötü kokulu lohusa kanamaları", "Doğum sonrası veya cerrahi sonrası endometrial enfeksiyon.", "Kadın Doğum"),
("Eklampsi", "nöbet, kasılma, konfüzyon", "Preeklampsinin nöbetle seyreden formu.", "Kadın Doğum"),
("Maternal Anemi", "yorgunluk, solgunluk, nefes darlığı", "Gebelikte kırmızı kan hücrelerinin yetersizliği.", "Kadın Doğum"),
("Maternal Venöz Tromboembolizm", "akciğer ağrısı, nefes darlığı, bacak şişliği", "Gebelikte artan tromboembolik risk nedeniyle oluşan venöz pıhtılaşması.", "Kadın Doğum")
    ]
    goz_diseases = [
        ("Katarakt", "bulanık görme, ışığa duyarlılık", "Lensin opaklaşması.", "Göz Hastalıkları"),
("Glokom", "görme alanında daralma, göz ağrısı", "Göz içi basıncın artması.", "Göz Hastalıkları"),
("Miyopi", "uzaktaki nesneler bulanık, yakındaki net", "Odaklama hatası nedeniyle oluşur.", "Göz Hastalıkları"),
("Konjenital Strabismus", "çarpık göz, çift görme", "Doğuştan gelen göz hizalanması bozukluğu.", "Göz Hastalıkları"),
("Makula Dejenerasyonu", "merkezi görme kaybı, bulanık görme", "Makula bölgesinde dejeneratif değişiklikler.", "Göz Hastalıkları"),
("Konjonktivit", "gözde kızarıklık, sulanma, yanma, kaşıntı", "Konjonktiva iltihabı; enfeksiyöz veya alerjik nedenli.", "Göz Hastalıkları"),
("Retinitis Pigmentosa", "gece körlüğü, görme alanında daralma, renk algı bozuklukları", "Retina fotoreseptör hücrelerinin dejenerasyonu.", "Göz Hastalıkları"),
("Uveit", "gözde ağrı, kızarıklık, fotofobi, bulanık görme", "Uvea tabakasının inflamasyonu.", "Göz Hastalıkları"),
("Blefarit", "göz kapaklarında yanma, kaşıntı, kızarıklık, pullanma", "Göz kapaklarının kronik inflamasyonu.", "Göz Hastalıkları"),
("Keratit", "göz ağrısı, sulanma, ışığa duyarlılık, bulanık görme", "Kornea iltihabı; enfeksiyöz veya travmatik nedenlerle.", "Göz Hastalıkları"),
("Amblyopi", "düşük görme keskinliği, göz tembelliği", "Beyindeki görsel uyarı eksikliği nedeniyle gelişen durum.", "Göz Hastalıkları"),
("Pterygium", "gözde kızarıklık, irritasyon, görme bulanıklığı", "Konjonktivadan korneaya doğru ilerleyen fibrovascular doku büyümesi.", "Göz Hastalıkları"),
("Diabetik Retinopati", "bulanık görme, görme kaybı, floater", "Diyabetin retina damarlarına zarar vermesi sonucu oluşan mikrovasküler değişiklikler.", "Göz Hastalıkları"),
("Retinal Detachment", "ışık çakmaları, ani görme kaybı, parda gibi görme", "Retinanın yerinden ayrılması.", "Göz Hastalıkları"),
("Kuru Göz Sendromu", "gözde yanma, batma, sulanma, rahatsızlık", "Göz yüzeyinin yeterince nemlendirilmemesinden kaynaklanır.", "Göz Hastalıkları"),
("Astigmatizma", "bulanık görme, göz yorgunluğu, baş ağrısı", "Kornea veya lensin düzensiz eğriliği nedeniyle oluşan refraktif bozukluk.", "Göz Hastalıkları"),
("Hipermetropi", "yakındaki nesnelerin bulanık, uzaktakilerin daha net", "Gözün yakın mesafeleri odaklamakta zorluk çekmesi.", "Göz Hastalıkları"),
("Presbiyopi", "yakına odaklanmada zorluk, bulanık görme, göz yorgunluğu", "Yaşlanmaya bağlı olarak lens esnekliğinin azalması.", "Göz Hastalıkları"),
("Vitreus Kanaması", "ani görme kaybı, bulanık görme, karanlık noktalar", "Göz içindeki vitreus sıvısının kanla kirlenmesi.", "Göz Hastalıkları"),
("Nistagmus", "kontrolsüz göz hareketleri, bulanık görme, konsantrasyon zorluğu", "Sinir sistemi veya göz kaslarındaki bozukluklara bağlı ritmik, istemsiz göz hareketleri.", "Göz Hastalıkları")
    ]
    immunoloji_diseases = [
        ("Sistemik Lupus Eritematozus", "eklem ağrısı, deri döküntüleri, yorgunluk", "Bağışıklık sisteminin kendine saldırması.", "İmmünoloji"),
("IgA Eksikliği", "tekrarlayan enfeksiyonlar, solunum yolu problemleri", "IgA antikorunun yetersizliği.", "İmmünoloji"),
("Alerjik Dermatit", "deri kaşıntısı, kızarıklık, döküntüler", "Ciltte alerjik reaksiyonlar.", "İmmünoloji"),
("Otoimmün Tiroiditis", "yorgunluk, kilo değişimi, soğuk intoleransı", "Tiroid bezinde otoimmün hasar.", "İmmünoloji"),
("Henoch-Schönlein Purpura", "deri döküntüleri, eklem ağrısı, karın ağrısı", "Küçük damar iltihabı; genellikle çocukluk döneminde görülür.", "İmmünoloji"),
("Romatoid Artrit", "eklem ağrısı, sabah tutukluğu, eklem şişliği", "Eklemlerde otoimmün inflamasyon ve yıkım.", "İmmünoloji"),
("Sjögren Sendromu", "ağız kuruluğu, göz kuruluğu, yorgunluk", "Tükürük ve gözyaşı bezlerinin otoimmün hasarı.", "İmmünoloji"),
("Graves Hastalığı", "kalp çarpıntısı, kilo kaybı, göz çıkması", "Tiroid bezinde otoimmün uyarı sonucu hipertirodizm.", "İmmünoloji"),
("Myasthenia Gravis", "kas güçsüzlüğü, çift görme, yutma güçlüğü", "Sinir ile kas arasındaki iletişimi etkileyen otoimmün bozukluk.", "İmmünoloji"),
("Otoimmün Hemolitik Anemi", "yorgunluk, solgunluk, sarılık", "Kırmızı kan hücrelerinin otoimmün yıkımı.", "İmmünoloji"),
("Psoriasis", "kızarıklık, pullu deri, kaşıntı", "Cilt hücrelerinin aşırı çoğalması ve inflamasyonu.", "İmmünoloji"),
("Ankilozan Spondilit", "bel ağrısı, sabah sertliği, hareket kısıtlılığı", "Omurga eklemlerinde kronik otoimmün inflamasyon.", "İmmünoloji"),
("Dermatomiyozit", "kas güçsüzlüğü, deri döküntüleri, yorgunluk", "Kas ve deri dokusunda otoimmün inflamasyon.", "İmmünoloji"),
("IgG4-Related Disease", "organ şişkinliği, fonksiyon bozuklukları", "IgG4 antikorlarının aşırı birikimi ile ilişkili fibroz inflamasyon.", "İmmünoloji"),
("Behçet Hastalığı", "oral/genital ülserler, deri döküntüleri, eklem ağrısı", "Vaskülit ve inflamasyon ile seyreden otoimmün hastalık.", "İmmünoloji"),
("İmmün Trombositopenik Purpura (ITP)", "morluk, kanama eğilimi, peteşi", "Bağışıklık sisteminin trombositleri hedef alarak yıkımı.", "İmmünoloji"),
("Otoimmün Hepatit", "yorgunluk, sarılık, karın ağrısı", "Karaciğerin otoimmün inflamasyonu.", "İmmünoloji"),
("Celiac Hastalığı", "karın ağrısı, ishal, kilo kaybı", "Gluten intoleransı sonucunda ince bağırsakta otoimmün yanıt.", "İmmünoloji"),
("Vitiligo", "deride lekelenme, renk kaybı", "Melanositlerin otoimmün yıkımı.", "İmmünoloji"),
("Stevens-Johnson Sendromu", "cilt döküntüleri, yanma, mukozal lezyonlar", "Ciddi ilaç reaksiyonu ile tetiklenen otoimmün reaksiyon.", "İmmünoloji")
    ]
    enfeksiyon_diseases = [
        ("Bakteriyel Menenjit", "yüksek ateş, ense sertliği, bilinç bulanıklığı", "Bakteri kaynaklı menenjit enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Sepsis", "ateş, düşük tansiyon, hızlı nabız", "Vücudun yaygın enfeksiyona verdiği aşırı tepki.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Pnömokok Enfeksiyonu", "ateş, öksürük, solunum güçlüğü", "Pnömokok bakterisinin neden olduğu enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("HIV Enfeksiyonu", "hızlı kilo kaybı, yorgunluk, tekrarlayan enfeksiyonlar", "İnsan bağışıklık yetmezliğine yol açan HIV enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Viral Hepatit", "sarılık, koyu idrar, bulantı", "Hepatit virüslerinin neden olduğu karaciğer enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Tüberküloz", "öksürük, gece terlemeleri, kilo kaybı", "Mycobacterium tuberculosis enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Bakteriyel Endokardit", "ateş, kalp üfürümü, yorgunluk", "Kalp kapaklarında bakteriyel enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Clostridium difficile Enfeksiyonu", "ishal, karın ağrısı, ateş", "Antibiyotik kullanımı sonrası gelişen Clostridium difficile enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Meningokokal Enfeksiyonu", "ateş, döküntü, ense sertliği", "Neisseria meningitidis'in neden olduğu enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Stafilokokik Sepsis", "yüksek ateş, şiddetli genel durum bozukluğu, yara lezyonları", "Staphylococcus aureus enfeksiyonunun invaziv seyri.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Sifiliz", "deri döküntüleri, oral lezyonlar, lenfadenopati", "Treponema pallidum bakterisinin neden olduğu enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Leptospirosis", "ateş, kas ağrıları, baş ağrısı, sarılık", "Leptospira bakterisinin neden olduğu zoonotik enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Kuduz", "hidrofobi, nörolojik semptomlar, kas spazmları", "Rabies virüsünün neden olduğu ölümcül enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Dengue Ateşi", "yüksek ateş, şiddetli kas ve eklem ağrıları, döküntü", "Dengue virüsünün neden olduğu arboviral enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Chikungunya", "yüksek ateş, şiddetli eklem ağrıları, döküntü", "Chikungunya virüsünün neden olduğu viral enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Norovirüs Gastroenteriti", "ishal, kusma, karın ağrısı", "Norovirüs kaynaklı akut viral gastroenterit.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Rotavirüs Enfeksiyonu", "ağır ishal, kusma, ateş", "Rotavirüs nedeniyle özellikle bebeklerde görülen gastroenterit.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Varisella (Suçiçeği)", "döküntü, hafif ateş, kaşıntı", "Varicella zoster virüsünün neden olduğu enfeksiyon.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Influenza", "yüksek ateş, kas ağrıları, öksürük, halsizlik", "Influenza virüsünün neden olduğu solunum yolu enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji"),
("Human Papilloma Virüs Enfeksiyonu", "genital siğiller, cilt lezyonları", "HPV virüsünün neden olduğu mukozal ve cilt enfeksiyonu.", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji")
    ]
    romatoloji_diseases = [
        ("Romatoid Artrit", "eklem ağrısı, şişlik, sabah tutukluğu", "Bağışıklık sisteminin eklemlere saldırması.", "Romatoloji"),
("Sjögren Sendromu", "ağız kuruluğu, göz kuruluğu, yorgunluk", "Tükürük ve gözyaşı bezlerine yönelik otoimmün reaksiyon.", "Romatoloji"),
("Lupus", "deri döküntüleri, eklem ağrısı, yorgunluk", "Sistemik lupus eritematozus.", "Romatoloji"),
("Skleroderma", "cilt sertleşmesi, eklem ağrısı", "Bağ dokusu hastalığı, cilt ve iç organlarda skleroz.", "Romatoloji"),
("Polimiyalji Romatik", "kas ağrısı, sabah tutukluğu, ateş", "Yaşlılarda görülen inflamatuar durum.", "Romatoloji"),
("Ankilozan Spondilit", "bel ağrısı, sabah tutukluğu, hareket kısıtlılığı", "Omurga ve pelvik eklemlerde kronik inflamasyon ve kaynaşma.", "Romatoloji"),
("Psoriatik Artrit", "eklem ağrısı, deri döküntüsü, tırnak deformiteleri", "Sedef hastalığı ile ilişkili olabilen artrit formu.", "Romatoloji"),
("Reaktif Artrit", "eklem ağrısı, göz iltihabı, idrar yolu belirtileri", "Bakteriyel enfeksiyon sonrası ortaya çıkan inflamatuar artrit.", "Romatoloji"),
("Osteoartrit", "eklem ağrısı, sertlik, hareket kısıtlılığı", "Kıkırdak aşınması ve eklem dejenerasyonu sonucu oluşan hastalık.", "Romatoloji"),
("Behçet Hastalığı", "oral/genital ülserler, eklem ağrısı, deri döküntüleri", "Multisistemik inflamatuar hastalık, vazulit ile seyreden durum.", "Romatoloji"),
("Familial Mediterranean Fever", "tekrarlayan ateş atakları, karın ağrısı, eklem ağrısı", "Genetik inflamatuar hastalık, özellikle Akdeniz kökenlilerde görülür.", "Romatoloji"),
("Adult Still's Hastalığı", "yüksek ateş, eklem ağrısı, döküntü", "Sistemik inflamatuar hastalık; yetişkin formu, eklem ve deri belirtileri ile.", "Romatoloji"),
("Juvenil İdiopatik Artrit", "eklem şişliği, ağrı, sabah tutukluğu", "Çocuklarda görülen kronik artrit, çeşitli alt tipleri mevcut.", "Romatoloji"),
("Mixed Connective Tissue Disease", "eklem ağrısı, deri döküntüleri, yorgunluk", "Birden fazla otoimmün hastalığın özelliklerini taşıyan bağ dokusu bozukluğu.", "Romatoloji"),
("Undifferentiated Connective Tissue Disease", "yorgunluk, eklem ağrısı, hafif deri döküntüleri", "Belirgin özellikleri tam ortaya çıkmamış bağ dokusu hastalığı.", "Romatoloji"),
("Antifosfolipid Sendromu", "tekrarlayan tromboz, obstetrik komplikasyonlar", "Kan pıhtılaşma bozukluğu; otoimmün reaksiyon sonucu antifosfolipid antikorlarının varlığı.", "Romatoloji"),
("Granülomatoz Poliangiitis (Wegener)", "sinüs problemleri, akciğer ve böbrek tutulum, eklem ağrıları", "Küçük damarları etkileyen sistemik inflamatuar hastalık.", "Romatoloji"),
("Eosinofilik Fasciitis", "eklem sertliği, cilt kalınlaşması, kas ağrıları", "Nadir görülen, eozinofil infiltrasyonu ile karakterize inflamatuar durum.", "Romatoloji"),
("Palindromik Artrit", "tekrarlayan, atak şeklinde eklem ağrısı ve şişlik", "Kısa süreli ve tekrarlayan artrit atakları; romatoid artrit öncülü olabilen durum.", "Romatoloji"),
("RS3PE Sendromu", "el ve ayaklarda şişlik, pitting ödem, eklem ağrısı", "Yaşlılarda görülen remitting seronegatif simetrik sinovit ve pitting ödem sendromu.", "Romatoloji")
    ]
    endokrin_diseases = [
        ("Diyabet Mellitus", "aşırı susuzluk, sık idrara çıkma, kilo kaybı", "Kronik yüksek kan şekeri durumu.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Hipotiroidizm", "yorgunluk, kilo alımı, soğuk intoleransı", "Tiroid hormonlarının yetersizliği.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Hipertiroidizm", "hızlı kalp atışı, kilo kaybı, titreme", "Tiroid hormonlarının aşırı üretimi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Polikistik Over Sendromu", "düzensiz adet, tüylenme, kilo artışı", "Hormonal dengesizlik nedeniyle yumurtalık kistleri oluşması.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Metabolik Sendrom", "obezite, yüksek tansiyon, dislipidemi", "Metabolik risk faktörlerinin bir araya gelmesi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Obezite", "aşırı kilo, yorgunluk, hareket kısıtlılığı", "Vücut yağ oranının sağlıksız şekilde artması.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Akromegali", "el ve ayaklarda büyüme, çene çıkması, kas güçsüzlüğü", "Büyüme hormonunun aşırı üretimi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Prolaktinom", "süt salgısı, adet düzensizliği, kısırlık", "Hipofiz bezinde prolaktin üreten tümör.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Adrenal Yetmezlik (Addison Hastalığı)", "yorgunluk, kilo kaybı, hiperpigmentasyon", "Adrenal bezlerin yetersiz hormon üretimi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Cushing Sendromu", "yüz yuvarlaklığı, kilo artışı, cilt incelmesi", "Aşırı kortizol üretimi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Multiple Endocrine Neoplazi", "aile öyküsü, hormonal dengesizlik, tümör gelişimi", "Genetik olarak belirlenen multiple endokrin tümör sendromu.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Paratiroid Hiperfonksiyonu", "kemik ağrısı, böbrek taşı, kas güçsüzlüğü", "Paratiroid bezlerinin aşırı paratiroid hormon üretimi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Paratiroid Hipofonksiyonu", "kas krampları, nöbet, düşük kan kalsiyumu", "Paratiroid hormonunun yetersizliği ile düşük kan kalsiyum düzeyi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Diabetik Ketoasidoz", "bulantı, karın ağrısı, karakteristik nefes kokusu", "Yetersiz insülin nedeniyle keton üretiminin artması.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Gonadal Yetmezlik", "infertilite, cinsel disfonksiyon, yorgunluk", "Yumurtalık veya testis fonksiyonlarının yetersizliği.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Turner Sendromu", "kısa boy, amenore, infertilite", "X kromozomunun eksikliği ile karakterize genetik durum.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Klinefelter Sendromu", "erkeklerde artmış göğüs dokusu, infertilite, uzun boy", "Erkeklerde ekstra X kromozomunun bulunması.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Hipotalamik Amenore", "adet düzensizliği, amenore, yorgunluk", "Hipotalamik aksın disfonksiyonu ile ilişkili hormonal bozukluk.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Lipodistrofi", "yağ dağılımı anormallikleri, insülin direnci, kas kaybı", "Vücut yağ dağılımının anormal düzenlenmesi.", "Endokrinoloji ve Metabolizma Hastalıkları"),
("Osteoporoza Bağlı Endokrin Bozukluk", "kemik kırıklığı, düşük kemik yoğunluğu, ağrı", "Hormon dengesizliğinden kaynaklı kemik erimesi.", "Endokrinoloji ve Metabolizma Hastalıkları")
    ]
    dermatoloji_diseases = [
        ("Akne Vulgaris", "sivilce, kızarıklık, yağlı cilt", "Ciltteki yağ bezlerinin tıkanması sonucu oluşan inflamasyon.", "Dermatoloji"),
("Egzama", "kaşıntı, kızarıklık, pullanma", "Ciltte inflamasyon ve kuruluk.", "Dermatoloji"),
("Sedef Hastalığı", "kırmızı lekeler, pullanma, kaşıntı", "Cilt hücrelerinin hızlanmış çoğalması.", "Dermatoloji"),
("Vitiligo", "deride renk kaybı", "Melanositlerin kaybolması sonucu oluşan depigmentasyon.", "Dermatoloji"),
("Rosacea", "yüzde kızarıklık, sivilce benzeri lezyonlar", "Yüzde sürekli kızarma ve iltihaplanma.", "Dermatoloji"),
("Melasma", "yaslanma, lekelenme, hiperpigmentasyon", "Güneş, hormonal değişiklikler ve genetik faktörlerin etkisiyle ortaya çıkan simetrik yüz lekeleri.", "Dermatoloji"),
("Alopecia Areata", "saç dökülmesi, yamalar halinde saç kaybı", "Bağışıklık sisteminin saç foliküllerine saldırması sonucunda meydana gelen lokal saç dökülmesi.", "Dermatoloji"),
("Dermatitis Herpetiformis", "yoğun kaşıntı, kabarcıklar, papüller", "Gluten duyarlılığına bağlı, ciltte veziküler döküntülerle seyreden inflamatuar durum.", "Dermatoloji"),
("Impetigo", "bal rengi kabuklar, lokal kızarıklık", "Stafilokok veya streptokok bakterilerinin neden olduğu yüzeysel cilt enfeksiyonu.", "Dermatoloji"),
("Tinea Corporis", "halka şeklinde, kaşıntılı, pullu deri lezyonları", "Dermatofit mantar enfeksiyonunun neden olduğu ringworm.", "Dermatoloji"),
("Pityriasis Rosea", "hafif kaşıntı, soluk döküntü, herald patch", "Başlangıçta ortaya çıkan tek büyük lezyon (herald patch) sonrası vücudun yaydığı döküntü.", "Dermatoloji"),
("Lichen Planus", "purpur, oval papüller, kaşıntı", "T-hücresi aracılı inflamasyon sonucu deri ve mukozada lezyon oluşumu.", "Dermatoloji"),
("Ürtiker", "ani kaşıntı, şişlik, kızarıklık", "Allerjik reaksiyon veya stresin tetiklediği geçici deri döküntüleri (hives).", "Dermatoloji"),
("Kontakt Dermatit", "deride kızarıklık, kabarcıklar, kaşıntı", "Direkt temas sonucu alerjik veya irritatif cilt reaksiyonu.", "Dermatoloji"),
("Seboreik Dermatit", "saçlı deride pullanma, kızarıklık", "Yağ bezlerinin aşırı aktivitesi ve mikroorganizmaların etkisiyle kronik inflamasyon.", "Dermatoloji"),
("Scabies", "yoğun kaşıntı, ince çizgili döküntüler, kabarcıklar", "Sarcoptes scabiei akarına bağlı enfestasyon, özellikle gece artan kaşıntı ile kendini gösterir.", "Dermatoloji"),
("Granuloma Annulare", "yuvarlak, halkasal döküntüler", "İnflamatuar dermatoz; genellikle el ve ayaklarda görülen nodüler lezyonlar.", "Dermatoloji"),
("Lichen Simplex Chronicus", "kalınlaşmış, kaşıntılı cilt, çizgili döküntüler", "Kronik tahriş ve sürekli kaşıntı sonucu cildin kalınlaşması.", "Dermatoloji"),
("Pityriasis Versicolor", "hipopigment veya hiperpigment lekeler, pullanma", "Malassezia mantarının neden olduğu, cildin renk dengesini bozan yüzeysel enfeksiyon.", "Dermatoloji"),
("İlaç Döküntüsü", "yaygın kızarıklık, döküntü, kaşıntı", "Alerjik reaksiyon sonucu ortaya çıkan ilaçlara bağlı dermatolojik yan etki.", "Dermatoloji")
    ]

    departments_data = {
        "Göğüs Hastalıkları": chest_diseases,
        "Nefroloji": nephro_diseases,
        "Kardiyoloji": cardio_diseases,
        "Nöroloji": neuro_diseases,
        "Ortopedi": ortho_diseases,
        "Hematoloji": hema_diseases,
        "Onkoloji": onco_diseases,
        "Dahiliye": dahiliye_diseases,
        "Gastroenteroloji": gastro_diseases,
        "Kulak Burun Boğaz": kulak_burun_bogaz_diseases,
        "Pediatri": pediatri_diseases,
        "Üroloji": uroloji_diseases,
        "Kadın Doğum": kadin_dogum_diseases,
        "Göz Hastalıkları": goz_diseases,
        "İmmünoloji": immunoloji_diseases,
        "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji": enfeksiyon_diseases,
        "Romatoloji": romatoloji_diseases,
        "Endokrinoloji ve Metabolizma Hastalıkları": endokrin_diseases,
        "Dermatoloji": dermatoloji_diseases,
    }
    for dept, records in departments_data.items():
        c.execute("SELECT COUNT(*) FROM diseases WHERE department = ?", (dept,))
        if c.fetchone()[0] == 0:
            c.executemany(
                "INSERT INTO diseases (name, symptoms, description, department) VALUES (?, ?, ?, ?)",
                records)
    conn.commit()
    print("Veritabanı güncellendi. Gerekli kayıtlar eklenmiştir.")
    conn.close()

# ----------------------------------------------------------------------
# AŞAMA 2b: SEÇİLEN BÖLÜME AİT HASTALIKLARI VE ARAMA YAPILAN KAYITLARI YÜKLE
# ----------------------------------------------------------------------
def load_diseases_by_department(department, name_query=None, symptomatic_filters=None):
    """
    Belirtilen bölüm için, isteğe bağlı olarak hastalık adında arama ve
    ve tıklanmış belirtiler üzerinden filtreleme yaparak verileri çeker.
    """
    conn = sqlite3.connect("chest_diseases.db")
    c = conn.cursor()
    query = "SELECT name, symptoms, description FROM diseases WHERE department = ?"
    params = [department]
    if name_query:
        query += " AND name LIKE ?"
        params.append(f"%{name_query}%")
    if symptomatic_filters:
        for sym in symptomatic_filters:
            query += " AND symptoms LIKE ?"
            params.append(f"%{sym}%")
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows

# ----------------------------------------------------------------------
# AŞAMA 3: ANA MENÜ (BÖLÜM SEÇİM EKRANI)
# ----------------------------------------------------------------------
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bölüm Seçim Uygulaması")
        self.geometry("1000x600")  # Pencere boyutunu büyüt
        self.configure(padx=20, pady=20, bg="lightgray")  # Ana pencere arka planı gri

        # Daha büyük yazı tipi boyutları için güncellenmiş etiket
        tk.Label(
            self,
            text="Lütfen bir bölüm seçin:",
            font=("Helvetica", 20, "bold"),  # Daha büyük bir font
            bg="lightgray",  # Arka plan rengi
            fg="darkslategray"  # Metin rengi
        ).pack(pady=20)

        # Daha fazla yer açmak için geniş çerçeve
        btn_frame = tk.Frame(self, bg="lightgray")  # Buton çerçevesinin arka planı gri
        btn_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Bölümleri ve buton düzenini ayarlamak
        departments = [
            "Göğüs Hastalıkları", "Nefroloji", "Kardiyoloji", "Nöroloji",
            "Ortopedi", "Hematoloji", "Onkoloji", "Dahiliye", "Gastroenteroloji",
            "Kulak Burun Boğaz", "Pediatri", "Üroloji", "Kadın Doğum", "Göz Hastalıkları",
            "İmmünoloji", "Enfeksiyon Hastalıkları ve Klinik Mikrobiyoloji", "Romatoloji",
            "Endokrinoloji ve Metabolizma Hastalıkları", "Dermatoloji"
        ]

        # Geniş bir grid yapısı için 4 sütun
        columns = 4
        for i, dept in enumerate(departments):
            count = self.get_disease_count(dept)
            tk.Button(
                btn_frame,
                text=f"{dept} ({count})",
                font=("Helvetica", 14),  # Buton metin boyutu büyütüldü
                bg="gray",  # Buton arka planı
                fg="white",  # Buton yazı rengi
                activebackground="darkgray",  # Tıklandığında arka plan
                activeforeground="lightgray",  # Tıklandığında yazı rengi
                width=20,  # Buton genişliği artırıldı
                command=lambda d=dept: self.open_disease_list(d)
            ).grid(row=i // columns, column=i % columns, padx=10, pady=10, sticky="nsew")

        for col in range(columns):
            btn_frame.grid_columnconfigure(col, weight=1)

        # Daha büyük bir çıkış butonu
        tk.Button(
            self,
            text="Çıkış",
            font=("Helvetica", 16),  # Daha büyük yazı tipi
            command=self.quit,
            bg="dimgray",  # Çıkış butonunun gri tonları
            fg="white"
        ).pack(pady=20)

    def get_disease_count(self, department):
        conn = sqlite3.connect("chest_diseases.db")
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM diseases WHERE department = ?", (department,))
        count = c.fetchone()[0]
        conn.close()
        return count

    def open_disease_list(self, department):
        DiseaseListWindow(self, department)

class DiseaseListWindow(tk.Toplevel):
    def __init__(self, parent, department):
        super().__init__(parent)
        self.department = department
        self.title(f"{department} Hastalık Listesi")
        self.geometry("900x500")
        self.configure(padx=10, pady=10, bg="lightgray")  # Pencerenin arka planı gri

        # Sol taraf
        self.left_frame = tk.Frame(self, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        search_frame = tk.Frame(self.left_frame, bg="lightgray")
        search_frame.pack(pady=5, fill=tk.X)

        tk.Label(search_frame, text="Hastalık Adında Ara:", font=("Helvetica", 12), bg="lightgray", fg="black").pack(side=tk.LEFT, padx=5)
        self.search_name_entry = tk.Entry(search_frame, font=("Helvetica", 12), bg="white", fg="black")
        self.search_name_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        btn_frame = tk.Frame(self.left_frame, bg="lightgray")
        btn_frame.pack(pady=5, fill=tk.X)

        tk.Button(btn_frame, text="Ara", font=("Helvetica", 12), bg="darkgray", fg="white", command=self.perform_search).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Yeni Hastalık Ekle", font=("Helvetica", 12), bg="gray", fg="white", command=self.add_disease).pack(side=tk.LEFT, padx=5)

        self.disease_listbox = tk.Listbox(self.left_frame, font=("Helvetica", 12), bg="gainsboro", fg="black")
        self.disease_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.disease_listbox.bind("<<ListboxSelect>>", self.show_details)

        self.details_text = tk.Text(self.left_frame, height=8, font=("Helvetica", 12), wrap=tk.WORD, bg="white", fg="black")
        self.details_text.pack(fill=tk.X, padx=10, pady=10)

        # Sağ taraf: Belirti filtresi
        self.symptom_panel = tk.Frame(self, bg="lightsteelgray", bd=2, relief=tk.GROOVE)
        self.symptom_panel.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.symptom_panel, text="Belirtiler:", font=("Helvetica", 14, "bold"), bg="lightsteelgray", fg="black").pack(pady=10)

        # Kaydırılabilir belirtiler paneli
        canvas = tk.Canvas(self.symptom_panel, bg="lightsteelgray")
        scrollbar = tk.Scrollbar(self.symptom_panel, orient="vertical", command=canvas.yview)
        symptom_container = tk.Frame(canvas, bg="lightsteelgray")
        canvas.create_window((0, 0), window=symptom_container, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# ----------------------------------------------------------------------
# AŞAMA 4: HASTALIK LİSTESİ VE DETAY PENCERESİ (SAĞDA BELİRTI FİLTRE PANELİ)
# ----------------------------------------------------------------------
class DiseaseListWindow(tk.Toplevel):
    def __init__(self, parent, department):
        super().__init__(parent)
        self.department = department
        self.title(f"{department} Hastalık Listesi")
        self.geometry("1200x700")
        self.configure(padx=10, pady=10)

        # Ana panoyu yatay olarak ayırıyoruz.
        paned = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)

        # Sol kısım: Arama, liste, detay metni.
        self.left_frame = tk.Frame(paned)
        paned.add(self.left_frame, stretch="always")

        search_frame = tk.Frame(self.left_frame)
        search_frame.pack(pady=5, fill=tk.X)
        tk.Label(search_frame, text="Hastalık Adında Ara:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        self.search_name_entry = tk.Entry(search_frame, font=("Helvetica", 12))
        self.search_name_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        btn_frame = tk.Frame(self.left_frame)
        btn_frame.pack(pady=5, fill=tk.X)
        tk.Button(btn_frame, text="Ara", font=("Helvetica", 12), command=self.perform_search).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Yeni Hastalık Ekle", font=("Helvetica", 12), command=self.add_disease).pack(side=tk.LEFT, padx=5)

        self.disease_listbox = tk.Listbox(self.left_frame, font=("Helvetica", 12))
        self.disease_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.disease_listbox.bind("<<ListboxSelect>>", self.show_details)

        self.details_text = tk.Text(self.left_frame, height=8, font=("Helvetica", 12), wrap=tk.WORD)
        self.details_text.pack(fill=tk.X, padx=10, pady=10)

        # Sağ kısım: Belirti filtreleme paneli.
        self.symptom_panel = tk.Frame(paned, bd=2, relief=tk.GROOVE)
        paned.add(self.symptom_panel, minsize=200)
        tk.Label(self.symptom_panel, text="Belirtiler:", font=("Helvetica", 14, "bold")).pack(pady=5)
        # Kaydırılabilir bir alan ekleyelim:
        canvas = tk.Canvas(self.symptom_panel)
        scrollbar = tk.Scrollbar(self.symptom_panel, orient="vertical", command=canvas.yview)
        self.symptom_container = tk.Frame(canvas)
        self.symptom_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.symptom_container, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Sözlük olarak tüm checkbutton değişkenlerini saklayalım.
        self.symptom_vars = {}
        self.update_symptom_panel()

        # İlk sıfırlama ile listeyi yükleyelim.
        self.load_diseases_data()

    def update_symptom_panel(self):
        """
        İlgili bölümde yer alan tüm hastalıkların belirtilerini sorgulayıp,
        benzersiz belirtileri checkbox şeklinde oluşturur.
        """
        # Mevcut widget'ları temizle.
        for widget in self.symptom_container.winfo_children():
            widget.destroy()
        self.symptom_vars.clear()
        conn = sqlite3.connect("chest_diseases.db")
        c = conn.cursor()
        c.execute("SELECT symptoms FROM diseases WHERE department = ?", (self.department,))
        rows = c.fetchall()
        conn.close()
        symptoms_set = set()
        for (symptoms_str,) in rows:
            for sym in symptoms_str.split(","):
                s = sym.strip()
                if s:
                    symptoms_set.add(s)
        unique_symptoms = sorted(symptoms_set)
        for s in unique_symptoms:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.symptom_container, text=s, variable=var,
                                command=self.perform_search)
            cb.pack(anchor="w")
            self.symptom_vars[s] = var

    def load_diseases_data(self, name_query=None, symptomatic_filters=None):
        # Filtre parametresi; symptomatic_filters listesi => toplanmış checkbutton seçimi.
        if symptomatic_filters is None:
            # Checkboxes'dan seçilenleri alıyoruz.
            symptomatic_filters = [sym for sym, var in self.symptom_vars.items() if var.get()]
        self.disease_data = load_diseases_by_department(self.department, name_query, symptomatic_filters)
        self.disease_listbox.delete(0, tk.END)
        for record in self.disease_data:
            self.disease_listbox.insert(tk.END, record[0])
        self.details_text.delete("1.0", tk.END)

    def perform_search(self):
        name_query = self.search_name_entry.get().strip()
        symptomatic_filters = [sym for sym, var in self.symptom_vars.items() if var.get()]
        self.load_diseases_data(name_query if name_query else None, symptomatic_filters)

    def show_details(self, event):
        selection = self.disease_listbox.curselection()
        if selection:
            index = selection[0]
            name, symptoms, description = self.disease_data[index]
            self.details_text.delete("1.0", tk.END)
            self.details_text.insert(tk.END, f"Hastalık: {name}\n\nBelirtiler: {symptoms}\n\nAçıklama: {description}")

    def add_disease(self):
        new_name = simpledialog.askstring("Yeni Hastalık", "Hastalık Adı:")
        if not new_name:
            return
        new_symptoms = simpledialog.askstring("Yeni Hastalık", "Belirtiler (virgülle ayırarak):")
        if not new_symptoms:
            return
        new_description = simpledialog.askstring("Yeni Hastalık", "Açıklama:")
        if not new_description:
            return
        conn = sqlite3.connect("chest_diseases.db")
        c = conn.cursor()
        c.execute("INSERT INTO diseases (name, symptoms, description, department) VALUES (?, ?, ?, ?)",
                  (new_name, new_symptoms, new_description, self.department))
        conn.commit()
        conn.close()
        messagebox.showinfo("Başarılı", "Yeni hastalık başarıyla eklendi.")
        self.update_symptom_panel()  # Belirti panelini güncelle
        self.perform_search()

# ----------------------------------------------------------------------
# AŞAMA 5: UYGULAMANIN BAŞLATILMASI
# ----------------------------------------------------------------------
if __name__ == "__main__":
    create_db()
    app = MainMenu()
    app.mainloop()