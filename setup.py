from setuptools import setup

setup(
    name='domain',
    license='MIT',
    version='0.0.1',
    packages=[
        'domain',
        'domain.models',
        'domain.services',
        'domain.services.sql'
    ],
    install_requires=[
        'knot >= 0.3.0',
        'SQLAlchemy >= 0.9.7'
    ],
)
