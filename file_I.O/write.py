f = open('files/newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To','file IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()