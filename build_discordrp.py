with open('discordrp_standalone_template.py') as f:
    src = f.read()

with open('pypresence.zip', 'rb') as f:
    zipdata = f.read()

src = src.replace('${DATA}', repr(zipdata))

with open('discordrp_standalone.py', 'w') as f:
    f.write(src)
