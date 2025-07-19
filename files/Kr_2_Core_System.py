from Kr_2 import Kr2
from datetime import datetime
import sys, os, time as t

Year = datetime.now()
os.system('cls' if os.name == 'nt' else 'clear')
print("Krypton 2 Core System [v0.2.0].\n"\
     f"Krypton 2(C) 2025 - {Year.year} All Rights Reserved.\n")
t.sleep(0.5)

try:
    while True:
        command = input("Kr_2# ")

        if command[:3] == "enc":
            args = command.split("\"")
            file_name = args[1]
            metod = args[2].strip(" ")
            try:
                Kr2(file_name, metod)
            except Exception as e:
                print(f"!!!  Error No.1: {e}  !!!")

        elif command == "cls":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif command == "keys":
            try:
                with open("keys.txt", "r") as file:
                    keys = file.readlines()
                    file.close()
                print("Keys:")
                for key in keys:
                    print(f"    {key.strip("\n")}")
                    t.sleep(0.25)
                print("")
            except Exception:
                print("No keys found.\n")
        
        elif command == "exit":
            sys.exit()
        
        elif command == "help":
            print("enc \"[path\\to\\the\\file]\" [t/f/rec]\n"\
                "cls - cleaning the terminal\n"\
                "exit - to close the terminal\n"\
                "keys - to show keys log\n"\
                "delkeys - to delete all keys\n")
        
        elif command == "delkeys":
            key_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
            os.remove(f"{key_dir}\\keys.txt")
            print("All keys successfully deleted.\n")
        
        else:
            print("Type \"help\" for help.\n")
except Exception as e:
    print(f"!!!  Error No.2 - {e}  !!!\n")
    t.sleep(15)