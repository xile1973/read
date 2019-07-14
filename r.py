# 读取档案

data = []
with open ('food.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

print('清单记录共有', len(data),'条')

sum_len = 0
for d in data:
	sum_len += len(d)
	print('字符长度是', sum_len)

print('留言平均长度是', sum_len/len(data))
