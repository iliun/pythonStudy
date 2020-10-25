from collections import ChainMap
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
#修改merge1的value，dic1/dic2不会同步变化
merge1 = {**dic1,**dic2}

#修改merge2的value，dic1/dic2会同步变化
merge2 = ChainMap(dic1,dic2)



