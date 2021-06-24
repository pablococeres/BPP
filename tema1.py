import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table 

# Creo una lista con los meses para comprobar que están todos y usarlo en un nuevo df
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
"""Months of the year"""
#compruebo que no hay meses vacíos
def hayval(elmes):
    """Check if each month have data"""
    hayvalores = df[elmes].count()
    """Counts the number of values of each month"""
    try:
        if hayvalores != None:
            # en tipodato limpio el df de valores de texto   
            tipodato(elmes)
            """If each month have values then calls the function tipodato"""        
    except Exception as e: 
        print('Hay columnas vacías')

# limpio el df
def tipodato(mese):
    """Convert string or null values in integers for each month"""
    try:
        df[mese] = pd.to_numeric(df[mese], errors='coerce').fillna(0).astype('Int64')
        """Transform the values of the month column in integers"""
        # con calculos hago los calculos para un nuevo df
        calculos(mese)
        """Calls the next function to make the calculus"""
    except Exception as e: 
        print('No ha sido posible convertir la tabla a numeros')

# creo un df vacío donde colocar las sumas
df1 = pd.DataFrame(columns=['Gastos', 'Ingresos', 'Ahorro'], index = meses)
"""A DataFrame that is going to have the result of the calculus"""
def calculos(calmes):
    """Calculate the values for each month"""
    gasto = 0
    """Initialize the variable"""
    ingreso = 0
    """Initialize the variable"""
    for val in df[calmes].values:     
        if val <= 0:
            gasto = gasto + val
        else:
            ingreso = ingreso + val
    """Filter the values gasto ingreso and sum all the values for ahorro"""
    df1['Gastos'][calmes] = gasto
    df1['Ingresos'][calmes] = ingreso
    df1['Ahorro'][calmes] = df[calmes].sum()
    """Put the values in the DataFrame"""
    

# Hago un nuevo df para almacenar la info
df2 = pd.DataFrame(columns=['Resultado'], index=['Mes gasto máximo', 'Mes ahorro máximo', 'Media anual de gasto', 'Gasto total', 'Ingreso total'])    
"""Create a new DataFrame with the inform results"""
def informe():
    """Use the df1 DataFrame to extract the results we are looking for and write de df2 DataFrame"""
    informe.maxgasto = df1.loc[df1['Gastos'] == df1['Gastos'].min()].index[0]
    """Name of the month with more expense"""
    informe.maxahorro = df1.loc[df1['Ahorro'] == df1['Ahorro'].max()].index[0]
    """Name of the month of more savings"""
    informe.mediagasto = int(df1['Gastos'].mean())
    """Mean of the year expense"""
    informe.gastototal = df1['Gastos'].sum()
    """Year total expense"""
    informe.ingresototal = df1['Ingresos'].sum()
    """Year total income"""
    df2['Resultado']['Mes gasto máximo'] = informe.maxgasto
    df2['Resultado']['Mes ahorro máximo'] = informe.maxahorro
    df2['Resultado']['Media anual de gasto'] = informe.mediagasto
    df2['Resultado']['Gasto total'] = informe.gastototal
    df2['Resultado']['Ingreso total'] = informe.ingresototal
    """Asign the values to the df2 DataFrame"""
    #imprimir()

#def imprimir():
    # ax = plt.subplot(111, frame_on=False) # no visible frame
    # ax.xaxis.set_visible(False)  # hide the x axis
    # ax.yaxis.set_visible(False)  # hide the y axis
    # table(ax, df1)  # where df is your data frame
    # plt.savefig('tabla1.png', bbox_inches='tight')
    # plt.close
#     ax2 = plt.subplot(111, frame_on=False) # no visible frame
#     ax2.xaxis.set_visible(False)  # hide the x axis
#     ax2.yaxis.set_visible(False)  # hide the y axis
#     plt.savefig('tabla2.png', bbox_inches='tight')
#     plt.close 

"""Initialize reading the data and working month to month"""
try:
    df = pd.read_csv('finanzas2020.csv', sep='\s+')
    """Read the data from a .csv"""
    try:
        contador = 0
        """Initialize a counter"""
        for mes in df.columns:
            """Loop month for month"""
            # comparo los meses del archivo con los meses de la list
            if mes == meses[contador]:
                """Compare the month names to know if the data have all the months"""
                #con hayval compruebo que no hay mese vacíos
                hayval(mes)
                """Start the function to know if each month have data"""   
                contador += 1
            else:
                print('Falta la columna del mes: ', mes)        
    except:
        print('no hay 12 meses')
    # ejecuto el informe con los valores que pide en ejercicio
    informe() 
except:
    print('fichero no encontrado')

print(df1)
print(df2)

plt.title('Ingresos')
plt.xticks(rotation=50)
plt.bar(df1.index,df1["Ingresos"])
plt.gcf().subplots_adjust(bottom=0.20)
plt.savefig('IngresosAnuales.png')

#plt.show()