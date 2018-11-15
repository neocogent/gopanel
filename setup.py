import setuptools, os
from distutils.core import setup

from gopanel import version

try:
   import pypandoc
   readme_md = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   readme_md = open('README.md').read()

datafiles = [('/etc/gopanel',['etc/site?.conf']),('/etc/nginx',['etc/gopanel.conf']),('/var/www/gopanel',['www/*']),
             ('/lib/systemd/system',['etc/gopanel.service'])]
   
setup(
    name='gopanel',
    packages=['gopanel'],
    version=version,
    author='neoCogent.com',
    author_email='info@neocogent.com',
    url='https://github.com/neocogent/gopanel',
    download_url='https://github.com/neocogent/gopanel/tarball/'+version,
    license='MIT',
    classifiers=[
    'Development Status :: 3 - Alpha',
    #'Development Status :: 4 - Beta',
    #'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Operating System :: POSIX :: Linux',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7'
    ],
    keywords='goaccess websocket analytics server',
    description='Simple Menu for Multi Site Web Analytics.',
    long_description=readme_md,
    scripts=['gopanel'],
    install_requires=[
        "flask >= 1.2.0"
    ],
    data_files=datafiles

)
