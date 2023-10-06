from PIL import Image
import sys
import os


def main(filename):
    try:
        logo = Image.open(filename)
        logo.save(os.path.splitext(filename)[0] + ".ico",format='ICO')

    except Exception as ex:
        print(ex)
        exit(-1)
    
    print(f"Done with conversion of {filename}")
    os.system ('pause')


if __name__ == "__main__":
    dropped_file = sys.argv[1]

    print(f"Converting file {dropped_file} to ico.")
    main(dropped_file)

