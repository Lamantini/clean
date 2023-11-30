from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Clean your trash files',
      url='https://github.com/Lamantini/hometask/blob/master/sort.py',
      author='Rybchenko Anastasiia',
      author_email='lamantiniuso@gmail.com',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})