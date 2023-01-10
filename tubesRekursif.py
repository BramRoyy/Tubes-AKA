import time

def rekursif(uang):
    
    if uang >= 100000:
        print(uang//100000, "Uang 100000")
        rekursif(uang % 100000)
    elif uang >= 50000:
        print(uang // 50000, "Uang 50000")
        rekursif(uang % 50000)
    elif uang >= 10000:
        print(uang // 10000, "Uang 10000")
        rekursif(uang % 10000)
    elif uang >= 5000:
        print(uang // 5000, "Uang 5000")
        rekursif(uang % 5000)
    elif uang >= 2000:
        print(uang // 2000, "Uang 2000")
        rekursif(uang % 2000)
    elif uang >= 1000:
        print(uang // 1000, "Uang 1000")
    
uang = 978000
    
start_time = time.time()
rekursif(uang)
end_times = time.time()
time_lapseds = end_times - start_time
print("Function rekursif: {0}".format(time_lapseds))

