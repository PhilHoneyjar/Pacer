import json
from datetime import timedelta, datetime
from time import strftime, gmtime


def load():
    print('Для просмотра истории тренировок напишите команду Результаты')
    with open('scores.json', 'r', encoding='UTF-8') as fh:
        list_to_load = json.load(fh)
        return list_to_load


def save(list_to_save):
    with open('scores.json', 'w', encoding='UTF-8') as fh:
        fh.write(json.dumps(list_to_save, ensure_ascii=False))
        print('Тренировка сохранена в файле scores.json')


def edit_scores(list_of_workouts):
    for workout in list_of_workouts:
        print(workout)


def get_pace() -> float:
    pace = float(input('\tТемп: ').replace(',', '.').replace(':', '.'))
    return sum(x for x in [pace // 1 * 60, round(pace % 1, 2) * 100])


def get_distance() -> float:
    return float(input('\tРасстояние: ').replace(',', '.'))


def get_time() -> int:
    return sum(x for x in [int(input('\tЧасы: ')) * 3600, int(input('\tМинуты: ')) * 60, int(input('\tСекунды: '))])


def main() -> None:
    try:
        scores = load()
    except:
        scores = []

    flag = input('\nНапишите что вы хотите рассчитать\nТемп, Время, Дистанция: ').lower()

    if flag in ['результаты', 'р', 'res', 'r']:
        edit_scores(scores)

    elif flag in ['темп', 'т', 'pace', 'p']:
        print('Задайте')
        time = get_time()
        distance = get_distance()
        pace = strftime('%M:%S', gmtime(time / distance))
        print(f'Темп: {pace}')
        new_score = {'Дата': datetime.now().strftime('%d-%m-%Y %H:%M'),
                     'Темп': pace,
                     'Время': str(timedelta(seconds=time)),
                     'Дистанция': str(distance)}
        scores.append(new_score)
        save(scores)

    elif flag in ['время', 'в', 'time', 't']:
        print('Задайте')
        distance = get_distance()
        pace = get_pace()
        time = str(timedelta(seconds=pace * distance)).split(".")[0]
        print(f'Время: {time}')
        new_score = {'Дата': datetime.now().strftime('%d-%m-%Y %H:%M'),
                     'Темп': strftime('%M:%S', gmtime(pace)),
                     'Время': time,
                     'Дистанция': str(distance)}
        scores.append(new_score)
        save(scores)

    elif flag in ['дистанция', 'д', 'distance', 'd']:
        print('Задайте')
        time = get_time()
        pace = get_pace()
        distance = round(time / pace, 2)
        print(f'Дистанция: {distance}')
        new_score = {'Дата': datetime.now().strftime('%d-%m-%Y %H:%M'),
                     'Темп': strftime('%M:%S', gmtime(pace)),
                     'Время': str(timedelta(seconds=time)),
                     'Дистанция': str(distance)}
        scores.append(new_score)
        save(scores)

    else:
        print('Некорректные данные')


if __name__ == '__main__':
    main()
