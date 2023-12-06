from setuptools import find_packages, setup

setup(
    name='random_variate_generator',
    packages = find_packages(include=['random_variate_generator']),
    version = '0.1.0',
    description = 'description',
    author = 'mromanelli6@gatech.edu',
    install_requires=['numpy','seaborn','matplotlib'],
    setup_requires=['wheel']
)