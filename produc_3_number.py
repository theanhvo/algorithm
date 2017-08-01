'''
Tìm tích lớn nhất của 3 số
'''

product = []
li = [1,2,3,4,-5]
for  i in range(len(li)):
    for j in range(i + 1, len(li)):
        for k in range(j+1, len(li)):
            product.append(li[i] * li[j] * li[k])

product_result = product[0]
for elem in product:
    if product_result < elem:
        product_result = elem
print('Product Max Result Of 3 Number : {}'.format(product_result))
