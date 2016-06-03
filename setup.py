import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtailfroala',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django>=1.8,<1.10', 'wagtail>=1.5'],
    license='MIT License',
    description='Extends Wagtail to use the Froala WYSIWYG editor in RichTextField/RichTextBlock.',
    url='https://github.com/jaydensmith/wagtailfroala',
    long_description=README,
    author='Jayden Smith',
    author_email='jayden@intelliscale.com.au',
    classifiers=[],
)
