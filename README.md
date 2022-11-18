# Steps to initiate the project
# 1 Get the Virtual Environment running
    Within project folder: 
    pipenv shell    --> Enter Virtual Environment
    pipenv install  --> Install all dependencies

# 2 Get the database running 
 
    pipenv run init     --> Create a migration repository
    pipenv run migrate  --> Generate a migration
    pipenv run upgrade  --> Apply the changes described by the migration script to the database
# 3 Start the application server
    Within src folder:
    pipenv run start    --> Start the local server
