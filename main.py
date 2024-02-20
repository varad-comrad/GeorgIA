import pathlib
import subprocess
import dataset_gen


def check_for_model():
    model = pathlib.Path(__file__).parent / 'model'
    return model.exists()


def create_model():
    subprocess.run('jupyter nbconvert --to python georgia.ipynb', shell=True)
    subprocess.run('python georgia.py', shell=True)
    subprocess.run('rm georgia.py', shell=True)


def main():
    dataset_gen.load_datasets()
    if not check_for_model():
        create_model()

if __name__ == '__main__':
    main()
