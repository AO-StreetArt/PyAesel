#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A User is a single account in an Aesel server.

:key: The Unique Identifier of the user (generated by Aesel).
:username: The username provided to login.
:password: The password used to login.
:email: The email of the user.
:is_admin: Does the user have admin access?
:is_active: Is the user active in the system?
:favorite_projects: A list of project ID's which the user has marked as a favorite.
:favorite_scenes: A list of scene ID's which the user has marked as favorite.
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

class AeselApplicationUser(object):
    def __init__(self):
        self.key = None
        self.username = None
        self.password = None
        self.email = None
        self.isAdmin = False
        self.isActive = True
        self.favoriteProjects = []
        self.favoriteScenes = []

    def to_dict(self):
        return copy.deepcopy(vars(self))
