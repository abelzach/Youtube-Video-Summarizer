import pandas as pd
flag = 0

with open("input.txt") as f:
    with open("output.txt", "w") as f1:
        for line in f:
            for i in line:
                if(i == '.'):
                    #f1.write('\n')
                    flag = 1
                    continue
                if(i == ' ' and flag == 0):
                    f1.write(',')
                if(i == ' ' and flag == 1):
                    flag = 0
                    f1.write('.\n')
                    continue
                if(i != ' ' and flag == 1):
                    f1.write(',')
                    flag = 0
                if(i == ','):
                    flag = 0
                    continue
                
                if(i == '?'):
                    flag = 0
                    continue
                if(i == '\n'):
                    flag = 1
                    continue
                else:
                    f1.write(i)


