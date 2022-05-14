from requests import get

def auth(token, vers):
    global TOKEN, version
    TOKEN = token
    version = vers


def method(METHOD, PARAMS = ''):
    return get(f"https://api.vk.com/method/{METHOD}?{PARAMS}&access_token={TOKEN}&v={version}").json()['response']
