from scipy import stats
import statistics


def trimmedman(arr, percent):
    n = len(arr)
    k = int(round(n*(float(percent)/100)/2))
    arr.sort()
    print(k)
    print(arr)
    return statistics.mean(arr[k+1:n-k])


trim = 0.3

data1 = []
data2 = []
data3 = []
with open("data.txt") as f:
    for line in f:
        row = [float(x) for x in line.split()]
        data1.append(row[0])
        data2.append(row[1])
        data3.append(row[2])

m1 = stats.trim_mean(data1, trim)
m2 = stats.trim_mean(data2, trim)
m3 = stats.trim_mean(data3, trim)
print(m1,m2,m3)

tm1 = trimmedman(data1, 40)
print(tm1)
statistics.geometric_mean(data1)