import jieba
path = 'D:\\117010800211\\红楼梦.txt'
txt = open('红楼梦.txt','r',encoding = 'GB18030').read()
words = jieba.lcut(txt)
excludes = {'这会子','怎么样','为什么','贾政道','袭人道','黛玉道','贾母笑','悄悄的','宝钗道','少不得','林姑娘','下回分解','老婆子','宝钗笑','黛玉笑','林妹妹','可不是','怡红院','老人家','这么着','女孩子','女孩儿','不在话下','周瑞家','了不得'}
counts = {}
for word in words:
    if len(word) == 1 or len(word) == 2:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))
