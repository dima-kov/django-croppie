import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-croppie',
    version='1.3',
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    description='Application for easy croppie.js integration to django',
    author='Dima Kovalchuk',
    author_email='dima.kovalchuk.v@gmail.com',
    url='https://github.com/dima-kov/django-croppie',
    download_url='https://github.com/dima-kov/django-croppie/archive/v1.3.tar.gz',
    keywords=[
        'python', 'django', 'croppie', 'croppie.js',
        'image-processing', 'image-cropping',
    ],
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
