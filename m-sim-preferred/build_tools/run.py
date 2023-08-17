import os
import subprocess
import time

if __name__ == "__main__":
    print("Running first mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 astarNS.1.arg dealIINS.1.arg gobmkNS.1.arg lbmNS.1.arg", shell=True);
    time.sleep(1)
    print("Running second mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 astarNS.1.arg gccNS.1.arg lbmNS.1.arg namdNS.1.arg", shell=True);
    time.sleep(1)
    print("Running third mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 astarNS.1.arg bzip2NS.1.arg dealIINS.1.arg gccNS.1.arg", shell=True);
    time.sleep(1)
    print("Running fourth mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 bzip2NS.1.arg dealIINS.1.arg gccNS.1.arg gobmkNS.1.arg", shell=True);
    time.sleep(1)
    print("Running fifth mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 gamessNS.1.arg hmmerNS.1.arg gccNS.1.arg gobmkNS.1.arg", shell=True);
    time.sleep(1)
    print("Running sixth mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 gamessNS.1.arg hmmerNS.1.arg xalancbmkNS.1.arg soplexNS.1.arg", shell=True);
    time.sleep(1)
    print("Running seventh mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 milcNS.1.arg lbmNS.1.arg gccNS.1.arg gobmkNS.1.arg", shell=True);
    time.sleep(1)
    print("Running eigth mix...");
    subprocess.run("cd ../../spec2006/ && ../m-sim-research/m-sim-preferred/sim-outorder -rf:size 160 povrayNS.1.arg calculixNS.1.arg specrandNS.1.arg leslie3dNS.1.arg", shell=True);
    time.sleep(1)
