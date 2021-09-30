import os

direc = os.listdir()
while True:
    fp = open('file1.txt', 'a+')
    print("give your input to add in the file")
    ip = input()
    fp.write(os.linesep + ip)
    fp.close()
    print("input added to", fp.name)
    answer = str(input("do you wnt to add more ? "
                       " if yes press (y) or press enter for next process. "))
    if 'y' in answer:
        continue
    else:
        x = str(
            input('do you want to check the content of the file and exit if yes press (y) or if you want to proceed to '
                  'next process press (n) '))
        fp = open('file1.txt', 'r')
        content = fp.readlines()
        file = open("file1.txt", "r")
        data = file.read()
        if x == 'y':
            for line in content:
                print(line)
                continue
        if x == 'y' or 'n':
            ans = input(
                'do you want to know the number of times a word is in the file if yes press (y) if no press (n)')
            if ans == 'y':
                inp = input('what name do you want to see the count of :')
                occ = data.split(inp)
                if inp in data:
                    print('the number of times ', inp, ' is in the file is :', len(occ))
                    input('press enter to exit')
                    exit()
                else:
                    print('invalid input')
                    input('press enter to exit')
                    exit()
            elif ans == 'n':
                print('bye')
                input('press enter to exit')
                exit()
