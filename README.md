# Arka Plan Silici (Background Remover)

Bu Python script'i, `rembg` kütüphanesini kullanarak JPEG görüntülerinin arka planını kaldırır ve sonucu PNG formatında kaydeder. Görüntülerin arka planını şeffaf hale getirerek daha fazla düzenleme veya işleme için uygun hale getirir.

## Özellikler

- **Arka Plan Kaldırma:** JPEG formatındaki görüntülerden arka planı kaldırır.
- **Şeffaf PNG Çıkışı:** Sonuç olarak arka planı şeffaf olan PNG formatında çıktı sağlar.
- **Basit Kullanım:** Kullanıcı dostu bir arayüz ile kolay kullanım sağlar.

## Gereksinimler

- Python 3.x
- `rembg` kütüphanesi

## Kurulum

Bu uygulamayı çalıştırmak için önce `rembg` kütüphanesini yüklemeniz gerekmektedir. Bunu yapmak için aşağıdaki komutu kullanabilirsiniz:

```sh
pip install rembg
