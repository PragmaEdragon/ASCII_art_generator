# ASCII_art_generator
Generating ascii arts with python via command prompt.
## How it works? 
     The input is a picture of one of the selected formats. After that, each pixel is processed, compressed and repainted in gray. Then a little magic happens that transforms the pixels into a specific sequence of ASCII characters.
* * *
## Useful formulas
>0-255 is divided into 11 ranges of 25 pixels each like: 255/25 (minimal range) After that converting to int value

     pixelList = list(image.getdata())
     pixels_to_char = [ASCII_CHARS[int(pixel_value / 25)] for pixel_value in pixelList]
>Some magic with new width == 100;

     image_ascii = [pixels_to_ascii[index: index + new_width] for index in
                   range(0, len_pixels_to_ascii, new_width)]
                   

### How to work via command prompt
* * *

     $root/<dir with main.py file> python main.py -h <for help>
     $root/<dir with main.py file> python main.py -d or --directory <to chose file in your directory. Like: C:\abc\123.jpg>
     $root/<dir with main.py file> python main.py -d <filename> --expansion <to choose extension of your fille>
     Example : $root/<dir with main.py file> python main.py -d C:\abc\123 --expansion .jpg
* * *
