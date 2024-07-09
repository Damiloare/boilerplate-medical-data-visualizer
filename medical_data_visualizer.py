import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df["overweight"] = np.where(df["weight"] / (df["height"] * df["height"]) * 10000 > 25,1,0)

# 3
df['cholesteral'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
# 4
def draw_cat_plot():
    # 5
    df_cat = df_cat = df.melt(id_vars = 'cardio',  value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                     value_name ='value')
    # 6
    df_cat = df_cat = pd.DataFrame({'total':df_cat.groupby(['cardio', 'variable'])['value'].value_counts()})\
                                     .rename(columns = {'cardio':'Cardio','variable':'Variable', 'value':'Value'})\
                                     .reset_index()
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = (df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))]
    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
