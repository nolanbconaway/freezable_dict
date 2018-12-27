from setuptools import setup, find_packages

long_description = '''
A `FreezableDict` is basically identical to a regular dict, but it offers the
additional possibility of freezing for use as a dictionary key, set item,
etc.

I stole most of the idea from https://stackoverflow.com/a/2704866 so props
to Mike (https://github.com/mikegraham).
'''

setup(
    name='freezable_dict',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/nolanbconaway/freezable_dict',
    author='Nolan Conaway',
    author_email='nolanbconaway@gmail.com',
    license='MIT',
    description='A freezable dictionary object.',
    keywords=['dictionary', 'mutability', 'immutable', 'mapping'],
    long_description=long_description,
    install_requires=[],
    python_requires='>=3.5',
    extras_require={
        'test': ['flake8']
    },
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
