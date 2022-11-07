import redis
import eel

r = redis.Redis(host='127.0.0.1', port=6379, db=0)



eel.init('public')

@eel.expose
def updateCounter(key):
    r.incr(key)

    eel.updateInfo(f"{key} wurde schon {r.get(key).decode('utf-8')} geklickt")

eel.start('index.html')
