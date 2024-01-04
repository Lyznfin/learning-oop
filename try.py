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

def weap_attack(*args, **kwargs):
    a = 0
    i = 0
    while i < len(kwargs['stat']):
        val = args[i]
        match kwargs['stat'][i]:
            case 'STR':
                a += val + 1
            case 'DEX':
                a += val + 2
            case 'CON':
                a += val + 3
            case 'INT':
                a += val + 4
            case 'WIS':
                a += val + 5
        i += 1
    return a

print(weap_attack(1, 1, 1, stat=['STR', 'STR', 'STR']))