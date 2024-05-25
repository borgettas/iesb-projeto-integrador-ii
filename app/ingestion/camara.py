from loguru import logger
from sqlalchemy import create_engine

import json
import pandas as pd
import re
import requests

BASE_ENDPOINT="https://dadosabertos.camara.leg.br/api/v2"
ANO=2022
TABLE_NAME_DEPUTADOS="deputados"
TABLE_NAME_DEPUTADOS_DESPESAS="despesas"

def normalize_dataframe_column_name(df):
    new_columns={}
    old_columns=df.columns.values.tolist()

    for column in old_columns:
        column_normalized = re.sub(r'([A-Z])', r'_\1', column)
        column_normalized = column_normalized.replace(' ', '_')
        column_normalized = column_normalized.replace(':', '_')
        column_normalized = column_normalized.replace('%', '_')
        column_normalized = column_normalized.replace('$', '_')
        column_normalized = column_normalized.replace('*', '_')
        column_normalized = column_normalized.replace('-', '_')
        column_normalized = column_normalized.replace(';', '_')
        column_normalized = column_normalized.replace('/', '_')
        column_normalized = column_normalized.replace('[', '_')
        column_normalized = column_normalized.replace(']', '_')
        column_normalized = column_normalized.lower()
        
        new_columns[column]=column_normalized


    df.rename(columns=new_columns, inplace=True)
    return df


def put_to_database(df, table_name, if_exists="append"):
    # Criando a engine para conexão
    engine = create_engine("postgresql://root:password@localhost/postgres")
    logger.info(f"Engine created!")

    # Salvando os dados no banco de dados
    df.to_sql(
        table_name
        , engine
        , index=False
        , if_exists=if_exists
    )
    # encerrando a engine
    engine.dispose()
    logger.info(f"Data save on \"{table_name}\"!")


def get_deputados(save_json=False):
    # requisitando os dados no endpoint da API
    response=requests.get(f"{BASE_ENDPOINT}/deputados?ordem=ASC&ordenarPor=nome").json()

    # caso exista os dados dos deputados
    if not response["dados"] == []:
        # criar um dataframe com as colunas normalizadas
        df=pd.DataFrame.from_dict(response["dados"], orient="columns")
        df=normalize_dataframe_column_name(df)

    # caso seja verdadeiro
    if save_json:
        # salvar os dados no diretório atual em formato .json
        with open("response_deputados.json", "w") as file:
            json.dump(response , file)
    
    return df


def get_deputados_despesas(id_candidato, save_json=False):
    response=requests.get(f"{BASE_ENDPOINT}/deputados/{id_candidato}/despesas?ano={ANO}&ordem=ASC&ordenarPor=ano").json()
    df=None

    # caso exista os dados dos deputados
    if not response["dados"] == []:
        # criar um dataframe com as colunas normalizadas
        df=pd.DataFrame.from_dict(response["dados"], orient="columns")
        df=normalize_dataframe_column_name(df)

    # caso seja verdadeiro
    if save_json:
        # salvar os dados no diretório atual em formato .json
        with open("response_deputados_despesas.json", "w") as file:
            json.dump(response , file)

    return df


def main():
    # deputados
    deputados=get_deputados()
    put_to_database(deputados, TABLE_NAME_DEPUTADOS, if_exists="replace")

    # despesas
    ids_candidatos=deputados["id"].to_list()
    for id in ids_candidatos:
        deputados_despesas=get_deputados_despesas(id_candidato=id)

        if isinstance(deputados_despesas, pd.DataFrame) and not deputados_despesas.empty:
            put_to_database(deputados_despesas, TABLE_NAME_DEPUTADOS_DESPESAS)


main()

# print(ids_candidatos)