==========
pyw3mimg
==========

What's this?
------------
A python wrapper for the w3mimgdisplay

Requirements
------------
| python 2.5 or later
| w3mimgdisplay

How to Install?
---------------
setuptools
++++++++++
::

  $ python setup.py install (run as admin/root)


Usage
-----
::

  >>> import pyw3mimg
  >>> display = pyw3mimg.W3MImageDisplay('/usr/lib/w3m/w3mimgdisplay')
  >>> display.draw('/home/seikichi/icon.jpg', n=1, x=0, y=0)


Other
-----
| Author: seikichi
| License: MIT
| Mail: seikichi[at]kmc.gr.jp

