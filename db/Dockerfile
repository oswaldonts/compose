FROM mariadb:latest

ENV MARIADB_ROOT_PASSWORD dbrp
ENV MARIADB_USER dbu
ENV MARIADB_PASSWORD dbp
ENV MARIADB_DATABASE db

COPY create_users_table.sql /docker-entrypoint-initdb.d/

CMD ["mariadbd"]
