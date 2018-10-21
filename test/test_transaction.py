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

import pytest

from aesel.model.AeselAssetMetadata import AeselAssetMetadata
from aesel.model.AeselAssetRelationship import AeselAssetRelationship
from aesel.model.AeselGraphHandle import AeselGraphHandle
from aesel.model.AeselObject import AeselObject
from aesel.model.AeselProperty import AeselProperty
from aesel.model.AeselPropertyValue import AeselPropertyValue
from aesel.model.AeselScene import AeselScene
from aesel.model.AeselSceneTransform import AeselSceneTransform
from aesel.model.AeselUserDevice import AeselUserDevice
from aesel.AeselTransactionClient import AeselTransactionClient

# Initial setup of Transaction client
@pytest.fixture
def transaction_client():
    return AeselTransactionClient("http://localhost:8080")

# Execute tests on the Scene API
def test_scene_api(transaction_client):
    print("Testing Scene API")
    # Create a Scene
    print("Create Scene")
    scn = AeselScene()
    scn.name = "test"
    scn.region = "US-MD"
    scn.latitude = 100.0
    scn.longitude = 100.0
    scn.tags = []
    scn.devices = []
    scn_crt_resp = None
    try:
        scn_crt_resp = transaction_client.create_scene("123", scn)
    except Exception as e:
        print(e)
        assert(False)
    print(scn_crt_resp)

    # Get the scene
    print("Get Scene")
    scn_get_resp = None
    try:
        scn_get_resp = transaction_client.get_scene("123")
    except Exception as e:
        print(e)
        assert(False)
    print(scn_get_resp)
    assert(len(scn_get_resp["scenes"]) > 0)

    # Update the scene
    print("Update Scene")
    scn_upd = AeselScene()
    scn_upd.region = "US-GA"
    scn_upd_resp = None
    try:
        scn_upd_resp = transaction_client.update_scene("123", scn_upd)
    except Exception as e:
        print(e)
        assert(False)
    print(scn_upd_resp)

    # Query for scenes
    print("Query Scenes")
    scn_query = AeselScene()
    scn_query.region = "US-GA"
    scn_query_resp = None
    try:
        scn_query_resp = transaction_client.scene_query(scn_query)
    except Exception as e:
        print(e)
        assert(False)
    print(scn_query_resp)
    assert(len(scn_query_resp["scenes"]) > 0)

    # Register a device to a Scene
    print("Scene Registration")
    ud = AeselUserDevice()
    ud.key = "testDevice"
    ud.hostname = "localhost"
    ud.port = 8080
    ud.connection_string = "http://localhost:8080"
    register_resp = None
    try:
        register_resp = transaction_client.register("123", ud)
    except Exception as e:
        print(e)
        assert(False)
    print(register_resp)
    assert(len(register_resp["scenes"]) > 0)

    # Synchronize a device transform
    print("Scene Synchronization")
    transform = AeselSceneTransform()
    transform.rotation = [0.0, 0.0, 0.0]
    transform.translation = [1.0, 1.0, 1.0]
    try:
        sync_resp = transaction_client.synchronize("123", "testDevice", transform)
    except Exception as e:
        print(e)
        assert(False)
    print(sync_resp)
    assert(len(sync_resp["scenes"]) > 0)

    # Deregister a device from a scene
    print("Scene Deregistration")
    deregister_resp = None
    try:
        deregister_resp = transaction_client.deregister("123", "testDevice")
    except Exception as e:
        print(e)
        assert(False)
    print(deregister_resp)

    # Delete the scene
    print("Delete Scene")
    delete_resp = None
    try:
        delete_resp = transaction_client.delete_scene("123")
    except Exception as e:
        print(e)
        assert(False)
    print(delete_resp)

