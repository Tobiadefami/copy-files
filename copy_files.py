import glob
import fire
import os
import tqdm
import shutil


def copy_file(file_path:str, new_file_path:str):

    fns = list(glob.glob(file_path, recursive=True))
    for file in tqdm.tqdm(fns):
        new_path = os.path.join(os.path.dirname(__file__), f'{new_file_path}')
        if not os.path.exists(new_path):
            os.makedirs(new_path)  
        shutil.copy(file, new_path) 



def main(src, dst):
    return move_file(src, dst)


if __name__ == "__main__":
    fire.Fire(main)
