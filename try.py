def set_health(value:float=0):
    health = None
    if not health == None:
        health = value
        return health
    health = get_max_health()
    return health

def get_max_health():
    return 100

a = set_health(10)

print(a)