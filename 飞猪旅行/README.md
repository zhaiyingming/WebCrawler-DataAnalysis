##  按全国各个城市抓取飞猪“景点门票”栏的景点门票销售数据5万条，并且对端午出行进行景点推荐

项目主要按全国各个城市抓取飞猪“景点门票”栏的景点门票销售数据，并且分析端午哪些景点会人挤人，哪些景点值得一去


主要的文件为：
- ../data/city_data.csv: 全国城市及所属省份列表
- ../code/爬取飞猪.py: 数据爬取代码 安装好mongoDB之后，直接点击运行
- ../data/飞猪旅行分析.ipynb:Jupyter notebook代码，对景点门票数据进行分析

#### 数据
飞猪景点门票销售数据5万条

- 运行程序后，可用mongoDB可视化工具看到

#### 运行环境：
- python3.6

#### 需要安装的包：
- requests
- pyecharts
- pandas
- numpy
- pymongo

