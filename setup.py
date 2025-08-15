from setuptools import setup, find_packages

setup(
    name='sichere-passwort-generator',
    version='0.1',
    packages=find_packages(),
    description='Ein einfacher Passwort-Generator',
    author='Dein Name',
    author_email='dein.email@example.com',
    license='MIT',
    entry_points={
        'console_scripts': ['passwort-generator=main:__main__'],
    },
)