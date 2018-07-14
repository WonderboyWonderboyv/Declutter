import os
from os.path import join,getsize
import sys
import platform
import operator
from shutil import copy2

start = os.path.expanduser('~')
desktop = start + '/Desktop'
documents = start + '/Documents'

exclude_prefixes = ('__', '.')
sizes = {}
for dirpath,subdirs,files in os.walk(start):
    files = [f for f in files if not f.startswith(exclude_prefixes)]
    subdirs[:] = [d for d in subdirs if not d.startswith(exclude_prefixes)]
    for x in files:
        try:
            sizes[x] = getsize(join(dirpath,x))/(1024*1024.0)
        except Exception as e:
            pass

tmp = sorted(sizes.items(), key=operator.itemgetter(1), reverse=True)
for i,x in enumerate(tmp[:10]):
    print("%d) %s file \t %0.2f MB size"%(i+1,x[0],x[1]))

_,_,filenames = next(os.walk(desktop))
if platform.system() == 'Linux': 
    filenames = [x for x in filenames if not x.endswith('.desktop')] 
elif platform.system() == 'Windows':
    exclude_extension = ('.ini', '.exe', '.lnk')
    filenames = [x for x in filenames if not x.endswith(exclude_extension)]

extensions = []
for file in filenames:
    extension = file.split('.')[-1]
    src = os.path.join(desktop,file)
    dst = documents + '/' + extension + ' files'
    if not extension in extensions:
        extensions.append(extension)
        if not os.path.exists(dst): 
            os.mkdir(dst)
    try:
        copy2(src,dst)
    except Exception as e:
        print('Could not copy %s'%file)
    os.remove(src)
