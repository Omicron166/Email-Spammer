from core.config import ConfigStorage
from os.path import isfile
from core.templates import Template

# Initializate the data storage
storage = ConfigStorage('./.data')

while True:
    cmd = input('email-spammer> ')
    args = cmd.split()
    command = args.pop(0)

    if command == '': continue

    if command == 'template':

        if args[0] == 'list':
            # Print the available template names

            print('Templates:')
            for template in storage.templates.keys():
                print('\t' + template)

        elif args[0] == 'show':
            if not storage.templates.get(args[1]):
                print(f'[!] Template {args[1]} not found')
                continue
            print(storage.templates[args[1]])

