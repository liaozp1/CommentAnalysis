#encoding:utf-8
import jieba

def extract_neg_comments():
  """ 找出负向评论"""
  with open(r'D:\work\text\Dicos\data\all.txt', 'r',encoding='utf-8') as f1:
    # with open(r'D:\work\text\Dicos\data\neg_20.txt', 'w',encoding='utf-8') as f2:
    with open(r'D:\work\text\Dicos\data\pos_40.txt', 'w', encoding='utf-8') as f2:
      for line in f1:
        print(line)
        try:
          if int(line.split('||')[0]) >=40:
            f2.write(line)
        except:
          print('这一行格式不对哦')

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(r'D:\work\text\Dicos\data\stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t'and'\n':
                outstr += word
                outstr += " "
    return outstr

if __name__ == "__main__":
  extract_neg_comments()
  # inputs = open(r'D:\work\text\Dicos\data\neg_20.txt', 'r', encoding='utf-8')
  # outputs = open(r'D:\work\text\Dicos\data\neg_cut_20.txt', 'w', encoding='utf-8')
  # for line in inputs:
  #   line_seg = seg_sentence(line)  # 这里的返回值是字符串
  #   outputs.write(line_seg + '\n')
  # outputs.close()
  # inputs.close()
