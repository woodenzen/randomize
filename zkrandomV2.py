import random
import os
from urllib.parse import urlparse
import os, pathlib
from plistlib import load
    
def TheArchivePath():
    """
    Returns the path to the users active The Archive Zettelkasten archive.

    The path is read from a plist file that is specific to the user's system.

    Returns:
    str: The path to the Zettelkasten archive.
    """
    bundle_id = "de.zettelkasten.TheArchive"
    team_id = "FRMDA3XRGC"
    #`fileName` is the path to the plist file that contains the path to the ZK.
    fileName = os.path.expanduser(
        "~/Library/Group Containers/{0}.{1}.prefs/Library/Preferences/{0}.{1}.prefs.plist".format(team_id, bundle_id))
    with open(fileName, 'rb') as fp:
        # load is a special function for use with a plist
        pl = load(fp) 
        # 'archiveURL' is the key that pairs with the zk path
        path = urlparse(pl['archiveURL']) 
    # path is the part of the path that is formatted for use as a path.
    return (path.path) 

directory = TheArchivePath()
num_files = 5  # change this to the desired number of random file names

#Returns a random filename, chosen among the files in The Archive path.
random_filename = lambda: random.choice(os.listdir(directory))

for i in range(num_files):
    target = random_filename()
    # Format the output to be MMD formatted links from the style Note Title[UUID](thearchive://match/Note Title UUID)
    # You will likely want to change this to suit your needs.
    print(f'{target[:-15]}[{target[-15:-3]}](thearchive://match/{target[:-3]})')