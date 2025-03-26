import tkinter as tk
from tkinter import messagebox
import sqlite3

# Veritabanı ve tablo oluşturma fonksiyonu
def create_patient_table():
    conn = sqlite3.connect("patients.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            adi TEXT NOT NULL,
            soyadi TEXT NOT NULL,
            yasi INTEGER,
            cinsiyeti TEXT,
            ozgecmis TEXT
        )
    """)
    conn.commit()
    conn.close()

# Hasta kaydı uygulaması (Tkinter arayüzü)
class PatientRegistrationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hasta Kaydı Uygulaması")
        self.geometry("500x500")
        self.configure(padx=20, pady=20, bg="lightgray")
        
        # Adı
        tk.Label(self, text="Adı:", font=("Helvetica", 12), bg="lightgray").pack(pady=5)
        self.entry_adi = tk.Entry(self, font=("Helvetica", 12))
        self.entry_adi.pack(pady=5, fill=tk.X, padx=10)
        
        # Soyadı
        tk.Label(self, text="Soyadı:", font=("Helvetica", 12), bg="lightgray").pack(pady=5)
        self.entry_soyadi = tk.Entry(self, font=("Helvetica", 12))
        self.entry_soyadi.pack(pady=5, fill=tk.X, padx=10)
        
        # Yaşı
        tk.Label(self, text="Yaşı:", font=("Helvetica", 12), bg="lightgray").pack(pady=5)
        self.entry_yasi = tk.Entry(self, font=("Helvetica", 12))
        self.entry_yasi.pack(pady=5, fill=tk.X, padx=10)
        
        # Cinsiyeti
        tk.Label(self, text="Cinsiyeti:", font=("Helvetica", 12), bg="lightgray").pack(pady=5)
        self.entry_cinsiyeti = tk.Entry(self, font=("Helvetica", 12))
        self.entry_cinsiyeti.pack(pady=5, fill=tk.X, padx=10)
        
        # Özgeçmiş (isteğe bağlı, kısa açıklama)
        tk.Label(self, text="Özgeçmiş:", font=("Helvetica", 12), bg="lightgray").pack(pady=5)
        self.text_ozgecmis = tk.Text(self, height=5, font=("Helvetica", 12))
        self.text_ozgecmis.pack(pady=5, fill=tk.X, padx=10)
        
        # Kaydet Butonu
        tk.Button(self, text="Kaydet", font=("Helvetica", 14), bg="blue", fg="white",
                  command=self.save_patient).pack(pady=20)

    def save_patient(self):
        # Kullanıcıdan verileri alıyoruz
        adi = self.entry_adi.get().strip()
        soyadi = self.entry_soyadi.get().strip()
        yasi_str = self.entry_yasi.get().strip()
        cinsiyeti = self.entry_cinsiyeti.get().strip()
        ozgecmis = self.text_ozgecmis.get("1.0", tk.END).strip()
        
        if not adi or not soyadi:
            messagebox.showwarning("Eksik Bilgi", "Lütfen Adı ve Soyadı giriniz.")
            return
        
        # Yaş bilgisini sayıya çevirme (girmeden bırakılırsa None olacak)
        try:
            yasi = int(yasi_str) if yasi_str else None
        except ValueError:
            messagebox.showwarning("Hatalı Giriş", "Lütfen Yaşı sayı olarak giriniz.")
            return
        
        # Veritabanına kaydı ekleyelim
        try:
            conn = sqlite3.connect("patients.db")
            c = conn.cursor()
            c.execute("""
                INSERT INTO patients (adi, soyadi, yasi, cinsiyeti, ozgecmis)
                VALUES (?, ?, ?, ?, ?)
            """, (adi, soyadi, yasi, cinsiyeti, ozgecmis))
            conn.commit()
            conn.close()
            messagebox.showinfo("Başarılı", "Hasta kaydı başarıyla eklendi!")
            self.clear_form()
        except sqlite3.Error as e:
            messagebox.showerror("Veritabanı Hatası", f"Bir hata oluştu: {e}")

    def clear_form(self):
        # Form alanlarını temizleyelim
        self.entry_adi.delete(0, tk.END)
        self.entry_soyadi.delete(0, tk.END)
        self.entry_yasi.delete(0, tk.END)
        self.entry_cinsiyeti.delete(0, tk.END)
        self.text_ozgecmis.delete("1.0", tk.END)

if __name__ == "__main__":
    create_patient_table()
    app = PatientRegistrationApp()
    app.mainloop()