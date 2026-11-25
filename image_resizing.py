import os
from PIL import Image
import time

def get_file_names(folder: str):
    files = os.listdir(folder)

    return [f'{folder}/{file}' for file in files]

def transform_and_copy(folder: str, images: list[str], new_size: int):
    started = time.time()
    
    for i, image in enumerate(images):
        file_name = image.split('/')[-1]

        img = Image.open(image).convert("RGB")
        res = img.resize([new_size, new_size])
        res.save(f'{folder}/{file_name}')

        if (i + 1) % 100 == 0:
            print(f'Transformed and copied {i + 1} images.')

    elapsed = time.time() - started
    print(f'Minutes: {elapsed // 60}, seconds: {elapsed % 60}')

if __name__ == '__main__':
    folder_from = 'Used data'
    folder_to = 'Resized data'
    
    inception_image_size = 299
    vgg_resnet_image_size = 224

    normal_file_names = get_file_names(f'{folder_from}/Normal')
    pneumonia_file_names = get_file_names(f'{folder_from}/Pneumonia')

    print('-- Inception')
    print('Transforming and copying normal images')
    transform_and_copy(f'{folder_to}/Inception/Normal', normal_file_names, inception_image_size)

    print('Transforming and copying pneumonia images')
    transform_and_copy(f'{folder_to}/Inception/Pneumonia', pneumonia_file_names, inception_image_size)

    print('-- VGG and ResNet')
    print('Transforming and copying normal images')
    transform_and_copy(f'{folder_to}/VGG_ResNet/Normal', normal_file_names, vgg_resnet_image_size)

    print('Transforming and copying pneumonia images')
    transform_and_copy(f'{folder_to}/VGG_ResNet/Pneumonia', pneumonia_file_names, vgg_resnet_image_size)
