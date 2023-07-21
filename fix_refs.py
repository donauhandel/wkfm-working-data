import glob


files = glob.glob('./data/editions/*xml')


for x in files:
    with open(x, 'r') as f:
        text = f.read()
    text = text.replace('ref="wkfm', 'ref="#wkfm')
    with open(x, 'w') as f:
        f.write(text)