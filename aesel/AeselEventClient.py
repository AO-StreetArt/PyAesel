#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Apache2 License Notice
Copyright 2018 Alex Barry
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
Central Aesel UDP Client Definition.
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from aesel.model.AeselDataList import AeselDataList
from aesel.model.AeselObject import AeselObject
from aesel.model.AeselProperty import AeselProperty

import socket

class AeselEventClient(object):
    """The Main Client for generating Aesel Events"""
    def __init__(self, host, port, encryption_key=None, encryption_iv=None):
        """
        Initialize the Client.

        :param str host: The host to send the message to.
        :param port: The port to send the message to.
        :param str encryption_key: AES-256 encryption key to use for outgoing UDP messages.
        :param str encryption_iv: AES-256 encryption IV to use for outgoing UDP messages.
        """
        self.socket = None
        self.host = None
        self.port = None
        self.cipher = None
        self.encryption_active = False
        self.backend = default_backend()
        self.update_endpoint(host, port, encryption_key, encryption_iv)

    def update_endpoint(self, host, port, encryption_key=None, encryption_iv=None):
        """
        Update Client address & encryption credentials (key & salt).

        :param str host: The host to send the message to.
        :param port: The port to send the message to.
        :param str encryption_key: AES-256 encryption key to use for outgoing UDP messages.
        :param str encryption_iv: AES-256 encryption IV to use for outgoing UDP messages.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port
        if (encryption_key is not None and encryption_iv is not None):
            self.encryption_active = True
            self.cipher = Cipher(algorithms.AES(encryption_key), modes.CBC(encryption_iv), backend=self.backend)

    # Private method to send a general UDP message
    def _send_update(self, msg):
        if self.encryption_active:
            # Send an encrypted message
            encryptor = cipher.encryptor()
            encrypted = encryptor.update(bytes(msg, 'UTF-8')) + encryptor.finalize()
            self.socket.sendto(encrypted, (self.host, int(self.port)))
        else:
            # Send a plaintext message
            self.socket.sendto(bytes(msg, 'UTF-8'), (self.host, int(self.port)))

    def send_object_update(self, obj):
        """
        Send an outgoing Object Update message over UDP.

        :param obj: AeselObject to convert into an event.
        """
        self._send_update(obj.to_transform_json())

    def send_property_update(self, prop):
        """
        Send an outgoing Property Update message over UDP.

        :param prop: AeselProperty to convert into an event.
        """
        self._send_update(prop.to_transform_json())
