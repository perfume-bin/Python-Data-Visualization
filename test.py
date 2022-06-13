import pandas as pd
from matplotlib import pyplot as plt
from pyecharts.charts import Pie
from pyecharts import options as opts


columns = ['区/县','区域','小区','总价','单价','房屋户型','楼层','总面积','户型结构','套内面积','建筑类型','朝向',
           '建筑结构','装修情况','梯户比例','供暖方式','配备电梯','产权年限','s','交易权属','u','形式','是否满五','产权形式',
           '是否有房本','小区均价','小区建成','style','总栋数']
data = pd.read_excel(r"data.xlsx", names = columns)
data['装修情况'] = data.apply(lambda x:x['建筑类型'] if ('南北' in str(x['户型结构'])) else x['装修情况'],axis=1)
data['建筑结构'] = data.apply(lambda x:x['套内面积'] if ('南北' in str(x['户型结构'])) else x['建筑结构'],axis=1)
data['朝向'] = data.apply(lambda x:x['户型结构'] if ('南北' in str(x['户型结构'])) else x['朝向'],axis=1)
data['套内面积'] = data.apply(lambda x:'㎡' if ('南北' in str(x['户型结构'])) else x['套内面积'],axis=1)
data['装修情况'] = data.apply(lambda x:x['朝向'] if ('㎡' in str(x['户型结构'])) else x['装修情况'],axis=1)
data['建筑结构'] = data.apply(lambda x:x['建筑类型'] if ('㎡' in str(x['户型结构'])) else x['建筑结构'],axis=1)
data['朝向'] = data.apply(lambda x:x['套内面积'] if ('㎡' in str(x['户型结构'])) else x['朝向'],axis=1)
data['套内面积'] = data.apply(lambda x:'㎡' if ('㎡' in str(x['户型结构'])) else x['套内面积'],axis=1)
data['套内面积'] = data.apply(lambda x:'㎡' if ('暂无数据' in str(x['套内面积'])) else x['套内面积'],axis=1)
data['装修情况'] = data.apply(lambda x:x['装修情况'] if ('㎡' in str(x['套内面积'])) else x['建筑结构'],axis=1)
data['建筑结构'] = data.apply(lambda x:x['建筑结构'] if ('㎡' in str(x['套内面积'])) else x['朝向'],axis=1)
data['朝向'] = data.apply(lambda x:x['朝向'] if ('㎡' in str(x['套内面积'])) else x['建筑类型'],axis=1)
data['建筑类型'] = data.apply(lambda x:x['建筑类型'] if ('㎡' in str(x['套内面积'])) else x['套内面积'],axis=1)
data['套内面积'] = data.apply(lambda x:x['套内面积'] if ('㎡' in str(x['套内面积'])) else '无信息',axis=1)
data['装修情况'] = data.apply(lambda x:x['建筑结构'] if (('户') in str(x['装修情况'])) else x['装修情况'],axis=1)
data['建筑结构'] = data.apply(lambda x:x['朝向'] if (('户') in str(x['装修情况'])) else x['建筑结构'],axis=1)
data['朝向'] = data.apply(lambda x:x['建筑类型'] if (('户') in str(x['装修情况'])) else x['朝向'],axis=1)
data['建筑结构'] = data.apply(lambda x:x['朝向'] if ('结构' in str(x['朝向'])) else x['建筑结构'],axis=1)
data['朝向'] = data.apply(lambda x:x['建筑类型'] if ('结构' in str(x['朝向'])) else x['朝向'],axis=1)
data['总楼层'] = data.apply(lambda x:str(x[6])[3:].strip('(共').strip('层)'),axis=1)
data['楼层'] = data.apply(lambda x:str(x[6])[:3],axis=1)
data['总面积'] = data.apply(lambda x:str(x[7]).strip('㎡'),axis=1)
data['小区均价'] = data.apply(lambda x:str(x[-5]).strip('元/㎡\n').strip('\n'),axis=1)
data['小区建成'] = data.apply(lambda x:str(x[-4])[:4],axis=1)
data['总栋数'] = data.apply(lambda x:str(x[-2])[:-1],axis=1)
data.to_csv('after_deal_data.csv',encoding='utf_8_sig')
need_data = data[['区/县','区域','小区','总价','单价','房屋户型','楼层','总面积','朝向','建筑结构','装修情况','交易权属','形式','是否满五','产权形式','是否有房本','小区均价','小区建成','总栋数']]
need_data.head()
# print(data.head(10))
# print(need_data.head(10))
#  图表中文显示
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
fig, ax=plt.subplots()
# print(need_data.info())
# print(need_data.describe())
'''
各区县房源分布情况
北京二手房各区、县房源分布信息
'''
need_data['区/县'].value_counts().plot(kind='bar',color=['green','red','blue','grey','pink'],alpha=0.5)
x = need_data['区/县'].value_counts()
plt.title('北京二手房各区、县房源分布信息',fontsize=15)
plt.xlabel('区、县名称',fontsize=15)
plt.ylabel('房源数量',fontsize=15)
plt.grid(linestyle=":", color="r")
plt.xticks(rotation=60)
plt.legend()
plt.show()

