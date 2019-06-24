#encoding:utf-8
import jieba
from collections import Counter

def extarct_not_positive():
    """提取负向词汇"""
    inputs = open(r'D:\work\text\Dicos\data\neg_20.txt', 'r', encoding='utf-8')
    outputs = open(r'D:\work\text\Dicos\data\extract2.txt', 'w', encoding='utf-8')
    for line in inputs:
        if '不' in line:
            print(line)
            cut_list=list(jieba.cut(line))
            if '不' in cut_list:
                print(cut_list.index('不'))
                print(''.join(cut_list[cut_list.index('不'):cut_list.index('不')+2]))
                outputs.write(''.join(cut_list[cut_list.index('不'):cut_list.index('不')+2]) + '\n')
            if '不是' in cut_list and '很' in cut_list:
                print(cut_list.index('不是'))
                print(''.join(cut_list[cut_list.index('不是'):cut_list.index('不是') + 3]))
                outputs.write(''.join(cut_list[cut_list.index('不是'):cut_list.index('不是') + 3]) + '\n')
    outputs.close()
    inputs.close()

def extract_negative():
    """提取负向词汇"""
    # negs=['不大','不丁点儿','不甚','不怎么','聊','没怎么','不可以','怎么不','几乎不','从来不','从不','不用','不曾','不该',\
    #      '不必','不会','不好','不能','很少','极少','没有 ','不是','难以','放下','扼杀','终止','停止','放弃','反对','缺乏',\
    #      '缺少','不','甭','勿','别','未','反','没','否','木有','非','无','请勿','无须','并非','毫无','决不','休想',\
    #      '永不','不要','未尝','未曾','毋','莫','从未','从未有过','尚未','一无','并未','尚无','从没','绝非','远非','切莫',\
    #      '绝不','毫不','禁止','忌','拒绝','杜绝','弗']
    negs=['拒绝']

    inputs = open(r'D:\work\text\Dicos\data\neg_20.txt', 'r', encoding='utf-8')
    outputs = open(r'D:\work\text\Dicos\data\extract4.txt', 'w', encoding='utf-8')
    linelist=[]
    for line in inputs:
        for neg in negs:
            if neg in line:
                # print(line)
                # print(line[line.index(neg):(line.index(neg)+4)].replace('，','').replace('!',''))
                linelist.append(line[line.index(neg):(line.index(neg)+7)].replace('，','').replace('!','')\
                                .replace('。','').replace('\n','')+'\n')
    result = dict(Counter(linelist))
    print(result)

    linelist=[item[0] for item in result.items() if item[1] >=30]
    for line in linelist:
        print(line)

    outputs.writelines(linelist)

def process():
    """处理负向词汇"""
    inputs = open(r'D:\work\text\Dicos\data\extract2.txt', 'r', encoding='utf-8')
    outputs = open(r'D:\work\text\Dicos\data\extract3.txt', 'w', encoding='utf-8')
    dic={}
    for line in inputs:
        print(line)
        if len(line.strip())==3:
            if line.strip() not in dic:
                dic[line.strip()]=0
            else:
                dic[line.strip()]+=1

        if len(line.strip())==5:
            if line.strip() not in dic:
                dic[line.strip()]=0
            else:
                dic[line.strip()]+=1

    for key in dic.keys():
        outputs.write(key + '\n')
    outputs.close()
    inputs.close()

def drop_duplicate():
    """词汇去重"""
    with open(r'D:\work\text\Dicos\data\extract3.txt','r',encoding='utf-8') as f:
        vacab=list(set(f.readlines()))
        with open(r'D:\work\text\Dicos\data\vocab.txt','w',encoding='utf-8') as f1:
            f1.writelines(vacab)

if __name__=='__main__':
    # extarct_not_positive()
    # process()
    # extract_negative()
    drop_duplicate()