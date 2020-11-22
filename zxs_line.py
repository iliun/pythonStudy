from pyecharts.charts import Line
cate = ['0-20', '20-50', '50-100', '100-200', '200以上']
#实例数目--一共
shop1_sales = [607, 711, 1038, 3451, 3876, 15409]
shop2_sales = [4888, 7023, 3989, 5873, 8876, 6409]

line = Line()

line.add_xaxis(cate)
line.add_yaxis('扩充前A',shop1_sales)
line.add_yaxis('扩充后B',shop2_sales)
line.render('./折线图.html')