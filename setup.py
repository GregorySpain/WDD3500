from setuptools import setup, find_packages

requires = [
    'flask',
]

setup(
    name='flask_first_app',
    version='0.0',
    description='My first Python web app built with Flask',
    author='Gregory Spain',
    author_email='spaing3850@clarkstate.edu',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)