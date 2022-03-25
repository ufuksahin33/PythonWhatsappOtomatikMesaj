import pywhatkit as kit

try:
    kit.sendwhatmsg ("+90**********","Günaydın \U0001F607",12,54)
    print ("Mesaj Başarıyla Gönderildi")
except :
    print ("Beklenmeyen bir hata sonucu mesaj gönderilemedi")