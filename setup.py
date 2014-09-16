from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='sanneal',
    version='0.1.dev1',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'sanneal-demo = sanneal.sanneal_demo:main',
        ],
    },
    
    install_requires = [
        'docutils>=0.3',
        'pillow',
    ],
    
    package_data = {
        '': ['*.txt', '*.rst', 'LICENSE'],
    },
    
    author='Yakov Shklarov',
    author_email='yshklarov@gmail.com',
    description='An implementation of the simulated annealing algorithm',
    license='MIT',
    keywords='sanneal anneal simulated annealing optimization',
    url='https://github.com/yshklarov/sanneal',
)
