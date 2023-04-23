

config.py中："class_num":2 ,可修改聚类类别


第一步：编码数据存放在dataset文件夹中，格式为：编码 + '\t'+标签  
		运行dataset文件夹中的 python make_pic.py ，生成picture文件及encode_data。
		picture里面是生成的图片，用于聚类复制使用），生成encode_data格式：名字+'\t' +label +'\t' + 编码
		注意（换编码数据之后，picture里面的数据要删除）
第二步：直接运行sh run.sh脚本,聚类结果存放在'结果'文件夹中，result.csv



sh run.sh 
python main.py 读取encode_data内标签、编码数据
python get_final_result.py 得到bagging结果图片存入result\bagging
python 2_statistics.py 得出各个方法的结果，保存在结果中
python 3_getFinalReport.py 读取结果文件夹内bagging各个方法结果，保存在final_result.pkl：
python 4_result.py 将final_result.pkl写到结果\result.csv