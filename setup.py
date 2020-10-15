from setuptools import setup, find_packages

setup(name='ftPwrDrive',
      version='1.1',
      url='https://github.com/elektrofuzzis/ftPwrDrive',
      license='GNU',
      author='Bloeckchengrafik',
      author_email='bloeckchengrafik@gamesucht.net',
      description='Adds the FTPwrDrive functionality',
      packages=find_packages('ftpwrdrive'),
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires=['ftpwrdrive'],
      )
