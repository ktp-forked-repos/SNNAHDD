import matplotlib.pyplot as plt

def read_data(fileName):
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def get_coordinates(data):
    x = []
    y = []
    for k in  data:
        ll =  k.split()
        x.append(ll[0])
        y.append(ll[2])
    return x, y

rkct = 'rkdct.txt'
kdct = 'kdct.txt'
pkct = 'pkct.txt'
rk = read_data(rkct)
kd = read_data(kdct)
pk = read_data(pkct)

xkd, ykd = get_coordinates(kd)
xrk, yrk = get_coordinates(rk)
xpk, ypk = get_coordinates(pk)

plt.plot(xrk, yrk, 'b-', xkd, ykd, 'r-', xpk, ypk, 'g-')

plt.ylabel('time in seconds');
plt.xlabel('number of points')
plt.show()
