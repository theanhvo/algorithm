'''
Tìm tổng lớn nhất của 2 số  trong 1 list
'''

tong = []
li = [20,11,30,33,2,555]
for  i in range(len(li)):
    for j in range(i + 1, len(li)):
        tong.append(li[i] + li[j])
# print(tong)

ex_tong = tong[0]
for elem in tong:
    if ex_tong < elem:
        ex_tong = elem
        
print('Max Sum Of 2 number : {}'.format(ex_tong))
