import random
import os
from archive_path import TheArchivePath
    
directory = TheArchivePath()
num_files = 5  # change this to the desired number of random file names

#Returns a random filename, chosen among the files in The Archive path.
random_filename = lambda: random.choice(os.listdir(directory))

for i in range(num_files):
    target = random_filename()
    # Format the output to be MMD formatted links from the style Note Title[UUID](thearchive://match/Note Title UUID)
    # You will likely want to change this to suit your needs.
    print(f'{target[:-15]}[{target[-15:-3]}](thearchive://match/{target[:-3]})')