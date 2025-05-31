import os

if __name__ == '__main__':
    while True:
        x = input("Enter to Speak: ")
        if x == 'q':
            os.system("espeak 'byy byy friend'")
            break
        command = f'espeak "{x}"'
        os.system(command)

