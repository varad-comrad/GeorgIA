import pathlib
import subprocess
import pyautogui as pag


def check_for_model():
    model = pathlib.Path(__file__).parent / 'model'
    return model.exists()


def create_model():
    subprocess.run('jupyter nbconvert --to python georgia.ipynb', shell=True)
    subprocess.run('python georgia.py', shell=True)
    subprocess.run('rm georgia.py', shell=True)

def get_screenshot():
    pass

def predict():
    pass

def main():
    if not check_for_model():
        create_model()
    get_screenshot()
    predict()    

if __name__ == '__main__':
    main()
