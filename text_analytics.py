# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:40:04 2017

@author: dmac21
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import pickle
from os import path
'''
pickle的解释
加工数据的，可以用来存取结构化数据。举个例子：
一个字典a = {'name':'Tom','age':22}，用pickle.dump存到本地文件，所存数据的结构就是字典，而普通的file.write写入文件的是字符串。读取时，pickle.load返回的是一个字典，file.read返回的是一个字符串。如下代码：
import pickle
a = {'name':'Tom','age':22}
with open('text.txt','wb') as file:
    pickle.dump(a,file)
with open('text.txt','rb') as file2:
    b = pickle.load(file2)
print(type(b))
得到的b的类型是字典，b和a是等价的，也就是说pickle可以把字典、列表等结构化数据存到本地文件，读取后返回的还是字典、列表等结构化数据。而file.write、file.read存取的对象是字符串。
'''
d=path.dirname(__file__)
text=''
background_image=plt.imread(path.join(d,'wusong.jpg'))

def read_text(filename):
    f=open(filename)
    return f

def handle_text(textfile,handled_file):
    global text
    for line in textfile.readlines():
        line=line.strip('\n')
        text +=' '.join(jieba.cut(line))
        text +=' '
    textfile.close()
    f=open(handled_file,'wb')
    pickle.dump(text,f)
    f.close()
    return handled_file

#绘制文字云
def draw_wordcloud(handled_file):
    f=open(handled_file,'rb')
    text=pickle.load(f)
    wc=WordCloud(background_color='white',#设置背景颜色
             mask=background_image,   #设置背景图片
             max_words=2000,          #设置最大实现的字数
             stopwords = STOPWORDS,   # 设置停用词
             font_path = 'C:/Users/Windows/fonts/msyh.ttf',# 设置字体格式，如不设置显示不了中文
             max_font_size = 50,            # 设置字体最大值
             random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
             )
    wc.generate(text)
    image_colors = ImageColorGenerator(background_image)
    wc.recolor(color_func = image_colors)
    return wc

#保存文字云图片
def save_wordcloud(wordcloud):
    wordcloud.to_file(path.join(d,'wordcloud.jpg'))
    
    
if __name__ == '__main__':
    f=read_text(path.join(d,'wusong.txt'))
    handled_file=handle_text(f,path.join(d,'text.txt'))
    wordcloud=draw_wordcloud(handled_file)
    save_wordcloud(wordcloud)
