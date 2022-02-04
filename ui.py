# input_processor.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nzubechi Ezeokoli
# nezeokol@uci.edu
# 56611321
from pathlib import Path
from Profile import Profile
from Profile import Post
def create(p, name):
    '''Creates a new file and automatically appends the suffix .dsu also gets a username, password, and bio'''
    p1 = Path(p) / name
    p2 = str(p1)
    if not p1.exists():
        p1.touch()
        print(name, 'was successfully created\n')
        return p2
    else:
        print('File already exists, opening file contents now\n\n')
        profile = Profile()
        profile.load_profile(p2)
        open_file(p2, profile)
    return


def open_file(p, profile):
    '''Opens a existing DSU file and prints out its contents showing it was successfully created'''
    if Path(p).exists() and p[-3:] == 'dsu':
        print('Username:', profile.username)
        print('Password:', profile.password)
        if profile.bio != '':
            print('Bio:', profile.bio)
    else:
        print('ERROR, file does not exist or is not a DSU file')
        

def edit_file(extra, profile, path_way):
    '''Edits the existing DSU file loaded by C or O commands and prints what the user selects'''
    for choice in extra:
        if choice.lower() == '-usr':
            use = input('Enter new username: ').strip()
            usr = white_space(use)
            if usr.strip() != '':
                profile.username = usr
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Username was not changed')
        elif choice.lower() == '-pwd':
            pa = input('Enter new password: ').strip()
            pas = white_space(pa)
            if pas.strip() != '':
                profile.password = pas
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Password was not changed')
        elif choice.lower() == '-bio':
            bio = input('Enter new bio: ')
            if bio.strip() != '':
                profile.bio = bio
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Bio was not changed')
        elif choice.lower() == '-addpost':
            post = input('Add a post: ')
            if post.strip() != '':
                profile.add_post(Post(post))
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Post was not added')
        elif choice.lower() == '-delpost':
            delete  = int(input('Which post would you like to delete (0 being the first post)? '))
            if type(delete) == int and len(profile._posts) > 0:
                profile.del_post(delete)
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Invalid option, please enter a number')
        elif choice.lower() != '-usr' or choice.lower() != '-pwd' or choice.lower() != '-bio' or choice.lower() != '-addpost' or choice.lower() != '-delpost':
            print('One of the choices were invalid')
            return

def print_file(extra, profile):
    '''Prints the contents of a DSU file selceted by user'''
    for choice in extra:
        if choice.lower() == '-usr':
            if profile.username != '':
                print('Your username is:', profile.username)
            else:
                print('You have no username')
        if choice.lower() == '-pwd':
            if profile.password != '':
                print('Your password is:', profile.password)
            else:
                print('You have no password')
        if choice.lower() == '-bio':
            if profile.bio != '':
                print('Your bio is:', profile.bio)
            else:
                print('You have no bio')
        if choice.lower() == '-posts':
            if profile._posts != []:
                for i in range(len(profile._posts)):
                    print(str(i) + ':', profile.get_posts()[i]['entry'])
            else:
                print('You have no posts')
        if choice.lower() == '-post':
            if profile.get_posts()[int(extra[-1])]['entry'] != '':
                print(extra[-1] + ':', profile.get_posts()[int(extra[-1])]['entry'])
            else:
                print('You have no post in that index')
        if choice.lower() == '-all':
            if profile.username != '':
                print('Your username is:', profile.username)
            else:
                print('You have no username')
            if profile.password != '':
                print('Your password is:', profile.password)
            else:
                print('You have no password')
            if profile.bio != '':
                print('Your bio is:', profile.bio)
            else:
                print('You have no bio')
            if profile._posts != []:
                print('Your posts:')
                for i in range(len(profile._posts)):
                    print(str(i) + ':', profile.get_posts()[i]['entry'])
            else:
                print('You have no posts')
        
def admin_create(p, option, suffix):
    '''Creates a new file and automatically appends the suffix .dsu also gets a username, password, and bio'''
    if option[-1] == '-n':
        new_file = suffix
        p1 = Path(p) / new_file
        p2 = str(p1)
        if not p1.exists():
            p1.touch()
            print(new_file, 'was successfully created')
            return p2
        else:
            print('File already exists, opening file contents now')
            profile = Profile()
            profile.load_profile(p2)
            open_file(p2, profile)
    else:
        print('ERROR, file option is invalid')
        return


def admin_edit_file(ex, profile, path_way):
    '''Edits the existing DSU file loaded by C or O commands and prints what the user selects but in admin mode so it takes single line input from the a2 module'''
    ctr = 0
    for i in range(0,len(ex)-1,2):
        if ex[i].lower().strip() == '-usr' and len(ex) > 1:
            usr = ex[i+1].strip()
            if white_space(usr) == True:
                print('ERROR')
                return
            if usr.strip() != '':
                profile.username = usr
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Username was not changed')
        elif ex[i].lower().strip() == '-pwd' and len(ex) > 1:
            pas = ex[i+1].strip()
            if white_space(pas) == True:
                print('ERROR')
                return
            if pas.strip() != '':
                profile.password = pas
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Password was not changed')
        elif ex[i].lower().strip() == '-bio' and len(ex) > 1:
            bio = ex[i+1]
            if bio.strip() != '':
                profile.bio = bio
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Bio was not changed')
        elif ex[i].lower().strip() == '-addpost' and len(ex) > 1:
            post = ex[i+1]
            if post.strip() != '':
                profile.add_post(Post(post))
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Post was not added')
        elif ex[i].lower().strip() == '-delpost' and len(ex) > 1:
            delete = int(ex[i+1])
            if type(delete) == int and len(profile._posts) > 0:
                profile.del_post(delete)
                profile.save_profile(path_way)
                print('Edit was successful')
            else:
                print('Invalid option, please enter a number')
        elif ex[i].lower() != '-usr' or ex[i].lower() != '-pwd' or ex[i].lower() != '-bio' or ex[i].lower() != '-posts' or ex[i].lower() != '-post' or ex[i].lower() != '-all':
            print('One of the choices were invalid')
            return

def white_space(inp):
    '''Sees if theres whitespaces in the username'''
    ctr = 0
    for i in inp:
        if i == ' ':
            ctr += i
    if ctr > 0:
        return True
    else:
        return False

def print_post(extra, profile):
    '''A special print post statement for my user interface class that tells user to choose which post to select'''
    for choice in extra:
        if choice.lower() == '-post':
            num = int(input('Which post would you like to delete (0 being the first post)? '))
            if profile.get_posts()[num]['entry'] != '' or profile.get_posts()[num]['entry'] != []:
                print(str(num) + ':', profile.get_posts()[num]['entry'])
            else:
                print('You have no post in that index')
