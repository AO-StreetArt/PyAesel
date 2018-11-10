#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Asset Metadata is stored as part of an Asset, and can be queried separately.
"""

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

import copy

class AeselAssetMetadata(object):
    def __init__(self):
        self.content_type = None #: The HTTP Content Type to store instead of multipart
        self.file_type = None #: The File Extension of the uploaded file
        self.asset_type = None #: The type of asset

    def to_dict(self):
        return copy.deepcopy(vars(self))
