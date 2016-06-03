import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtailfroala',
    packages=['wagtailfroala'],
    version='0.2.3',
    author='Jayden Smith',
    author_email='jayden@intelliscale.com.au',
    include_package_data=True,
    install_requires=['Django>=1.8,<1.10', 'wagtail>=1.5.0'],
    license='MIT License',
    description='Extends Wagtail to use the Froala WYSIWYG editor in RichTextFields/RichTextBlocks.',
    url='https://github.com/jaydensmith/wagtailfroala',
    long_description=README,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
