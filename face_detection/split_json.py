import os
import json


if __name__ == '__main__':
    img_dir = '/Users/ptrivedi/git-repos/ravdess-images/ravdess-train-test'
    whole_json_path = '/Users/ptrivedi/git-repos/ravdess-images/ravdess_data.json'

    whole = None
    with open(whole_json_path) as f:
        whole = json.load(f)
    train = {}
    test = {}



    for mode in ['train', 'test']:

        for root, dir, files in os.walk(os.path.join(img_dir, mode)):

            for file in files:
                if file[-4:] == '.jpg':
                    key = file[:-4]
                    if mode == 'train':
                        train[key] = whole[key]
                    else:
                        test[key] = whole[key]


    with open('train.json', 'w') as f:
        json.dump(train,f)

    with open('test.json', 'w') as f:
        json.dump(test,f)

