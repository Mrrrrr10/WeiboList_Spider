import jieba
import pymongo
import jieba.posseg as posseg
import jieba.analyse as analyse
from collections import Counter
from pyecharts import Bar, WordCloud, ThemeRiver
from WeiboList_Spider.WeiboList_Spider import settings


class Analysis(object):
    def __init__(self):
        client = pymongo.MongoClient(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
        self.db = client.Spider
        self.collection = self.db.WeiboItem

    def takeFirst(self, elem):
        return elem[0]

    def start(self):
        self.analysis_time()
        self.analysis_count()
        self.analysis_weibo()

    def analysis_time(self):
        """对用户ETF拯救世界2017年的所有微博的创建时间进行分析，并且数据可视化"""
        y_filed, y_attr, m_attr, d_attr = eval("[]," * 4)
        m_filed = ["{}月".format(i) for i in range(1, 13)]
        d_filed = ["{}号".format(i) for i in range(1, 32)]
        print("开始分析：%s" % self.__class__.analysis_time.__name__)

        cursor = self.collection.find({}, {"created_at": 1, "_id": 0})
        created_at = [item.get('created_at') for item in cursor]
        created_year = [t.split('-')[0] for t in created_at]
        created_month = [t.split('-')[1] for t in created_at if "2017" in t]
        day = [t.split('-')[2] for t in created_at if "2017" in t]
        y_counter, m_counter, d_counter = eval("Counter()," * 3)

        # 年
        for year in created_year:
            y_counter[year] += 1
        rank = y_counter.most_common()
        rank.sort(key=self.takeFirst)
        for k, v in rank:
            y_filed.append(k)
            y_attr.append(v)

        """制作柱状图"""
        bar = Bar("发布微博之年度情况")
        bar.add('', y_filed, y_attr)
        bar.render('PublishYear.html')
        print("生成 PublishYear.html 成功")

        # 月
        for month in created_month:
            m_counter[month] += 1
        rank = m_counter.most_common()
        rank.sort(key=self.takeFirst)
        for k, v in rank:
            m_attr.append(v)

        """制作柱状图"""
        bar = Bar("发布微博之月季情况")
        bar.add('', m_filed, m_attr, mark_line=["average"], mark_point=["max", "min"])
        bar.render('PublishMonth.html')
        print("生成 PublishMonth.html 成功")

        # 日
        for d in day:
            d_counter[d] += 1
        rank = d_counter.most_common()
        rank.sort(key=self.takeFirst)
        for k, v in rank:
            d_attr.append(v)

        """制作柱状图"""
        bar = Bar("发布微博之日统计情况")
        bar.add('', d_filed, d_attr, mark_line=["average"], mark_point=["max", "min"])
        bar.render('PublishDay.html')
        print("生成 PublishDay.html 成功")

        print("分析结束：%s" % self.__class__.analysis_time.__name__)

    def analysis_count(self):
        """从3个维度3个方面对用户ETF拯救世界的2017年所有的微博的转发数、点赞数、评论数进行分析，并且数据可视化"""
        print("开始分析：%s" % self.__class__.analysis_count.__name__)

        def get_datetime():
            cursor = self.collection.find({}, {"created_at": 1})
            created_at = [day.get("created_at").replace('-', '/') for day in cursor if "2017" in day.get("created_at")]
            return created_at

        def get_attitudes():
            cursor = self.collection.find({}, {"attitudes_count": 1, "created_at": 1})
            attitudes_count = [count.get('attitudes_count') for count in cursor if "2017" in count.get("created_at")]
            return attitudes_count

        def get_comments():
            cursor = self.collection.find({}, {"comments_count": 1, "created_at": 1})
            attitudes_count = [count.get('comments_count') for count in cursor if "2017" in count.get("created_at")]
            return attitudes_count

        def get_reposts():
            cursor = self.collection.find({}, {"reposts_count": 1, "created_at": 1})
            reposts_count = [count.get('reposts_count') for count in cursor if "2017" in count.get("created_at")]
            return reposts_count

        created_at = get_datetime()
        attitudes_count = get_attitudes()
        comments_count = get_comments()
        reposts_count = get_reposts()

        attitude = list(zip(created_at, attitudes_count, ["attitudes_count"] * len(attitudes_count)))
        comment = list(zip(created_at, comments_count, ["comments_count"] * len(comments_count)))
        repost = list(zip(created_at, reposts_count, ["reposts_count"] * len(reposts_count)))
        attitude_data = [list(a) for a in attitude]
        comment_data = [list(a) for a in comment]
        repost_data = [list(a) for a in repost]

        data = attitude_data + comment_data + repost_data

        """制作主题河流图"""
        tr = ThemeRiver()
        tr.add(['attitudes_count', 'comments_count', 'reposts_count'], data, is_label_show=True)
        tr.render("Attitude_Comment_Repost.html")
        print("生成 Attitude_Comment_Repost.html 成功")
        print("分析结束：%s" % self.__class__.analysis_count.__name__)

    def analysis_weibo(self):
        """对用户ETF拯救世界的所有的微博进行文本分析，包括去停词，关键词提取，词频分析，并且数据可视化"""
        print("开始分析：%s" % self.__class__.analysis_weibo.__name__)
        cursor = self.collection.find({}, {"text": 1, "_id": 0})
        weibos = list(filter(None, [item.get('text') for item in cursor]))
        jieba.load_userdict("userdict.txt")  # 导入自定义词典
        stop = [line.strip() for line in open('../stop_words.txt', 'r', encoding='utf-8').readlines()]  # 加载停用词表
        w_filed, w_attr, words, keywords, k_filed, k_attr = eval("[]," * 6)
        for weibo in weibos:
            segs = posseg.cut(weibo)
            for seg, flag in segs:
                if seg not in stop:
                    if flag != 'm' and flag != 'x':  # 去数词和去字符串
                        words.append(seg)  # 输出分词

        # 词频分析
        counter = Counter()
        for word in words:
            counter[word] += 1

        for word, count in counter.most_common():
            w_filed.append(word)
            w_attr.append(count)

        """制作词云图"""
        wordcloud = WordCloud(width=1300, height=620)
        wordcloud.add("", w_filed, w_attr, word_size_range=[30, 100], shape='diamond')
        wordcloud.render("Word_Frequency_Count.html")
        print("生成 Word_Frequency_Count.html 成功")

        # 关键词提取
        counter = Counter()
        for weibo in weibos:
            for x in jieba.analyse.extract_tags(weibo, withWeight=False):
                keywords.append(x)

        for keyword in keywords:
            counter[keyword] += 1

        for word, count in counter.most_common():
            k_filed.append(word)
            k_attr.append(count)

        """制作词云图"""
        wordcloud = WordCloud(width=1300, height=620)
        wordcloud.add("", k_filed, k_attr, word_size_range=[30, 100], shape='diamond')
        wordcloud.render("KeyWord_Count.html")
        print("生成 KeyWord_Count.html 成功")
        print("分析结束：%s" % self.__class__.analysis_weibo.__name__)


if __name__ == '__main__':
    analysis = Analysis()
    analysis.start()
