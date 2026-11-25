import os


def rename_files(folder: str, new_name: str):
    files = os.listdir(folder)

    for index, file in enumerate(files):
        file_extension = file.split('.')[-1]
        transformed_name = f'{new_name}_{index + 1}.{file_extension}'

        os.rename(f'{folder}/{file}', f'{folder}/{transformed_name}')

if __name__ == '__main__':
    folder = 'Filtered data'

    rename_files(f'{folder}/Normal', 'Normal')
    rename_files(f'{folder}/Pneumonia', 'Pneumonia')
