clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -rf {} \;i

run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate
	python manage.py migrate blog

migrations:
	python manage.py makemigrations
	python manage.py makemigrations blog

user:
	python manage.py createsuperuser

shell:
	python manage.py shell

staticfiles:
	python manage.py collectstatic
