# -*- coding:UTF-8 -*-
import pickle
import csv 
import glob

def selsct_data(dataset,method,data_dict,to_path,num_lst):
    header = ['dim','class'] + num_lst + ['overall', 'reject'] #, '8','14','15','18',['overall', 'reject']
    # print(header)
    # exit()
    da = []
    for dim,num in data_dict.items():
        for class_,data in num.items():
            precision = data['bagging']['precision']
            overall = data['bagging']['overall']
            reject = data['bagging']['reject']
            print(data['bagging']['precision'])
            list_keys = [k for k,v in precision.items()]
            for i in num_lst:
                if i not in list_keys:
                    precision[i] = 0
            # print(precision)
            print('==========')
            all_nn = []
            for i in num_lst:
                nn = precision[i]
                all_nn.append(nn)
            
            data = [dim,class_] + all_nn +[overall, reject]#, a,b,c,d,[overall, reject]
            da.append(data)

    file_name = to_path+'/'+dataset + '_' +method + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(da)
        
        
def get_result():
    with open("final_result.pkl","rb")as f:
        data=pickle.load(f)
    # data_path="datas\\binary_data"
    
    dataset = list(data.keys())[0]
    print(dataset)
    
    data_path="datas\\"+ str(dataset)
    # dataset = data_path.split('\\')[-1]
    num_lst = []
    for i in glob.glob(data_path + '/*'):
        label = i.strip().split('\\')[-1].split('_')[0]
        num_lst.append(label)
    num_lst = list(set(num_lst))
    to_path = '结果'
    for one in data[dataset].keys():
        data_dict = data[dataset][one]
        selsct_data(dataset,one,data_dict,to_path,num_lst)


def main():
    get_result()
if __name__=="__main__":
    with open("final_result.pkl","rb")as f:
        data=pickle.load(f)
    # print(data)
    # exit()
    dataset = list(data.keys())[0]
    data_path="datas\\"+ dataset
    # print(data_path)
    # exit()
    num_lst = []
    for i in glob.glob(data_path + '/*'):
        label = i.strip().split('\\')[-1].split('_')[0]
        num_lst.append(label)
    num_lst = list(set(num_lst))
    # print(num_lst)
    # exit()
    to_path = '结果'
    for one in data[dataset].keys():
        data_dict = data[dataset][one]
        selsct_data(dataset,one,data_dict,to_path,num_lst)
    
