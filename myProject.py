# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:11:22 2021

@author: Gady
"""
import csv
import pandas as pd
import numpy as np

#change 13-14
#get details from csv file:
    
from pathlib import Path

sizes=[0]*200 #arbitary amount of files
file_counter=1           
for p in Path('OriginalData').glob('*.csv'):
    with p.open() as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        line_count = 0
        
        i=0
        j=0
        flag_g=0
        flag_a=0
        for line in csv_reader:
            line_count+=1
            if "Gyro" in line:
                flag_g+=1
            if "Accel" in line:
                flag_a+=1
            if flag_g==2:
                gyro_first_line=line_count-1
                flag_g+=1 #so we won't come back to this if statement again
            if flag_a==2:
                acc_first_line=line_count-1
                gyro_last_line=line_count-5
                flag_a+=1 #so we won't come back to this if statement again
        #end for
        acc_last_line=line_count
        print(gyro_first_line, gyro_last_line, acc_first_line, acc_last_line)
        
        data_gyro_x=[0]*(gyro_last_line-gyro_first_line)
        data_gyro_y=[0]*(gyro_last_line-gyro_first_line)
        data_gyro_z=[0]*(gyro_last_line-gyro_first_line)
        data_gyro_timeStamp=[0]*(gyro_last_line-gyro_first_line)
        data_acc_x=[0]*(acc_last_line-acc_first_line-1)
        data_acc_y=[0]*(acc_last_line-acc_first_line-1)
        data_acc_z=[0]*(acc_last_line-acc_first_line-1)
        data_acc_timeStamp=[0]*(acc_last_line-acc_first_line-1)
        
        line_count=0
        csv_file.seek(0)
        
        for row in csv_reader:
            if line_count<gyro_first_line:
                line_count += 1
                continue
            elif line_count< gyro_last_line:
                data_gyro_timeStamp[i]=row[3]
                data_gyro_x[i]=row[5]
                data_gyro_y[i]=row[6]
                data_gyro_z[i]=row[7]
                
            elif  acc_last_line>line_count > acc_first_line:
                data_acc_timeStamp[j]=row[3]
                data_acc_x[j]=row[5]
                data_acc_y[j]=row[6]
                data_acc_z[j]=row[7]  
                j+=1
            #print(data_arr_timeStamp[i],data_arr_x[i],data_arr_y[i],data_arr_z[i])
            i=i+1
    
            line_count += 1
        #end for
        integer_g = map(float, data_gyro_timeStamp)
        integer_a = map(float, data_acc_timeStamp)
        
        integer_gx= map(float, data_gyro_x)
        integer_gy= map(float, data_gyro_y)
        integer_gz= map(float, data_gyro_z)
        integer_ax= map(float, data_acc_x)
        integer_ay= map(float, data_acc_y)
        integer_az= map(float, data_acc_z)
        
        data_gyro_timeStamp = list(integer_g)
        data_acc_timeStamp = list(integer_a)
        data_gyro_x = list(integer_gx)
        data_gyro_y = list(integer_gy)
        data_gyro_z = list(integer_gz)
        data_acc_x = list(integer_ax)
        data_acc_y = list(integer_ay)
        data_acc_z = list(integer_az)
        
        i=0
        j=0
        line_count=0
        csv_file.seek(0)
        
        arr_g = np.array([data_gyro_timeStamp, data_gyro_x, data_gyro_y, data_gyro_z])
        arr_g = arr_g.transpose()
        arr_a = np.array([data_acc_timeStamp, data_acc_x, data_acc_y, data_acc_z])
        arr_a = arr_a.transpose()
        size=len(arr_g)+len(arr_a)
        sizes[file_counter]=size
        arr_united=np.zeros(shape=(size,7))
        
        ########################################################################################
        #arr_united: 0. timestamp, 1. gyro_x, 2. gyro_y, 3. gyro_z, 4. acc_x, 5. acc_y, 6. acc_z
        ########################################################################################
        #arr=np.concatenate([arr_g,arr_a])
        df_g = pd.DataFrame(data=arr_g, index=None, columns=None)
        df_a = pd.DataFrame(data=arr_a, index=None, columns=None)
        df=pd.merge(df_g, df_a, how='outer', on=0, sort='true')
        
        df.columns = ['time', 'gyro_x', 'gyro_y', 'gyro_z', 'acc_x', 'acc_y', 'acc_z']
        #df['time'] = pd.to_datetime(df['time'], unit='ms')
        df = df.set_index('time')
        df_interpol=df.interpolate(method='index')
        #change 115 instead of myDataSet.csv call it per file name
        df2=df_interpol.to_csv('ProccessedDataSets\ProccessedDataSet_'+ str(file_counter) +'.csv', date_format='%Y-%m-%d %H:%M:%S%f')
        file_counter+=1


file_counter=1
i=1           
for p in Path('ProccessedDataSets').glob('*.csv'):
    with p.open() as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        proccessed_data_timeStamp=[0]*sizes[file_counter]
        vy = [0]*sizes[file_counter]
        vx = [0]*sizes[file_counter]
        vz = [0]*sizes[file_counter]
        v = 0
        line_count = 0
        for line in csv_reader:
            line_count+=1
            
            proccessed_data_timeStamp[i-1]=line[0]
            
            if (line_count>=10):
                dt =  proccessed_data_timeStamp[i]-proccessed_data_timeStamp[i-1]
                #continue here!!!
                for j in range(line[5]):
                    v = v + ax[j]*dt
                    vy.append(v)
                vy = np.array(vy)
        file_counter+=1 
        i+=1