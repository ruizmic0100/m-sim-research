import os
import subprocess

if __name__ == "__main__":
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-latest/sim-outorder -rf:size 160 astarNS.1.arg dealIINS.1.arg gobmkNS.1.arg lbmNS.1.arg", shell=True);
