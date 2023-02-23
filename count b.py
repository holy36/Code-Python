
# Tìm số lần xuất hiện của mỗi phần từ trong List

# import Counter
from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # Xác định đối tượng counter

print(count) # In thông tin tất cả
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b']) # Số lần xuất hiện của phần tử cụ thể
# 3

print(count.most_common(1)) # Phần tử xuất hiện nhiều nhất
# [('d', 5)]
