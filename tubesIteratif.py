import time

def iteratif(uang):
    start_time = time.time()
    while uang >= 100:
        if uang >= 100000:
            print(uang//100000, "Uang 100000")
            uang = uang % 100000
        elif uang >= 50000:
            print(uang // 50000, "Uang 50000")
            uang = uang % 50000
        elif uang >= 10000:
            print(uang // 10000, "Uang 10000")
            uang = uang % 10000
        elif uang >= 5000:
            print(uang // 5000, "Uang 5000")
            uang = uang % 5000
        elif uang >= 2000:
            print(uang // 2000, "Uang 2000")
            uang = uang % 2000
        elif uang >= 1000:
            print(uang // 1000, "Uang 1000")
            uang = uang % 1000
    end_time = time.time()
    time_lapsed = end_time - start_time
    print("Function iteratif: {0}".format(time_lapsed))



uang = 978000



iteratif(uang)

            