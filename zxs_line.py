from pyecharts.charts import Line

cate = ['0-20', '20-50', '50-100', '100-200', '200以上']


shop1_sales = [607, 711, 1038, 3451, 3876]
shop2_sales = [6888, 7023, 7989, 8873, 8285]

line = Line()

line.add_xaxis(cate)
line.add_yaxis('扩充前A', shop1_sales)
line.add_yaxis('扩充后B', shop2_sales)
line.render('./折线图.html')

