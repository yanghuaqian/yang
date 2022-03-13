import numpy as np
with open("C:\\Users\\86183\\Desktop\\软件工程\\yq_in.txt", mode="rt") as f:
     pd= f.read()                      #读入文件
data=pd.split()                        #读取文件里面的数据
data1=np.array(data)                   #将文件中的数据转换成为数组
data2=data1.reshape(129,3)
print(data2[0][0])                     #输出数组模式的数据
for i in range(128):
    if(data2[i][0]==data2[i+1][0]):    #判断数组中该行的省份是否和前一行相同  
        print(data2[i][1]+'\t'+data2[i][2]) #相同输出市+数据
    else:
        print(data2[i][1]+'\t'+data2[i][2]+'\n')#不同输出后一行的省份+市+数据
        print(data2[i+1][0])
  
