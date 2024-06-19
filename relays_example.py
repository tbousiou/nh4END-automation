import time
t = (0.42, 1.12, 0.87)

t = [int(x*10) for x in t]
print(t)

for i in range(max(t)):
    print(i)
    if i < t[0]:
        print("PIN 1 ON")
    else:
        print("PIN 1 OFF")
    if i < t[1]:
        print("PIN 2 ON")
    else:
        print("PIN 2 OFF")
    if i < t[2]:
        print("PIN 3 ON")
    else:
        print("PIN 3 OFF")
    time.sleep(0.1)

    