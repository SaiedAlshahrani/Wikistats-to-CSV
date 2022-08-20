import codecs
from setuptools import setup
from setuptools import find_packages


with codecs.open('README.md', 'r', 'utf8') as reader:
    long_description = reader.read()


setup(
    name = 'wikistats2csv',
    version = '0.1.1',
    license = 'MIT',
    author = 'Saied Alshahrani',
    author_email = 's3ed.fala7@gmail.com',
    packages = find_packages(),
    description='Wikistats-to-CSV downloads Wikipedia Statistics in CSV format for a given Wikipedia.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SaiedAlshahrani/Wikistats-to-CSV',
    keywords = ['wikipedia','statistics', 'wikimedia', 'csv'],
    install_requires = ['lxml==4.9.1', 'rich==12.5.1','pandas==1.4.3','selenium==3.141.0', 'geckodriver-autoinstaller==0.1.0'],
    entry_points = {'console_scripts':['wikistats2csv = wikistats2csv.wikistats2csv:main']},
    classifiers = ['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent']
    )
