# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="API de Gestion des Cours en Ligne - OpenAPI 3.0",
    author_email="support@exemple.com",
    url="",
    keywords=["Swagger", "API de Gestion des Cours en Ligne - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Ceci est une API permettant de gérer le contenu des cours en ligne. Elle expose des fonctionnalités pour créer, consulter, mettre à jour, et supprimer des cours et leurs séances. 
    """
)
