'''
Tìm 3 số có tích lớn thứ nhì
'''
product = []
dict = {}
li = [1,2,3,4,-5,-20,-30]
for  i in range(len(li)):
    for j in range(i + 1, len(li)):
        for k in range(j+1, len(li)):
            so1 = li[i]
            so2 = li[j]
            so3 = li[k]
            tich = li[i] * li[j] * li[k]
            product.append(li[i] * li[j] * li[k])
            dict[tich] = [so1,so2,so3]

product_result = product[0]
for elem in product:
    if product_result < elem:
        product_result = elem

lst_product = [i for i in product if i != product_result]
product_result2 = lst_product[0]
for elem1 in lst_product:
    if product_result2 < elem1:
        product_result2 = elem1
print('Ba Số có tích lớn thứ nhì : {}'.format(dict[product_result2]))
