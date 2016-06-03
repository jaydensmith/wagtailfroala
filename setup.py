import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-intelliscale',
    version='0.1.14',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django>=1.8,<1.10', 'wagtail>=1.4.2,<1.5.0', 'PyYAML>=3.11'],
    license='BSD License',
    description='Internal IntelliScale wagtail tools.',
    long_description=README,
    author='Jayden Smith',
    author_email='jayden@intelliscale.com.au',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 8.8',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
