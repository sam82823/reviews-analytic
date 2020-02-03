data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count +1
		if count % 1000 == 0: 
			print(len(data))
print('Finished loading', len(data), 'in total')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len/len(data))

new = []
for  d in data:
	if len(d) < 100:
		new.append(d)
print('Total', len(new), 'less than 100')
print(new[2])

good = []
for d in data:
	if  'good' in d:
		good.append(d)
print('共有', len(good), '筆留言提到good')
print(good[0])
