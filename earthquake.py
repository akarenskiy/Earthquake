import requests
import matplotlib.pyplot as plt

BASE_URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'


def get_value(info_message):
    result = input(info_message)
    return result if result else None


params = {
    'format': 'geojson',
    'starttime': get_value('Начало периода(гггг-мм-дд)'),
    'endtime': get_value('Конец периода(гггг-мм-дд)'),
    'latitude': get_value('Широта'),
    'longitude': get_value('Долгота'),
    'maxradiuskm': get_value('Максимальный радиус'),
    'minmagnitude': get_value('Минимальная магнитуда'),
    'maxmagnitude': get_value('Максимальная магнитуда'),
}

# стандартные параметры для запроса
# default_params = {
#     'format': 'geojson',
#     'starttime': '2019-01-01',
#     'endtime': '2019-05-01',
#     'latitude': '50',
#     'longitude': '50',
#     'maxradiuskm': '1500',
#     'minmagnitude': '2',
#     'maxmagnitude': '7',
# }

response = requests.get(BASE_URL, headers={'Accept': 'application/json'},
                        params=params)

raw_json_data = response.json()
json_data = {}
for features in raw_json_data['features']:
    json_data[features['properties']['place']] = float(
            features['properties']['mag'])

fig, ax = plt.subplots()

x_axis = json_data.keys()
y_axis = json_data.values()

ax.set_xticklabels(json_data.keys(), rotation=90)
ax.bar(x_axis, y_axis)

plot_name = 'earthquake.png'
plt.savefig(plot_name, format='png', dpi=200, bbox_inches='tight')
print(f'график "{plot_name}" сохранён')
plt.show()
