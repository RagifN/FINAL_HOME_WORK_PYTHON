import logging
import argparse

def setup_logging(log_file=None):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def triangle_type(a, b, c):
    logger = logging.getLogger(__name__)
    logger.info(f'Проверка треугольника со сторонами: a={a}, b={b}, c={c}')

    if a + b <= c or a + c <= b or b + c <= a:
        logger.error(f'Треугольник с такими сторонами не существует: a={a}, b={b}, c={c}')
        return "Треугольник с такими сторонами не существует"

    if a != b and b != c and a != c:
        result = "Треугольник разносторонний"
    elif a == b and b == c:
        result = "Треугольник равносторонний"
    else:
        result = "Треугольник равнобедренный"

    logger.info(f'Определен тип треугольника: {result}')
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Определение типа треугольника по его сторонам.')
    parser.add_argument('--a', type=float, required=True, help='Сторона a треугольника.')
    parser.add_argument('--b', type=float, required=True, help='Сторона b треугольника.')
    parser.add_argument('--c', type=float, required=True, help='Сторона c треугольника.')
    parser.add_argument('--log_file', type=str, help='Файл для логирования.')

    args = parser.parse_args()

    setup_logging(args.log_file)

    result = triangle_type(args.a, args.b, args.c)
    print(result)

#python triangle_script.py --a 3 --b 4 --c 5 --log_file triangle.log - запуск из ком. строки