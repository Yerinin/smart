## User
ALREADY_EXISTS_USER = "이미 존재하는 유저입니다."
NOT_MATCHED_PASSWORD = "비밀번호와 비밀번호 확인 값이 일치하지 않습니다."
NOT_FOUND_USER = "가입자가 존재하지 않습니다."


class Error(Exception):
    pass


class ApiException(Error):
    def __init__(self, message):
        self.message = message
        super().__init__(message)