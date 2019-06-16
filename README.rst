Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-circuitpython-neotrellism4/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/neotrellism4/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/arofarn/Circuitpython_CircuitPython_NeoTrellisM4.svg?branch=master
    :target: https://travis-ci.com/arofarn/Circuitpython_CircuitPython_NeoTrellisM4
    :alt: Build Status

Use Adafruit TrellisM4 Express board as 2 Neotrellis board. You can you use this to extend TrellisM4 with Neotrellis (seesaw) boards.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Adafruit Seesaw helper <https://github.com/adafruit/Adafruit_CircuitPython_seesaw>`_
* `Adafruit MatrixKeypad <https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad>`_
* `Neopixel <https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

To use Trellis as 2 Neotrellis (seesaw):
.. code-block:: python
    from neotrellism4 import NeoTrellisM4
    trellis_left = NeoTrellisM4()
    trellis_right = NeoTrellisM4(left_part=trellis_left)

To use TrellisM4 tilled with Neotrellis (seesaw):
.. code-block:: python
    from board import SCL, SDA
    import busio
    from adafruit_neotrellis.neotrellism4 import NeoTrellisM4
    from adafruit_neotrellis.neotrellis import NeoTrellis
    from adafruit_neotrellis.multitrellis import MultiTrellis
    I2C = busio.I2C(SCL, SDA)
    trellim4_left = NeoTrellisM4()
    trellim4_right = NeoTrellisM4(left_part=trellim4_left)
    trelli = [
        [trellim4_left, trellim4_right],
        [NeoTrellis(I2C, False, addr=0x2F), NeoTrellis(I2C, False, addr=0x2E)]
        ]
    trellis = MultiTrellis(trelli)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/arofarn/Circuitpython_CircuitPython_NeoTrellisM4/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix circuitpython-circuitpython-neotrellism4 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
