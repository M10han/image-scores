import pandas as pd
import glob
import platform
from PIL import Image


def generate_csv(file_name='input.csv', imgs_dir='./imgs/'):
    """Generate CSV file from images directory.

    Keyword Arguments:
        file_name {str} -- Name of the CSV file (default: {'input.csv'})
        imgs_dir {str} -- Relative path to the directory where images are stored (default: {'./imgs/'})
    """
    img_files = glob.glob(imgs_dir + '*')
    img_files.sort()

    if platform.system().lower() == 'windows':
        # Process/cleanup paths
        for i, val in enumerate(img_files):
            img_files[i] = val.replace('\\', '/')

    img1_list = []
    img2_list = []
    for img1 in img_files:
        for img2 in img_files:
            if img1 != img2:
                img1_list.append(img1)
                img2_list.append(img2)

    data = {'image1': img1_list, 'image2': img2_list}
    df = pd.DataFrame(data, columns=data.keys())
    df.to_csv('input.csv', index=False)


def augment_data(imgs_dir='./imgs/'):
    """Augment data

    Keyword Arguments:
        imgs_dir {str} -- Directory with images (default: {'./imgs/'})
    """
    files = glob.glob('./imgs/*.png')
    for f in files:
        print('Working on - {}'.format(f))
        img_name = f[:-4]
        img = Image.open(f)
        img.save(img_name + '.jpg', quality=100)
        img.save(img_name + '.bmp', quality=100)
        img.save(img_name + '.gif', save_all=True,
                 append_images=[img], quality=100)
    print('DONE!')


if __name__ == '__main__':
    generate_csv()
    # augment_data()
