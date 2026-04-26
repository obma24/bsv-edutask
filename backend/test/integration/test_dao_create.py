import pytest

from src.util.dao import DAO

#i test that when the document is compliant with the validator, it is created successfully
@pytest.mark.integration
def test_create_succeeds_for_validator_compliant_document(clean_it_collection):
    dao = DAO(collection_name=clean_it_collection)
    created = dao.create({"description": "integration ok", "done": False})
    assert created["description"] == "integration ok"
    assert created["done"] is False
    assert "_id" in created

#now im going to test that when the document is not compliant with the validator, it fails
@pytest.mark.integration
def test_create_fails_when_required_property_missing(clean_it_collection):
    dao = DAO(collection_name=clean_it_collection)
    with pytest.raises(Exception):
        dao.create({"done": False})

#if the document is not compliant with the validator, it fails
@pytest.mark.integration
def test_create_fails_when_property_type_wrong(clean_it_collection):
    dao = DAO(collection_name=clean_it_collection)
    with pytest.raises(Exception):
        dao.create({"description": "bad type", "done": "False"})

#now im going to test that when the unique items are violated, it fails
@pytest.mark.integration
def test_create_fails_when_unique_items_violated(clean_it_collection):
    dao = DAO(collection_name=clean_it_collection)
    dao.create({"description": "dup", "done": False})
    with pytest.raises(Exception):
        dao.create({"description": "dup", "done": True})
