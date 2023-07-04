

import os, re, random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from archive_path import TheArchivePath

 # Get a random file from the zettelkasten folder with more than 1000 words
   
def random_size(minsize, maxsize, num=1):
    """
    This function selects a random file from the zettelkasten folder with a word count between minsize and maxsize.
    
    Args:
        minsize (int): The minimum number of words a file should have.
        maxsize (int): The maximum number of words a file should have.
        num (int, optional): The number of files to select. Defaults to 1.
        
    Returns:
        None: The function prints out a list of random notes between minsize and maxsize in a Mardown link format.
    """
    target_dir = TheArchivePath()
    files = os.listdir(target_dir)
    files = [f for f in files if f.endswith('.md')] # Only select markdown files
    zettel=0
    while zettel < num:
        # open a random file
        random.shuffle(files)
        file_name, file_ext = os.path.splitext(os.path.basename(files[0])) # Get the file name and extension
        with open(f'{target_dir}/{files[0]}', 'r') as file: # Open the file
            data = file.read()
            words = data.split()
            if len(words) > minsize and len(words) < maxsize:
                print(f"{len(words):>5} words: [{file_name[:-13]}](thearchive://match/{file_name})") # print(f"{file_name} has {len(words)} words.")
                zettel+=1
        continue            
        return 
if __name__ == "__main__":
    random_size(800, 1400, 6)