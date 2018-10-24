.. _quickstart:

Getting Started with Aesel
==========================

This tutorial assumes that you have successfully :ref:`Installed PyAesel <install>`,
and have a `running Aesel Server <https://aesel.readthedocs.io/en/latest/pages/quickstart.html>`__.

Please note that this is just intended as an overview of the functionality
presented, for full documentation please refer to :ref:`modindex`.

Using the Library
-----------------

The first object you will generally interact with is the AeselTransactionClient.
This is where we specify the Aesel address, which we'll have on localhost for
this tutorial.

.. code-block:: python

   from aesel.AeselTransactionClient import AeselTransactionClient
   http_client = AeselTransactionClient("http://localhost:8080")

The Transaction Client gives us access to the all of the
`HTTP Operations in the Aesel API <https://aesel.readthedocs.io/en/latest/pages/DVS_API.html>`__.
PyAesel also supplies some basic classes as a data model that is passed to the
client, for example creating an Asset with metadata can be accomplished by:

.. code-block:: python

   from aesel.model.AeselAssetMetadata import AeselAssetMetadata
   metadata = AeselAssetMetadata()
   metadata.file_type = "json"
   metadata.asset_type = "test"
   new_key = None
   try:
      new_key = http_client.create_asset("testupload.json", metadata)
   except Exception as e:
      print(e)

Security
--------



:ref:`Go Home <index>`
