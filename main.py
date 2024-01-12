from flask import Flask

app = Flask(__name__)

def add_meter(name, meters={}):
    meters[name] = 'Не підтверджено'
    print(f'Лічильник {name}  успішно додано.')

def verify_meter(name, meters={}):
    if name in meters:
        meters[name] = 'Підтверджено'
        print(f'Лічильник {name} підтверджено.')
    else:
        print(f'Лічильник {name} не знайдено.')
        raise KeyError(f'Лічильник {name} не знайдено.')

def display_meters(meters={}):
    result = '\nСписок лічильників:\n'
    for name, status in meters.items():
        result += f'{name}: {status}\n'
    return result

@app.route('/')
def home():
    meters = {}
    add_meter('Лічильник1', meters)
    verify_meter('Лічильник1', meters)
    add_meter('Лічильник2', meters)

    dm = display_meters(meters)
    return dm

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
