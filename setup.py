from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='bot',
      version=version,
      description="just a twitter bot",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='bot twitter paulla pycon.fr',
      author='paulla',
      author_email='',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "python-twitter",
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      bot = bot:main
      """,
      )
