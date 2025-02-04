import re
import sys

def main(*args, **kwargs):
    name_regex = r'^[a-zA-Z0-9-_]+$'
    name = '{{ cookiecutter.name }}'

    if not re.match(name_regex, name):
        print(f'ERROR: {name} is not a valid name! Should match pattern {name_regex}')
        sys.exit(1)

main()