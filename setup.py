from setuptools import setup, find_packages
import os

setup(
    name='library_management',
    version=version,
    description='library management system',
    author='Frappe',
    author_email='mk5086944@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
