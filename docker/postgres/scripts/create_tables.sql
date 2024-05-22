CREATE TABLE if not exists postgres.deputados(
    id integer PRIMARY KEY
    , nome VARCHAR(100)
    , sigla_partido VARCHAR(100)
    , uri_partido VARCHAR(100)
    , sigla_uf VARCHAR(100)
    , id_legislatura VARCHAR(100)
    , url_foto VARCHAR(100)
    , email VARCHAR(100)
);