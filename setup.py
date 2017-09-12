from setuptools import setup

setup(name='ssdeep-windows',
      version='0.0.1',
      description='Python wrapper for the ssdeep library',
      author='Intezer Labs Ltd.',
      author_email='info@intezer.com',
      packages=['ssdeep'],
      zip_safe=False,
      package_data={'ssdeep': ['bin/*.*']})
