"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    #
    # Inserte su código aquí
    #
    df.dropna(axis=0, inplace=True)
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace(',', '')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    df.fecha_de_beneficio = [i if i[1] == '/' or i[2] == '/' else f'{i[8:]}/{i[5:7]}/{i[0:4]}' for i in df.fecha_de_beneficio]
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio)
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.replace('-',' ')
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ')
    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.replace('-',' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ')
    df.drop_duplicates(inplace=True)
    return df

if __name__ == "__main__":
    print(clean_data())
