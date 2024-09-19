from User.models import User
from util.common_util import hash_password


def to_user(data):
    """
    This function is used to convert the incoming data to user model

    Parameters:
        data (dict) : Data to be converted

    Returns:
         User (User) : Converted User
    """
    name = data.get("name")
    mobile_number = data.get("mobile_number")
    email_id = data.get("email_id")
    gender = data.get("gender")
    date_of_birth = data.get("date_of_birth")
    password = hash_password(data.get("password"))
    return User(name=name, mobile_number=mobile_number, email_id=email_id, gender=gender,
                date_of_birth=date_of_birth, password=password)