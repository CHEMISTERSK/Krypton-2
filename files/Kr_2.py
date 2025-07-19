import random, string, sys, os       # Rule-Driven Substitution Cipher with Dynamic State

key = ""

def generate_key(ascii):
    key = ""
    for j in range(6):
        for i in range(8):
            key += ascii[random.randint(0, 40)]
        key += "-"
    key = key[0 : -1]

    key_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    with open(f"{key_dir}\\keys.txt", "a") as keys:
        keys.write(key + "\n")
        keys.close()
        print("key: " + key)

    return key

def get_key():
    key = input("Enter the key: ")
    if len(key) != 53 or key.count("-") != 5:
        print("Invalid key format. Please enter a valid key.")
        return get_key()
    else:
        return key

def get_maps(key, ascii, code):
    segments = key.split("-")
    for i in range(1, 5):
        random.seed(segments[i])
        shuffled_codes = code.copy()
        random.shuffle(shuffled_codes)

        if i == 1:
            enc_map_1 = dict(zip(ascii, shuffled_codes))
        if i == 2:
            enc_map_2 = dict(zip(ascii, shuffled_codes))
        if i == 3:
            enc_map_3 = dict(zip(ascii, shuffled_codes))
        if i == 4:
            enc_map_4 = dict(zip(ascii, shuffled_codes))

    return enc_map_1, enc_map_2, enc_map_3, enc_map_4

def start_generation(key):
    segments = key.split("-")
    random.seed(segments[5])

    start_sequence = []

    for i in range(4):
        x = random.randint(0, 3)
        if x == 0:
            start_sequence.append("an1")
        if x == 1:
            start_sequence.append("an2")
        if x == 2:
            start_sequence.append("an3")
        if x == 3:
            start_sequence.append("an4")
    return start_sequence

def generate_rules(key):
    segments = key.split("-")
    random.seed(segments[0])
    rules_a = []
    rules_b = []
    state = []

    while len(rules_a) != 256:
        w = random.randint(1, 4)
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        z = random.randint(1, 4)

        states = f"an{w},an{x},an{y},an{z}"
        if states not in rules_a:
            rules_a.append(states)
        else:
            continue

    while len(rules_b) != 256:
        v = random.randint(1, 4)
        state = f"an{v}"
        rules_b.append(state)

    rules = dict(zip(rules_a, rules_b))
    return rules

def loading_message(file_name):
    try:
        with open(f"{file_name}", "r") as file:
            message = file.read()
        return message, True
    except Exception as e:
        print(f"Loading message error: {e}")
        return file_name, False

def encripting(enc_map_1, enc_map_2, enc_map_3, enc_map_4, rules, start_sequence, message):            
    slideing_window = start_sequence
    output = []
    row = []
    pos = 0

    for char in message:
        pos += 1
        set_ = rules[f"{slideing_window[0]},{slideing_window[1]},{slideing_window[2]},{slideing_window[3]}"]

        slideing_window[3] = slideing_window[2]
        slideing_window[2] = slideing_window[1]
        slideing_window[1] = slideing_window[0]

        try:
            if set_ == "an1":
                row.append(enc_map_1[char])
                slideing_window[0] = "an1"
            elif set_ == "an2":
                row.append(enc_map_2[char])
                slideing_window[0] = "an2"
            elif set_ == "an3":
                row.append(enc_map_3[char])
                slideing_window[0] = "an3"
            elif set_ == "an4":
                row.append(enc_map_4[char])
                slideing_window[0] = "an4"
        except Exception:
            raise ValueError(f"invalid character - [{char} - {pos}]")

        if len(row) >= 32:
            output.append(row)
            row = []
        else:
            continue

    output.append(row)
    return output

def decripting(enc_map_1, enc_map_2, enc_map_3, enc_map_4, rules, start_sequence, message):
    
    def get_decription_map(rules, start_sequence, message):
        message = message.split()
        slideing_window = start_sequence
        decription_map = []

        for value in message:
            set_ = rules[f"{slideing_window[0]},{slideing_window[1]},{slideing_window[2]},{slideing_window[3]}"]
            decription_map.append(set_)

            slideing_window[3] = slideing_window[2]
            slideing_window[2] = slideing_window[1]
            slideing_window[1] = slideing_window[0]
            slideing_window[0] = set_

        return decription_map, message

    output = ""
    decription_map, message = get_decription_map(rules, start_sequence, message)
    
    for i in range(len(message)):
        if decription_map[i] == "an1":
            for key, value in enc_map_1.items():
                if value == message[i]:
                    output += key
        elif decription_map[i] == "an2":
            for key, value in enc_map_2.items():
                if value == message[i]:
                    output += key
        elif decription_map[i] == "an3":
            for key, value in enc_map_3.items():
                if value == message[i]:
                    output += key
        elif decription_map[i] == "an4":
            for key, value in enc_map_4.items():
                if value == message[i]:
                    output += key
        
    return output

def saveing(file_name, output):
    if type(output) == list:
        with open(f"{file_name}", "w") as file:
            for row in output:
                row_str = " ".join(str(item) for item in row)
                file.write(row_str + "\n")
    elif type(output) == str:
        with open(f"{file_name}", "w") as file:
            file.write(output)
            file.close()

def Kr2(file_name, metod):
    message, file = loading_message(file_name)
    ascii = list(string.printable)
    code = ["{:02X}".format(i) for i in range(len(ascii))]
    global key
    
    
    if metod == "t" or metod == "T":
        key = generate_key(ascii)
        enc_map_1, enc_map_2, enc_map_3, enc_map_4 = get_maps(key, ascii, code)
        rules = generate_rules(key)
        start_sequence = start_generation(key)
        output = encripting(enc_map_1, enc_map_2, enc_map_3, enc_map_4, rules, start_sequence, message)
        print("file encrypted\n")
        if file == True:
            saveing(file_name, output)
            return key, None
        else:
            output_str = ""
            for row in output:
                row_str = " ".join(str(item) for item in row)
                print(f"{row_str}\n")
                output_str += f"{row_str}\n"
            return key, output_str
        

    elif metod == "f" or metod == "F":
        if len(key) != 53:
            key = get_key()
        enc_map_1, enc_map_2, enc_map_3, enc_map_4 = get_maps(key, ascii, code)
        rules = generate_rules(key)
        start_sequence = start_generation(key)
        output = decripting(enc_map_1, enc_map_2, enc_map_3, enc_map_4, rules, start_sequence, message)
        print("file decrypted\n")
        if file == True:
            saveing(file_name, output)
        else:
            print("\n" + output + "\n")
            return output

    elif metod == "rec":
        print("Note: Only ~90% of the document is recoverable.\n"\
              "key 1 - The key with which the document was incorrectly decrypted.\n"\
              "key 2 - The key with which the document was originally encrypted.\n")
        
        key_1 = input("Enter key 1: ")
        key_2 = input("Enter key 2: ")

        enc_map_1, enc_map_2, enc_map_3, enc_map_4 = get_maps(key_1, ascii, code)
        rules = generate_rules(key_1)
        start_sequence = start_generation(key_1)
        output = encripting(enc_map_1, enc_map_2, enc_map_3, enc_map_4, rules, start_sequence, message)

        saveing(file_name, output)
        message = ""
        message, file = loading_message(file_name)

        enc_map_1, enc_map_2, enc_map_3, enc_map_4 = get_maps(key_2, ascii, code)
        rules = generate_rules(key_2)
        start_sequence = start_generation(key_2)
        output = decripting(enc_map_1, enc_map_2, enc_map_3, enc_map_4, rules, start_sequence, message)

        saveing(file_name, output)