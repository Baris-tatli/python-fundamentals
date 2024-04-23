#Tuple (Demetler)
#List'ler gibi benzer mantığa sahiptirler, lakin listelere uyguladığımız built-in fonksiyonlara sahip değildir. İndekxleme mantığı tuple dada mevcuttur.
#Hem listelerde hemde demetelerde ki ortak noktalardan bir diğerine slicing (dilimleme)
#tuple sabitlerimi tutacağımı bir yapı gibi düşünebiliriz. Yani değiştirilemezler, 2 tuple birleştime gibi opsiyonlar vardır.

# tuple_1 = ("galatasaray", "fenerbahçe", "beşiktaş", "trabzonspor")
# tuple_2 = ("12", "b", "35.5", "red skins", "eagles")
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
#
# #Dilimleme (Slicing)
#
# print(tuple_3[0:3])# output => ('galatasaray', 'fenerbahçe', 'beşiktaş')
# print(tuple_3[2:4])# output => ('beşiktaş', 'trabzonspor')
#
# print(tuple_3[:4])# output => ('galatasaray', 'fenerbahçe', 'beşiktaş', 'trabzonspor')
# print(tuple_3[-1])# output => eagles
# print(tuple_3[::-1])# output => ('eagles', 'red skins', '35.5', 'b', '12', 'trabzonspor', 'beşiktaş', 'fenerbahçe', 'galatasaray')
# print(tuple_3[::-2])# output => ('eagles', '35.5', '12', 'beşiktaş', 'galatasaray')
# print(tuple_3[3::-2])# output => ('trabzonspor', 'fenerbahçe')

# tuple  (demetler)
#  listler gibi benzer mantiğa sahiptirler lakin built in fonksiyonmlara sahip degğildir. lakin indexleme mantıgı mevcuttur hemlistelerde hem de demetlerdeki ortak noktalardan bir diğeri de silicing (dilimlemedir)
# tuple sabitleri tutacagımız bir yapı gibidir kısaca. degistirilemezler 2 tuole birleştirme gibi opsiyonlar vardır.

# tuple_1 =('GS' , 'fb', 'BJK', 'trabzon')
# tuple_2 = ('12', '35.5', 'b', 'eagles', 'patrios', 'red skins')
# tuple_3 =  tuple_1 + tuple_2
# print(tuple_3)
# # tule lar normal parantezle tanımlanır, listeler kareli parantez ile tanımlanır.
# #slicing
# print(tuple_3[0:3])
# print(tuple_3[2:4])
# print(tuple_3[::2])
# print(tuple_3[::-1])
# print(tuple_3[::-2])
# print(tuple_3[3::-2])

# my_family = [
#     ("Burak Yılmaz", 35, "beast"),
#     ("Hakan Yılmaz", 38, "bear"),
#     ("İpek Yılmaz", 40, "keko"),
# ]
#
# for x, y, z in my_family:
#     print(f'full name: {x}\n'
#           f'age: {y}\n'
#           f'alias: {z}')