"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='circuitpython-neotrellism4',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='Use Adafruit TrellisM4 Express board as 2 Neotrellis board. You can you use this to extend TrellisM4 with Neotrellis (seesaw) boards.',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='https://github.com/arofarn/NeoTrellisM4',

    # Author details
    author='arofarn',
    author_email='arofarn@arofarn.info',

    install_requires=[
        'Adafruit-Blinka',
        'adafruit-circuitpython-busdevice',
        'Adafruit_CircuitPython_NeoPixel',
        'adafruit_seesaw',
        'Adafruit_CircuitPython_MatrixKeypad',
        'Adafruit_CircuitPython_NeoTrellis',
    ],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='adafruit blinka circuitpython micropython neotrellism4 neotrellis trellisM4',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # TODO: IF LIBRARY FILES ARE A PACKAGE FOLDER,
    #       CHANGE `py_modules=['...']` TO `packages=['...']`
    py_modules=['neotrellism4'],
)
