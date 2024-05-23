CREATE TABLE if not exists public.deputados(
    id INTEGER PRIMARY KEY
    , nome VARCHAR(100)
    , sigla_partido VARCHAR(100)
    , uri_partido VARCHAR(100)
    , sigla_uf VARCHAR(100)
    , id_legislatura VARCHAR(100)
    , url_foto VARCHAR(100)
    , email VARCHAR(100)
)

CREATE TABLE IF NOT EXISTS public.despesas(
    id SERIAL PRIMARY KEY
    , ano INTEGER
    , mes INTEGER
    , tipo_despesa VARCHAR(100)
    , cod_documento INTEGER
    , tipo_documento VARCHAR(100)
    , cod_tipo_documento BIGINT
    , data_documento DATE
    , num_documento VARCHAR(300)
    , valor_documento FLOAT
    , url_documento VARCHAR(300)
    , nome_fornecedor VARCHAR(100)
    , cnpj_cpf_fornecedor BIGINT
    , valor_liquido FLOAT
    , valor_glosa FLOAT
    , num_ressarcimento VARCHAR(100)
    , cod_lote BIGINT
    , parcela INTEGER
)