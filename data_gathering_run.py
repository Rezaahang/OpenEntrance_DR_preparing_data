import pandas as pd
import os
import numpy as np


filepath = f"C:/Users/mohaa/Desktop/Projects and papers/Open entrance/Open Entrance/DR data/The latest data/countries data"

country_name = 'DE' #Enter the name of country

AC_tshift = 2
EV_tshift = 4
Heat_tshift = 12
Ref_tshift = 2
Wash_tshift = 6





dict_countries = {"AT": "Austria",
                "BE": "Belgium", "BG": "Bulgaria",
                "CH": "Switzerland", 
                "CZ": "CzechR", "DE": "Germany",
                "DK": "Denmark", "EE": "Estonia", 
                "ES": "Spain", "FI": "Finland",
                "FR": "France", "UK": "GreatBrit.",
                "EL": "Greece", "HR": "Croatia", 
                "HU": "Hungary", "IE": "Ireland", 
                "IT": "Italy", "LT": "Lithuania",
                "LU": "Luxemb.", "LV": "Latvia",
                "NL": "Netherlands","PL": "Poland",
                "PT": "Portugal","RO": "Romania", 
                "SE": "Sweden","SI": "Slovenia",
                "SK": "Slovakia","NO": "NO2"}

c_n = country_name + '.xlsx'

Nodes = country_name

for key in dict_countries:
    if  Nodes == key:
        Nodes = dict_countries[key]
    else:
        pass
    



def file_reader(filepath,excel,sheet):
    input_sheet = pd.read_excel(filepath + "/" + excel, sheet)
    return input_sheet

def sheets(filepath,excel):
    sheet_names = {'sheet_SH' : "Reduction_SpaceHeater",    'sheet_SH1' : "Dispatch_SpaceHeater",
                   'sheet_WH' : "Reduction_WaterHeater",    'sheet_WH1' : "Dispatch_WaterHeater",
                   'sheet_Dr' : "Reduction_Dryer",          'sheet_Dr1' : "Dispatch_Dryer",
                   'sheet_Di' : "Reduction_DishWasher",     'sheet_Di1' : "Dispatch_DishWasher",
                   'sheet_Wa' : "Reduction_WashingMachine", 'sheet_Wa1' : "Dispatch_WashingMachine",
                   'sheet_ev' : "Reduction_ElectricVehicle",'sheet_ev1' : "Dispatch_ElectricVehicle",
                   'sheet_ac' : "Reduction_AirConditioning",'sheet_ac1' : "Dispatch_AirConditioning",
                   'sheet_rf' : "Reduction_Refrigeration",  'sheet_rf1' : "Dispatch_Refrigeration"}

    sheet_values = {}


    for key in sheet_names:
        x=file_reader(filepath,excel,sheet_names[key])
        sheet_values[key]=x.iloc[:,1:] 
        
    return sheet_values

sheet_values = sheets(filepath,c_n)    #A dictionary from all sheets

agg_sheets = {}

agg_sheets['EV_Red']= sheet_values['sheet_ev']
agg_sheets['EV_Dis']= sheet_values['sheet_ev1']

agg_sheets['Wash_Red']= sheet_values['sheet_Dr']+sheet_values['sheet_Di']+sheet_values['sheet_Wa']
agg_sheets['Wash_Dis']= sheet_values['sheet_Dr1']+sheet_values['sheet_Di1']+sheet_values['sheet_Wa1']

agg_sheets['Heat_Red']= sheet_values['sheet_SH']+sheet_values['sheet_WH']
agg_sheets['Heat_Dis']= sheet_values['sheet_SH1']+sheet_values['sheet_WH1']

agg_sheets['Ref_Red']= sheet_values['sheet_rf']
agg_sheets['Ref_Dis']= sheet_values['sheet_rf1']

agg_sheets['AC_Red']= sheet_values['sheet_ac']
agg_sheets['AC_Dis']= sheet_values['sheet_ac1']


def coll(agg_sheets):  #Seperating columns to get each long_term period
    agg_sheets_period = {}
    for key in agg_sheets:
        h={}
        for col in agg_sheets[key].columns:
            data_table = agg_sheets[key].loc[:, col]
            data_table.index = np.arange(1, len(data_table) + 1)
            h[col] =  data_table.to_frame()
        agg_sheets_period[key] = h   
    return agg_sheets_period
        
 
agg_sheets_period = coll(agg_sheets)


def  expert_scenario(num):
    for i in range(1,13):
        if 1*i<= num <= 24*i:
            for n in [1,4,7,10]:    
                if i == n:        
                    return 'scenario1'
            for n in [2,5,8,11]: 
                if i == n:        
                    return 'scenario2'
            for n in [3,6,9,12]: 
                if i == n:        
                    return 'scenario3'
        else:
            pass


