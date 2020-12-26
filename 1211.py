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
        print(value)
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
#两个列表中相同元素与不同元素
def interview6():
    list1 = [3, 2, 3, 5, 7, 1, 6]
    list2 = [1, 4, 2, 8, 9, 5]
    xiangtong = []
    butong = []
    for i in list1:
        if i not in list2:
            butong.append(i)
        else:
            xiangtong.append(i)
    print(xiangtong)
    print(butong)

#列表中有没有两数相加等于8，返回下标
def study():
    list1 = [2, 3, 5, 7]
    value = 8
    for i in list1:
        if value - i in list1 and (value - i)!=i :
            return [list1.index(i),list1.index(value-i)]






#编写一个函数来查找字符串数组中的最长公共前缀
def study1():
    list1 =  ["flower","flow","flight"]
    list2 = ["dog”,”carcar","car"]
    list3 = []
    result  = ''
    if len(list1) == 0:
        return 0
    for i in zip(*(list3)):
        print(i)
        if len(set(i)) == 1:
            result += i[0]
        else:
            break
    print(result)

# 一支中性笔，设计case：
# 通过测试：可正常写出字（汉字or英文or其他）
# 功能测试：
# 笔的长度，粗细
# 是否可替换笔芯
# 笔的开关
#
# 易用性：
# 儿童使用：长度，粗细
# 是否容易更换笔芯
#
# 兼容性：
# 各种笔芯的兼容性
# 笔芯颜色的兼容
# 使用场景的兼容（白纸or画板or玻璃）
#
# 安全性：
# 儿童使用是否容易将笔墨吸出来
# 是否易碎
# 是否可拆卸为小部件（儿童的安全性）
#
# UI：
# 文案是否不易接受（强迫症or密集恐惧症）
# 敏感文字（反动思想的文字）
# 颜色：避免黑色
#
# 其他：
# 不同温度（高温or低温）
# 压强
# 易于放置（满足正常铅笔盒的长度）






#判断一个整数是不是回文数
def study3():
    num = 12321
    num1 = -12321
    num2 = 123321
    #判断整数的范围
    # if
    #     pass
    str1 = str(num3)
    if len(str1) == 0 :
        return 0
    for i in str1:
        if i == '-':
            return 0
        else:
            res = str1[::-1]
            if str1 == res :
                return 1




if __name__ == '__main__':
    print(study3())
