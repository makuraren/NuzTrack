def nuz():
    achar = ['Kirby', 'Mario']
    lchar = []
    cchar = []
    
    checkTxt = open('char.txt', 'r')
    items = checkTxt.readlines()
    for line in items:
        if line != items[len(items)-1]:
            cchar.append(line[0:-1])
    checkTxt.close()

    print()
    print('This program is made to simplify the tracking of characters dring the nuzlocke challenge in the world of light. If you want to add or remove a character, use the following [-/+] symbols directly infront of the name like (+Mario). Feel free to use this and distribute it to friends')
    print()

    while not ' ' in achar:
        if not 'reset' in achar:
            print()
            print('{0:<25}{1:<25}'.format('Characters Available:', 'Characters Lost:'))
            if len(achar) > len(lchar):
                sp_count = len(achar) - len(lchar)
                for i in range(sp_count):
                    lchar.append(' ')
                for k in range(len(achar)):
                    print('{0:<25}{1:<25}'.format(achar[k], lchar[k]))
                for j in range(sp_count):
                    lchar.remove(' ')
            else:
                sp_count = len(lchar) - len(achar)
                for i in range(sp_count):
                    achar.append(' ')
                for k in range(len(lchar)):
                    print('{0:<25}{1:<25}'.format(achar[k], lchar[k]))
                for j in range(sp_count):
                    achar.remove(' ')
            print()
        
            print()
            check = input('Did you lose or gain a character: ')
            print()

            if check[1:len(check)] in cchar:            
                if (check[0] == '+') and not(check[1:len(check)] in achar) and not(check[1:len(check)] in lchar):
                    achar.append(check[1:len(check)])
                elif (check[0] == '+') and (check[1:len(check)] in achar):
                    print()
                    print('Make sure the character doesn\'t already exist in the Available column.')
                    print()
                elif (check[0] == '+') and (check[1:len(check)] in lchar):
                    print()
                    print('This character has already been added before and placed into Lost column.')
                    print()
                elif (check[0] == '-') and (check[1:len(check)] in achar) and not(check[1:len(check)] in lchar):
                    lchar.append(check[1:len(check)])
                    achar.remove(check[1:len(check)])
                elif (check[0] == '-') and not(check[1:len(check)] in achar):
                    print()
                    print('Make sure the character wanting to be removed has been added in the Available column.')
                    print()
                elif (check[0] == '-') and (check[1:len(check)] in lchar):
                    print()
                    print('This character has already been removed before and placed into Lost column.')
                    print()
            elif check in cchar:
                print()
                print('Make sure there is a +/- sign infront of the character.')
                print()
            else:
                print()
                print('Make sure your inputing the characters name in write')
                print(f'For reference: {cchar}')
                print()
                

            if len(achar) == 0:
                print()
                resp2 = input('Would you like a reset [yes/no]: ')
                print()
            
                if resp2 == 'yes':
                    achar = ['Kirby', 'Mario']
                    lchar = []
                    print()
                    achar.append(input('Please input your first fighter: '))
                    print()
                
                elif resp2 == 'no':
                    break
                
nuz()
