import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'ghostwriter',
    version = '0.1.0',
    author = ['Ryan J. Price'],
    author_email = ['ryapric@gmail.com'],
    description = 'Short description',
    long_description = long_description,
    url = 'https://github.com/ryapric/ghostwriter',
    packages = setuptools.find_packages(),
    python_requires = '>= 3.6.*',
    install_requires = [
        'jinja2 >= 2.11.2',
        'pyyaml >= 5.3.1'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    entry_points = {
        'console_scripts': [
            'ghostwrite = ghostwriter.cli.main:main',
            'gw = ghostwriter.cli.main:main'
        ]
    },
    include_package_data = True
)
