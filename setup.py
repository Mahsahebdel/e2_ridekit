from setuptools import setup, find_packages

setup(
    name='e2ridekit_package',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'e2ridekit_package = e2ridekit_package.main:main'
        ]
    }
)