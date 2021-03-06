import os
import itertools


def find_duplicates(folder_path):
    files_list = []
    duplicates = []
    for (thisdir, subshere, files) in os.walk(folder_path):
        files_list.extend([os.path.join(thisdir, fname) for fname in files])

    for file1, file2 in itertools.combinations(files_list, 2):
        fname1, fname2 = os.path.basename(file1), os.path.basename(file2)
        fsize1, fsize2 = os.path.getsize(file1), os.path.getsize(file2)
        if fname1 == fname2 and fsize1 == fsize2:
            duplicates.extend([file1, file2])
    return duplicates


if __name__ == '__main__':
    folder_path = input('Enter the path to the folder: ')
    print('Found duplicates')
    [print(full_file_name) for full_file_name in find_duplicates(folder_path)]
