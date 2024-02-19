import subprocess
import pathlib


commands = [('.', 'mkdir datasets'),
            ('datasets', 'kaggle datasets download -d annaglass1/geoguessr-55countries'),
            ('datasets', 'kaggle datasets download -d ubitquitin/geolocation-geoguessr-images-50k')]


def check_for_datasets():
    base_path = pathlib.Path(__file__).parent / 'datasets'
    datasets = base_path / 'geolocation-geoguessr-images-50k.zip', base_path / ''
    if not (base_path.exists() and all(dataset.exist() for dataset in datasets)):
        create_dataset()


def check_kaggle_api():
    ret = subprocess.run('kaggle -h', shell=True, capture_output=True)
    return bool(ret.stderr)

def create_dataset():
    if not check_kaggle_api():
        subprocess.run('pip install kaggle', shell=True)
    for cwd, command in commands:
        subprocess.run(command, shell=True, cwd=cwd)
    print('Dataset created')

if __name__ == '__main__':
    check_for_datasets()