# HSV ile Renk Tespiti

## HSV Nedir ve Neden Renk Ayrımında HSV Kullanılır?

Kameradan gelen görüntüde ışık, parlaklık ve gölge sürekli değişir.  
BGR (veya RGB) renk uzayında bu bilgiler renklerle iç içe olduğu için aynı renk farklı değerler alabilir.

HSV renk uzayında ise:

- **H (Hue)** -> rengin kendisi  
- **S (Saturation)** -> rengin canlılığı  
- **V (Value)** -> parlaklık  

Bu ayrım sayesinde:

- Işık değişse bile rengi daha stabil şekilde yakalayabiliyorum.  
- Sadece ilgilendiğim renk aralığını kontrol edebiliyorum.  

Bu yüzden renk tespiti yaparken HSV, BGR’ye göre çok daha mantıklı bir seçim oldu.

---

## Algoritmik Akış

1. Kameradan görüntü al  
   -> Üzerinde işlem yapacağım ham veri bu.  
   -> Ancak görüntü şu an BGR formatında, renk ayrımı için uygun değil.

2. Görüntüyü BGR’den HSV’ye çevir  
   -> Rengi, parlaklıktan ve ışıktan ayırmam gerekiyor.  
   -> HSV’de renk (H) daha stabildir.  
   -> Artık renk bazlı işlem yapabilirim.

3. Hedef rengin HSV aralığını belirle  
   -> Tek bir HSV değeri yeterli değil.  
   -> Işık ve kamera farkları için tolerans gerekir.  
   -> Bu yüzden hedef rengin alt ve üst sınırlarını oluşturmalıyım.

4. Belirlenen HSV aralığına göre maske oluştur  
   -> Görüntüde sadece bu renge ait pikselleri ayıklamak istiyorum.  
   -> Hedef renk beyaz, diğer her şey siyah olacak şekilde maske üretirim.

5. Maskede beyaz alanın konumunu bul  
   -> Renk var mı bilgisi yeterli değil.  
   -> Nerede olduğunu bilmem gerekiyor.  
   -> Beyaz alanı saran en küçük dikdörtgeni (bounding box) hesaplarım.

6. Bulunan konumu orijinal görüntü üzerinde işaretle  
   -> Maskeyi değil, gerçek görüntüyü göstermek istiyorum.  
   -> Bulduğum koordinatları kullanarak dikdörtgen çizerim.

7. Görüntüyü ekranda göster ve çıkış kontrolü yap  
   -> İşlemin gerçek zamanlı çalıştığını görürüm.  
   -> Kullanıcı çıkmak isterse programı düzgün şekilde sonlandırırım.

