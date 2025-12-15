import json

equipos = [
    {"Nombre": "Barcelona", "País": "España", "nivelAtaque": 90, "nivelDefensa": 85},
    {"Nombre": "Bayern", "País": "Alemania", "nivelAtaque": 92, "nivelDefensa": 88},
    {"Nombre": "River", "País": "Argentina", "nivelAtaque": 85, "nivelDefensa": 80}
]

json_str = json.dumps(equipos, indent=4, ensure_ascii=False)
print(json_str)
