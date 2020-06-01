import pandas as pd
import time
from image_matcher import read_image, bjorn_score


def main(data_location='../data/', data_file='input.csv'):
    df = pd.read_csv(data_location + data_file)
    score_list, runtime_list = [], []
    for idx, row in df.iterrows():
        image1_file, image2_file = data_location + \
            row.image1, data_location + row.image2
        image1 = read_image(image1_file)
        image2 = read_image(image2_file)

        start = time.time()
        score = bjorn_score(image1, image2)
        end = time.time()

        score_list.append(score)
        runtime_list.append(f"{end-start:9f}")

    df['similar'] = score_list
    df['elapsed'] = runtime_list
    df.to_csv('output.csv', index=False)


if __name__ == "__main__":
    main()
