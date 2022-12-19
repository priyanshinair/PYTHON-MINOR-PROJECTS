#idea behind is to store multiple things from our clipboard and then easily loads things from clipboard

import sys  #for command line arguments
import clipboard
import json


SAVED_DATA = 'clipboard.json'
#paste the data from clipboard to this variable 'data
'''
clipboard.copy('abc')
data = clipboard.paste()    
print(data)
'''

'''
print(sys.argv) #gives a list of all the command line arguments that are passsed along side when you run the python file

print(sys.argv[1:]) #this will alice off the first element from command line
'''

#function to create and read a json file
def save_data(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('enter a key: ')
        data[key]=clipboard.paste()
        save_data(SAVED_DATA, data)
        print('data saved!')

    elif command =='load':
        key = input('enter a key: ')
        if key in data:
            clipboard.copy(data[key])
        else:
            print('key doesnt exists')

    elif command == 'list':
        print(data)
    else:
        print('unknown command')
else:
    print('please pass exactly one command')