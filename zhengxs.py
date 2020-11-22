from pyecharts.charts import Line
fruits = ['0-20', '20-50', '50-100', '100-200', '200以上']
#实例数目--一共
shop1_sales = [607, 711, 1038, 3451, 3876, 15409]
shop2_sales = [4888, 7023, 3989, 5873, 8876, 6409]

line = Line('折线图')
line.add('扩充前A', fruits, shop1_sales, mark_point=['max'])
line.add('扩充后B', fruits, shop2_sales, mark_point=['min'])
line.show_config()
line.render('./折线图.html')