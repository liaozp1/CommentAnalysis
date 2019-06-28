#encoding:utf-8
from keywords import *
import os
import shutil
from collections import Counter


class CommentClassfier():
    """
    comment classfier
    """
    def __init__(self, sentense):
        self.sentense=sentense

        self.tastelist= [word.strip() for word in open('../qsvc/data/words/口味词.txt',encoding='utf-8').readlines()]
        self.envlist = [word.strip() for word in open('../qsvc/data/words/环境词.txt',encoding='utf-8').readlines()]
        self.servicelist = [word.strip() for word in open('../qsvc/data/words/服务词.txt',encoding='utf-8').readlines()]
        self.pricelist = [word.strip() for word in open('../qsvc/data/words/价格词.txt',encoding='utf-8').readlines()]

        self.taste_len =len(self.tastelist)
        self.env_len = len(self.envlist)
        self.service_len = len(self.servicelist)
        self.price_len = len(self.pricelist)

        self.classdict = {}

    def classify(self):
            line=self.sentense
            self.classdict[line]=[]
            ziplist=zip(['口味','环境','服务','价格'],[self.taste_len,self.env_len,self.service_len,self.price_len])
            type_dict=dict(ziplist)

            for word in self.tastelist:
                if word in line:
                    self.classdict[line].append('口味')

            for word in self.envlist:
                if word in line:
                    self.classdict[line].append('环境')

            for word in self.servicelist:
                if word in line:
                    self.classdict[line].append('服务')

            for word in self.pricelist:
                if word in line:
                    self.classdict[line].append('价格')

            if len(self.classdict[line]) != 0:
                num_dict = dict(Counter(self.classdict[line]))
                for cla in num_dict:
                    num_dict[cla] = num_dict[cla]/type_dict[cla]
                self.classdict[line] = sorted(num_dict.items(), key=lambda item: item[1], reverse=True)[0][0]
            else:
                self.classdict[line] = '其他'

            return self.classdict


def split_files(filepath):
    """
    生成 口味/环境/服务/价格 txt文件
    """
    with open(filepath, encoding='utf-8') as f1:
        dic={}
        for line in f1:
            classifier = CommentClassfier(line)  ###实例化 接收单条评论
            classifier.classify()
            print(line, classifier.classdict[line])
            # for cla in classifier.classdict[line]:
            cla = classifier.classdict[line]
            if cla not in dic:
                dic[cla]=[line]
            else:
                dic[cla].append(line)

        total = 0
        for key in dic:
            print(key,len(dic[key]))
            total += len(dic[key])
            with open('../qsvc/data/'+ key + '.txt', 'w', encoding='utf-8') as f2:
                    f2.writelines(dic[key])
        print('total:', total)
def word_cloud(in_path, out_path):
    """
    生成词云
    """
    with open(in_path, encoding='utf-8') as f:
        title=in_path.split('/')[-1].replace('.txt', '')
        # path= '../qsvc/data/wc/'
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        savepath=out_path + title + '.png'

        sentense = f.read()
        seg = Keywords(sentense)
        seg.wordCloud(title, savepath,200)

def main(filepath):
    """
    主函数
    """
    split_files(filepath) ##总文件进行分类
    dir='../qsvc/data/'
    out_path= '../qsvc/data/wc/'
    if os.path.exists(out_path):  ##每次运行删除之前生成的词云文件夹
        shutil.rmtree(out_path)

    for file in [file for file in os.listdir(dir) if file.endswith('txt')]: ##遍历分类好的txt文件生成词云图
        # print(file)
        in_path=os.path.join(dir, file)
        print(in_path)
        word_cloud(in_path, out_path)


if __name__=="__main__":
    # split_files('../data/neg_20.txt')
    main('../data/neg_20.txt')




