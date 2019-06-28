#encoding:utf-8

class WorstComment():
    """
    Worst Comment
    """
    def __init__(self):
        self.worstlist = [word.strip() for word in open('../qsvc/data/words/极差评词.txt', encoding='utf-8').readlines()]
        self.in_path = '../data/neg_20.txt'
        self.out_path = '../qsvc/data/极差评论.txt'
        self.worst_comment=[]

    def find_worst_comments(self):
        with open(self.in_path, encoding='utf-8') as f1:
            for line in f1:
                for word in self.worstlist:
                    if word in line:
                        self.worst_comment.append(line)
                        break
        with open(self.out_path, 'w', encoding='utf-8') as f2:
            f2.writelines(self.worst_comment)
        return self.worst_comment

if __name__ == '__main__':
    ws = WorstComment()
    ws.find_worst_comments()
    print(len(ws.worst_comment))