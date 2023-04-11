import os
import subprocess

project_root_dir_path = os.getcwd()

def initial_setup():
    f = open("./build_tools/PROJECT_ROOT_DIR_PATH.txt", "w")
    f.write(project_root_dir_path)
    f.close()
    os.environ['PATH'] += ':'+project_root_dir_path
    print("Initial Setup Complete.")

def build_normal():
    instr_1 = f"cd {project_root_dir_path} && make"
    subprocess.run(instr_1, shell=True, universal_newlines=False)

if __name__ == "__main__":
    if not (os.path.isfile("./build_tools/PROJECT_ROOT_DIR_PATH.txt")):
        initial_setup()
    else:
        print("Setup Already Completed.")

    build_normal()
