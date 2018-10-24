.. _quickstart:

Getting Started with Aesel
==========================

This tutorial assumes that you have successfully :ref:`Installed PyAesel <install>`,
and have a `running Aesel Server <https://aesel.readthedocs.io/en/latest/pages/quickstart.html>`__.

Reading through `the Aesel Workflow <https://aesel.readthedocs.io/en/latest/pages/overview.html>`__
and `the process for loading an Aesel Scene <https://aesel.readthedocs.io/en/latest/pages/loading.html>`__
is also recommended.

Please note that this is just intended as an overview of the functionality
presented, for full documentation please refer to :ref:`modindex`.

Using the Transaction Client
----------------------------

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
   new_key = http_client.create_asset("testupload.json", metadata)

In this case, a file in the base python directory called 'testupload.json' will
be sent in a multipart file upload, and the variable 'new_key' will be
populated with the string key of the asset in the Aesel server.  The same key
can then be used to retrieve the asset back out.

If the client is unable to connect, or receives a 400 or 500 HTTP Response from
the server, then it will throw an appropriate Exception.

Likewise, we can register to a Scene:

.. code-block:: python

   from aesel.model.AeselUserDevice import AeselUserDevice
   ud = AeselUserDevice()
   ud.key = "testDevice"
   ud.hostname = "localhost"
   ud.port = 8182
   ud.connection_string = "http://localhost:8182"
   register_resp = transaction_client.register("scene-key", ud)

In this case, the device will be registered to the specified scene, with the
address specified being the UDP address the device is listening on.  The response
will be a dictionary populated with the JSON information of the response from
the Aesel server.

Using the Event Client
----------------------

In the response of a Scene Registration, you will be presented with UDP information
(including IP/hostname, port, and encryption information) which can then be used
by the Event Client to send UDP updates for Objects and/or Properties.

.. code-block:: python

   from aesel.AeselEventClient import AeselEventClient
   event_client = AeselEventClient("localhost", 8762)

The same data model objects used in the Transaction Client are used by the Event
Client, for example, to send an object update:

.. code-block:: python

   from aesel.model.AeselObject import AeselObject
   obj = AeselObject()
   obj.key = "obj-key"
   obj.scene = "scene-key"
   obj.transform = [2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0]
   event_client.send_object_update(obj)

Security
--------

The Transaction Client accepts both HTTP and HTTPS locations, and is capable of
adding an authentication token via the 'set_auth_info' method:

.. code-block:: python

   http_client = AeselTransactionClient("http://localhost:8080")
   http_client.set_auth_info("auth-token")

After calling this method, all calls to the Aesel servers will include the
provided authentication token.

The Event client accepts AES-256-cbc encryption details as part of it's constructor
and the 'update_endpoint' method.  These are generally provided by the registration
response from the Aesel Server.

.. code-block:: python

   event_client = AeselEventClient("localhost", 8762, "encryption-key", "encryption-iv")

:ref:`Go Home <index>`
