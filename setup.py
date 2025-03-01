from setuptools import setup

setup(
    name='iterminal',
    version='1.0.0',
    py_modules=['iterminal'],
    entry_points={
        'console_scripts': [
            'iterminal=iterminal:main',
        ],
    },
)