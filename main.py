from post import main
import logging
import traceback

logging.basicConfig(level=logging.INFO)

def __init__():
    while True:
        try:
            main()
        except Exception as e:
            return 'Ошибка:\n' + traceback.format_exc()
            #print('Ошибка:\n' + traceback.format_exc())

if __name__ == '__main__':
    __init__()