'''
Cho một list các số, định nghĩa một hàm sao cho hàm trả lại một list mới
với điều kiện mỗi số trong list mới là tích của từng số trong list được nhận,
ngoại trừ số ở index hiện tại :
ví dụ :
- Hàm nhận [1, 2, 3] và trả lại [6, 3, 2]
(vì 2*3 = 6, 1*3 = 3, 1*2 = 2)
- Hàm nhận [4, 5, 2, -1] và trả lại [-10, -8, -20, 40]
(vì 5 * 2 * -1 = -10, 4 * 2 * -1 = -8,
    4 * 5 * -1 = -20, 4 * 5 * 2 = 40)
'''
_input = [1, 2, 3]
# _input = [4, 5, 2, -1]


def find_multi(_input):
    result = []
    for number in _input:
        multi = 1
        for number_2 in _input:
            if not number == number_2:
                multi *= number_2
        result.append(multi)
    return result


print(find_multi(_input))
