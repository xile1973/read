data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('档案读取完毕，总共有', len(data), '笔资料')

print(data[0])

wc = {} #word_count
for d in data:# data是一个清单，里面装着100万笔留言，而d是全部留言中的一个。
	words = d.split()# 把留言用空格分割，split()使用的是该函数的预设值，使用空格来分割句子中的单词，且不会把连续的空格当做单词。
	for word in words:# 把分割后的每一个字放到word中
		if word in wc:#如果这个字出现在字典里
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key进入字典，同时给value赋值为1
for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])

print('对话文件中共有', len(wc),'个字' )

while True:
	word = input('请问你想查什么单词：') 
	if word == 'q':
		break
	if word in wc:
		print(word,'出现过的次数为',wc[word])
	else:
		print('该单词没有出现')
	
print('感谢使用本功能')
	