'''
各区县房源均价分布情况
北京二手房各区、县房屋均价分布信息
'''
need_data.groupby('区/县').mean()['单价'].sort_values(ascending=True).plot(kind='barh',color=['r','g','y','b'],alpha=0.5)
plt.title('北京二手房各区、县房屋均价分布信息',fontsize=15)
plt.xlabel('房屋均价',fontsize=15)
plt.ylabel('区、县名称',fontsize=15)
plt.grid(linestyle=":", color="r")
plt.legend()
plt.show()

'''
各区县房源分布情况
北京二手房房屋户型情况
'''
need_data['房屋户型'].value_counts().plot(kind='bar',color=['green','red','blue','grey','pink'],alpha=0.5)
plt.title('北京二手房房屋户型情况',fontsize=15)
plt.xlabel('房屋户型',fontsize=15)
plt.ylabel('房源数量',fontsize=15)
plt.grid(linestyle=":", color="r")
plt.xticks(rotation=60)
plt.legend()
plt.show()

# print(need_data[need_data.房屋户型 == '5室2厅4卫'])

# 北京二手房总价最大、最小值及其房源信息
total_price_min = need_data['总价'].min()
total_price_min_room_info = need_data[need_data.总价==total_price_min]
# print('二手房总价最低价位为：\n{}'.format(total_price_min))
# print('二手房总价最低的房源信息为：\n{}'.format(total_price_min_room_info))
total_price_max = need_data['总价'].max()
total_price_max_room_info = need_data[need_data.总价==total_price_max]
# print('二手房总价最高价位为：\n{}'.format(total_price_max))
# print('二手房总价最低的房源信息为：\n{}'.format(total_price_max_room_info))


#  绘制总面积和总价的散点关系图
home_area = need_data['总面积'].apply(lambda x:float(x))
# print(home_area.head())
total_price = need_data['总价']
# print(total_price.head())
plt.scatter(home_area,total_price,s=3)
plt.title('北京二手房房屋户型情况',fontsize=15)
plt.xlabel('房屋面积',fontsize=15)
plt.ylabel('房源总价',fontsize=15)
plt.grid(linestyle=":", color="r")
plt.show()

#  分析面积大但是价格较低的房源
area_max = home_area.max()
area_max_room_info = need_data[home_area==area_max]
# print('二手房面积最大的房源信息为：\n{}'.format(area_max_room_info))

# 使用pyecharts绘制楼层和房屋数量的饼图

x = need_data['楼层'].value_counts()
y = ['高楼层', '低楼层', '中楼层', '地下室', '未知']
# print("x =", x)
# print("y =", y)
c = (
    Pie()
    .add("", [list(z) for z in zip(y, x)])
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="房源楼层分布图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("房源楼层分布图.html")
)
