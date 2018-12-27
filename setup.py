from setuptools import setup, find_packages

setup(
    name='freezeable_dict',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.5',
    extras_require={
        'test': ['flake8'],
        'docs': [
            'numpydoc',
            'recommonmark',
            'sphinx',
        ]
    }
)
