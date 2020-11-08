def nuz():
    achar = ['Kirby']
    lchar = []
    print()
    achar.append(input('Please input your first fighter: '))
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
        
            if check[0] == '+':
                achar.append(check[1:len(check)])
            elif check[0] == '-':
                lchar.append(check[1:len(check)])
                achar.remove(check[1:len(check)])
            else:
                print()
                print('Make sure there is a +/- sign infront of the character')
                print()

            if len(achar) == 0:
                print()
                resp2 = input('Would you like a reset [yes/no]: ')
                print()
            
                if resp2 == 'yes':
                    achar = ['Kirby']
                    lchar = []
                    print()
                    achar.append(input('Please input your first fighter: '))
                    print()
                
                elif resp2 == 'no':
                    break
                
nuz()
