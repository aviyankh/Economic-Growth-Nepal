import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


link1 = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Nepal"
df = pd.read_html(link1 , encoding='utf-8')
party = []
name = []
took = []
left = []
for i in range(7,9):
    f_pmo = df[i]
    f_pmo.columns = f_pmo.columns.droplevel()
    f_pmo = f_pmo.drop([f_pmo.columns[-1], f_pmo.columns[1] , 'No.' , 'Portrait'], axis = 1)
    f_pmo.rename(columns={f_pmo.columns[0]:'Name'} , inplace = True)
    f_pmo['Name'] = f_pmo['Name'].str.replace(r'\(.*','')
    f_pmo['Political Party'] = f_pmo['Political Party'].str.replace(r'\(U.*','')
    f_pmo.replace({'Nepali Congress' : 'NC' , 'Rastriya Prajatantra Party (Chand)': 'RPPC' , 'Rastriya Prajatantra Party':'RPP' , 'Nepali Congress (Democratic)':'NCD' , 'Communist Party of Nepal ':'UML' , 'Unified Communist Party of Nepal (Maoist)':'Maoist','Independent':'Indpt' , 'Nepal Communist Party':'NCP' , '—' : 'King','Communist Party of Nepal (Maoist Centre)':'CPN-MC' } , inplace=True)

    party1 = list(f_pmo['Political Party'])
    party = party + party1
    t_office = list(f_pmo['Took Office'].str.replace(r'\[.*\]','').str[-4:])
    took = took + t_office
    l_office = list(f_pmo['Left Office'].str.replace(r'\[.*\]','').str[-4:])
    left = left + l_office


# world bank data
eco = pd.read_csv('Growth_rate.csv', skiprows=3)

eco.index = eco['Country Name']
eco = eco.drop([eco.columns[0] , eco.columns[1] , eco.columns[2] , eco.columns[3]], axis = 1)
nepal_eco = eco.loc['Nepal'].dropna()
i_eco = np.around(list(nepal_eco[:-29]), decimals=2)
y1 = pd.to_numeric(nepal_eco.index.values)
year = [i for i in y1 if i>=1990]
fig , ax = plt.subplots(figsize=(11, 4))
bars = ax.plot(year, i_eco  , color = "skyblue" , marker = 's' ,  label = "Economic Growth", linewidth=1.5)
ax.set_yticks(np.arange(-4,11, 1.5))
plt.xticks(np.arange(min(year), max(year)+1, 1.0))
took = pd.to_numeric(took)
left[-1] = "2018"
left = pd.to_numeric(left)



dec = -4
colol = 50
for i,j,k in zip(took,left,party):

    x1 ,y1 = [i,j] , [dec+0.5,dec+0.5]

    ax.plot(x1,y1 , marker='s' , linestyle = "--", linewidth=1 , markersize=2 , color=(colol/100,colol/150,colol/200))
    plt.text(((i+j)/2)-0.4 , dec+0.5 , str(k) ,fontsize=6.5 , color='#003366')
    dec = dec+0.5

    colol = colol-0.01

ax.plot([2006,2006],[-4,9.5] , color = 'red' , linestyle='--' , linewidth=1)
plt.text(2006,9.5 , "Peoples Revolution II", fontsize=6.5 , color='k' , bbox = dict(alpha=0.5,pad=2))


ax.tick_params(axis='x', which='major', labelsize=7)
ax.set_facecolor('#f8f8f8')
ax.set_xlabel("Years")
ax.set_ylabel("Economic Growth(%)")
plt.title("Economic Growth of Nepal from 1960-1990 under Different Governments")
plt.grid()
plt.show()
