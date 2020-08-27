from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, '00d737bc-b643-4832-8656-820eaf188fa8', '05393244-44fd-4755-8a5c-ecb08b6da11d')
]

clientId_table = {u.username : u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username , password):
    user = clientId_table.get(username , None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)