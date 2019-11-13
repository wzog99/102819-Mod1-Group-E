
def studio_list_year(df, year):
    df1_year = bom_df.loc[bom_df['year'] == year]
    df1_year['studio'].unique()
    studio_list = df1_year['studio'].unique()

    return studio_list

def studio_gross_year(df, year): 
    df = bom_df
    studio_list = studio_list_year(df, year)
    studio_dic = {} #this dictionary contains studio and 2018 domestic gross 
    #key = studio name
    #value = domestic_gross
    
    for studio in studio_list: 
    
        bom_df2017 = bom_df.loc[bom_df['year'] == year ]
        bom_df2017_WB = bom_df2017.loc[bom_df2017['studio'] == studio]
        bom_df2017_WB['domestic_gross'].sum()
        studio_gross_dic2017.update({studio : bom_df2017_WB['domestic_gross'].sum()
                             
                             })
                             


