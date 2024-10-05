import os
import logging
from pathlib import Path

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: [%(message)s]')
project_name = 'ecomeal'
list_of_directories = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configurations.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'logs/running_logs.log'
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'templates/index.html'
]

for file_path in list_of_directories:
    file_path = Path(file_path)
    file_directory, file_name = os.path.split(file_path)

    if file_directory != '':
        os.makedirs(file_directory, exist_ok= True)
        logging.info(f'Created directory: {file_directory} for file: {file_name}')
    
    if (not os.path.exists(file_path) or (os.path.getsize(filename= file_path) == 0)):
        with open(file= file_path, mode= 'w') as f:
            pass
            logging.info(f'Created file: {file_path}')            
    else:
        logging.info(f'File {file_name} already exists')