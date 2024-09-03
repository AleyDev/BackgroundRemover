from rembg import remove  # rembg kütüphanesinden remove fonksiyonunu içe aktarıyorum

# Girdi olarak arka planı silinmesi istenen .jpeg dosyasını belirtiyorum
input_path = "aley.sb.jpeg"  
"""
    Bu dosya, arka planı kaldırmak istediğim görüntüyü içeriyor. Normalde dosyayı
    klasör içerisine yerleştirmemiş olsaydım, tam dosya yolunu yazmam gerekirdi.
"""

# Çıktı olarak bir png dosyası belirtiyorum çünkü arka planı transparan yapabilen dosya türü png'dir
output_path = "output.png"  
"""
    JPEG formatı transparan arka planı desteklemez, bu yüzden çıktıyı PNG formatında alıyorum.
"""

# Dosyayı okuma modunda açıyorum
with open(input_path, "rb") as i:  # rb: read, binary - dosyayı binary formatında okuyorum
    
    # Çıktı dosyasını yazma modunda açıyorum
    with open(output_path, "wb") as o:  # wb: write, binary - dosyayı binary formatında yazıyorum
        
        # Giriş dosyasını okuyorum
        input_file = i.read()  # i.read(): girdi dosyasını okuyorum

        # Arka planı kaldırmak için rembg kütüphanesinin remove fonksiyonunu kullanıyorum
        output_file = remove(input_file)  # remove: rembg kütüphanesinden gelen fonksiyon, arka planı kaldırıyor
        
        # Çıktı dosyasını yazıp kaydediyorum
        o.write(output_file)  # o.write(): çıktı dosyasını yazıp kaydediyorum
