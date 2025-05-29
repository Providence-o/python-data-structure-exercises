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
    print(get_colour_match_result(colour_args))

def get_colour_match_result(colour_args):
    matched_value = matching_value(colour_args)
    
    if not matched_value:
        return f"I don't know the RGB code for {colour_args}"
    return matched_value
    
def matching_value(colour_args):
    for colour, rgb_code in colours_dict().items():
        if colour.lower() == colour_args.lower():
            return f"The RGB code for {colour_args} is #{rgb_code}"
        elif rgb_code.upper() == colour_args.upper():
            return f"The colour name for #{colour_args} is {colour}"


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
 