rm -R -f ./migrations &&
pipenv run init &&
psql -U juan -c 'DROP DATABASE template_juan;' || true &&
psql -U juan -c 'CREATE DATABASE template_juan;' &&
psql -U juan -c 'CREATE EXTENSION unaccent;' -d example &&
pipenv run migrate &&
pipenv run upgrade