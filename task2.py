# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
book = pages * lines * symbols * 4
Volume = 1.44
Volume_in_kb = Volume * 1024**2
Books = round(Volume_in_kb//book)
print("Количество книг, помещающихся на дискету:", Books)
