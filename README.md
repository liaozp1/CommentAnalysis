德克士大众点评评论关键词分析
1、项目文件：CommentAnalysis
2、项目内容：
data/:
	all.txt         解析完的评论
	neg_20.txt     负向评论
	pos_40.txt     正向评论
stopwords.txt   停用词
vocab.txt      自添词典
dicos_json_extract.py  解析json
extract_neg_pos_comments.py   评论正向向分类
extract_neg_vocab.py   否定词提取
keywords.py    关键词提取

说明：关键词提取默认返回topk个，返回字典格式
