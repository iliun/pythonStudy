from pyecharts.charts import Bar
from pyecharts import options as opts

fruits = ['0-20', '20-50', '50-100', '100-200', '200以上']
shop1_sales = [607, 711, 1038, 3451, 3876, 15409]
shop2_sales = [4888, 7023, 3989, 5873, 8876, 6409]

bar = Bar()

bar.add_xaxis(fruits)
bar.add_yaxis('shop1_sales',shop1_sales)
bar.add_yaxis('shop2_sales',shop2_sales)
bar.set_global_opts(datazoom_opts=opts.DataZoomOpts(orient="vertical"))


bar.render('./柱状图.html')