# Notas

* +5 Las instrucciones funcionan
* +5 El sistema funciona
* +4 Buen docker-compose. Separación BD-server, Dockerfile y reaprovechamiento de la imagen
y container de server para aprovisionamiento.
* +4 Migraciones con alembic
* +4 Covertura total de la spec
* +4 Serialización con marshmallow
* +2 ORM (SQLAlchemy) para migración y estructura
* +2 Estructura simple para una app simple 
* +1 variables de entorno config y docker-compose  
* +0 El postman tiene /age-gender-ts mal
* -1 Hubiese sido ideal que funcionase todo (includo inicialización de la BD) con 
un sólo ``docker-compose up``. Hay que correr 6 o 7 comandos.
* -1 ``/paystats`` devuelve realmente códigos postales
* -2 la estrucutra de URLs podría ser un poco mejor. Al menos usar resources a lo restful e incluir
un prefijo para api.
* -2 Las geometrías se sirven al FE en WKB y no en GEOJson 
* -3 Necesitó más tiempo del otorgado