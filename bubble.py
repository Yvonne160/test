
def bubble_sort(list):
	count = len(list)
	for i in range(0,count):
		for j in range(i+1,list):
			if list[i]>list[j]:
				list[i],list[j]=list[j],list[i]
	return list
lists = [2,5,1,3,7,4]
print bubble_sort(lists)


