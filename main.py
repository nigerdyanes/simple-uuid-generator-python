from random import randint

def get_random_index(length):
    return randint(0, length - 1)

def generate_uuid(length_uuid):
    uuid = []
    letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
    letters_upper = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    numbers = [str(i) for i in range(1, 10)]
    symbols = ['!','¡','=','-','+']
    characteres = letters + letters_upper + numbers + symbols

    for _ in range(0, length_uuid):
        random_index = get_random_index(len(characteres))
        uuid.append(characteres[random_index])

    return ''.join(uuid)

def uuid(length = 10):
    uuids = []
    
    def uuid():
        uuid = generate_uuid(length)
        if not uuid in uuids:
            return uuid
        else:
            return generate_uuid(length)
            
    return uuid

if __name__ == '__main__':
    uuid = uuid(25)
    for _ in range(0, 20):
        print(uuid())
    
        