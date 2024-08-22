import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import os
file_path = os.path.join(os.getcwd(), "Rice1.xlsx")
#TODO: 1st Part
try:
    data = pd.read_excel(file_path, sheet_name='Rice')
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
#TODO: 2nd Part
print("index:",len(data.index)," | ","columns:",len(data.columns))
print(data[0:10])
def print_max_min(data,feature):
    print('{:20}'.format(feature),'|',"Max:",data[feature].max(),',',"Min:",data[feature].min())
print_max_min(data,'Area')
print_max_min(data,'Perimeter')
print_max_min(data,'Major_Axis_Length')
print_max_min(data,'Minor_Axis_Length')
print_max_min(data,'Eccentricity')
print_max_min(data,'Convex_Area')
print_max_min(data,'Extent')
#TODO: 3rd Part
def Normalize(data,path):
    element = pd.DataFrame(data, columns=[path])
    normalized_element=(element-element.mean())/element.std()
    return normalized_element
def Normalization_tuple(data):
    normalized_Area=Normalize(data,'Area')
    normalized_Perimeter=Normalize(data,'Perimeter')
    normalized_Major_Axis_Length=Normalize(data,'Major_Axis_Length')
    normalized_Minor_Axis_Length=Normalize(data,'Minor_Axis_Length')
    normalized_Eccentricity=Normalize(data,'Eccentricity')
    normalized_Convex_Area=Normalize(data,'Convex_Area')
    normalized_Extent=Normalize(data,'Extent')
    Class = pd.DataFrame(data, columns=['Class'])
    return normalized_Area,normalized_Perimeter,normalized_Major_Axis_Length,normalized_Minor_Axis_Length,normalized_Eccentricity,normalized_Convex_Area,normalized_Extent,Class
#Testing:
print("MEAN Area Before Normalization:",int((data)['Area'].mean()))
print("MEAN Area After Normalization:",int(Normalization_tuple(data)[0].mean()))
print("STD Area After Normalization:",int((data)['Area'].std()))
print("STD Area After Normalization:",int(Normalization_tuple(data)[0].std()))
#TODO: 4th Part
print("New Rice:")
Area = float(input(f'{1}. Enter Area: '))
Perimeter = float(input(f'{2}. Enter Perimeter: '))
Major_Axis_Length = float(input(f'{3}. Enter Major_Axis_Length: '))
Minor_Axis_Length = float(input(f'{4}. Enter Minor_Axis_Length: '))
Eccentricity = float(input(f'{5}. Enter Eccentricity: '))
Convex_Area = float(input(f'{6}. Enter Convex_Area: '))
Extent = float(input(f'{7}. Enter Extent: '))
Class='NAN'
new_data={"Area":[Area],"Perimeter":[Perimeter],"Major_Axis_Length":[Major_Axis_Length],
          "Minor_Axis_Length":[Minor_Axis_Length],"Eccentricity":[Eccentricity],
          "Convex_Area":[Convex_Area],"Extent":[Extent],"Class":[Class]}
df = pd.concat([data, pd.DataFrame.from_records(new_data)]).reset_index(drop=True)
df.to_excel(r'/home/hpmoon/Desktop/Rice_input.xlsx',sheet_name='Rice',index=False)
#Testing:
print("MEAN Normalized Area:",int(Normalization_tuple(df)[0].mean()))
print("STD Normalized Area:",int(Normalization_tuple(df)[0].std()))
#TODO: 5th Part
######################################################## Spliting Columns
normalized_Area1=np.array_split(Normalization_tuple(df)[0],3811)
normalized_Perimeter1=np.array_split(Normalization_tuple(df)[1],3811)
normalized_Major_Axis_Length1=np.array_split(Normalization_tuple(df)[2],3811)
normalized_Minor_Axis_Length1=np.array_split(Normalization_tuple(df)[3],3811)
normalized_Eccentricity1=np.array_split(Normalization_tuple(df)[4],3811)
normalized_Convex_Area1=np.array_split(Normalization_tuple(df)[5],3811)
normalized_Extent1=np.array_split(Normalization_tuple(df)[6],3811)
def distances(a,b):
    return math.pow((b-a),2)
def euclidean_distances(sigma):
    return math.sqrt(sigma)
def text_to_float(x,order,Col):
    return float(str(x[order][Col]).replace(str(order    ),"").partition('\n')[0])
euclidean_distance=[]
saved_index=[]
for i in range(0, 3810):
    a1=distances(text_to_float(normalized_Area1,i,'Area'),text_to_float(normalized_Area1,3810,'Area'))
    a2=distances(text_to_float(normalized_Perimeter1,i,'Perimeter'),text_to_float(normalized_Perimeter1,3810,'Perimeter'))
    a3=distances(text_to_float(normalized_Major_Axis_Length1,i,'Major_Axis_Length'),text_to_float(normalized_Major_Axis_Length1,3810,'Major_Axis_Length'))
    a4=distances(text_to_float(normalized_Minor_Axis_Length1,i,'Minor_Axis_Length'),text_to_float(normalized_Minor_Axis_Length1,3810,'Minor_Axis_Length'))
    a5=distances(text_to_float(normalized_Eccentricity1,i,'Eccentricity'),text_to_float(normalized_Eccentricity1,3810,'Eccentricity'))
    a6=distances(text_to_float(normalized_Convex_Area1,i,'Convex_Area'),text_to_float(normalized_Convex_Area1,3810,'Convex_Area'))
    a7=distances(text_to_float(normalized_Extent1,i,'Extent'),text_to_float(normalized_Extent1,3810,'Extent'))
    sigma=a1+a2+a3+a4+a5+a6+a7
    euclidean_distance.append(euclidean_distances(sigma))
    saved_index.append(np.array([[i],[euclidean_distance[i]]]))
final_result = sorted(euclidean_distance, key = float)
k = int(input('Enter K as K-nearest?'))
k_nearest=[]
for i in range(0,k):
    k_nearest.append(final_result[i])
list_index=[]
for i in range(0,3809):
    for j in range(0,k):
        if (float(saved_index[i][1])==k_nearest[j]):
            list_index.append(int(saved_index[i][0]))
def Vote(k,list_index):
    a=0
    b=0
    for i in range(0,k):
        out=df.at[list_index[i],'Class']
        if out == 'Cammeo':
            a = a + 1
        if out == 'Osmancik':
            b = b + 1
    if(a>=b):
        print("Class is Cammeo")
        return str("Cammeo")
    if(b>a):
        print("Class is Osmancik")
        return str("Osmancik")
df.loc[[int(3810)] ,["Class"]] = Vote(k,list_index)
#TODO: 6th part
def show(Normalize_item,feature):
    for i in range(0,10):
        x=random.randrange(0,3810,1)
        xarray=np.array([df.at[x,feature]])
        yarray=np.array([text_to_float(Normalize_item,x,feature)])
        plt.scatter(xarray,yarray ,c="red",s=20,marker="+")
        plt.title(("After and Before Normalization"))
        plt.xlabel("Not Normalized yet")
        plt.ylabel("Normalized")
    plt.show()
show(normalized_Area1,'Area')
show(normalized_Perimeter1,'Perimeter')
show(normalized_Major_Axis_Length1,'Major_Axis_Length')
show(normalized_Minor_Axis_Length1,'Minor_Axis_Length')
show(normalized_Eccentricity1,'Eccentricity')
show(normalized_Convex_Area1,'Convex_Area')
show(normalized_Extent1,'Extent')
