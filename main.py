import pytesseract
import cv2
from PIL import Image

discord="dao026"#discordum

#bunu indirmeniz gerekli https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v4.0.0-beta.4.20180912.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"#eğer bunu yapmasaydık pytesseract metin çıkarma işlemini kullanamazdık 

cap = cv2.VideoCapture(0)#kamera açıyor


while True:
    calis, yeni_resim = cap.read()#cap.read iki tane değer döndürüyor birisi görüntü gelip gelmediğini (yani True,False) biriside direk çerçeviyi kaplıyor

    if calis==False:#burda eğer görüntü yoksa çalışmıyorsa döngüyü kır diyoruz
        break
    metin = pytesseract.image_to_string(Image.fromarray(yeni_resim))#burda görüntüyü yazıya dönüştürüyoruz Image.fromarray bu komut videodan görüntü alıyor

    print(metin)#burda metin

    cv2.imshow("Resim", yeni_resim)#burda videoyu pencere şeklinde gösteriyor
    
    key = cv2.waitKey(1)#burda basılan tuşu döndürüyor ve 1 milisaniye bekliyor tuşdan cevap almak için
    if key == 27:#ascii tablosundaki 27 dec yani esc temsil ediyor eğer klavyede esc basarsak döngü kırılıyor
        break

cap.release()#burda zatem döngü kırıldığında yada programı kapattığımızda video akışını serbest bırakıyor
cv2.destroyAllWindows()#bütün pencereleri kapatıyor
