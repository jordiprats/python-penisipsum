from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'penisipsum',
  packages = ['penisipsum'], # this must be the same as the name above
  version = '2019.06',
  description = 'penis ipsum',
  long_description=long_description,
  author = 'Jordi Prats',
  author_email = 'jprats@systemadmin.es',
  url = 'https://github.com/jordiprats/python-penisipsum', # use the URL to the github repo
  download_url = 'https://github.com/jordiprats/python-penisipsum/archive/2018.02.tar.gz', # I'll explain this in a second
  keywords = ['penis', 'ipsum', 'textgenerator', 'sample'], # arbitrary keywords
  classifiers = [],
)

