# import pytest
# from unittest.mock import MagicMock

# from src.controllers.usercontroller import UserController


# @pytest.mark.unit
# def test_get_user_by_email_returns_user_for_existing_email():
#     dao = MagicMock()
#     controller = UserController(dao=dao)

#     user = {"id": "u1", "email": "a@b"}
#     dao.find.return_value = [user]

#     assert controller.get_user_by_email("a@b") == user



import pytest
from unittest.mock import MagicMock

from src.controllers.usercontroller import UserController

#here i test that an invalid email raises a value error
@pytest.mark.unit
def test_get_user_by_email_invalid_email_raises_value_error():
    dao = MagicMock()
    controller = UserController(dao=dao)

    with pytest.raises(ValueError):
        controller.get_user_by_email("not-an-email")

    # här ska jag testa att en email adress som finns i databasen returnerar rätt user
@pytest.mark.unit
def test_get_user_by_email_one_match_returns_user():
    dao = MagicMock()
    controller = UserController(dao=dao)

    user = {"id": "u1", "email": "a@b"}
    dao.find.return_value = [user]

    result = controller.get_user_by_email("a@b")

    assert result == user
    dao.find.assert_called_once_with({"email": "a@b"})

# here i test that when there is one match, the user is returned
@pytest.mark.unit
def test_get_user_by_email_multiple_matches_prints_warning_and_returns_first(capsys):
    dao = MagicMock()
    controller = UserController(dao=dao)

    user1 = {"id": "u1", "email": "a@b"}
    user2 = {"id": "u2", "email": "a@b"}
    dao.find.return_value = [user1, user2]

    result = controller.get_user_by_email("a@b")
    captured = capsys.readouterr()

    assert result == user1
    assert "more than one user found with mail a@b" in captured.out
    dao.find.assert_called_once_with({"email": "a@b"})

# here i test that when there is no match, none is returned
@pytest.mark.unit
def test_get_user_by_email_no_match_returns_none():
    dao = MagicMock()
    controller = UserController(dao=dao)

    dao.find.return_value = []

    result = controller.get_user_by_email("a@b")

    assert result is None
    dao.find.assert_called_once_with({"email": "a@b"})

# here i test that when the database operation fails, an exception is raised
@pytest.mark.unit
def test_get_user_by_email_dao_failure_raises_exception():
    dao = MagicMock()
    controller = UserController(dao=dao)

    dao.find.side_effect = Exception("db down")

    with pytest.raises(Exception):
        controller.get_user_by_email("a@b")

    dao.find.assert_called_once_with({"email": "a@b"})