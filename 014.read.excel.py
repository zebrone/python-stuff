import pandas
df = pandas.read_excel('f:/test.xlsx')
#print the column names
print (df.columns)
#get the values for a given column
values = df['Arm_id'].values
#get a data frame with selected columns
FORMAT = ['colonna_1', 'colonna_2', 'colonna_3']
df_selected = df[FORMAT]

 