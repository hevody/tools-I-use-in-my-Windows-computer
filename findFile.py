import os


def walker(case, potFileName):
    fileCounter = 0
    potFileName = potFileName.lower()
    print('\n[*] This is where you can find the file...\n')
    if case == 2:
        for dir, sub, files in os.walk('C:\\'):
            for file in files:
                file = file.lower()
                if file.endswith(potFileName):
                    fileCounter = fileCounter + 1
                    print(f'{file}: {dir}')
        print()
        if fileCounter == 0:
             print("Sorry, we can't find the file")
        input()
        exit()
    for dir, sub, files in os.walk('C:\\'):
        for file in files:
            file = file.lower()
            if file.startswith(potFileName):
                fileCounter = fileCounter + 1
                print(f'{file}: {dir}')
    print()
    if fileCounter == 0:
        print("Sorry, we can't find the file")
    

                    


print('''
      What file are you finding?
      
      [1] I remember the first few letters
      [2] I remember the last few letters including the file type
      [Enter] I remember the name of the file
      ''')
userCase = (input('      > '))
if userCase == '':
    userCase = 1

userCase = int(userCase)

print('\nWhat is it that you remember?')
potentialFile = input()

walker(userCase, potentialFile)

print('\nWanna open the directory in file explorer? (y)es (n)o')
yon = input()

if yon == 'y':
    print('What is the path of the directory?')
    directory = input('> ')
    os.system('explorer ' + directory)


