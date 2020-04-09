# ASCII_art_generator
Generating ascii arts with python via command prompt.
## How it works? 
     The input is a picture of one of the selected formats. After that, each pixel is processed, compressed and repainted in gray. Then a little magic happens that transforms the pixels into a specific sequence of ASCII characters.
* * *
## Useful formulas
>0-255 is divided into 11 ranges of 25 pixels each like: 255/25 (minimal range) After that converting to int value
     pixelList = list(image.getdata()); pixels_to_char = [ASCII_CHARS[int(pixel_value / 25)] for pixel_value in pixelList]
