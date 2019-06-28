
tastelist= \
    ['口味', '好吃', '难吃' ,'喝', '酸', '甜', '苦', '辣', '麻', '咸', '甘', '淡', '香', '苦涩', '平淡', '鲜美',
     '诱人', '独特', '醇厚', '甜美' ,'香辣', '油腻', '清香', '甜蜜', '甘甜', '浓香', '轻香', '松脆', '甘苦',
     '甜津津', '甜丝丝', '酸溜溜', '甜蜜蜜', '辣酥酥' ,'辣丝丝', '美滋滋', '香喷喷', '辣乎乎', '苦涩涩',
     '臭烘烘', '咸津津', '油滋滋', '麻辣辣' ,'新鲜' ,'味道' ,'吃起来' ,'口感', '凉']
envlist = ['环境', '干净', '优雅', '脏', '乱', '厕所', '臭', '香', '难闻', '装修', '宽敞明亮', '整洁',
                '明亮' ,'空调' ,'太热了']
servicelist = ['服务', '态度', '傲慢', '素质', '慢', '快点', '速度' ,'等', '人性' ,'吃不饱' ,'爱搭不理' ,'排队',
                    '网络' ,'退款' ,'大众点评' ,'美团' ,'wifi']
pricelist = ['贵', '便宜', '价格', '实惠', '划算', '划得来', '合算']

with open(r'D:\work\text\CommentAnalysis\qsvc\data\words\口味词.txt','w',encoding='utf-8') as f:
    for line in tastelist:
        f.write(line+'\n')

with open(r'D:\work\text\CommentAnalysis\qsvc\data\words\环境词.txt', 'w', encoding='utf-8') as f:
    for line in envlist:
        f.write(line + '\n')

with open(r'D:\work\text\CommentAnalysis\qsvc\data\words\服务词.txt', 'w', encoding='utf-8') as f:
    for line in servicelist:
        f.write(line + '\n')

with open(r'D:\work\text\CommentAnalysis\qsvc\data\words\价格词.txt', 'w', encoding='utf-8') as f:
    for line in pricelist:
        f.write(line + '\n')