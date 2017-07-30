'''
Tìm tích lớn nhất của 2 số
'''

product = []
li = [-11,4,2,2,2,-5]
for  i in range(len(li)):
    for j in range(i + 1, len(li)):
        product.append(li[i] * li[j])
# print(product)

product_result = product[0]
for elem in product:
    if product_result < elem:
        product_result = elem

print('Product Result Of 2 Number : {}'.format(product_result))
