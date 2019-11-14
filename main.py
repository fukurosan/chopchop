import argparse
import os
from chopchop import ChopChop

if __name__ == "__main__":
    # Parse User Parameters
    parser = argparse.ArgumentParser(description="Utility that automatically cuts your videos for you.")
    parser.add_argument("--file", type=str, help="The video file to be cut.")
    args = parser.parse_args()

    # Init Constants
    INPUT_FILE = args.file
    OUTPUT_FILE = "EDITED_{0}".format(args.file) 

    # Assert Parameters
    assert INPUT_FILE != None, "You need to specify a file. Use --file"
    assert os.path.exists(INPUT_FILE), "No such file."

    # Run Script
    chopchop = ChopChop()
    chopchop.jumpcut(INPUT_FILE, OUTPUT_FILE)