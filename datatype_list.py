# slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

type(thislist)
# <class 'list'>
# special variables
# function variables
len(thislist)
# 7
thislist[1:3]
# ['banana', 'cherry']
thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

# change value in list
thislist[1] = 'watermelon'

thislist[1:3] = ['cherry', 'melon']  # 1번과 2번의 이름을 바꿈
thislist.sort() # 정렬 시키는 방법, 앞 첫글자로 오름차순, 앞글자 같으면 두번째 글자 비교
thislist.sort(reverse=True) # 내림차순으로 정렬
pass