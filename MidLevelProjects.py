# #--------------------------------------------------------------------------Sayı Listesinin Ortalaması----------------------------------------------------------------------------------

# terimSayisi=int(input("Kaç adet terimin ortalamasını bulmak istiyorsunuz:"))
# sayilar=[]
# toplam=0

# for x in range(0,terimSayisi):
#     sayi=int(input("Sayılarınızı giriniz: "))
#     sayilar.append(sayi)
#     toplam=toplam+sayi
# ort=toplam/terimSayisi
# print(ort)

#---------------------------------------------------------------------------En Küçük Ve En Büyük Sayıyı Bulma---------------------------------------------------------------------------

# terimSayisi=int(input("Kaç Terim gireceksiniz:"))
# sayilar=[]

# for x in range(0,terimSayisi):
#     sayi=int(input("Sayılarınızı giriniz:"))
#     sayilar.append(sayi)
# sayilar.sort()
# print(f"En küçük terim: {sayilar[0]} en büyük terim ise: {sayilar[-1]} ")





#---------------------------------------------------------------------------Tekrarlayan Sayıları Bulma-----------------------------------------------------------------------------
# terimSayısı=int(input("Kaç adet terim gireceksiniz"))
# liste=[]

# for x in range(0,terimSayısı):
#     sayi=int(input("Sayılarınızı giriniz"))
#     liste.append(sayi)
# tekrarList=[]

# for eleman in liste:
#     if liste.count(eleman)>1 and eleman not in tekrarList:
#         tekrarList.append(eleman)
# if tekrarList:
#     for eleman in tekrarList:
#         tekrarSayisi=liste.count(eleman)
#         print(f"{eleman} --> {tekrarSayisi} kez")

# else:
#     print("Tekrarlayan eleman yok")

#-----------------------------------------------------------------------Sayı Tahmin Oyunu-------------------------------------------------------------------------------------------

# import random
# randomNum=random.randint(1,100)
# tahimSayisi=3

# while True:
#      tahmin=int(input("Tahmininiz olan sayıyı giriniz"))
#      tahimSayisi-=1

#      if randomNum<tahmin:
#       print(f"Yanlış tahmin lütfen daha düşük bir sayı giriniz {tahimSayisi} hakkınız kaldı")
#       if tahimSayisi==0:
#         print("Hakkınız doldu oyunu kaybettiniz")
#         break 
#      elif randomNum>tahmin:
#       print(f"Tahmimininiz yanlış lütfen daha büyük bir sayı giriniz {tahimSayisi} hakkınız kaldı")
#       if tahimSayisi==0:
#         print("Hakkınız doldu oyunu kaybettiniz")
#         break
#      else:
#       print(f"Tahimininz Doğru! {tahimSayisi} hakkınız kalmıştı")

#--------------------------------------------------------------------------ToDo List---------------------------------------------------------------------------------------------------

# todoList=[]

# while True:

#     choises={
        
#         "1":"Görev EKle",
#         "2":"Görevleri Göster",
#         "3":"Görev Sil",
#         "4":"Çıkış"
    
# }
    
#     print(choises)
#     secim=int(input("Seçimizi Giriniz:"))
#     if secim<=0 or secim>=5:
#         print("Seçiminiz 1 ile  4 arasında olmalıdır")
#     else:
#      if secim==1:
#         print("Görevinizi Ekleyin:")
#         görev=input("Görevinizi giriniz:")
#         todoList.append(görev)
#      elif secim==2:
#         if len(todoList)>=1:
#             for görev in todoList:
#                 print(görev)
#         else:
#             print("Göreviniz bulunmamaktadır!")
#      elif secim==3:
#             sayac=1
#             for görev in todoList:
#              print(sayac,görev)
#              sayac+=1
#             sil=int(input("Silmek İstedğiniz numarayı giriniz:"))
#             todoList.pop(sil-1)
#      elif secim==4:
#         print("Uygulamadan çıktınız!")
#         break


#------------------------------------------------------------------Phone Book--------------------------------------------------------------------------------------------------------

    



# phoneList={}

# while True:
         
#         menu={
#         "1":"Kişi Ekle",
#         "2":"Kişileri Göster",
#         "3":"Kişi Sil",
#         "4":"Çıkış"
#     }
#         print(menu)
        
#         secim=int(input("Seçiminizi yapınız: "))

#         if secim<=0 or secim>=5:
#              print("Lütfen 1 ile 4 arası bir sayı giriniz")
#         else:
#             if secim==1:
#                 issim=input("Eklemek istediğiniz kişinin ismini giriniz")
#                 numara=input("Numarayı giriniz")
#                 phoneList[issim]=numara
#             elif secim==2:
#                  if not phoneList:
#                       print("Kayıtlı kişi bulunmuyor")
#                  for issim,numara in phoneList.items():
#                       print(f"{issim} --> {numara}")
#             elif secim==3:
#                  print(issim)
#                  sil=input("Silmek istediğiniz kişinin ismini siliniz")
#                  if sil in phoneList:
#                       phoneList.pop(sil)
#                       print("Kişi silindi")
#                  else:
#                     print("Kayıtlı issim bulunamadı!")
#             elif secim==4:
#                  print("Uygulamadan çıktınız")
#                  break
                      
#-----------------------------------------------------------------------ATM UYGULAMASI-------------------------------------------------------------------------------------------------

# bakiye=0

# while True:
    
#  menu={
#     "1":"Bakiye Görüntüle",
#     "2":"Para Yatır",
#     "3":"Para Çek",
#     "4":"Çıkış"
# }
#  print(menu)
#  islem=input("Lütfen yapmak istediğinz işlemin rakamını giriniz.")

#  if islem=="1":
#   print(f"Güncel bakiyeniz {bakiye} TL dir.")
#  elif islem=="2":
#   yeniBakiye=int(input("Lütfen yatırmak istediğiniz mevlayı giriniz: "))
#   bakiye=bakiye+yeniBakiye
#  elif islem=="3":
#   paraCek=int(input(f"Çekmek istediğiniz bakiyeyi giriniz. Güncel bakiyeniz: {bakiye} TL"))
#   if paraCek<=bakiye:
#    bakiye=bakiye-paraCek
#    print(f"Paranız çekilmiştir güncel bakiyeniz {bakiye} TL")
#   elif paraCek>bakiye:
#    print("Lütfen sahip olduğunuz paradan daha fazlasını çekmeye çalışmayınız !")
#  elif islem=="4":
#   print("Uygulamadan Çıktınız !")
#   break


