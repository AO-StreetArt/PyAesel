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

import copy
import json

class AeselProperty(object):
    """
    Data Model for Properties.
    """
    def __init__(self):
        self.key = None
        self.name = None
        self.parent = None
        self.asset_sub_id = None
        self.scene = None
        self.frame = None
        self.timestamp = None
        self.values = []

    def to_dict(self):
        return_dict = copy.deepcopy(vars(self))
        return_dict['values'] = []
        for val in self.values:
            val_dict = vars(val)
            return_dict['values'].append(val_dict)
        return return_dict

    def to_transform_json(self):
        msg_dict = {
                    "msg_type": 9,
                    "key":self.key,
                    "name":self.name,
                    "frame":self.frame,
                    "scene":self.scene,
                    "values": []
                    }
        for val in self.values:
            val_dict = vars(val)
            msg_dict['values'].append(val_dict)
        return json.dumps(msg_dict)
