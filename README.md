# django-search-app

net stop winnat
docker-compose up
net start winnat


# to fixed the "django.db.utils.ProgrammingError: operator class "gin_trgm_ops" does not exist for access method "gin" "
# we have to update the migration file inside the book component.
# add this before create the index
    migrations.RunSQL(
            [
                "CREATE EXTENSION IF NOT EXISTS pg_trgm;",
                "UPDATE pg_opclass SET opcdefault = true WHERE opcname='gin_trgm_ops';",
            ]
        ),
    
# after the update is done in the database, now we can create the index in the book table
        migrations.AddIndex(
            model_name="book",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["title"], name="NewGinIndex", opclasses=["gin_trgm_ops"]
            ),
        ),
        
       
# load json data into postgres database Usually you use django-admin.py to start a new project or application and manage.py to do the rest.

django-admin loaddata mydata.json
python manage.py loaddata mydata.json
