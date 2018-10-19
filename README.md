# WeiboList_Spider
**基于scrapy的爬虫**
## 说明：
1. 爬取指定用户的用户信息以及该用户发布的微博信息
2. 存储在mongodb，并且利用mongodb相关api在pipeline.py文件进行数据去重和增量更新
3. 对爬取的数据进行用户行为数据清洗、分析、可视化操作

## 用法：
```
scrapy crawl weibo
```
## 模式选择：
* 单用户模式：指定用户的用户信息以及该用户发布的微博信息
* 多用户模式：指定用户的用户信息以及该用户发布的微博信息，还有其粉丝、关注者的信息及其发布的微博信息，以此类推
* 默认是单用户模式，如果想配置多用户模式，请在settings.py中修改如下内容即可：```IS_SINGLE = False```
## 数据分析、可视化：
1. 目标用户微博的点赞数、转发数、评论数
![Result1](https://github.com/Mrrrrr10/WeiboList_Spider/blob/master/Data_Analysis/weibo/%E7%82%B9%E8%B5%9E%E6%95%B0%E3%80%81%E8%AF%84%E8%AE%BA%E6%95%B0%E3%80%81%E8%BD%AC%E5%8F%91%E6%95%B0.png)
2. 每条微博的关键词提取
![Result1](https://github.com/Mrrrrr10/WeiboList_Spider/blob/master/Data_Analysis/weibo/%E5%85%B3%E9%94%AE%E8%AF%8D.png)
3. 高频词
![Result1](https://github.com/Mrrrrr10/WeiboList_Spider/blob/master/Data_Analysis/weibo/%E9%AB%98%E9%A2%91%E8%AF%8D.png)
4. 年微博统计
![Result1](https://github.com/Mrrrrr10/WeiboList_Spider/blob/master/Data_Analysis/weibo/%E5%B9%B4%E7%BB%9F%E8%AE%A1%E5%BE%AE%E5%8D%9A%E6%95%B0.png)
5. 月微博统计
![Result1](https://github.com/Mrrrrr10/WeiboList_Spider/blob/master/Data_Analysis/weibo/%E6%9C%88%E7%BB%9F%E8%AE%A1%E5%BE%AE%E5%8D%9A%E6%95%B0.png)
6. 日微博统计
![Result1](https://github.com/Mrrrrr10/WeiboList_Spider/blob/master/Data_Analysis/weibo/%E6%97%A5%E7%BB%9F%E8%AE%A1%E5%BE%AE%E5%8D%9A%E6%95%B0.png)

## 后续工作：
可以分析该用户粉丝的位置和转发关系

## 不足：
会出现数据不完整，经过我多次检验，原因不是代码有问题，而是新浪微博本身就只能提供给这么多数据，所谓所见即所爬，我尝试过维护一个cookie池，加上ip代理，均出现数据不完整的现象，不完整的部分是粉丝那一块。但是对于分析用户行为影响不大。
