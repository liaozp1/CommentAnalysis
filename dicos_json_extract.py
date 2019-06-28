#coding:UTF-8
import json
import os
import re

def remove_img_tags(line):
    # p = re.compile(r'<img.*?/>')
    line = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", line)
    line = re.sub(r'<img.*/>', ' ', line).replace('-', ',').strip() + '\n'
    return line

def etl(dir):
    contents=[]
    for file in [file for file in os.listdir(dir) if file.endswith('json')]:
        filepath=os.path.join(dir, file)
        print(filepath)
        content = []
        with open(filepath, 'r', encoding='utf-8') as f:
            line = f.read()
            jobject = json.loads(line)
            # for key in jobject:
            #     print(key)
            print(jobject['shopId'])
            for comment in jobject['CommentData']['comment']:
                if comment['reviewBody'] == '':
                    continue
                # print('前', comment['reviewBody'])
                # print('后', remove_img_tags(comment['reviewBody']))
                content.append(str(jobject['shopId'])+'  ' + str(comment['star']) + '  ' + \
                               remove_img_tags(comment['reviewBody']))
                contents.append(str(comment['star']) + '||' + remove_img_tags(comment['reviewBody']))

        filename=file.replace('json', 'txt')
        outfile=os.path.join(dir, filename)
        with open(outfile,'w',encoding='utf-8') as f1:
            f1.writelines(content)

    outfile2 = os.path.join(dir, 'all.txt')
    with open(outfile2, 'w', encoding='utf-8') as f2:
        f2.writelines(contents)

    print('finish')

if __name__=="__main__":
    # dir = r'D:\work\text\Dicos'
    dir=r'C:\Users\zepingliao.X2ERA\Desktop\MasterKong'
    etl(dir)