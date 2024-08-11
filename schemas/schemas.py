from dataclasses import dataclass

@dataclass
class user:
    id:int
    first_name:str
    last_name:str
    userid:int
    register:str

@dataclass
class message:
    id:int
    message:str
    key:str
    userid:int
    register:str

def REGISTERUSER(first_name,last_name,userid,register):
    return dict(
        first_name=first_name,
        last_name=last_name,
        userid=userid,
        register=register
    )

def NEWMESSAGE(message,key,userid,register):
    return dict(
        message=message,
        key=key,
        userid=userid,
        register=register
    )

def check(status,data):
    if status == "user":
        return user(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
    elif status == "message":
        return message(data[0],data[1],data[2],data[3],data[4])
    return None