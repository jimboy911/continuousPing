20240122

setup:
    py -m venv contPing_env <<<< creates venv folder
    ./contPing_env/Scripts/activate <<<< jumps into virtual environment
    pip install ping3

file = open("show_commands.txt", "r") #opens the file and reads it in
lines = file.readlines() #reads each line and puts it into a list
