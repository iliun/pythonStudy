import operator,re
def s1():
    str1 = "k:1|k1:2|k2:3|k3:4"
    print(str1.split('|'))

    list = ['a', 'b', 'c', 'd', 'e']
    print(list[10:])

def s2():
    list1 = [1,2,3,4,3]
    list2 = [2,4,1,5,3]
    set1 = set(list1)
    set2 = set(list2)
    print(set1 & set2)
    print(set1 ^ set2)

def s3():
    list1 = [1,2,3,4,3]
    list2 = [2,4,1,5,3]

def sList():
    #创建列表
    list1 = [i for i in range(5)] #[0, 1, 2, 3, 4]
    list2 = list(range(5))  #[0, 1, 2, 3, 4]

    #访问列表
    print(list1[0])
    print(list1[0:-1:2])  #不包含最后一个元素 [0, 2]
    print(list1[0::2])  #包含最后一个元素 [0, 2, 4]
    print(list2[::-1])  #反向索引 [4, 3, 2, 1, 0]
    print(list2[-1::-2]) #[4, 2, 0]

    #查询列表
    colors = ['blue', 'red', 'yellow', 'pink', 'white', 'black']
    print(colors.index('red'))  #1

    #修改列表
    colors[1]='green'
    print(colors)   #['blue', 'green', 'yellow', 'pink', 'white', 'black']

    #增加
    colors.append('red')
    print(colors)   #['blue', 'green', 'yellow', 'pink', 'white', 'black', 'red']
    colors.insert(1,'pink')
    print(colors)   #['blue', 'pink', 'green', 'yellow', 'pink', 'white', 'black', 'red']

    #删除元素
    del colors[1]
    print(colors)   #['blue', 'green', 'yellow', 'pink', 'white', 'black', 'red']

    colors.remove('pink')
    print(colors)   #['blue', 'green', 'yellow', 'white', 'black', 'red']

    colors.pop(3)
    print(colors)    #['blue', 'green', 'yellow', 'black', 'red']

    #拓展
    colors_other = ['green', 'gray', 'orange']
    colors.extend(colors_other)
    print(colors) #['blue', 'green', 'yellow', 'black', 'red', 'green', 'gray', 'orange']

    colors.append(colors_other)
    print(colors)  #['blue', 'green', 'yellow', 'black', 'red', 'green', 'gray', 'orange', ['green', 'gray', 'orange']]

    #统计
    print(colors.count('green'))   #2

    #排序
    '''
        key = int ;针对数字类型排序
        key = str ;针对字符串内容排序
        key = len ;针对字符串的长度进行排序
        列表内类型不一致，不能使用排序方法。会导致崩溃
    '''
    nums = [1, 22, 35, 63, 3, 11, 7]
    nums.sort(key= str)
    print(nums) #[1, 11, 22, 3, 35, 63, 7, 'aaa', 'cc']


def sDict():
    dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

    color= ['blue', 'green', 'yellow', 'black']
    print(color[len(color)-1:0:-1])
    name = ['blue', 'green', 'yellow', 'black']
    print(color.index())
def interview():
    s = '123'
    num = 0
    for i in s:
        for j in range(10):
            if i == str(j):
                num = num * 10 + j
    print(type(num))

def interview2():
    alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
    alistSorted = sorted(alist,key=operator.itemgetter('age'))
    print(alistSorted)

def interview3():
    list1 = []
    word_dict = {}
    with open('./zxs.txt','r') as f:
        value = f.readlines()
        for i in value:
            i = i.strip()
            word = re.findall(r'[a-zA-Z]+',i)
            list1 = list1 + word
    for i in list1:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    print(sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)[:10])

def interview4():
    l1 = [3, 4, 5, 6, 7]
    l2 = [4, 5, 6, 7, 8]
    temp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] <= l2[0]:
            temp.append(l1[0])
            del l1[0]
        else:
            temp.append(l2[0])
            del l2[0]
    while len(l1)>0:
        temp.append(l1[0])
        del l1[0]
    while len(l2)>0:
        temp.append(l2[0])
        del l2[0]
    print(temp)

def interview5():
    #让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'
    l = '1235346250'
    if isinstance(l,str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    print(l)
    for i in range(len(l)):
        if l[i]%2 == 0:
            l.insert(0,l.pop(i))
    print(''.join(str(m) for m in l))

def func1(l):
    if isinstance(l, str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    print(''.join(str(e) for e in l))

def interview6():
    a = 10
    b = 20
    c = [a]
    a = 15
    print(c)



if __name__ == '__main__':
    interview6()
