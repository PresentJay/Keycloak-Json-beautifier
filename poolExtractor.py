import json

def pool_extract(data, root='start', depth=0):
    trial = 0
    
    if root == 'start':
        print('\npool method')
    else:
        print(f'\t(from {root} . . .)')
    for key, value in data.items():
        if value is None:
            continue
        trial = trial + 1
        for i in range(depth):
            print('\t', end='')
        print(f'[{depth}] {trial} : {key} => ', end='')
        
        if isinstance(value, dict):
            print(f'{len(value)} size dict')
            if len(value) > 1:
                pool_extract(value, key, depth = depth + 1)
                continue
            elif len(value) ==0 and depth ==0:
                print('\t{ <empty> }\n')
            else:
                print("\t{ ", end='')
                print(f'{value.keys()}', end='')
                print(" }")
        elif isinstance(value, list):
            print(f'{len(value)} size list')
            for i in range(depth):
                print('\t', end='')
            print('\t[', end='')
            if len(value) > 0:
                for cnt, item in enumerate(value):
                    if isinstance(item, dict):
                        if cnt > 0 :
                            print(", ", end='')
                        if 'name' in item:
                            print(f'{item.get("name")}', end='')
                        elif 'alias' in item:
                            print(f'{item.get("alias")}', end='')
                        elif 'id' in item:
                            print(f'{item.get("id")}', end='')
                    else:
                        if len(item)>0:
                            print(f'{item}', end='')
                        else:
                            print("<empty>", end='')
            else:
                print('<empty>', end='')
            print(']\n')
        else:
            if value == "":
                print('<empty>')
            else:
                print(f'{value}\n')
            

def main():
    print('start extracting . . .')
    print('* * *')
    
    with open('./realm.json') as f:
        data = json.load(f)
        pool_extract(data)

    print("* * *")
    print("done")



if __name__ == "__main__":
    # execute only if run as a script
    main()