




all_label = []
with open('encode_data','w',encoding = 'utf-8')as f:  #生成新的编码数据，格式是图片对应的编码
    for i,line in enumerate(open ('model_1_data.txt','r',encoding = 'utf-8')):  #读取编码数据
        data,label = line.strip().split('\t')
        all_label.append(label)
        data_ = eval(data)
        label = int(label)
            
        if label == 0:
            label_ = str(label)+ '_' + str(i)+'.png'
        if label == 1:
            label_ = str(label)+ '_' + str(i)+'.png'
        if label == 2:
            label_ = str(label)+ '_' + str(i)+'.png'
        if label == 3:
            label_ = str(label)+ '_' + str(i)+'.png'
        import cv2
        import numpy
        #全黑的灰度图
        f.write(str(label_) +'\t'+ str(label)+'\t' + str(data)+'\n')
        
        # f1.write(str(label_) +'\t'+ str(label)+'\n')

        gray0=numpy.zeros((500,500),dtype=numpy.uint8)
        cv2.imwrite('picture'+'//'+label_, gray0)   #生成的图片存放在picture文件夹中，每次换新的编码数据记得清除文件夹中的内容
    print(len(all_label)) #
    #exit()