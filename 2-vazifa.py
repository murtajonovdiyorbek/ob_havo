from threading import Thread

def katta(ismlar):
    result = []
    for i in ismlar:
        result.append(i.capitalize())
    print(result)

ism = ['teshavoy', 'baltavoy', 'ali', 'vali']

th = Thread(target=katta, args=(ism,))
th.start()
th.join()