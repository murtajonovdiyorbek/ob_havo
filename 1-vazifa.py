import threading

def butun(n):
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n //= 10
    print(f"Natija: {yigindi}")

t = threading.Thread(target=butun, args=(108,))
t.start()
t.join()