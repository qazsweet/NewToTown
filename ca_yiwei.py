#coding=utf8  
#N = 1471  
#n = 4  
#str_cell = "00011110101010"  
N = int (input("请输入N值："))  
n = int (input("请输入计算代数："))  
str_cell = input("请输入原始序列：")  
if ( N>=128 ):  
    str_N = bin(N)  
    str_N = str_N[2:]  
elif (N > 0):  
    str_N = bin(N)  
    num = len(str_N[2:])  
    str0 = "00000000"  
    str_N =str0[:8-num] + str_N[2:]  
print("映射序列: "+str_N ) 
print("第  0 代：" + str_cell  )
li_num = []  
num = 0  
for i in range (0,8):  
    if ( num >= 4):  
        str_num = bin(num)  
        str_num = str_num[2:]  
        li_num.append(str_num)  
    elif (num >= 0):  
        str_num = bin(num)  
        num0 = len(str_num[2:])  
        str0 = "000"  
        str_num =str0[:3-num0] + str_num[2:]  
        li_num.append(str_num)  
    num = num +1  
dict_N = dict([(li_num[t],str_N[t])for t in range (0,8)])  
for k in range (1,n+1):  
    str_cell_new = str_cell[0]  
    for i in range (0,len(str_cell)-2):  
        if i >=0 & i<(len(str_cell)-2):  
            cmp_cell = str_cell[i:i+3]  
            str_cell_new = str_cell_new + dict_N.get(str_cell[i:i+3])    
    str_cell_new = str_cell_new + str_cell[len(str_cell)-1]  
    str_cell = str_cell_new  
    print("第",'%2d'%k,"代："+str_cell)  
