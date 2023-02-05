from datetime import timedelta


def get_pace() -> float:
    return float(input('\tТемп: ').replace(',', '.').replace(':', '.'))


def get_distance() -> float:
    return float(input('\tРасстояние: ').replace(',', '.'))


def get_time() -> int:
    return sum(x for x in [int(input('\tЧасы: ')) * 3600, int(input('\tМинуты: ')) * 60, int(input('\tСекунды: '))])


def convert_pace_to_seconds(pace) -> float:
    """Converts minutes:seconds per distance to seconds per distance"""
    return sum(x for x in [pace // 1 * 60, round(pace % 1, 2) * 100])


def main() -> str:
    flag = input('Напишите что вы хотите рассчитать\nТемп, Время, Дистанция: ').lower()
    if flag in ['темп', 'т', 'pace', 'p']:
        print('Задайте')
        time = get_time()
        distance = get_distance()
        return f'Темп: {int((time / distance) / 60)}:{round((time / distance) % 60)}'

    elif flag in ['время', 'в', 'time', 't']:
        print('Задайте')
        distance = get_distance()
        pace = convert_pace_to_seconds(get_pace())
        return f'Время: {str(timedelta(seconds=pace * distance)).split(".")[0]}'

    elif flag in ['дистанция', 'д', 'distance', 'd']:
        print('Задайте')
        time = get_time()
        pace = convert_pace_to_seconds(get_pace())
        return f'Дистанция: {round(time / pace, 4)}'

    else:
        return 'Некорректные данные'


if __name__ == '__main__':
    print(main())
