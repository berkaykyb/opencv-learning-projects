## YOLO Nedir ?

**YOLO (You Only Look Once)**, derin öğrenme tabanlı bir nesne tespit yaklaşımıdır.

Klasik yöntemlerden farklı olarak:
- Görüntüyü parça parça incelemez
- Tek seferde (single forward pass) tüm görüntüyü işler
- Aynı anda hem **nesnenin yerini** hem de **hangi sınıfa ait olduğunu** tahmin eder

Bu sayede avantajları:
- Baştan sona öğrenme (end-to-end learning)
- Çok daha hızlı
- Ölçek, ışık ve arka plan değişimlerine daha dayanıklı

## Klasik (Geleneksel) Nesne Tespit Yöntemleri

Derin öğrenme öncesinde kullanılan bazı yöntemler:

- **Haar Cascade (Viola–Jones)**  
  Özellikle yüz algılamada kullanılan, elle tanımlanmış özelliklere dayalı yöntem.

- **HOG + SVM**  
  Görüntüden özellik çıkarılır (Histogram of Oriented Gradients),
  ardından SVM gibi bir sınıflandırıcı kullanılır.

- **Sliding Window Yaklaşımı**  
  Görüntü üzerinde küçük pencereler gezdirilerek nesne aranır.

Bu yöntemlerin sorunları:
- Özellikler manuel olarak tasarlanır
- Karmaşık sahnelerde başarısız olurlar
- Gerçek zamanlı çalışmakta zorlanırlar

## Ultralytics Nedir?

**Ultralytics**, YOLOv8 modellerini kolayca kullanmamızı sağlayan bir Python kütüphanesidir.

Ultralytics bize şunları sağlar:
- Hazır eğitilmiş YOLOv8 modelleri
- Nesne tespiti, takip, eğitim ve test için hazır fonksiyonlar
- OpenCV ve video akışlarıyla kolay entegrasyon

Bu proje kapsamında:
- Derin öğrenme modelini sıfırdan yazmak yerine hazır, endüstri standardı bir modeli doğru şekilde kullanmayı öğrendim.

## Algoritma Akışı

1. **YOLO modelini yükle**
   - Hazır eğitilmiş bir YOLOv8 modeli kullanıyorum.

2. **Videoyu aç**
   - `cv2.VideoCapture` ile videoyu frame frame okuyacağım.

3. **Frame döngüsüne gir**
   - Videodaki her kareyi tek tek alıyorum.
   - Video bittiğinde döngü kendiliğinden duruyor.

4. **Frame’i YOLO’ya ver**
   - YOLO bu karede hangi nesneler var, nerede ve hangisi hangisi söylüyor.
   - `persist=True` sayesinde aynı nesne her karede aynı ID’yi alıyor.
   - Yani artık sadece “tespit” değil, “takip” yapıyorum.

5. **Sonuçları frame üzerine çizdir**
   - Kutular, sınıf isimleri ve takip ID’leri otomatik çiziliyor.
   - Modelin ne gördüğünü görsel olarak net şekilde görebiliyorum.

6. **Ekranda göster**

7. **Kaynakları kapat**

