from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='pyw3mimg',
      version=version,
      description="a pyton wrapper of w3mimgdisplay",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python w3m-img',
      author='seikichi',
      author_email='seikichi@kmc.gr.jp',
      url='http://d.hatena.ne.jp/se-kichi',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