def rename_periods(h):
    x = {}
    for key in h:
        h[key]['Operationalhour'] = h[key].index
        h[key]['DemandResponseType'] = DemandResponseType
        h[key]['Nodes'] = Nodes
        if key == '2020':
            h[key]['Period'] = 1
            h[key].rename(columns={'2020': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        elif key == '2025':
            h[key]['Period'] = 2
            h[key].rename(columns={'2025': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        elif key == '2030':
            h[key]['Period'] = 3
            h[key].rename(columns={'2030': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        elif key == '2035':
            h[key]['Period'] = 4
            h[key].rename(columns={'2035': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        elif key == '2040':
            h[key]['Period'] = 5
            h[key].rename(columns={'2040': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        elif key == '2045':
            h[key]['Period'] = 6
            h[key].rename(columns={'2045': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        elif key == '2050':
            h[key]['Period'] = 7
            h[key].rename(columns={'2050': "BaselineDemand"},inplace = True)
            #h[key]['CumulativeFrequency'] = h[key]['BaselineDemand'].cumsum()
            h[key]['Nodes'] = Nodes
        else:
            pass
        
        h[key]['Scenario'] = h[key]['Operationalhour'].apply(expert_scenario)
        h[key] = h[key][['Nodes','DemandResponseType','Operationalhour','Period','Scenario','BaselineDemand']]
    
       
        
        x[key + 'scenario1']  = h[key][(h[key]['Scenario'] == 'scenario1')]
        x[key + 'scenario2']  = h[key][(h[key]['Scenario'] == 'scenario2')]
        x[key + 'scenario3']  = h[key][(h[key]['Scenario'] == 'scenario3')]
    
    g = {}
    for key in x:
        x[key].index = np.arange(1, len(x[key]) + 1)
        g[key+'_peak1'] = x[key].loc[49:72, :].copy()
        g[key+'_peak2'] = x[key].loc[49:72, :].copy()
        for i in range(1,8):
            g[key+'_wi_' + str(i)] = x[key].loc[0:24, :].copy()
            g[key+'_sp_' + str(i)] = x[key].loc[25:48, :].copy()
            g[key+'_su_' + str(i)] = x[key].loc[49:72, :].copy()
            g[key+'_fa_' + str(i)] = x[key].loc[73:96, :].copy()
    
    for key in g:
        if 'peak1' in key:    
            g[key]['CumulativeFrequency'] = g[key]['BaselineDemand'].cumsum()
            g[key]['season']= 'peak1'
        elif 'peak2' in key:    
            g[key]['CumulativeFrequency'] = g[key]['BaselineDemand'].cumsum()
            g[key]['season']= 'peak2'
        else:
            pass

    return g
    
    
for key in agg_sheets_period:
    DemandResponseType = key.split("_")[0]
    agg_sheets_period[key] = rename_periods(agg_sheets_period[key])
    












def seperator (g):
    sce = ['scenarios1','scenarios2', 'scenarios3']
    period = ['2020','2025','2030','2035','2040','2045','2050']
    seas = ['wi','sp','su','fa','peak1','peak2']
    nam = []
    for s in sce:
        for p in period:
            for e in seas:
                nam.append(s+'_'+p+'_'+e)
    
    for i in nam:
        globals()[i] = dict()   

                
    # scenarios1_2020_wi = {}
    # scenarios1_2020_sp = {}
    # scenarios1_2020_su = {}
    # scenarios1_2020_fa = {}
    # scenarios1_2020_peak1 = {}
    # scenarios1_2020_peak2 = {}
    
    # scenarios1_2025_wi = {}
    # scenarios1_2025_sp = {}
    # scenarios1_2025_su = {}
    # scenarios1_2025_fa = {}
    # scenarios1_2025_peak1 = {}
    # scenarios1_2025_peak2 = {}
    
    # scenarios1_2030_wi = {}
    # scenarios1_2030_sp = {}
    # scenarios1_2030_su = {}
    # scenarios1_2030_fa = {}
    # scenarios1_2030_peak1 = {}
    # scenarios1_2030_peak2 = {}
    
    # scenarios1_2035_wi = {}
    # scenarios1_2035_sp = {}
    # scenarios1_2035_su = {}
    # scenarios1_2035_fa = {}
    # scenarios1_2035_peak1 = {}
    # scenarios1_2035_peak2 = {}
    
    # scenarios1_2040_wi = {}
    # scenarios1_2040_sp = {}
    # scenarios1_2040_su = {}
    # scenarios1_2040_fa = {}
    # scenarios1_2040_peak1 = {}
    # scenarios1_2040_peak2 = {}
    
    # scenarios1_2045_wi = {}
    # scenarios1_2045_sp = {}
    # scenarios1_2045_su = {}
    # scenarios1_2045_fa = {}
    # scenarios1_2045_peak1 = {}
    # scenarios1_2045_peak2 = {}
    
    # scenarios1_2050_wi = {}
    # scenarios1_2050_sp = {}
    # scenarios1_2050_su = {}
    # scenarios1_2050_fa = {}
    # scenarios1_2050_peak1 = {}
    # scenarios1_2050_peak2 = {}
    
    
    
    
    # scenarios2_2020_wi = {}
    # scenarios2_2020_sp = {}
    # scenarios2_2020_su = {}
    # scenarios2_2020_fa = {}
    # scenarios2_2020_peak1 = {}
    # scenarios2_2020_peak2 = {}
    
    # scenarios2_2025_wi = {}
    # scenarios2_2025_sp = {}
    # scenarios2_2025_su = {}
    # scenarios2_2025_fa = {}
    # scenarios2_2025_peak1 = {}
    # scenarios2_2025_peak2 = {}
    
    # scenarios2_2030_wi = {}
    # scenarios2_2030_sp = {}
    # scenarios2_2030_su = {}
    # scenarios2_2030_fa = {}
    # scenarios2_2030_peak1 = {}
    # scenarios2_2030_peak2 = {}
    
    # scenarios2_2035_wi = {}
    # scenarios2_2035_sp = {}
    # scenarios2_2035_su = {}
    # scenarios2_2035_fa = {}
    # scenarios2_2035_peak1 = {}
    # scenarios2_2035_peak2 = {}
    
    # scenarios2_2040_wi = {}
    # scenarios2_2040_sp = {}
    # scenarios2_2040_su = {}
    # scenarios2_2040_fa = {}
    # scenarios2_2040_peak1 = {}
    # scenarios2_2040_peak2 = {}
    
    # scenarios2_2045_wi = {}
    # scenarios2_2045_sp = {}
    # scenarios2_2045_su = {}
    # scenarios2_2045_fa = {}
    # scenarios2_2045_peak1 = {}
    # scenarios2_2045_peak2 = {}
    
    # scenarios2_2050_wi = {}
    # scenarios2_2050_sp = {}
    # scenarios2_2050_su = {}
    # scenarios2_2050_fa = {}
    # scenarios2_2050_peak1 = {}
    # scenarios2_2050_peak2 = {}
    
    
    
    # scenarios3_2020_wi = {}
    # scenarios3_2020_sp = {}
    # scenarios3_2020_su = {}
    # scenarios3_2020_fa = {}
    # scenarios3_2020_peak1 = {}
    # scenarios3_2020_peak2 = {}
    
    # scenarios3_2025_wi = {}
    # scenarios3_2025_sp = {}
    # scenarios3_2025_su = {}
    # scenarios3_2025_fa = {}
    # scenarios3_2025_peak1 = {}
    # scenarios3_2025_peak2 = {}
    
    # scenarios3_2030_wi = {}
    # scenarios3_2030_sp = {}
    # scenarios3_2030_su = {}
    # scenarios3_2030_fa = {}
    # scenarios3_2030_peak1 = {}
    # scenarios3_2030_peak2 = {}
    
    # scenarios3_2035_wi = {}
    # scenarios3_2035_sp = {}
    # scenarios3_2035_su = {}
    # scenarios3_2035_fa = {}
    # scenarios3_2035_peak1 = {}
    # scenarios3_2035_peak2 = {}
    
    # scenarios3_2040_wi = {}
    # scenarios3_2040_sp = {}
    # scenarios3_2040_su = {}
    # scenarios3_2040_fa = {}
    # scenarios3_2040_peak1 = {}
    # scenarios3_2040_peak2 = {}
    
    # scenarios3_2045_wi = {}
    # scenarios3_2045_sp = {}
    # scenarios3_2045_su = {}
    # scenarios3_2045_fa = {}
    # scenarios3_2045_peak1 = {}
    # scenarios3_2045_peak2 = {}
    
    # scenarios3_2050_wi = {}
    # scenarios3_2050_sp = {}
    # scenarios3_2050_su = {}
    # scenarios3_2050_fa = {}
    # scenarios3_2050_peak1 = {}
    # scenarios3_2050_peak2 = {}
    
    
    for key in g:
        if '2020' in key:
            if 'scenario1' in key:
                if 'wi' in key:
                    scenarios1_2020_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2020_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2020_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2020_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2020_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2020_peak2[key] = g[key]
                    
                else:
                    pass
            elif 'scenario2' in key:
                if 'wi' in key:
                    scenarios2_2020_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2020_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2020_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2020_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2020_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2020_peak2[key] = g[key]
                    
                else:
                    pass
                
            elif 'scenario3' in key:
                if 'wi' in key:
                    scenarios3_2020_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2020_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2020_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2020_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2020_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2020_peak2[key] = g[key]
                    
                else:
                    pass
                
            else:
                pass
                
                
            
        elif '2025' in key:
            if 'scenario1' in key:
                
                if 'wi' in key:
                    scenarios1_2025_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2025_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2025_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2025_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2025_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2025_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario2' in key:
                
                if 'wi' in key:
                    scenarios2_2025_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2025_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2025_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2025_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2025_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2025_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario3' in key:
                
                if 'wi' in key:
                    scenarios3_2025_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2025_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2025_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2025_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2025_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2025_peak2[key] = g[key]
                else:
                    pass
            
            else:
                pass
    
        elif '2030' in key:
            if 'scenario1' in key:
                if 'wi' in key:
                    scenarios1_2030_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2030_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2030_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2030_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2030_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2030_peak2[key] = g[key]
                else:
                    pass
            elif 'scenario2' in key:
                if 'wi' in key:
                    scenarios2_2030_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2030_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2030_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2030_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2030_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2030_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario3' in key:
                if 'wi' in key:
                    scenarios3_2030_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2030_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2030_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2030_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2030_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2030_peak2[key] = g[key]
                else:
                    pass
                
            else:
                pass
     
        
        elif '2035' in key:
            if 'scenario1' in key:
                
                if 'wi' in key:
                    scenarios1_2035_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2035_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2035_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2035_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2035_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2035_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario2' in key:
                
                if 'wi' in key:
                    scenarios2_2035_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2035_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2035_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2035_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2035_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2035_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario3' in key:
                
                if 'wi' in key:
                    scenarios3_2035_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2035_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2035_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2035_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2035_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2035_peak2[key] = g[key]
                else:
                    pass
                
            else:
                pass
                
                
    
                
        
        elif '2040' in key:
            if 'scenario1' in key:
                if 'wi' in key:
                    scenarios1_2040_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2040_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2040_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2040_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2040_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2040_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario2' in key:
                if 'wi' in key:
                    scenarios2_2040_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2040_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2040_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2040_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2040_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2040_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario3' in key:
                if 'wi' in key:
                    scenarios3_2040_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2040_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2040_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2040_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2040_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2040_peak2[key] = g[key]
                else:
                    pass
                
            else:
                pass
     
        
        
        elif '2045' in key:
            if 'scenario1' in key:
                if 'wi' in key:
                    scenarios1_2045_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2045_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2045_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2045_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2045_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2045_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario2' in key:
                if 'wi' in key:
                    scenarios2_2045_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2045_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2045_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2045_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2045_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2045_peak2[key] = g[key]
                else:
                    pass
                
                
            elif 'scenario3' in key:
                if 'wi' in key:
                    scenarios3_2045_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2045_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2045_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2045_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2045_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2045_peak2[key] = g[key]
                else:
                    pass
                
            else:
                pass
                
                
    
                
        
        elif '2050' in key:
            if 'scenario1' in key:
                if 'wi' in key:
                    scenarios1_2050_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios1_2050_sp[key]= g[key]
                elif 'su' in key:
                    scenarios1_2050_su[key]= g[key]
                elif 'fa' in key:
                    scenarios1_2050_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios1_2050_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios1_2050_peak2[key] = g[key]
                else:
                    pass
            elif 'scenario2' in key:
                if 'wi' in key:
                    scenarios2_2050_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios2_2050_sp[key]= g[key]
                elif 'su' in key:
                    scenarios2_2050_su[key]= g[key]
                elif 'fa' in key:
                    scenarios2_2050_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios2_2050_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios2_2050_peak2[key] = g[key]
                else:
                    pass
                
            elif 'scenario3' in key:
                if 'wi' in key:
                    scenarios3_2050_wi[key]= g[key]
                elif 'sp' in key:
                    scenarios3_2050_sp[key]= g[key]
                elif 'su' in key:
                    scenarios3_2050_su[key]= g[key]
                elif 'fa' in key:
                    scenarios3_2050_fa[key]= g[key]
                elif 'peak1' in key:
                    scenarios3_2050_peak1[key] = g[key]
                elif 'peak2' in key:
                    scenarios3_2050_peak2[key] = g[key]
                else:
                    pass
                
            else:
                pass 
        else:
            pass
            
    




# scenarios_2020_wi = {}
# scenarios_2020_sp = {}
# scenarios_2020_su = {}
# scenarios_2020_fa = {}
# scenarios_2020_pe = {}

# scenarios_2025_wi = {}
# scenarios_2025_sp = {}
# scenarios_2025_su = {}
# scenarios_2025_fa = {}
# scenarios_2025_pe = {}

# scenarios_2030_wi = {}
# scenarios_2030_sp = {}
# scenarios_2030_su = {}
# scenarios_2030_fa = {}
# scenarios_2030_pe = {}

# scenarios_2035_wi = {}
# scenarios_2035_sp = {}
# scenarios_2035_su = {}
# scenarios_2035_fa = {}
# scenarios_2035_pe = {}

# scenarios_2040_wi = {}
# scenarios_2040_sp = {}
# scenarios_2040_su = {}
# scenarios_2040_fa = {}
# scenarios_2040_pe = {}

# scenarios_2045_wi = {}
# scenarios_2045_sp = {}
# scenarios_2045_su = {}
# scenarios_2045_fa = {}
# scenarios_2045_pe = {}

# scenarios_2050_wi = {}
# scenarios_2050_sp = {}
# scenarios_2050_su = {}
# scenarios_2050_fa = {}
# scenarios_2050_pe = {}



    sce1_2020_wi = pd.concat(scenarios1_2020_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2020_wi['Operationalhour'] = range(1,169)
    
    
    sce1_2020_sp = pd.concat(scenarios1_2020_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2020_sp['Operationalhour'] = range(1,169)
    
    sce1_2020_su = pd.concat(scenarios1_2020_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2020_su['Operationalhour'] = range(1,169)
    
    sce1_2020_fa = pd.concat(scenarios1_2020_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2020_fa['Operationalhour'] = range(1,169)
    
    sce1_2020_pe1 = pd.concat(scenarios1_2020_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2020_pe1['Operationalhour'] = range(1,25)
    
    sce1_2020_pe2 = pd.concat(scenarios1_2020_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2020_pe2['Operationalhour'] = range(1,25)
    
    
    sce2_2020_wi = pd.concat(scenarios2_2020_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2020_wi['Operationalhour'] = range(1,169)
    
    sce2_2020_sp = pd.concat(scenarios2_2020_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2020_sp['Operationalhour'] = range(1,169)
    
    sce2_2020_su = pd.concat(scenarios2_2020_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2020_su['Operationalhour'] = range(1,169)
    
    sce2_2020_fa = pd.concat(scenarios2_2020_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2020_fa['Operationalhour'] = range(1,169)
    
    
    sce2_2020_pe1 = pd.concat(scenarios2_2020_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2020_pe1['Operationalhour'] = range(1,25)
    
    sce2_2020_pe2 = pd.concat(scenarios2_2020_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2020_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    
    
    sce3_2020_wi = pd.concat(scenarios3_2020_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2020_wi['Operationalhour'] = range(1,169)
    
    sce3_2020_sp = pd.concat(scenarios3_2020_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2020_sp['Operationalhour'] = range(1,169)
    
    sce3_2020_su = pd.concat(scenarios3_2020_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2020_su['Operationalhour'] = range(1,169)
    
    sce3_2020_fa = pd.concat(scenarios3_2020_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2020_fa['Operationalhour'] = range(1,169)
    
    
    sce3_2020_pe1 = pd.concat(scenarios3_2020_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2020_pe1['Operationalhour'] = range(1,25)
    
    sce3_2020_pe2 = pd.concat(scenarios3_2020_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2020_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    sce1_2025_wi = pd.concat(scenarios1_2025_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2025_wi['Operationalhour'] = range(1,169)
    
    sce1_2025_sp = pd.concat(scenarios1_2025_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2025_sp['Operationalhour'] = range(1,169)
    
    sce1_2025_su = pd.concat(scenarios1_2025_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2025_su['Operationalhour'] = range(1,169)
    
    sce1_2025_fa = pd.concat(scenarios1_2025_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2025_fa['Operationalhour'] = range(1,169)
    
    sce1_2025_pe1 = pd.concat(scenarios1_2025_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2025_pe1['Operationalhour'] = range(1,25)
    
    sce1_2025_pe2 = pd.concat(scenarios1_2025_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2025_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    sce2_2025_wi = pd.concat(scenarios2_2025_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2025_wi['Operationalhour'] = range(1,169)
    
    sce2_2025_sp = pd.concat(scenarios2_2025_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2025_sp['Operationalhour'] = range(1,169)
    
    sce2_2025_su = pd.concat(scenarios2_2025_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2025_su['Operationalhour'] = range(1,169)
    
    sce2_2025_fa = pd.concat(scenarios2_2025_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2025_fa['Operationalhour'] = range(1,169)
    
    
    sce2_2025_pe1 = pd.concat(scenarios2_2025_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2025_pe1['Operationalhour'] = range(1,25)
    
    sce2_2025_pe2 = pd.concat(scenarios2_2025_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2025_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce3_2025_wi = pd.concat(scenarios3_2025_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2025_wi['Operationalhour'] = range(1,169)
    
    sce3_2025_sp = pd.concat(scenarios3_2025_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2025_sp['Operationalhour'] = range(1,169)
    
    sce3_2025_su = pd.concat(scenarios3_2025_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2025_su['Operationalhour'] = range(1,169)
    
    sce3_2025_fa = pd.concat(scenarios3_2025_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2025_fa['Operationalhour'] = range(1,169)
    
    sce3_2025_pe1 = pd.concat(scenarios3_2025_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2025_pe1['Operationalhour'] = range(1,25)
    
    sce3_2025_pe2 = pd.concat(scenarios3_2025_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2025_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    
    sce1_2030_wi = pd.concat(scenarios1_2030_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2030_wi['Operationalhour'] = range(1,169)
    
    sce1_2030_sp = pd.concat(scenarios1_2030_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2030_sp['Operationalhour'] = range(1,169)
    
    sce1_2030_su = pd.concat(scenarios1_2030_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2030_su['Operationalhour'] = range(1,169)
    
    sce1_2030_fa = pd.concat(scenarios1_2030_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2030_fa['Operationalhour'] = range(1,169)
    
    sce1_2030_pe1 = pd.concat(scenarios1_2030_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2030_pe1['Operationalhour'] = range(1,25)
    
    sce1_2030_pe2 = pd.concat(scenarios1_2030_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2030_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce2_2030_wi = pd.concat(scenarios2_2030_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2030_wi['Operationalhour'] = range(1,169)
    
    sce2_2030_sp = pd.concat(scenarios2_2030_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2030_sp['Operationalhour'] = range(1,169)
    
    sce2_2030_su = pd.concat(scenarios2_2030_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2030_su['Operationalhour'] = range(1,169)
    
    sce2_2030_fa = pd.concat(scenarios2_2030_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2030_fa['Operationalhour'] = range(1,169)
    
    
    sce2_2030_pe1 = pd.concat(scenarios2_2030_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2030_pe1['Operationalhour'] = range(1,25)
    
    sce2_2030_pe2 = pd.concat(scenarios2_2030_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2030_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce3_2030_wi = pd.concat(scenarios3_2030_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2030_wi['Operationalhour'] = range(1,169)
    
    sce3_2030_sp = pd.concat(scenarios3_2030_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2030_sp['Operationalhour'] = range(1,169)
    
    sce3_2030_su = pd.concat(scenarios3_2030_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2030_su['Operationalhour'] = range(1,169)
    
    sce3_2030_fa = pd.concat(scenarios3_2030_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2030_fa['Operationalhour'] = range(1,169)
    
    sce3_2030_pe1 = pd.concat(scenarios3_2030_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2030_pe1['Operationalhour'] = range(1,25)
    
    sce3_2030_pe2 = pd.concat(scenarios3_2030_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2030_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    
    
    
    sce1_2035_wi = pd.concat(scenarios1_2035_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2035_wi['Operationalhour'] = range(1,169)
    
    sce1_2035_sp = pd.concat(scenarios1_2035_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2035_sp['Operationalhour'] = range(1,169)
    
    sce1_2035_su = pd.concat(scenarios1_2035_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2035_su['Operationalhour'] = range(1,169)
    
    sce1_2035_fa = pd.concat(scenarios1_2035_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2035_fa['Operationalhour'] = range(1,169)
    
    sce1_2035_pe1 = pd.concat(scenarios1_2035_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2035_pe1['Operationalhour'] = range(1,25)
    
    sce1_2035_pe2 = pd.concat(scenarios1_2035_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2035_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce2_2035_wi = pd.concat(scenarios2_2035_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2035_wi['Operationalhour'] = range(1,169)
    
    sce2_2035_sp = pd.concat(scenarios2_2035_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2035_sp['Operationalhour'] = range(1,169)
    
    sce2_2035_su = pd.concat(scenarios2_2035_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2035_su['Operationalhour'] = range(1,169)
    
    sce2_2035_fa = pd.concat(scenarios2_2035_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2035_fa['Operationalhour'] = range(1,169)
    
    sce2_2035_pe1 = pd.concat(scenarios2_2035_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2035_pe1['Operationalhour'] = range(1,25)
    
    sce2_2035_pe2 = pd.concat(scenarios2_2035_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2035_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce3_2035_wi = pd.concat(scenarios3_2035_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2035_wi['Operationalhour'] = range(1,169)
    
    sce3_2035_sp = pd.concat(scenarios3_2035_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2035_sp['Operationalhour'] = range(1,169)
    
    sce3_2035_su = pd.concat(scenarios3_2035_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2035_su['Operationalhour'] = range(1,169)
    
    sce3_2035_fa = pd.concat(scenarios3_2035_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2035_fa['Operationalhour'] = range(1,169)
    
    sce3_2035_pe1 = pd.concat(scenarios3_2035_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2035_pe1['Operationalhour'] = range(1,25)
    
    sce3_2035_pe2 = pd.concat(scenarios3_2035_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2035_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    
    
    
    sce1_2040_wi = pd.concat(scenarios1_2040_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2040_wi['Operationalhour'] = range(1,169)
    
    sce1_2040_sp = pd.concat(scenarios1_2040_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2040_sp['Operationalhour'] = range(1,169)
    
    sce1_2040_su = pd.concat(scenarios1_2040_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2040_su['Operationalhour'] = range(1,169)
    
    sce1_2040_fa = pd.concat(scenarios1_2040_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2040_fa['Operationalhour'] = range(1,169)
    
    sce1_2040_pe1 = pd.concat(scenarios1_2040_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2040_pe1['Operationalhour'] = range(1,25)
    
    sce1_2040_pe2 = pd.concat(scenarios1_2040_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2040_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    sce2_2040_wi = pd.concat(scenarios2_2040_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2040_wi['Operationalhour'] = range(1,169)
    
    sce2_2040_sp = pd.concat(scenarios2_2040_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2040_sp['Operationalhour'] = range(1,169)
    
    sce2_2040_su = pd.concat(scenarios2_2040_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2040_su['Operationalhour'] = range(1,169)
    
    sce2_2040_fa = pd.concat(scenarios2_2040_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2040_fa['Operationalhour'] = range(1,169)
    
    sce2_2040_pe1 = pd.concat(scenarios2_2040_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2040_pe1['Operationalhour'] = range(1,25)
    
    sce2_2040_pe2 = pd.concat(scenarios2_2040_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2040_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce3_2040_wi = pd.concat(scenarios3_2040_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2040_wi['Operationalhour'] = range(1,169)
    
    sce3_2040_sp = pd.concat(scenarios3_2040_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2040_sp['Operationalhour'] = range(1,169)
    
    sce3_2040_su = pd.concat(scenarios3_2040_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2040_su['Operationalhour'] = range(1,169)
    
    sce3_2040_fa = pd.concat(scenarios3_2040_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2040_fa['Operationalhour'] = range(1,169)
    
    sce3_2040_pe1 = pd.concat(scenarios3_2040_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2040_pe1['Operationalhour'] = range(1,25)
    
    sce3_2040_pe2 = pd.concat(scenarios3_2040_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2040_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    
    
    
    sce1_2045_wi = pd.concat(scenarios1_2045_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2045_wi['Operationalhour'] = range(1,169)
    
    sce1_2045_sp = pd.concat(scenarios1_2045_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2045_sp['Operationalhour'] = range(1,169)
    
    sce1_2045_su = pd.concat(scenarios1_2045_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2045_su['Operationalhour'] = range(1,169)
    
    sce1_2045_fa = pd.concat(scenarios1_2045_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2045_fa['Operationalhour'] = range(1,169)
    
    sce1_2045_pe1 = pd.concat(scenarios1_2045_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2045_pe1['Operationalhour'] = range(1,25)
    
    sce1_2045_pe2 = pd.concat(scenarios1_2045_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2045_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce2_2045_wi = pd.concat(scenarios2_2045_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2045_wi['Operationalhour'] = range(1,169)
    
    sce2_2045_sp = pd.concat(scenarios2_2045_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2045_sp['Operationalhour'] = range(1,169)
    
    sce2_2045_su = pd.concat(scenarios2_2045_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2045_su['Operationalhour'] = range(1,169)
    
    sce2_2045_fa = pd.concat(scenarios2_2045_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2045_fa['Operationalhour'] = range(1,169)
    
    sce2_2045_pe1 = pd.concat(scenarios2_2045_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2045_pe1['Operationalhour'] = range(1,25)
    
    sce2_2045_pe2 = pd.concat(scenarios2_2045_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2045_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce3_2045_wi = pd.concat(scenarios3_2045_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2045_wi['Operationalhour'] = range(1,169)
    
    sce3_2045_sp = pd.concat(scenarios3_2045_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2045_sp['Operationalhour'] = range(1,169)
    
    sce3_2045_su = pd.concat(scenarios3_2045_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2045_su['Operationalhour'] = range(1,169)
    
    sce3_2045_fa = pd.concat(scenarios3_2045_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2045_fa['Operationalhour'] = range(1,169)
    
    sce3_2045_pe1 = pd.concat(scenarios3_2045_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2045_pe1['Operationalhour'] = range(1,25)
    
    sce3_2045_pe2 = pd.concat(scenarios3_2045_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2045_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    
    sce1_2050_wi = pd.concat(scenarios1_2050_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2050_wi['Operationalhour'] = range(1,169)
    
    sce1_2050_sp = pd.concat(scenarios1_2050_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2050_sp['Operationalhour'] = range(1,169)
    
    sce1_2050_su = pd.concat(scenarios1_2050_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2050_su['Operationalhour'] = range(1,169)
    
    sce1_2050_fa = pd.concat(scenarios1_2050_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2050_fa['Operationalhour'] = range(1,169)
    
    sce1_2050_pe1 = pd.concat(scenarios1_2050_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2050_pe1['Operationalhour'] = range(1,25)
    
    sce1_2050_pe2 = pd.concat(scenarios1_2050_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce1_2050_pe2['Operationalhour'] = range(1,25)
    
    
    
    
    sce2_2050_wi = pd.concat(scenarios2_2050_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2050_wi['Operationalhour'] = range(1,169)
    
    sce2_2050_sp = pd.concat(scenarios2_2050_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2050_sp['Operationalhour'] = range(1,169)
    
    sce2_2050_su = pd.concat(scenarios2_2050_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2050_su['Operationalhour'] = range(1,169)
    
    sce2_2050_fa = pd.concat(scenarios2_2050_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2050_fa['Operationalhour'] = range(1,169)
    
    sce2_2050_pe1 = pd.concat(scenarios2_2050_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2050_pe1['Operationalhour'] = range(1,25)
    
    sce2_2050_pe2 = pd.concat(scenarios2_2050_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce2_2050_pe2['Operationalhour'] = range(1,25)
    
    
    
    sce3_2050_wi = pd.concat(scenarios3_2050_wi).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2050_wi['Operationalhour'] = range(1,169)
    
    sce3_2050_sp = pd.concat(scenarios3_2050_sp).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2050_sp['Operationalhour'] = range(1,169)
    
    sce3_2050_su = pd.concat(scenarios3_2050_su).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2050_su['Operationalhour'] = range(1,169)
    
    sce3_2050_fa = pd.concat(scenarios3_2050_fa).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2050_fa['Operationalhour'] = range(1,169)
    
    sce3_2050_pe1 = pd.concat(scenarios3_2050_peak1).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2050_pe1['Operationalhour'] = range(1,25)
    
    sce3_2050_pe2 = pd.concat(scenarios3_2050_peak2).reset_index().drop(['level_0','level_1'],axis=1)
    sce3_2050_pe2['Operationalhour'] = range(1,25)
    Sto = {'sce1_2020_wi':sce1_2020_wi,'sce1_2020_sp':sce1_2020_sp,'sce1_2020_su':sce1_2020_su,'sce1_2020_fa':sce1_2020_fa,
          'sce2_2020_wi':sce2_2020_wi,'sce2_2020_sp':sce2_2020_sp,'sce2_2020_su':sce2_2020_su,'sce2_2020_fa':sce2_2020_fa,
          'sce3_2020_wi':sce3_2020_wi,'sce3_2020_sp':sce3_2020_sp,'sce3_2020_su':sce3_2020_su,'sce3_2020_fa':sce3_2020_fa,
          'sce1_2025_wi':sce1_2025_wi,'sce1_2025_sp':sce1_2025_sp,'sce1_2025_su':sce1_2025_su,'sce1_2025_fa':sce1_2025_fa,
          'sce2_2025_wi':sce2_2025_wi,'sce2_2025_sp':sce2_2025_sp,'sce2_2025_su':sce2_2025_su,'sce2_2025_fa':sce2_2025_fa,
          'sce3_2025_wi':sce3_2025_wi,'sce3_2025_sp':sce3_2025_sp,'sce3_2025_su':sce3_2025_su,'sce3_2025_fa':sce3_2025_fa,
          'sce1_2030_wi':sce1_2030_wi,'sce1_2030_sp':sce1_2030_sp,'sce1_2030_su':sce1_2030_su,'sce1_2030_fa':sce1_2030_fa,
          'sce2_2030_wi':sce2_2030_wi,'sce2_2030_sp':sce2_2030_sp,'sce2_2030_su':sce2_2030_su,'sce2_2030_fa':sce2_2030_fa,
          'sce3_2030_wi':sce3_2030_wi,'sce3_2030_sp':sce3_2030_sp,'sce3_2030_su':sce3_2030_su,'sce3_2030_fa':sce3_2030_fa,
          'sce1_2035_wi':sce1_2035_wi,'sce1_2035_sp':sce1_2035_sp,'sce1_2035_su':sce1_2035_su,'sce1_2035_fa':sce1_2035_fa,
          'sce2_2035_wi':sce2_2035_wi,'sce2_2035_sp':sce2_2035_sp,'sce2_2035_su':sce2_2035_su,'sce2_2035_fa':sce2_2035_fa,
          'sce3_2035_wi':sce3_2035_wi,'sce3_2035_sp':sce3_2035_sp,'sce3_2035_su':sce3_2035_su,'sce3_2035_fa':sce3_2035_fa,
          'sce1_2040_wi':sce1_2040_wi,'sce1_2040_sp':sce1_2040_sp,'sce1_2040_su':sce1_2040_su,'sce1_2040_fa':sce1_2040_fa,
          'sce2_2040_wi':sce2_2040_wi,'sce2_2040_sp':sce2_2040_sp,'sce2_2040_su':sce2_2040_su,'sce2_2040_fa':sce2_2040_fa,
          'sce3_2040_wi':sce3_2040_wi,'sce3_2040_sp':sce3_2040_sp,'sce3_2040_su':sce3_2040_su,'sce3_2040_fa':sce3_2040_fa,
          'sce1_2045_wi':sce1_2045_wi,'sce1_2045_sp':sce1_2045_sp,'sce1_2045_su':sce1_2045_su,'sce1_2045_fa':sce1_2045_fa,
          'sce2_2045_wi':sce2_2045_wi,'sce2_2045_sp':sce2_2045_sp,'sce2_2045_su':sce2_2045_su,'sce2_2045_fa':sce2_2045_fa,
          'sce3_2045_wi':sce3_2045_wi,'sce3_2045_sp':sce3_2045_sp,'sce3_2045_su':sce3_2045_su,'sce3_2045_fa':sce3_2045_fa,
          'sce1_2050_wi':sce1_2050_wi,'sce1_2050_sp':sce1_2050_sp,'sce1_2050_su':sce1_2050_su,'sce1_2050_fa':sce1_2050_fa,
          'sce2_2050_wi':sce2_2050_wi,'sce2_2050_sp':sce2_2050_sp,'sce2_2050_su':sce2_2050_su,'sce2_2050_fa':sce2_2050_fa,
          'sce3_2050_wi':sce3_2050_wi,'sce3_2050_sp':sce3_2050_sp,'sce3_2050_su':sce3_2050_su,'sce3_2050_fa':sce3_2050_fa}    
        





    for key in Sto:
        Sto[key]['CumulativeFrequency'] = Sto[key]['BaselineDemand'].cumsum()
        if 'wi' in key:
            Sto[key]['season'] = 'wi'
        elif 'sp' in key:
            Sto[key]['season'] = 'sp'
        elif 'su' in key:
            Sto[key]['season'] = 'su'
        elif 'fa' in key:
            Sto[key]['season'] = 'fa'
        else:
            pass


################################
###############################
#############################

    
    sce1_2020 = []
    sce2_2020 = []
    sce3_2020 = []
    
    sce1_2025 = []
    sce2_2025 = []
    sce3_2025 = []
    
    sce1_2030 = []
    sce2_2030 = []
    sce3_2030 = []
    
    sce1_2035 = []
    sce2_2035 = []
    sce3_2035 = []
    
    sce1_2040 = []
    sce2_2040 = []
    sce3_2040 = []
    
    sce1_2045 = []
    sce2_2045 = []
    sce3_2045 = []
    
    sce1_2050 = []
    sce2_2050 = []
    sce3_2050 = []
    
    sce = ['sce1','sce2','sce3']
    seasons = ['wi', 'sp','su','fa']
    
    for key in Sto:
        for s in sce:
            for se in seasons:
                if s in key:
                    if se in key:
                        if '2020' in key:
                            if s == 'sce1':
                                sce1_2020.append(Sto[key])
                            if s == 'sce2':
                                sce2_2020.append(Sto[key])
                            if s == 'sce3':
                                sce3_2020.append(Sto[key])
                                
                        elif '2025' in key:
                            if s == 'sce1':
                                sce1_2025.append(Sto[key])
                            if s == 'sce2':
                                sce2_2025.append(Sto[key])
                            if s == 'sce3':
                                sce3_2025.append(Sto[key])
                            
     
                        elif '2030' in key:
                            if s == 'sce1':
                                sce1_2030.append(Sto[key])
                            if s == 'sce2':
                                sce2_2030.append(Sto[key])
                            if s == 'sce3':
                                sce3_2030.append(Sto[key])
                            
    
                        elif '2035' in key:
                            if s == 'sce1':
                                sce1_2035.append(Sto[key])
                            if s == 'sce2':
                                sce2_2035.append(Sto[key])
                            if s == 'sce3':
                                sce3_2035.append(Sto[key])
                           
                        elif '2040' in key:
                            if s == 'sce1':
                                sce1_2040.append(Sto[key])
                            if s == 'sce2':
                                sce2_2040.append(Sto[key])
                            if s == 'sce3':
                                sce3_2040.append(Sto[key])
                        
                        elif '2045' in key:
                            if s == 'sce1':
                                sce1_2045.append(Sto[key])
                            if s == 'sce2':
                                sce2_2045.append(Sto[key])
                            if s == 'sce3':
                                sce3_2045.append(Sto[key])
    
                        elif '2050' in key:
                            if s == 'sce1':
                                sce1_2050.append(Sto[key])
                            if s == 'sce2':
                                sce2_2050.append(Sto[key])
                            if s == 'sce3':
                                sce3_2050.append(Sto[key])
                        else:
                            pass
                    else:
                        pass
                    
                else:
                    pass
                
    
    
    sce1_2020.append(sce1_2020_pe1)
    sce2_2020.append(sce2_2020_pe1)
    sce3_2020.append(sce3_2020_pe1)
    sce1_2025.append(sce1_2025_pe1)
    sce2_2025.append(sce2_2025_pe1)
    sce3_2025.append(sce3_2025_pe1)
    sce1_2030.append(sce1_2030_pe1)
    sce2_2030.append(sce2_2030_pe1)
    sce3_2030.append(sce3_2030_pe1)
    sce1_2035.append(sce1_2035_pe1)
    sce2_2035.append(sce2_2035_pe1)
    sce3_2035.append(sce3_2035_pe1)
    sce1_2040.append(sce1_2040_pe1)
    sce2_2040.append(sce2_2040_pe1)
    sce3_2040.append(sce3_2040_pe1)
    sce1_2045.append(sce1_2045_pe1)
    sce2_2045.append(sce2_2045_pe1)
    sce3_2045.append(sce3_2045_pe1)
    sce1_2050.append(sce1_2050_pe1)
    sce2_2050.append(sce2_2050_pe1)
    sce3_2050.append(sce3_2050_pe1)            
         
    sce1_2020.append(sce1_2020_pe2)
    sce2_2020.append(sce2_2020_pe2)
    sce3_2020.append(sce3_2020_pe2)
    sce1_2025.append(sce1_2025_pe2)
    sce2_2025.append(sce2_2025_pe2)
    sce3_2025.append(sce3_2025_pe2)
    sce1_2030.append(sce1_2030_pe2)
    sce2_2030.append(sce2_2030_pe2)
    sce3_2030.append(sce3_2030_pe2)
    sce1_2035.append(sce1_2035_pe2)
    sce2_2035.append(sce2_2035_pe2)
    sce3_2035.append(sce3_2035_pe2)
    sce1_2040.append(sce1_2040_pe2)
    sce2_2040.append(sce2_2040_pe2)
    sce3_2040.append(sce3_2040_pe2)
    sce1_2045.append(sce1_2045_pe2)
    sce2_2045.append(sce2_2045_pe2)
    sce3_2045.append(sce3_2045_pe2)
    sce1_2050.append(sce1_2050_pe2)
    sce2_2050.append(sce2_2050_pe2)
    sce3_2050.append(sce3_2050_pe2) 
    
    
    
    
    sto1_2020 = pd.concat(sce1_2020).reset_index().drop(['index'],axis=1)
    sto1_2020['Operationalhour'] = range(1,721)
    
    sto2_2020 = pd.concat(sce2_2020).reset_index().drop(['index'],axis=1)
    sto2_2020['Operationalhour'] = range(1,721)
    
    sto3_2020 = pd.concat(sce3_2020).reset_index().drop(['index'],axis=1)
    sto3_2020['Operationalhour'] = range(1,721)
    
    
    
    sto1_2025 = pd.concat(sce1_2025).reset_index().drop(['index'],axis=1)
    sto1_2025['Operationalhour'] = range(1,721)
    
    sto2_2025 = pd.concat(sce2_2025).reset_index().drop(['index'],axis=1)
    sto2_2025['Operationalhour'] = range(1,721)
    
    sto3_2025 = pd.concat(sce3_2025).reset_index().drop(['index'],axis=1)
    sto3_2025['Operationalhour'] = range(1,721)
    
 
    
    sto1_2030 = pd.concat(sce1_2030).reset_index().drop(['index'],axis=1)
    sto1_2030['Operationalhour'] = range(1,721)
    
    sto2_2030 = pd.concat(sce2_2030).reset_index().drop(['index'],axis=1)
    sto2_2030['Operationalhour'] = range(1,721)
    
    sto3_2030 = pd.concat(sce3_2030).reset_index().drop(['index'],axis=1)
    sto3_2030['Operationalhour'] = range(1,721)
    
    
    
    sto1_2035 = pd.concat(sce1_2035).reset_index().drop(['index'],axis=1)
    sto1_2035['Operationalhour'] = range(1,721)
    
    sto2_2035 = pd.concat(sce2_2035).reset_index().drop(['index'],axis=1)
    sto2_2035['Operationalhour'] = range(1,721)
    
    sto3_2035 = pd.concat(sce3_2035).reset_index().drop(['index'],axis=1)
    sto3_2035['Operationalhour'] = range(1,721)
    
    

    sto1_2040 = pd.concat(sce1_2040).reset_index().drop(['index'],axis=1)
    sto1_2040['Operationalhour'] = range(1,721)
    
    sto2_2040 = pd.concat(sce2_2040).reset_index().drop(['index'],axis=1)
    sto2_2040['Operationalhour'] = range(1,721)
    
    sto3_2040 = pd.concat(sce3_2040).reset_index().drop(['index'],axis=1)
    sto3_2040['Operationalhour'] = range(1,721)
    
    
    
    sto1_2045 = pd.concat(sce1_2045).reset_index().drop(['index'],axis=1)
    sto1_2045['Operationalhour'] = range(1,721)
    
    sto2_2045 = pd.concat(sce2_2045).reset_index().drop(['index'],axis=1)
    sto2_2045['Operationalhour'] = range(1,721)
    
    sto3_2045 = pd.concat(sce3_2045).reset_index().drop(['index'],axis=1)
    sto3_2045['Operationalhour'] = range(1,721)
    

    
    sto1_2050 = pd.concat(sce1_2050).reset_index().drop(['index'],axis=1)
    sto1_2050['Operationalhour'] = range(1,721)
    
    sto2_2050 = pd.concat(sce2_2050).reset_index().drop(['index'],axis=1)
    sto2_2050['Operationalhour'] = range(1,721)
    
    sto3_2050 = pd.concat(sce3_2050).reset_index().drop(['index'],axis=1)
    sto3_2050['Operationalhour'] = range(1,721)
    

    
    #####################################
    ######################################
    ########################################## The same as period 7
    sto1_2055 = pd.concat(sce1_2050).reset_index().drop(['index'],axis=1)
    sto1_2055['Operationalhour'] = range(1,721)
    sto1_2055['Period'] = 8
    
    sto2_2055 = pd.concat(sce2_2050).reset_index().drop(['index'],axis=1)
    sto2_2055['Operationalhour'] = range(1,721)
    sto2_2055['Period'] = 8
    
    sto3_2055 = pd.concat(sce3_2050).reset_index().drop(['index'],axis=1)
    sto3_2055['Operationalhour'] = range(1,721)
    sto3_2055['Period'] = 8
    
    ####################
    ############
    #########
    
    
    sto_app = pd.concat([sto1_2020,sto1_2025,sto1_2030,
                        sto1_2035, sto1_2040,sto1_2045,
                        sto1_2050, sto1_2055,
                        sto2_2020,sto2_2025, sto2_2030,
                        sto2_2035, sto2_2040,sto2_2045,
                        sto2_2050, sto2_2055,
                        sto3_2020,sto3_2025, sto3_2030,
                        sto3_2035, sto3_2040,sto3_2045,
                        sto3_2050, sto3_2055])
    return sto_app



for key in agg_sheets_period:
    agg_sheets_period[key] = seperator(agg_sheets_period[key])
    
shift = agg_sheets_period.copy()

def column_add(shift):
    for key in shift:
        shift[key]['maximum']=shift[key]['CumulativeFrequency']
        shift[key]['new_time']=0
        
    
    
    season = ['wi','sp','su','fa']
    period = [1,2,3,4,5,6,7,8]
    scenario= ['scenario1','scenario2','scenario3']
    
    
    
    for i in season:
        for b in period:
            for m in scenario:
                for key in shift:
                    y= (shift[key]['season'] == i)&(shift[key]['Period']==b)&(shift[key]['Scenario']==m)
                    shift[key]['new_time'][y] = list(range(1,169))
    
    
    
    
    Pea = ['peak1','peak2']
    for i in Pea:
        for b in period:
            for m in scenario:
                for key in shift:
                    y= (shift[key]['season'] == i)&(shift[key]['Period']==b)&(shift[key]['Scenario']==m)
                    shift[key]['new_time'][y] = list(range(1,25))
                
    
    # AC_tshift = 2
    # EV_tshift = 4
    # Heat_tshift = 12
    # Ref_tshift = 2
    # Wash_tshift = 6
    df = shift.copy()
    
    def intt (e,key):
        b = e
        bine = [0,e] 
        while e <168:
            e = e +b
            bine.append(e)

        listmax = []
        for i in bine:
            listmax.append('max'+str(i))
            df[key]['max'+str(i)] = np.where(df[key]['new_time'] == i, 1, 0)
 
        df[key]['max'] = 0
    
        for i in listmax:
            df[key]['max'] = df[key]['max'] + df[key][i]
        
        df[key] = df[key].drop(listmax,axis=1)
    

        en = []
        for count, value in enumerate(df[key]['maximum']):
            en.append((count, value))
            
        df[key]['en'] = en

        en1=[]
        for count, value in enumerate(df[key]['max']):
            en1.append((count, value))
        df[key]['en1']=en1
        df[key]['minimum'] = 0
        return df[key]
        
        
    for key in df:
        if 'AC' in key:
            e = AC_tshift
            df[key] = intt (e,key)
            
        elif 'EV' in key:
            e = EV_tshift
            df[key] = intt (e,key)
            
        elif 'Heat' in key:
            e = Heat_tshift
            df[key] = intt (e,key)
            
        elif 'Ref' in key:
            e = Ref_tshift
            df[key] = intt (e,key)
        
        elif 'Wash' in key:
            e = Wash_tshift
            df[key] = intt (e,key)
            
        else:
            pass


    df1=df.copy()
    return df1

df1 = column_add(shift)
df1 = df1.copy()

def max_min(df1):
    def slicing(key,e,s):
        for c, v in df1[key]['en'][df1[key]['season']==s]:
            for c1 ,v1 in df1[key]['en1'][df1[key]['season']==s]:
                if v1 == 1:
                    if c == c1:
                        r = list(range(c-(e-1),c+1))
                        for i in r:
                            df1[key].iloc[i,8] = v
                        b=list(range(c,c+(e+1)))
                        for i in b:
                            df1[key].iloc[i,13] = v
                    elif c != c1:
                        pass
                    else:
                        pass
                else:
                    pass
        return df1[key]
    
    # AC_tshift = 2
    # EV_tshift = 4
    # Heat_tshift = 12
    # Ref_tshift = 2
    # Wash_tshift = 6
    
    def seasonnnn(s):
        for key in df1:
            if 'AC' in key:
                e = AC_tshift
                df1[key] = slicing(key,e,s)
            elif 'EV' in key:
                e = EV_tshift
                df1[key] = slicing(key,e,s)
            elif 'Heat' in key:
                e = Heat_tshift
                df1[key] = slicing(key,e,s)
            elif 'Ref' in key:
                e = Ref_tshift
                df1[key] = slicing(key,e,s)
            elif 'Wash' in key:
                e = Wash_tshift
                df1[key] = slicing(key,e,s)
            else:
                pass

        return df1
    
    
    seasonnnn('wi')
    
    
    season1 = ['sp','su','fa', 'peak1','peak2']
    for key in df1:
        for i in season1:    
            df1[key]['minimum'][df1[key]['season']==i]=0
    
    seasonnnn('sp')
    
    
    season2 = ['su','fa', 'peak1','peak2']
    for key in df1:
        for i in season2:    
            df1[key]['minimum'][df1[key]['season']==i]=0
    
    
    seasonnnn('su')
    
    
    season3 = ['fa', 'peak1','peak2']
    for key in df1:
        for i in season3:    
            df1[key]['minimum'][df1[key]['season']==i]=0
    
    
    seasonnnn('fa')
    
    
    season4 = [ 'peak1','peak2']
    for key in df1:
        for i in season4:    
            df1[key]['minimum'][df1[key]['season']==i]=0
    
    
    seasonnnn('peak1')
    
    
    season5 = ['peak2']
    for key in df1:
        for i in season5:    
            df1[key]['minimum'][df1[key]['season']==i]=0
    
    for key in df1:
        df1[key].reset_index(drop=True, inplace=True)
    
    
    
    def slicingPeak2(key,e):
        for c, v in df1[key]['en'][df1[key]['season']=='peak2']:
            for c1 ,v1 in df1[key]['en1'][df1[key]['season']=='peak2']:
                if v1 == 1:
                    if c == c1:
                        
                        r = list(range(c-(e-1),c+1))
                        for i in r:
                          
                            df1[key].iloc[i,8] = v
                            
                        b=list(range(c,c+(e+1)))
                        
                        for i in b:
                            if int(i)<= 17279:
                                
                                h = df1[key].iloc[i,:].tolist()
                                if h.count('peak2')>0:
                                    
                                    df1[key].iloc[i,13] = v
                                else:
                                    pass
                            else:
                                pass
                
                    else:
                        pass
                else:
                    pass
        return df1[key]
    
    for key in df1:   
        if 'AC' in key:
            e = AC_tshift
            df1[key] = slicingPeak2(key,e)
        elif 'EV' in key:
            e = EV_tshift
            df1[key] = slicingPeak2(key,e)
        elif 'Heat' in key:
            e = Heat_tshift
            df1[key] = slicingPeak2(key,e)
        elif 'Ref' in key:
            e = Ref_tshift
            df1[key] = slicingPeak2(key,e)
        elif 'Wash' in key:
            e = Wash_tshift
            df1[key] = slicingPeak2(key,e)
        else:
            pass
            
    return df1

df1 = max_min(df1)


###################
###########
######
sce = ['scenario1','scenario2','scenario3']
seasons = ['wi', 'sp','su','fa','peak1','peak2']
period = [1,2,3,4,5,6,7,8]

mdis = {}

for key in df1:
    if 'Dis' in key:
        for s in sce:
            for e in seasons:
                for i in period:
                    filt = (df1[key]['season']==e)&(df1[key]['Scenario']==s)&(df1[key]['Period']==i)
                    df1[key].loc[filt,'max_dis']=df1[key].loc[filt,'BaselineDemand'].max()  
        df1[key]['ch_avai'] = df1[key]['BaselineDemand']/df1[key]['max_dis']
        mdis[key]=df1[key]['max_dis'].to_frame()
    else:
        pass


def availa(tech):
    df1[tech + '_Red']['max_dis']=df1[tech +'_Dis']['max_dis']
    df1[tech +'_Red']['dis_avai']=df1[tech +'_Red']['BaselineDemand']/df1[tech +'_Red']['max_dis']
    df1[tech +'_Red']['ch_avai'] = df1[tech +'_Dis']['ch_avai']
    return df1

tech = ['AC','EV','Heat','Ref','Wash']

for i in tech:
    availa(i)



df2=df1.copy()

for key in df2.copy():
    if 'Dis' in key:
        df2.pop(key)
    else:
        pass        


# for key in df2:
#     df2[key].drop(['BaselineDemand','season','new_time','max','en','en1'],axis=1, inplace= True)
for key in df2:
     df2[key].drop(['CumulativeFrequency','season','new_time','max','en','en1'],axis=1, inplace= True)

df_list = [ v for k,v in df2.items()] 

dff = pd.concat(df_list ,axis=0).reset_index(drop=True)


# DemandResponseDemand = dff.copy()
# DemandResponseDemand.rename(columns={ 'minimum': 'VolumetricDemand'}, inplace=True)
# DemandResponseDemand.drop(['CumulativeFrequency','maximum','ch_avai','dis_avai'],axis=1)
# DemandResponseDemand=DemandResponseDemand[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','VolumetricDemand']]

DemandResponseDemand = dff.copy()
DemandResponseDemand.rename(columns={ 'minimum': 'VolumetricDemand'}, inplace=True)
DemandResponseDemand.drop(['BaselineDemand','maximum','ch_avai','dis_avai'],axis=1)
DemandResponseDemand=DemandResponseDemand[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','VolumetricDemand']]

# DemandResponseMax = dff.copy()
# DemandResponseMax.rename(columns={ 'maximum': 'VolumetricDemand'}, inplace=True)
# DemandResponseMax.drop(['CumulativeFrequency','minimum','ch_avai','dis_avai'],axis=1)
# DemandResponseMax=DemandResponseMax[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','VolumetricDemand']]

DemandResponseMax = dff.copy()
DemandResponseMax.rename(columns={ 'maximum': 'VolumetricDemand'}, inplace=True)
DemandResponseMax.drop(['BaselineDemand','minimum','ch_avai','dis_avai'],axis=1)
DemandResponseMax=DemandResponseMax[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','VolumetricDemand']]

# DischargeAvailability = dff.copy()
# DischargeAvailability.rename(columns={ 'dis_avai':'Availability'}, inplace=True)
# DischargeAvailability.drop(['CumulativeFrequency','maximum','minimum','ch_avai'],axis=1)
# DischargeAvailability=DischargeAvailability[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','Availability']]

DischargeAvailability = dff.copy()
DischargeAvailability.rename(columns={ 'dis_avai':'Availability'}, inplace=True)
DischargeAvailability.drop(['BaselineDemand','maximum','minimum','ch_avai'],axis=1)
DischargeAvailability=DischargeAvailability[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','Availability']]

# ChargeAvailability = dff.copy()
# ChargeAvailability.rename(columns={ 'ch_avai':'Availability'}, inplace=True)
# ChargeAvailability.drop(['CumulativeFrequency','maximum','minimum','dis_avai'],axis=1)
# ChargeAvailability=ChargeAvailability[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','Availability']]

ChargeAvailability = dff.copy()
ChargeAvailability.rename(columns={ 'ch_avai':'Availability'}, inplace=True)
ChargeAvailability.drop(['BaselineDemand','maximum','minimum','dis_avai'],axis=1)
ChargeAvailability=ChargeAvailability[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','Availability']]

# Baseline = dff.copy()
# Baseline.rename(columns={ 'CumulativeFrequency':'BaselineDemand'}, inplace=True)
# Baseline.drop(['maximum','minimum','dis_avai','ch_avai'],axis=1)
# Baseline = Baseline[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','BaselineDemand']]

Baseline = dff.copy()
Baseline.drop(['maximum','minimum','dis_avai','ch_avai'],axis=1)
Baseline = Baseline[['Nodes','DemandResponseType','Operationalhour', 'Period', 'Scenario','BaselineDemand']]




result_file_path = filepath + '_' + country_name

if not os.path.exists(result_file_path):
        os.makedirs(result_file_path)

writer = pd.ExcelWriter(result_file_path + '/' +'DRModuleStochastic.xlsx', engine='xlsxwriter')

DemandResponseDemand.to_excel(writer, sheet_name='DemandResponseDemand', startrow = 2, index=False)
workbook  = writer.book
worksheet1 = writer.sheets['DemandResponseDemand']
text = 'Description: Minimum requirement of filled volumetric energy in DR type in specific hours, periods and scenarios'
worksheet1.write(1, 0, text)


DemandResponseMax.to_excel(writer, sheet_name='DemandResponseMax', startrow = 2, index=False)
workbook  = writer.book
worksheet2 = writer.sheets['DemandResponseMax']
text = 'Description: Maximum filled volumetric energy in DR type in specific hours, periods and scenarios'
worksheet2.write(1, 0, text)


DischargeAvailability.to_excel(writer, sheet_name='DischargeAvailability', startrow = 2, index=False)
workbook  = writer.book
worksheet3 = writer.sheets['DischargeAvailability']
text = 'Description: Availability for down-regulation as a share of installed regulation capacity by DR type in specific hours, periods and scenarios (default=1)'
worksheet3.write(1, 0, text)


ChargeAvailability.to_excel(writer, sheet_name='ChargeAvailability', startrow = 2, index=False)
workbook  = writer.book
worksheet4 = writer.sheets['ChargeAvailability']
text = 'Description: Availability for up-regulation as a share of installed regulation capacity by DR type in specific hours, periods and scenarios (default=1)'
worksheet4.write(1, 0, text)


Baseline.to_excel(writer, sheet_name='Baseline', startrow = 2, index=False)
workbook  = writer.book
worksheet5 = writer.sheets['Baseline']
text = 'Description: Energy consumed in any hour without any demand response (already part of the total demand in EMPIRE)'
worksheet5.write(1, 0, text)


writer.save()


season = ['wi','sp','su','fa']
period = [1,2,3,4,5,6,7,8]
scenario= ['scenario1','scenario2','scenario3']

InitialPowerCapacity = {}
for b in period:
    for key in df2:
        y= (df2[key]['Period']==b)
        InitialPowerCapacity[key+str(b)] = df2[key]['max_dis'][y].max()



EnergyInitialCapacity = {}
for b in period:
    for key in df2:
        y= (df2[key]['Period']==b)
        EnergyInitialCapacity[key+str(b)] = df2[key]['maximum'][y].max()

























