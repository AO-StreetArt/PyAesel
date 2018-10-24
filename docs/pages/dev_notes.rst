.. _devnotes:

Developer Notes
===============

This page contains a series of notes intended to be beneficial for any
contributors to the Python Aesel Client.

Running Tests
-------------

PyAesel tests require a running Aesel server on localhost, and can be run with:

.. code-block:: bash

   python -m pytest

Generating Pip Distributions
----------------------------

In order to generate a PIP distribution, you'll need a ~/.pypirc file with the
contents:

.. code-block:: bash

   [distutils]
   index-servers=pypi

   [pypi]
   username: username
   password: password

Then, the following commands will generate the distribution:

.. code-block:: bash

   pip install --user twine
   python setup.py sdist bdist_wheel
   twine register dist/python_aesel_client-0.1-py3-none-any.whl
   twine upload dist/*

:ref:`Go Home <index>`
