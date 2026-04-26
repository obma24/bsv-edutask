import pytest
from src.util.helpers import hasAttribute

@pytest.mark.unit
def test_hasAttribute_True():
    print("test")
    result = hasAttribute({"name": "Jane"}, "name")
    # print(result)
    assert result == True

# @pytest.mark.unit
# def test_hasAttribute_False():
#     print("test")
#     result = hasAttribute({"name": "Jane"}, "age")
#     # print(result)
#     assert result == False

@pytest.mark.unit
def test_hasAttribute_None():
    my_dict = {"name": "Jane"}
    print("test")
    result = hasAttribute(my_dict, "age")
    # print(result)
    assert result == False