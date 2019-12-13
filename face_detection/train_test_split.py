import os
import random
from shutil import copyfile

"""
    

"""

def getDirAndFileDict(imgDir):
    # Get subdirectories
    dirTree = list(os.walk(imgDir))

    subDirs = dirTree[0][1]
    corrFiles = dirTree[1:]
    dirFileDict = {}

    for subDir, files in zip(subDirs, corrFiles):
        dirFileDict[subDir] = files[2]

    return dirFileDict

def getCount(dict):
    counts = {}
    for dir, files in dict.items():
        print("For class {}, the count is {}".format(dir, str(len(files))))
        counts[dir] = files
    return counts

def sampleAndSelect(dirFileDict, trainSplitPercent):
    train = {}
    test = {}

    for dir, files in dirFileDict.items():
        files = set(files)
        k = int(trainSplitPercent * len(files))
        train_set = set(random.sample(files,k))
        test_set = files.difference(train_set)
        train[dir] = train_set
        test[dir] = test_set

    return (train, test)

def writeToDisk(targetDir, imgDir, train, test):

    for label, set_dict in [("train", train), ("test", test)]:
        os.mkdir(os.path.join(targetDir, label))

        for dir, files in set_dict.items():
            os.mkdir(os.path.join(targetDir,label,dir))

            for file in files:
                src = os.path.join(imgDir, dir, file)
                dest = os.path.join(targetDir, label, dir, file)
                copyfile(src, dest)







if __name__ == '__main__':
    imgDir = "/Users/ptrivedi/git-repos/ravdess-images/ravdess-data"
    targetDir = "/Users/ptrivedi/git-repos/ravdess-images/ravdess-train-test"

    dict = getDirAndFileDict(imgDir)

    train, test = sampleAndSelect(dict, 0.8)

    print("Training set counts:")
    train_counts = getCount(train)

    print("Testing set counts:")
    test_counts = getCount(test)

    print("Writing to disk...")
    writeToDisk(targetDir, imgDir, train, test)

    print("Split completed!")









