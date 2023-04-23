import config as CF
import glob
import os,random
def get_first_label(file_path):
    files=glob.glob(file_path+"/*")
    ret_im2label={}
    ret_label2im={}
    for files_ in files:
        label=files_.split("/")[-1]
        if label not in ret_label2im:
            ret_label2im[label]=[]
        ims_path=glob.glob(files_+"/*")
        for ims in ims_path:
            ims=ims.split("/")[-1]
            ret_im2label[ims]=label
            ret_label2im[label].append(ims)
    return ret_im2label,ret_label2im
def get_max(t):
    max_=""
    max_v=0
    for key,value in t.items():
        if value >max_v:
            max_=key
            max_v=value
    return max_

def get_non_first_label(t_first_im2label,file_path):
    files=glob.glob(file_path+"/*")
    ret_label2im={}
    print(files)
    print("?????????????????")
    for files_ in files:
        t_count={}
        tmp=[]
        ims_path=glob.glob(files_+"/*")
        print(files_+":",ims_path)
        print(t_first_im2label)
        for ims in ims_path:
            ims=ims.split("/")[-1]
            label=t_first_im2label[ims]
            t_count[label]=t_count.get(label,0)+1
            tmp.append(ims)
        print(t_count)
        this_label=get_max(t_count)
        print(this_label)
        ret_label2im[this_label]=tmp
        tmp=[]
    return ret_label2im

def keep(file_path):
    files=glob.glob(file_path+"/*")
    if len(files)>0 and len(files)<=class_num:
        return True
    else:
        return False
def make_blank_dict(raw_path):
    t={}
    raw_file_lst=glob.glob(raw_path+"/*")
    for raw in raw_file_lst:
        t[raw]={}
    print("there are %s clusters"%len(t))
    return t
def inter(lst1,lst2):
    ret=[]
    for x in lst1:
        if x in lst2:
            ret.append(x)
    return ret

if __name__=="__main__":
    class_num=CF.config["class_num"]
    t_whole={}
    files=glob.glob("result/*")
    print(files)
    for fi in files:
        print(glob.glob("%s/*"%fi))
        if len(glob.glob("%s/*"%fi))==class_num:  
            print("the first chosen file is %s"%fi) 
            t_im2label_first,t_label2im_first=get_first_label(fi)
            for label,im in t_label2im_first.items():
                print(label,len(im))
            print(t_label2im_first)
            files.remove(fi)
            t_whole[fi]=t_label2im_first 
            break
        elif not keep(fi):
            files.remove(fi)
    
    for fi in files:
        if keep(fi):
            t_label2im_=get_non_first_label(t_im2label_first,fi)
            for label,im in t_label2im_.items():
                print(label,len(im))
            t_whole[fi]=t_label2im_
            print(len(t_label2im_),fi)
        else:
            print("abandom %si"%(fi))

    t_final=t_label2im_first
    print("一共有%s个聚类方法"%(len(t_whole)))
    for fi,items in t_whole.items():
        print(len(items))
        for label,ims in items.items():
            if label not in t_final:
                t_final[label]=[]
            print("现在处理聚类方法%s。取并集前，类别%s 有%s个样本"%(fi,label,len(t_final[label])))
            t_final[label]=inter(t_final[label],ims)
            print("取并集后，类别%s 有%s个样本"%(label,len(t_final[label])))
    if glob.glob("result_final")==[]:
        os.system("mkdir result_final")
    
    all_img_path=CF.all_path#"../data/demo_uncrop"
    ims_all=[x.split("/")[-1] for x in glob.glob("%s/*"%all_img_path)]
    total_num_pic=len(ims_all)
    
    for label,ims in t_final.items():
        path_t="result_final/bagging/%s"%label
        if glob.glob(path_t)==[]:
            os.system("mkdir %s"%path_t)
        else:
            os.system("rm -r %s && mkdir %s"%(path_t,path_t))
        print(ims)
        for im in ims:
            print(im)
            ims_all.remove(im)
            os.system("cp %s/%s %s"%(all_img_path,im,path_t))
        print(label)
        print("===============")
    print("total number is %s, the number of well classified is %s"%(total_num_pic,len(ims_all)))
    rest_file_path="result_final/bagging/rest"
    if glob.glob(rest_file_path)!=[]:
        os.system("rm -r %s"%rest_file_path)
    os.system("mkdir %s"%rest_file_path)
    for im in ims_all:
        os.system("cp %s/%s %s"%(all_img_path,im,rest_file_path))
  #############################
  ################################
    random_path="result_final/random/0"
    if glob.glob(random_path)!=[]:
        os.system("rm -r "+random_path)
    os.mkdir(random_path)
    ims_all=[x.split("/")[-1] for x in glob.glob("%s/*"%all_img_path)]
    random.shuffle(ims_all)
    for img in ims_all:
        if random.random()>0.9:
            cmd ="cp %s/%s %s"%(all_img_path,img,random_path)
            os.system(cmd)
        
    
