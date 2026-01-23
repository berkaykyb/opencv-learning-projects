# Text Detection with OCR

## Tesseract

Tesseract, görüntülerin içindeki yazıları **tahmin etmeye çalışan** bir OCR motoru.

- yazıyı okur
- kütüphane değil, sistemde çalışan bir programdır
- %100 doğruluğu garanti etmez

## pytesseract

pytesseract, Tesseract’ın **Python’da kullanılabilmesi için yazılmış bir köprü**.

## OCR

OCR, görüntü içindeki yazıları **okumaya çalışmak** demektir.

## PIL Image (Pillow)

Tesseract görüntüyü **PIL Image + RGB** formatında ister.

PIL Image deyince:

- ekranda bakınca “bu PIL Image” diye ayırt edilecek farklı bir görüntü yok
- fark, görüntünün **bellekte tutulma şekli** ve **hangi kütüphanenin kullandığı**

OpenCV görüntüyü kendi formatında tutar,  
OCR ise PIL Image formatında daha düzgün çalışır.

---

## Algoritma Akışı

1. Görüntüyü oku
   - Görüntüdeki yazıları okutmam için OCR'a atmam lazım.
   - OCR için mevcut görüntü formatı uygun değil

2. Görüntüyü BGR’den RGB'ye çevir ve PIL Image'e dönüştür
   - Şu an elimde OCR'a verecek bir görüntü var.

3. Tesseract'a görüntüyü ver
   - burada bana “bulabildiği yazı parçaları” için bir liste gibi çıktı dönüyor
   - her parçada text + koordinat bilgisi var (aynı index’te)
   - kaç parça geldiğini bilmem gerekiyor ona göre for başlatıp işlemleri yapıcam

4. Kaç parça geldiğini öğren
   - parça kadar gezip içlerindeki textleri ve koordinatları kaydetmem gerekiyor

5. For ile her parçayı gez ve bilgileri al
   - Elimde textler ve koordinatlar var
   - İlk önce bu texlerin etrafına kutu çekmem gerekiyor

6. Koordinatlardan kutuyu çiz
   - Şimdi altlarına içinde okuyup kaydettiğim yazıyı yazmam gerekiyor

7. Kutunun altına yazılarını yaz
   - En son yaptığım işlemleri göstermem gerekiyor

8. Göster

---

## Ekran Görüntüleri

![OCR](../images/02-text_detection_tabela.png)
