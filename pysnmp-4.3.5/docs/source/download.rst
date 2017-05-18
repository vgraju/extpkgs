Download PySNMP
===============

.. toctree::
   :maxdepth: 2

The PySNMP software is provided under terms and conditions of BSD-style 
license, and can be freely downloaded from Source Forge
`download servers <http://sourceforge.net/projects/pysnmp/files/>`_ or 
`PyPI <http://pypi.python.org/pypi/pysnmp/>`_. 

Besides official releases, it's advisable to try the cutting-edge
development code that could be taken from PySNMP
`source code repository <https://github.com/etingof/pysnmp>`_.
It may be less stable in regards to general operation and changes to
public interfaces, but it's first to contain fixes to recently discovered bugs.

The best way to obtain PySNMP and dependencies is to run:

.. code-block:: bash

   $ pip install pysnmp

or

.. code-block:: bash

   $ easy_install pysnmp

In case you do not have the easy_install command on your system but still 
would like to use the on-line package installation method, please install 
`setuptools <http://pypi.python.org/pypi/setuptools>`_ package by 
downloading and running `ez_setup.pz <https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py>`_ bootstrap:

.. code-block:: bash

   # wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py 
   # python ez_setup.py

In case you are installing PySNMP on an off-line system, the following 
packages need to be downloaded and installed for PySNMP to become 
operational:

* `PyASN1 <https://pypi.python.org/pypi/pyasn1>`_,
  used for handling ASN.1 objects
* `PySNMP <https://pypi.python.org/pypi/pysnmp/>`_,
  SNMP engine implementation

Optional, but recommended:

* `PyCryptodome <https://pypi.python.org/pypi/pycryptodome/>`_,
  used by SNMPv3 crypto features (Windows users need 
  `precompiled version <http://www.voidspace.org.uk/python/modules.shtml>`_)
* `PySMI <https://pypi.python.org/pypi/pysmi/>`_ for automatic
  MIB download and compilation. That helps visualizing more SNMP objects
* `Ply <https://pypi.python.org/pypi/ply/>`_, parser generator
  required by PySMI

The installation procedure for all the above packages is as follows 
(on UNIX-based systems):

.. code-block:: bash

   $ tar zxf package-X.X.X.tar.gz 
   $ cd package-X.X.X 
   # python setup.py install 
   # cd .. 
   # rm -rf package-X.X.X

In case of any issues, please `let us know <http://pysnmp.sourceforge.net/contact.html>`_ so we could try to help out.


