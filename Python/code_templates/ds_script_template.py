"""

This script is a simple template for when starting to write a script for Data Science projects

Last tested on E019 from available from https://github.com/kierenAW/EnvironmentConfigurationsForDataScience

"""



import numpy as np
import pandas as pd
import dask
import datetime
import time
import argparse
import pathlib



def main():

    #setup arg parser
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--a_int', type=int, default=1, help="Info about a thing,(Default: 1)")
    parser.add_argument('--a_str', type=str, default="hello", help="Info about a thing,(Default: \"hello\")")
    
    ## to complete the setup, create args object
    args = parser.parse_args()

    print("Hello World")
    print("a_int equals:",args.a_int)
    print("a_str equals:", args.a_str)



if __name__ == '__main__':
    main()


