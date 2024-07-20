from rsa_lib import gcd, find_mod_inverse, find_cipher_text, find_message
import argparse
from rich.traceback import install

def file_contents(input_file_path):
    f = open(input_file_path)
    return f.read().strip()

def encrypt(contents, e, n):
    return find_cipher_text(contents, e, n)

def decrypt(cipher_contents, d, n):
    return find_message(cipher_contents, d, n)

def write_file(file_content, output_file_path):
    f = open(output_file_path, "w")
    f.write(file_content)

def main(args):
    install()
    p = 907
    q = 773
    n = p*q
    e = 65537
    phi = (p-1)*(q-1)
    d = find_mod_inverse(e, phi)

    input_contents = int(file_contents(args.input))
    if args.encrypt:
        write_file(str(encrypt(input_contents, e, n)), args.output)
    elif args.decrypt:
        write_file(str(decrypt(input_contents, d, n)), args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--encrypt", "-e", action = "store_true", help = "Argument to Encrypt")
    group.add_argument("--decrypt", "-d", action = "store_true", help = "Argument to Decrypt")
    parser.add_argument("--input", type = str, help = "Input file path")
    parser.add_argument("--output", type = str, help  = "Output file path")

    args = parser.parse_args()
    main(args)
