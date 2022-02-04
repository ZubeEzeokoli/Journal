import ui
from Profile import Profile
from Profile import Post
from pathlib import Path
inp = input('Hello! Would you like to create or open a file today (press C for create or O for open)? You may also enter \"admin\" to enter ADMIN mode or enter \'Q\' to quit\n')
if inp.lower() != 'admin':
    while inp.upper() != 'Q':
        try:
            #try and except to make sure my code doesn't crash at any point, but can quit if given command q
            if inp.upper() == 'C':
                #Creates a new file in the specified directory and saves the inputed contents such as username, password, and bio if they choose to enter one, into the dsu file
                p = input('Please enter the path you would like this new file to go in\n')
                name = input('What would you like to name your file?\n')
                name = name + '.dsu'
                path_way = str(Path(p) / name)
                if not Path(path_way).exists():
                    print('If any input contains a space it will result in an error')
                    user = input('Enter a username: ')
                    if ui.white_space(user) == True:
                        print('ERROR')
                        break
                    pas = input('Enter a password: ')
                    if ui.white_space(pas) == True:
                        print('ERROR')
                        break
                    bio = input('Enter a bio(optional): ')
                    if user != '' and pas != '':
                        file = ui.create(p, name)
                        if file != None:
                            profile = Profile('localhost', user, pas)
                            profile.bio = bio
                            profile.save_profile(file)
                    else:
                        print('File wasn\'t created, input username and password')
                else:
                    #if the created file name already exists, justs opens the existing file
                    print('File already exists, opening file contents now\n')
                    profile = Profile()
                    profile.load_profile(path_way)
                    ui.open_file(path_way, profile)
                    print()
            elif inp.upper() == 'O':
                #Calls the open_file function in the UI module to load the contents of the directory if it exists
                p = input('Please enter the DSU file path you would like to open\n')
                print()
                path_way = p
                profile = Profile()
                profile.load_profile(p)
                ui.open_file(p, profile)
                print()
            elif inp.upper() == 'E':
                #Allows user to change the contents saved in the chosen directory
                choice = input('Enter any of the following choices you would like to edit(ex: -addpost or -bio -usr for multiple edits):\n-usr(USERNAME)\n-pwd(PASSWORD)\n-bio(BIO)\n-addpost(NEW POST)\n-delpost(DELETE POST)\n\n')
                extra = choice.split()
                ui.edit_file(extra, profile, path_way)
                print()
            elif inp.upper() == 'P':
                #Prints the contents specified by the user
                choice = input('Enter any of the following choices you would like to print(ex: -usr or -usr -pwd for multiple prints):\n-usr(USERNAME)\n-pwd(PASSWORD)\n-bio(BIO)\n-posts(ALL POSTS)\n-post(A POST)\n-all(PRINTS EVERYTHING)\n\n')
                extra = choice.split()
                if choice.lower() == '-post':
                    ui.print_post(extra, profile)
                else:
                    ui.print_file(extra, profile)
                print()
            inp = input('Choose a new command!\nC-create a new file\nO-opens a file and loads its contents\nE-edit the contents of a file\nP-print the contents of a file\nQ-quit\n\n')
        except:
            print('ERROR')
            print('Something went wrong, if you didn\'t already load or create a file please enter C or O to continue. Else, enter a valid command and follow the instructions')
            print('C-create a new file\nO-opens a file and loads its contents\nE-edit the contents of a file\nP-print the contents of a file\nQ-quit\n')
            inp = input()
else:
    print('ADMIN MODE ENTERED')
    #Enters admin mode so this gets rid of all input messages and user must enter inputs according to the assignment
    print('Please create or open a file')
    inp = input()
    while inp[:1].upper() != 'Q':
        try:
            #try and except to make sure my code doesn't crash at any point, but can quit if given command q
            if ((inp[:1].upper() == 'C' or inp[:1].upper() == 'O' or inp[:1].upper() == 'E' or inp[:1].upper() == 'P') and inp[:2].upper() != 'C:'):
                #Error handles if a command was given, if not an error will be printed
                for i in range(len(inp)):#Gets index of the space after the option so I can split after input/path
                    index = 0
                    if inp[i:i+2] == '-n':
                        index = i
                        break
                    else:
                        extra = inp[2:].split()
            cmd = inp[:1]
            if index != 0:
                p = inp[2:index-1]
            else:
                p = inp[2:]
            option = []
            suffix = ''
            extra = inp[index:].split()
            if len(inp) != 1:
                #Error handles to see if more than a command was given
                for x in range(len(extra)-1):#Differenciates from the list 'extra' to make a list of options, give a single option, and give suffix a value if given
                    if extra[x] == '-n':
                        option.append(extra[x])
                    else:
                        suffix += extra[x]
                if extra[-1] == '-n':
                    option.append(extra[-1])
                else:
                    suffix += extra[-1]
                if cmd.upper() == 'C':
                    #Creates a new file in the specified directory and saves the inputed contents into the dsu file
                    suffix = suffix + '.dsu'
                    path_way = str(Path(p) / suffix)
                    if not Path(path_way).exists():
                        print('If any input contains a space it will result in an error')
                        print('Enter username:')
                        user = input()
                        if ui.white_space(user) == True:
                            print('ERROR')
                            break
                        print('Enter password:')
                        pas = input()
                        if ui.white_space(pas) == True:
                            print('ERROR')
                            break
                        print('Enter bio(optional):')
                        bio = input()
                        if user != '' and pas != '':
                            file = ui.admin_create(p, option, suffix)
                            if file != None:
                                profile = Profile('localhost', user, pas)
                                profile.bio = bio
                                profile.save_profile(file)
                        else:
                            print('File wasn\'t created, input username and password')
                    else:
                        #if the created file name already exists, justs opens the existing file
                        print('File already exists, opening file contents now')
                        profile = Profile()
                        profile.load_profile(path_way)
                        ui.open_file(path_way, profile)
                elif cmd.upper() == 'O':
                    #Calls the open_file function in the UI module to load the contents of the directory if it exists
                    path_way = p
                    profile = Profile()
                    profile.load_profile(p)
                    ui.open_file(p, profile)
                elif cmd.upper() == 'E':
                    #Allows user to change the contents saved in the chosen directory
                    ctr = 0
                    for i in inp:#splits the input by quotes so I can get each value that I need
                        if i == "\"":
                            ctr = 1
                        if i == '\'':
                            ctr = 2
                    if ctr == 1:
                        ex = inp[2:].split("\"")
                        ex.pop(-1)
                    elif ctr == 2:
                        ex = inp[2:].split('\'')
                        ex.pop(-1)
                    else:
                        ex = inp[2:].split()
                    ui.admin_edit_file(ex, profile, path_way)
                elif cmd.upper() == 'P':
                    #Prints the contents specified by the user
                    extra.pop(0)
                    ui.print_file(extra, profile)
            print('Enter new command or enter \'q\' to quit:')
            inp = input()
        except:
            print("ERROR")
            inp = input()
