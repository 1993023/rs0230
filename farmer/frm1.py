# import pandas as pd
# df = pd.read_csv("OFIS_Farmer_Name_DOB.csv") 
# # print(df)

# k=list(df['Module Name'].unique())
# # print(k)
# for i in k:
#     df[i]= 0
# # print(df)

# for j in k:
#     for i in range(len(df)):
#         if df["Module Name"][i]==j:
#             df[j][i]= 1
#         else:
#             df[j][i]= 0

# # print(df)
# pvt=df.pivot_table(index=['Farmer Id','Module Name'], values=["Farmer Name","Gender","DOB","Product Name","Country Name","Region Name","District Name","Place Name","Farmer Group Name",
#                 "Partner Name","Programmer Name","Section Name","Enumerator Name",'Cocoa Baseline Survey', 'Cocoa Annual Survey', 'SWIFT', 'Implementation of GAP SAN and CSA', 'Ecuador Internal Audit', 'UTZ Internal Inspection', 'Verification of Recommendations', 'Cocoa - Impact Evaluation Survey', 'Cocoa Plan follow up survey', 'Cocoa - follow-up of plantation', 'Creation of Plantation', 'Implementation of GAP', 'Darwin Project'], aggfunc='first')

# print(pvt)

# pvt.to_csv('file2.csv')



# Another Solution 
import pandas as pd
df = pd.read_csv("OFIS_Farmer_Name_DOB.csv") 

df['date'] = pd.to_datetime(df['Submitted On'])
df['year']= df['date'].dt.year

# for i in range(len(df)):
#     df["Module Name_updated"]=df["Module Name"][i]+str(df["year"][i])
    

# i=0
# while i<(len(df)):
#     df["Module Name_updated"]=df["Module Name"][i]+str(df["year"][i])
#     i=i+1

    
# print(df)
# df.to_csv('testt.csv')

df['Module Name_updated']=df['Module Name']+str(df['year'])
df["year"].apply(str)
df["year"]=df["year"].apply(str)
df["Module Name_updated"]=df[["Module Name","year"]].apply(lambda x:"".join(x),axis=1)
print(df)


df.to_csv('testt.csv')