from termcolor import colored
from PIL import Image
import colorama
import argparse
import os

colorama.init()

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
ALLOWED_EXPANSIONS = ['.jpg', '.jpeg', '.png', '.jp2']


def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def checkFile(filename):
    try:
        if os.path.isfile(filename) and filename[filename.find('.'):] in ALLOWED_EXPANSIONS:
            print(colored("[+]Successfully found file. Creating your image...\n", 'green'))
            return True
        elif not os.path.isfile(filename) and filename[filename.find('.'):] not in ALLOWED_EXPANSIONS:
            print(colored(f"[-]Not in allowed expansions : {filename[filename.find('.'):]}. "
                          f"List of it: {ALLOWED_EXPANSIONS}", 'red'))
            return False
        elif not os.path.isfile(filename):
            print(colored("[-]No such file in directory.", 'red'))
            return False
    except Exception:
        print(colored("[-]Wrong syntax.", 'red'))
        return None


def openImage(filename):
    try:
        image = Image.open(filename)
        image_ascii = ascii_art(image)
        print(image_ascii)
    except IOError:
        print(colored("[-]Unable to open image.", 'red'))
        raise


def changePixels(image):
    pixelList = list(image.getdata())
    pixels_to_char = [ASCII_CHARS[int(pixel_value / 25)] for pixel_value in pixelList]
    return "".join(pixels_to_char)


def transform_to_gray(image):
    return image.convert('L')


def ascii_art(image, new_width=100):
    image = scale_image(image)
    image = transform_to_gray(image)

    pixels_to_ascii = changePixels(image)
    len_pixels_to_ascii = len(pixels_to_ascii)

    image_ascii = [pixels_to_ascii[index: index + new_width] for index in
                   range(0, len_pixels_to_ascii, new_width)]

    return "\n".join(image_ascii)


def parsingArgs():
    parser = argparse.ArgumentParser(usage=f'ASCII_image_gen -d <dirname> --expansion <.jpg>')
    parser.add_argument('-d', '--directory', help="Argument for dir in witch file saved.")
    parser.add_argument('--expansion', help="File expansion")
    args, options = parser.parse_known_args()

    if args.directory is not None:
        if args.expansion is None and checkFile(args.directory):
            openImage(args.directory)
        elif args.expansion is not None and checkFile(args.directory + args.expansion):
            if args.expansion in ALLOWED_EXPANSIONS:
                try:
                    openImage(args.directory + args.expansion)
                except Exception:
                    print(colored(f"[-]Error in expansion value: {args.expansion}", 'red'))
            else:
                print(colored(f"[-]Not in allowed expansions: {ALLOWED_EXPANSIONS}", 'red'))
    else:
        print(parser.print_help())
