import pathlib
import pyautogui as pag


def check_for_model():
    model = pathlib.Path(__file__).parent / 'model'
    return model.exists()


def create_model():
    pass


def main():
    if not check_for_model():
        create_model()
    print('Model created')


if __name__ == '__main__':
    main()
