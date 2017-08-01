'''
Tìm tích lớn thứ nhì của 3 số
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

lst_product = [i for i in product if i != product_result]
product_result2 = lst_product[0]
for elem1 in lst_product:
    if product_result2 < elem1:
        product_result2 = elem1
print('Three Number product second max : {}'.format(product_result2))
