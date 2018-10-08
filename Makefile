.PHONY: coverage test list docs prebuild build

coverage:
	green -vvv --quiet-coverage
	coverage html

test:
	pytest -vvv test

lint:
	pylint  *.py src/baumeister/*.py test/*.py

docs:
	python setup.py build_sphinx

prebuild:
	mv id_rsa /root/.ssh/id_rsa
	chmod 0600 /root/.ssh/id_rsa
	pip3 install -r requirements.txt
	rm /root/.ssh/id_rsa

build:
	apt-get update
	apt-get install -y --allow-unauthenticated default-jre
	apt-get autoclean
	apt-get clean
	rm -rf /var/lib/apt/lists/* /usr/share/doc/* /tmp/*
	python3 setup.py install