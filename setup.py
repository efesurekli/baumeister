# -*- coding: utf-8 -*-
"""
===========
baumeister
===========

Bauhaus for your slides.

"""
import os
from setuptools import setup, find_packages

version = "1.0.0"

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), "r").read().strip()

long_description = "\n\n".join(
    [read(*paths) for paths in (("README.md",),
                                ("docs", "contributors.md"),
                                ("docs", "changes.md"))]
)
dev_require = ["Sphinx"]
dev_require += ["nose", "coverage", "pytest", "pytest-cov"]

setup(name="baumeister",
      version=version,
      description="Baumeister",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords="",  # FIXME: Add whatefer fits
      author="Baumeister Team",
      author_email="info@baumeister.ai",
      url="https://github.com/efesurekli/baumeister",
      license="GPLv3",
      packages=find_packages(exclude=["contrib", "docs", "test"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'opencv-python',
        'python-pptx'
      ],
      dependency_links=[],
      entry_points={
      },
      tests_require=dev_require,
      test_suite="nose.collector",
      extras_require={
          "dev": dev_require
      })
