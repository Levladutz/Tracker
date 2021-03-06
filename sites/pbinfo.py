
import requests
import json
import datetime
import time

URL = "https://www.pbinfo.ro/ajx-module/profil/json-jurnal.php"


def getUser(user):
    PARAMS = {"user": user, "force_reload": "true"}
    r = requests.get(url=URL, params=PARAMS)
    data = json.loads(r.content)

    result = []
    for i in data['content']:
        data = datetime.datetime.strptime(i['data_upload'], "%Y-%m-%d")
        result.append({
            "problema": i['denumire'],
            "scor": int(i['scor']),
            "sursa": "pbinfo",
            "data": int(time.mktime(data.timetuple()))
        })
    return result


def testUser(user):
    PARAMS = {"user": user, "force_reload": "true"}
    try:
        r = requests.get(url=URL, params=PARAMS)
    except Exception as e:
        print(e)
        return False
    data = json.loads(r.content)
    # The user dosen't exist
    if data['content'] is False:
        return False
    return True
