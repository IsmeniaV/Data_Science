#improtar pandas
from cmath import nan
from numpy import NaN
import pandas as pd

#importar datos a usar del csv
df = pd.read_csv("properatti.csv"
           , encoding = 'latin1')

print(df.index)

#saber nombre columnas para renombrar
print(df.columns)

#renombrar columnas
df.columns = ["nº","operacionAviso","tipoPropiedad","lugar","lugarYpadres","pais","estado","geonombres","lat_lon","lat","lon","precioOriginal","monedaOriginal","precioMonedLocal","precioAproxUSD","supM2","supCubM2","precioUSDM2","precioM2","piso","hab","gastos","urlProp","descripcion","titulo","foto"]
print(df)

#resultado: [121220 rows x 26 columns]

#mostrar una vivienda con todas las columnas (ejemplo)
#print(df.iloc[10])

#ME FALTA SABER QUÉ ES EL VALOR GEONOMBRES!!!!!! -------------------------------------------

#identificar suma de filas que tienen valores NaN
#print(df.isnull().sum())

#identificar suma de columnas que tienen valores NaN
#print(df.columns[df.isnull().any()])

#df["tipoPropiedad"] = df["tipoPropiedad"].map(str.lower)

print(df["lat"].isnull().sum())

mediaLat=(df["lat"].mean())
print(mediaLat)

print(df["lat"])

df.replace(NaN,mediaLat)
print(df["lat"].isnull().sum())

#no funciona : --------------------------
# df.replace({df["lugar"]:"CÃ³rdoba"},"cordoba")
#print(df["gastos"].describe())

# ver QUANTILES de una columna:
#print(df["lugar"].describe())
# ver TOTALES de una columna:
#print(df["pais"].value_counts())


#no funciona:
# col = df["piso"]
# col[df.abs(col) > 3000.000000]

#print(df["lugar"].value_counts())
#print(df["lugar"].unique(),type=str)

#df["lugar"] = df["lugar"].map(str.lower)
#df.replace({df["lugar"]:"CÃ³rdoba"},"cordoba")
#print(df["lugar"].value_counts())


# media de "hab"
#mediahab=df["hab"].mean()
#print(mediahab)

#sustituir valor NaN por mean
#df["hab"].replace(NaN,"3574442.317893135")

#print(df["hab"])

#df["hab"].replace(df["hab"]>10,mediahab)