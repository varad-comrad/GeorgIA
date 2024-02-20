import subprocess
import pathlib


commands = [('.', 'mkdir datasets'),
            ('datasets', 'kaggle datasets download -d annaglass1/geoguessr-55countries'),
            ('datasets', 'kaggle datasets download -d ubitquitin/geolocation-geoguessr-images-50k')]


def load_datasets():
    base_path = pathlib.Path(__file__).parent / 'datasets'
    datasets = base_path / 'geolocation-geoguessr-images-50k.zip', base_path / ''
    if not (base_path.exists() and all(dataset.exist() for dataset in datasets)):
        create_dataset()

def create_dataset():
    for cwd, command in commands:
        subprocess.run(command, shell=True, cwd=cwd)
    print('Dataset created')

if __name__ == '__main__':
    load_datasets()