import multiprocessing as mp  # Библеотека
from PIL import Image, ImageFilter
import time


# =====================================================
def resize_image(image_paths, queue):
    for image_path in image_paths:
        img = Image.open(image_path)
        imgs = img.resize((800, 500))
        queue.put((image_path, imgs))  # передаем кортеж вместо двух аргументов


def check_allow(queue):
    image_path, imgs = queue.get()
    imgs = imgs.convert("L")
    imgs = imgs.filter(ImageFilter.BLUR)
    imgs.save(f'{image_path.split(".")[0]}.png')

# ====================================================


if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    date_start = time.time()
    for image in range(1):
        data.append(f'img_{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    chanch_allow = mp.Process(target=check_allow, args=(queue,))

    resize_process.start()
    chanch_allow.start()
    ss = time.time()
    print(f'Время выполнения {ss - date_start:.2f}')

    resize_process.join()
    chanch_allow.join()
