import argparse

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]

description = 'This program knows about the RGB code corresponding to common colours.'

def main(colour_args):
    print(get_rgb_code(colour_args))

def get_rgb_code(colour_args):
    result = [rgb_code for colour, rgb_code in colours_dict().items() if colour == colour_args]

    if result:
        return f"The RGB code for {colour_args} is {result[0]}"       
    else:
        return f"I don't know the RGB code for {colour_args}"

def colours_dict():
    return dict(colours)

def run():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("colour_name", type=str, help="Gets RGB code for a given colour")
    args = parser.parse_args()
    colour_args = args.colour_name
   
    main(colour_args)


if __name__ == "__main__":
    run()
 