# Execute tests on the Property API
def test_property_api(transaction_client):
    print("Testing Property API")
    # Save a base scene to store the properties in
    print("Create base scene")
    scn = AeselScene()
    scn.name = "testPropScene"
    scn.region = "US-MD"
    scn.latitude = 100.0
    scn.longitude = 100.0
    scn.tags = []
    scn.devices = []
    scn_crt_resp = None
    try:
        scn_crt_resp = transaction_client.create_scene("propTestScene", scn)
    except Exception as e:
        print(e)
        assert(False)
    print(scn_crt_resp)

    # Create a new Property
    print("Create Property")
    prop = AeselProperty()
    prop.name = "testProperty"
    prop.scene = "propTestScene"
    prop.frame = 0
    val = AeselPropertyValue()
    val.value = 100.0
    prop.values.append(val)
    prop_crt_resp = None
    try:
        prop_crt_resp = transaction_client.create_property("propTestScene", prop)
    except Exception as e:
        print(e)
        assert(False)
    print(prop_crt_resp)
    assert(len(prop_crt_resp["properties"]) > 0)
    assert(len(prop_crt_resp["properties"][0]["key"]) > 0)
    prop_key = prop_crt_resp["properties"][0]["key"]

    # Get the property
    print("Get Property")
    prop_get_resp = None
    try:
        prop_get_resp = transaction_client.get_property("propTestScene", prop_key)
    except Exception as e:
        print(e)
        assert(False)
    print(prop_get_resp)
    assert(len(prop_get_resp["properties"]) > 0)

    # Update an existing Property
    print("Update Property")
    prop_upd = AeselProperty()
    prop_upd.name = "testProperty2"
    prop_upd_resp = None
    try:
        prop_upd_resp = transaction_client.update_property("propTestScene", prop_key, prop_upd)
    except Exception as e:
        print(e)
        assert(False)
    print(prop_upd_resp)

    # Query for Properties
    print("Query Properties")
    prop_query = AeselProperty()
    prop_query.name = "testProperty2"
    prop_query_resp = None
    try:
        prop_query_resp = transaction_client.property_query("propTestScene", prop_query)
    except Exception as e:
        print(e)
        assert(False)
    print(prop_query_resp)
    assert(len(prop_query_resp["properties"]) > 0)

    # Delete a Property
    print("Delete Property")
    try:
        transaction_client.delete_property("propTestScene", prop_key)
    except Exception as e:
        print(e)
        assert(False)

# Execute tests on the Object API
def test_object_api(transaction_client):
    print("Testing Object API")
    # Save a base scene to store the objects in
    print("Create base scene")
    scn = AeselScene()
    scn.name = "test"
    scn.region = "US-MD"
    scn.latitude = 100.0
    scn.longitude = 100.0
    scn.tags = []
    scn.devices = []
    scn_crt_resp = None
    try:
        scn_crt_resp = transaction_client.create_scene("objTestScene", scn)
    except Exception as e:
        print(e)
        assert(False)
    print(scn_crt_resp)

    # Create a new Object
    print("Create Object")
    obj = AeselObject()
    obj.name = "testObject"
    obj.scene = "objTestScene"
    obj.type = "mesh"
    obj.subtype = "cube"
    obj.frame = 0
    obj.translation = [1, 1, 1]
    obj_crt_resp = None
    try:
        obj_crt_resp = transaction_client.create_object("objTestScene", obj)
    except Exception as e:
        print(e)
        assert(False)
    print(obj_crt_resp)
    assert(len(obj_crt_resp["objects"]) > 0)
    assert(len(obj_crt_resp["objects"][0]["key"]) > 0)
    obj_key = obj_crt_resp["objects"][0]["key"]

    # Get the object
    print("Get Object")
    obj_get_resp = None
    try:
        obj_get_resp = transaction_client.get_object("objTestScene", obj_key)
    except Exception as e:
        print(e)
        assert(False)
    print(obj_get_resp)
    assert(len(obj_get_resp["objects"]) > 0)

    # Update an existing Object
    print("Update Object")
    obj_upd = AeselObject()
    obj_upd.name = "testObject2"
    obj_upd.type = "curve"
    obj_upd.subtype = "circle"
    obj_upd_resp = None
    try:
        obj_upd_resp = transaction_client.update_object("objTestScene", obj_key, obj_upd)
    except Exception as e:
        print(e)
        assert(False)
    print(obj_upd_resp)
    assert(len(obj_upd_resp["objects"]) > 0)

    # Query for Objects
    print("Query Objects")
    obj_query = AeselObject()
    obj_query.name = "testObject2"
    obj_query.frame = 0
    obj_query_resp = None
    try:
        obj_query_resp = transaction_client.object_query("objTestScene", obj_query)
    except Exception as e:
        print(e)
        assert(False)
    print(obj_query_resp)
    assert(len(obj_query_resp["objects"]) > 0)

    # Lock an Object
    print("Lock Object")
    try:
        transaction_client.lock_object("objTestScene", obj_key, "testDevice")
    except Exception as e:
        print(e)
        assert(False)

    # Unlock an Object
    print("Unlock Object")
    try:
        transaction_client.unlock_object("objTestScene", obj_key, "testDevice")
    except Exception as e:
        print(e)
        assert(False)

    # Delete an Object
    print("Delete Object")
    try:
        transaction_client.delete_object("objTestScene", obj_key)
    except Exception as e:
        print(e)
        assert(False)

