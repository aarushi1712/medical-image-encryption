import sys
import argparse

from pvd_lib import pvd_lib

def main(args):
    pvd_obj = pvd_lib()

    if args.embed:
        pvd_obj.pvd_embed(args.ref, args.inmessage, args.outimage)
    elif args.extract:
        pvd_obj.pvd_extract(args.ref, args.outmessage, args.inimage)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--embed", "-e", action = "store_true", help = "Flag for Embedding Secret Message")
    group.add_argument("--extract", "-d", action = "store_true", help = "Flag for Extracting Secret Message")
    parser.add_argument("--ref", type = str, help = "Reference Image Path", required = True)
    parser.add_argument("--inmessage", type = str, help = "Secret Message Current Path")
    parser.add_argument("--inimage", type = str, help = "Embedded Image Current Path")
    parser.add_argument("--outmessage", type = str, help = "Output Secret Message Path")
    parser.add_argument("--outimage", type = str, help = "Embedded Image Path")
    
    args = parser.parse_args()

    main(args)
