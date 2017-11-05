import matplotlib.pyplot as plt

def read_data(fileName):
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

l = read_data('2 - const_time.txt')

x  = []
y  = []
for e in l:
    ll =  e.split()
    x.append(ll[0])
    y.append(ll[2]);
#    print ll[0] + ' ' + ll[2]

plt.plot(x, y, 'bo')
plt.ylabel('time');
plt.xlabel('number of points')
plt.show()


naive_result = read_data('naive.txt')
k_result     = read_data('kd_result.txt')

x_axis = []
n_axis = []
k_axis = []
for i in range(0, len(k_result)):
    kl = k_result[i].split()
    if float(kl[1]) > 1000 and float(kl[1]) < 100000:
        nl = naive_result[i].split()
        x_axis.append(kl[0])
        n_axis.append(nl[2])
        k_axis.append(kl[2])

plt.plot(x_axis, n_axis, 'ro', x_axis, k_axis, 'go')
plt.ylabel('time')
plt.xlabel('number of points')
plt.show()
