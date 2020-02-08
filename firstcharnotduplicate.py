string = input('Enter the string: ')
chars = {}
for ind,char in enumerate(string):
    if char in chars:
        chars[char]['num'] = int(chars[char]['num']) + 1 
    else:
        chars[char] = dict.fromkeys(['num','pos'])
        chars[char]['num'] = 1
        chars[char]['pos'] = ind
flag = 0
minchar = 'None'
for key in chars:
    if chars[key]['num'] == 1 and flag == 0:
        minchar = key
        flag = 1
    elif chars[key]['num'] == 1 and flag == 1:
        if chars[key]['pos'] < chars[minchar]['pos']:
            minchar = key
print(minchar)
    
