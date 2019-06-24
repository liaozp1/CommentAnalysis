#coding:UTF-8
import json
import os
import re

def remove_img_tags(data):
    # p = re.compile(r'<img.*?/>')
    return re.sub(r'<img.*>', ',',data)

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
                print(str(jobject['shopId'])+'  '+ str(comment['star'])+ '  '+ remove_img_tags(comment['reviewBody']))

                content.append(str(jobject['shopId'])+'  '+ str(comment['star'])+ '  '+ \
                               remove_img_tags(comment['reviewBody'] + '\n'))
                contents.append(str(comment['star'])+ '||'+ remove_img_tags(comment['reviewBody'] + '\n'))

        filename=file.replace('json', 'txt')
        outfile=os.path.join(dir, filename)
        outfile2=os.path.join(dir, 'all.txt')

        with open(outfile,'w',encoding='utf-8') as f1:
            f1.writelines(content)

    with open(outfile2, 'w', encoding='utf-8') as f2:
        f2.writelines(contents)

    print('finish')

if __name__=="__main__":
    dir = r'D:\work\text\Dicos'
    etl(dir)