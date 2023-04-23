import config as CF
import model as m
import glob
import os
import time
import numpy as np

def load_data(file_):
    data=[]
    file_lst=[]
    for line in open(file_,"r",encoding="utf-8"):
        label,_,da =line.strip().split("\t")
        da = [float(i)for i in da.split(',')[:-1]]
        #print(label)
        #exit()
        #label=label.replace("\\","/").split("/")
        label = CF.all_path + '/' + label
        #print(label)
        #exit()
        data.append(da)
        file_lst.append(label)
    return file_lst,data
st=time.time()
file_lst,data=load_data("dataset/encode_data")

print("sample number is %s, sample dim is %s"%(len(data),len(data[0])))
class_num=CF.config["class_num"]
for model_type in CF.config["type"]: 
    model= m.model(class_num=class_num)
    model.build(model_type)
    model.run(data)
    model.show(file_lst)

print("聚类完成，一共用时:%s秒"%(time.time()-st))
