import glob
import re
id = 0

with open('reviews.tsv', 'w') as f:

    for filename in glob.iglob('./neg/*.txt'):
         id += 1
         file = open(filename, encoding="utf8", errors='ignore')
         text = file.read()
         text = re.sub("[^a-zA-Z0-9]"," ", text)
         f.write(str(id) + "\t" + "0" + "\t" + re.sub("[^a-zA-Z0-9]"," ", text) + "\n")
     
    for filename in glob.iglob('./pos/*.txt'):
        id += 1
        file = open(filename, encoding="utf8", errors='ignore')
        text = file.read()
        text = re.sub("[^a-zA-Z0-9]"," ", text)
        f.write(str(id) + "\t" + "1" + "\t" + re.sub("[^a-zA-Z0-9]"," ", text) + "\n")
