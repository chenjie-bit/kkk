import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


def load_data(file_path):
    with open(file_path,'r') as f:
        label_lst=[]
        data_lst=[]
        for info in f.readlines():
            name = info.split('\t')[0].split('/')[-1].split('_')[0]
            data = [float(x) for x in info.split('\t')[1].split('<=>')]
            label_lst.append(name)
            data_lst.append(data)
            data_np = np.array(data_lst)
    return label_lst, data_np


def plot_embedding(data, label):
    #分配不同数据的颜色和形状以及注释
    color_dict={'8':'red','14':'yellow','15':'blue','16':'pink','18':'green'}
    maker_dict={'8':'.','14':'s','15':'1','16':'*','18':'+'}
    #label_dict={'A':'Arch','T':'Tented arch','L':'Left loop','R':'Right loop','W':'whorl'} 
    data_dict={}
    fig = plt.figure()
    #制作label为key的字典，用于画图分配形状和颜色
    for i in range(data.shape[0]):
        if label[i] not in data_dict:
            data_dict[label[i]]=[]
        data_dict[label[i]].append((data[i,0],data[i,1]))
    
    with open('encode.txt','w',encoding="utf-8")as f1:
    #这块没想好怎么去增加图例
        for label,value in data_dict.items():
            for value_ in value:
                f1.write(label+'\t'+str(value_[0])+'\t'+str(value_[1])+'\n')
                plt.scatter(value_[0],value_[1],color=color_dict[label],marker=maker_dict[label])
               # plt.legend('8','18')
        plt.xticks([])
        plt.yticks([])
       # plt.legend('8','18')
        plt.savefig('t-SNE.png')
    
if __name__=="__main__":
    #获取label和data对应的信息，data需要时numpy格式
    file_path = 'raw_data'
    label,data = load_data(file_path)
    #print(data.shape)
    #exit()
    #T-SNE
    tsne = TSNE(n_components=2, init='pca',random_state=4)
    result = tsne.fit_transform(data)
  
    #T-SNE后画图需要归一化处理
    max_,min_ = np.max(result,0),np.min(result,0)
    data = (result - min_)/(max_ - min_)
    plot_embedding(data, label)


