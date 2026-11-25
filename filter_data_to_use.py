import os
import random
import shutil


def get_file_names(folder: str):
    files = os.listdir(folder)

    return [f'{folder}/{file}' for file in files]

def copy_images(max_to_copy: int, folder: str, images: list[str]):
    used_indexes = []

    for i in range(max_to_copy):
        index = 0

        while True:
            index = random.randint(0, len(images) - 1)

            if index not in used_indexes:
                used_indexes.append(index)
                break

        file_name = images[index].split('/')[-1]
        shutil.copyfile(images[index], f'{folder}/{file_name}')

        if (i + 1) % 100 == 0:
            print(f'Copied {i + 1} images.')

if __name__ == '__main__':
    folder_from = 'Filtered data'
    folder_to = 'Used data'
    max = 2150

    normal_file_names = get_file_names(f'{folder_from}/Normal')
    pneumonia_file_names = get_file_names(f'{folder_from}/Pneumonia')

    print('Copying normal images')
    copy_images(max, f'{folder_to}/Normal', normal_file_names)

    print('Copying pneumonia images')
    copy_images(max, f'{folder_to}/Pneumonia', pneumonia_file_names)
