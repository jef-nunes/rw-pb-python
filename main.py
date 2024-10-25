import multiprocessing
import subprocess
from os import getcwd

BASE_DIR = getcwd()
print(BASE_DIR)

def open_in_terminal(script_name):
    subprocess.Popen([
        "xfce4-terminal", 
        "--hold", 
        "-x", 
        "bash", 
        "-c", 
        f"cd {BASE_DIR} && source ./venv/bin/activate && python3 {script_name}"
    ])


def main():
   p1 = multiprocessing.Process(target=open_in_terminal, args=("writer.py",))
   p2 = multiprocessing.Process(target=open_in_terminal, args=("reader.py",))
   p1.start()
   p2.start()
   p1.join()
   p2.join()

if __name__ == "__main__":
    main()
