import os
import filecmp

from os.path import expanduser

#label: initiate
path = input('Enter Folder path:\t')
if len(path) is 0:
    home = expanduser("~")
    path = home + '/Downloads'
    
if not os.path.isdir(path):
    print("Folder Does'nt exists")
    exit()
    #goto initiate

files = []

for file in os.listdir(path):
    if(os.path.isfile(os.path.join(path,file))):
        files.append(file)
a=[]

for x in range(len(files)):
    if '.' in files[x]:
        a.append([files[x][ : files[x].rindex('.') ],files[x][files[x].rindex('.') :  ]])
    
a.sort(key = lambda l: l[0].lower())

print("Available files:\n\n")
for i in a:
    print(i[0]+i[1])
print("\n")

removableItems = []
print('\nRemovable Items: \n')

i = 0
while i < len(a) - 1:
    if(a[i][0] is ""):
        i+=1
        continue
    if a[i][0] in a[i + 1][0] and filecmp.cmp(path+'/'+a[i][0]+a[i][1], path+'/'+a[i+1][0]+a[i+1][1]):
            print(a[i+1][0]+a[i+1][1])
            removableItems.append(path+'/'+a[i+1][0]+a[i+1][1])
            del a[i+1]
            
    else:
        i += 1
if len(removableItems):
    if input('\n' + str(len(removableItems)) + " detected. Delete those files? (yes/no): \t").lower() is '' or 'yes':
        for rem in removableItems:
            os.remove(rem)
            print("\nFile(s) Deleted.\n")
    else:
        print("\nFiles not Deleted.\n")
