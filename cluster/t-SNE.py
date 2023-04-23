import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import matplotlib

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
    color_dict={'8':'red','14':'yellow','15':'blue','18':'green'}
    maker_dict={'8':'.','14':'s','15':'1','18':'+'}
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
        plt.title('t-SNE %s performance')
        plt.legend()
        plt.savefig('t-SNE.png')
'''
def plot_embedding(data, label):
    #分配不同数据的颜色和形状以及注释
    # color_dict={'8':'red','14':'yellow','15':'blue','16':'pink','18':'green'}
    # maker_dict={'8':'.','14':'s','15':'1','16':'*','18':'+'}

    # label_dict={'A':'Arch','T':'Tented arch','L':'Left loop','R':'Right loop','W':'whorl'} 
    data_dict={}
    fig = plt.figure()
    
    #max_=max(label)
    #min_=min(label)
    #label_num=max_-min_+1
    #制作label为key的字典，用于画图分配形状和颜色
    for i in range(data.shape[0]):
        if label[i] not in data_dict:
            data_dict[label[i]]=[]
        data_dict[label[i]].append((data[i,0],data[i,1]))
    
    with open('encode.txt','w',encoding="utf-8")as f1:
    #这块没想好怎么去增加图例
        
        #if label_num==5 or label_num==4:
            # color_dict={'8':'red','4':'yellow','15':'blue','18':'green'}
            # maker_dict={'8':'.','14':'s','15':'1','18':'+'}
        color_dict={1:'gray',2:'cyan',3:'blue',4:'green',5:'red'}
        maker_dict={1:'<',2:'.',3:'1',4:'*',5:'+'}
        label_dict={1:'8',2:'14',3:'15',4:'18',5:'rest'}
            # flag=[0]*100
        # for data,index in zip(data,label):
            # if flag[index]==0:
                # plt.scatter(data[0],data[1],color=color_dict[index],marker=maker_dict[index],label=label_dict[],s=11)
                # flag[index]+=1
            # else:
                # plt.scatter(data[0],data[1],color=color_dict[index],marker=maker_dict[index],s=11)
                
        for label,value in data_dict.items():
            for value_ in value:
                f1.write(label+'\t'+str(value_[0])+'\t'+str(value_[1])+'\n')
                plt.scatter(value_[0],value_[1],color=color_dict[label],marker=maker_dict[label])
            # plt.legend('8','18')
        plt.xticks([])
        plt.yticks([])
        plt.title('t-SNE %s performance')
        plt.legend()
        plt.savefig('plot_result/t_SNE_%s.png')
        plt.close()
       # plt.legend('8','18')
        # plt.savefig('t-SNE.png')
'''
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


