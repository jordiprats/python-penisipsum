import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
  name = 'penisipsum',
  packages = ['penisipsum'], # this must be the same as the name above
  version = '2020.7.2',
  author = 'Jordi Prats',
  author_email = 'jprats@systemadmin.es',
  description = 'penis ipsum',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url = 'https://github.com/jordiprats/python-penisipsum',
  classifiers = [
    "Operating System :: OS Independent",
  ],
)
