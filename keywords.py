#encoding:utf-8
import jieba
from matplotlib import pyplot as plt
from jieba.analyse import extract_tags
from jieba.analyse import textrank
import jieba.analyse
from wordcloud import WordCloud
from collections import Counter


class Keywords():
    """
    基于词频
    """
    def __init__(self,sentense):
        jieba.load_userdict(r'data\vocab.txt')
        stopfile = open(r'data\stopwords.txt', 'r', encoding='utf-8')
        stopwords_lst = stopfile.readlines()
        STOPWORDS = [x.strip() for x in stopwords_lst]
        STOPWORDS += [' ', '','\n']
        self.stopwords = set(STOPWORDS)
        self.sentense=sentense
        stopfile.close()

    def cut_line(self):
        word_list = []
        for text in self.sentense: ##这里sentense为list 元素为单条文本
            word_list.extend(list(jieba.cut(text.strip())))
        word_list = [word for word in word_list if word not in self.stopwords]
        return word_list

    def cut_all(self):
        cutted=jieba.lcut(self.sentense)  ##这里sentense为str,所有文本合并
        word_list=[word for word in cutted if word not in self.stopwords]
        return word_list

    def topWord(self, top=100):
        word_list=self.cut_all()
        result = dict(Counter(word_list))
        sortlist = sorted(result.items(), key=lambda item: item[1], reverse=True)
        top_dict = {}
        try:
            for i in range(0, top):
                top_dict[sortlist[i][0]] = sortlist[i][1]
        except:
            print('not enough %s words, please set top parameter down'%(top))
        print(top_dict)
        return top_dict

    def wordCloud(self, title):
        top_dict=self.topWord()
        wc = WordCloud(font_path="msyh.ttc",
                       background_color='white',
                       max_words=100,
                       stopwords=self.stopwords,
                       max_font_size=80,
                       random_state=42,
                       margin=3)  # 配置词云参数
        wc.generate_from_frequencies(top_dict)  # 生成词云
        plt.imshow(wc, interpolation="bilinear")  # 作图
        plt.axis("off")  # 不显示坐标轴
        plt.xticks([])
        plt.yticks([])
        plt.title(title)
        plt.show()


class KeywordsTfidf(Keywords):
    """
    基于TFIDF
    """
    def __init__(self,sentense):
        Keywords.__init__(self, sentense)
        jieba.analyse.set_stop_words(r"data\stopwords.txt")

    def topWord(self, top=100):
        top_dict = {}
        # withFlag=True  标注词性 withWeight=True
        for keyword, weight in extract_tags(self.sentense, withWeight=True, topK=top, allowPOS=('nz', 'a', 'v', 'z')):
            top_dict[keyword] = weight
        print(top_dict)
        return top_dict


class KeywordsTextrank(Keywords):
    """
    基于TextRank
    """
    def __init__(self,sentense):
        Keywords.__init__(self, sentense)
        jieba.analyse.set_stop_words(r"data\stopwords.txt")

    def topWord(self, top=100):
        top_dict = {}
        # withFlag=True  标注词性 withWeight=True
        for keyword, weight in textrank(self.sentense, withWeight=True, topK=top, allowPOS=('nz', 'a', 'v', 'z')):
            top_dict[keyword] = weight
        print(top_dict)
        return top_dict


class KeywordsWc(Keywords):
    """
    基于WordCloud自带分词
    """
    def __init__(self,sentense):
        Keywords.__init__(self, sentense)

    def topWord(self, top=100):
        wc = WordCloud()
        result=wc.process_text(self.sentense)
        sortlist = sorted(result.items(), key=lambda item: item[1], reverse=True)
        top_dict = {}
        try:
            for i in range(0, top):
                top_dict[sortlist[i][0]] = sortlist[i][1]
        except:
            print('not enough %s words, please set top parameter down'%(top))
        print(top_dict)
        return top_dict


def main(filepath):
    with open(filepath,encoding='utf-8') as f:
        sentense = f.read()
        seg = Keywords(sentense)
        topwords = seg.topWord()
        print(len(topwords))

if __name__ == "__main__":
    main('data/neg_20.txt')


