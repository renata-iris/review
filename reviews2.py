data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了總共有', len(data), '筆資料')

print(data[0])

#平均留言長度計算
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))


#留言的篩選
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

#特定字是否存在
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')


#文字計數，使用dic功能
wc = {} #字計數
for d in data:
	words = d.split() #預設值是空字串，如果沒有強制寫幾個空格，
	#此功能在遇到空字串時皆會跳過(不論幾個空格)
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc: #抓出字典中的key
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc)) #該字典的長度
print(wc['Iris'])

while True: #無限迴圈
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本次查詢功能')