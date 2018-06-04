"""Build configuration """
from setuptools import setup, find_packages

setup(name='rock_paper_scissors',
      version='1.0',
      description='Small sample about how to test python code',
      author='Victor Cabello',
      author_email='vmeca87@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['connexion',
                        'waitress'],
      setup_requires=['nose>=1.0',
                      'nosexcover',
                      'mock'],
      test_suite='nose.collector',
      entry_points={
          'console_scripts': [
              'rock_paper_scissors_restapi = rock_paper_scissors.rest_api:main'
          ]
      }
     )
