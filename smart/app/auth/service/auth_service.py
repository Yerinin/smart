from smart.app.user.domain.user import User
from smart.database.config import db
from smart.utils.errors import (
    ApiException,
    
    ALREADY_EXISTS_USER,
    NOT_MATCHED_PASSWORD,
    NOT_FOUND_USER,
)

def save_to_db(user) -> None:
    db.session.add(user)
    db.session.commit()

def get_user_by_id(id) -> User:
    return db.session.query(User).get(id)

## password와 re_password값 가져와서 두 값을 비교하고 이후 다르면 예외 발생
# def valid_regist_password(origin_password, re_password) -> None:
#     if origin_password == re_password:
#         raise ApiException(NOT_MATCHED_PASSWORD)

## 유저 등록
def register_user(id, password, phone) -> User:
    savedUser = get_user_by_id(id)
    
    if savedUser:
        raise ApiException(ALREADY_EXISTS_USER)

    # valid_regist_password(password, re_password)

    user = User.create(id, password, phone)
    save_to_db(user)
    
    return user


def login_user(id, password):
    savedUser = get_user_by_id(id)
    
    if not savedUser:
        raise ApiException(NOT_FOUND_USER)
    
    
    if not savedUser.check_password(password=password):
        raise ApiException(NOT_MATCHED_PASSWORD)
    
    return savedUser.id
    