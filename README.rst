======
VoR12_
======

Copyright (c) 2015 Jeremie DECOCK (http://www.jdhp.org)


* Web site: http://www.jdhp.org/projects_en.html#vor12
* Online documentation: http://vor12.readthedocs.org
* Source code: https://github.com/volab/vor12
* Issue tracker: https://github.com/volab/vor12/issues
* VoR12 on PyPI: https://pypi.python.org/pypi/vor12


Description
===========

The VoR12 project is a mobile video camera.
It uses two `Dynamixel AX-12`_ actuators and the OpenCV_ computer vision
library for object tracking experiments.

|Photo 1|_

Note:

    This project is still in beta stage, so the API is not finalized yet.


Dependencies
============

-  Python 2.7
-  `OpenCV`_ (v2)
-  `PyAX-12`_
-  `NumPy`_

.. VoR12 is tested to work with Python 3.4 under Gnu/Linux Debian 8 and Windows
.. 7.
.. It should also work with Python 3.X under recent Gnu/Linux and Windows systems.
.. It hasn't been tested (yet) on MacOSX and BSD systems.
.. 
.. `Python-serial`_ is required to install VoR12.

.. note::

    If you use ``pip`` to install VoR12, PyAX-12 and Numpy will be
    automatically downloaded and installed (see the following install_
    section).

    OpenCV cannot be installed with ``pip``, thus you have to install it
    manually.


.. _install:

Installation
============

Gnu/Linux
---------

You can install, upgrade, uninstall VoR12 with these commands (in a
terminal)::

    pip install --pre vor12
    pip install --upgrade vor12
    pip uninstall vor12

Or, if you have downloaded the VoR12 source code::

    python3 setup.py install

.. There's also a package for Debian/Ubuntu::
.. 
..     sudo apt-get install vor12

Windows
-------

.. .. note::
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under Windows 7.
..     It should also work with recent Windows systems.

You can install, upgrade, uninstall VoR12 with these commands (in a
`command prompt`_)::

    py -m pip install --pre vor12
    py -m pip install --upgrade vor12
    py -m pip uninstall vor12

Or, if you have downloaded the VoR12 source code::

    py setup.py install

MacOSX
-------

.. .. note::
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under MacOSX 10.6 (*Snow Leopard*).
..     It should also work with recent MacOSX systems.

You can install, upgrade, uninstall VoR12 with these commands (in a
terminal)::

    pip install --pre vor12
    pip install --upgrade vor12
    pip uninstall vor12

Or, if you have downloaded the VoR12 source code::

    python3 setup.py install




Bug reports
===========

To search for bugs or report them, please use the VoR12 Bug Tracker at:

    https://github.com/volab/vor12/issues


License
=======

The ``VoR12`` library is provided under the terms and conditions of the
`MIT License <http://opensource.org/licenses/MIT>`__.


.. _VoR12: http://www.jdhp.org/projects_en.html
.. _PyAX-12: https://pypi.python.org/pypi/pyax12
.. _Dynamixel AX-12: http://support.robotis.com/en/product/dynamixel/ax_series/dxl_ax_actuator.htm
.. _OpenCV: http://opencv.org/
.. _NumPy: http://www.numpy.org/
.. _command prompt: https://en.wikipedia.org/wiki/Cmd.exe

.. |Photo 1| image:: http://download.tuxfamily.org/jdhp/image/small_vor12-2.jpeg
.. _Photo 1: http://download.tuxfamily.org/jdhp/image/vor12-2.jpeg