# Execute tests on the Asset API
def test_asset_api(transaction_client):
    print("Testing Asset API")
    # Save a new file with metadata
    print("Create Asset")
    metadata = AeselAssetMetadata()
    metadata.file_type = "json"
    metadata.asset_type = "test"
    relationship = AeselAssetRelationship()
    relationship.type = "scene"
    relationship.related = "12345"
    new_key = None
    try:
        new_key = transaction_client.create_asset("test/resources/testupload.txt", metadata, relationship)
    except Exception as e:
        print(e)
        assert(False)
    assert(len(new_key) > 0)

    # Pull down the file and validate the contents
    print("Asset Get")
    file_contents = None
    try:
        file_contents = transaction_client.get_asset(new_key)
    except Exception as e:
        print(e)
        assert(False)
    print(file_contents)
    assert(file_contents == b"""{"test": 1}\n""")

    # Query for the asset by metadata
    print("Asset Metadata Query")
    metadata_query = AeselAssetMetadata()
    metadata_query.file_type = "json"
    mquery_return = None
    try:
        mquery_return = transaction_client.query_asset_metadata(metadata_query)
    except Exception as e:
        print(e)
        assert(False)
    print(mquery_return)
    assert(mquery_return[0]["key"] == new_key)

    # Update an existing file with metadata
    print("Asset Update")
    metadata2 = AeselAssetMetadata()
    metadata2.content_type = "application/json"
    metadata2.file_type = "json"
    metadata2.asset_type = "second"
    updated_key = None
    try:
        updated_key = transaction_client.update_asset("test/resources/testupload2.txt", metadata2)
    except Exception as e:
        print(e)
        assert(False)
    assert(len(updated_key) > 0)

    # Query for the Asset History of the updated asset
    print("Get Asset History")
    history_return = None
    try:
        history_return = transaction_client.get_asset_history(updated_key)
    except Exception as e:
        print(e)
        assert(False)
    print(history_return)

    # Save an additional Asset Relationship
    print("Save Asset Relationship")
    new_relationship = AeselAssetRelationship()
    new_relationship.asset = updated_key
    new_relationship.type = "object"
    new_relationship.related = "23456"
    newrel_return = None
    try:
        newrel_return = transaction_client.save_asset_relationship(new_relationship)
    except Exception as e:
        print(e)
        assert(False)
    print(newrel_return)
    assert(len(newrel_return[0]["id"]) > 0)

    # Query Asset Relationships
    print("Asset Relationship Query")
    query_relationship = AeselAssetRelationship()
    query_relationship.asset = updated_key
    relq_return = None
    try:
        relq_return = transaction_client.query_asset_relationships(query_relationship)
    except Exception as e:
        print(e)
        assert(False)
    print(relq_return)
    assert(len(relq_return[0]["id"]) > 0)

    # Delete an Asset Relationship
    print("Asset Relationship Delete")
    reld_return = None
    try:
        reld_return = transaction_client.delete_asset_relationship(updated_key, "object", "23456")
    except Exception as e:
        print(e)
        assert(False)
    print(reld_return)
