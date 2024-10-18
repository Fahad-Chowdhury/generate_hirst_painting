import colorgram

def extract_colors_from_image(image, number_of_colors):
    """ Extracts 'number_of_colors' colors from given image and retuns it
    as a list of tuples. """
    image_colors = []
    colors = colorgram.extract(image, number_of_colors)
    image_colors = [tuple(color.rgb) for color in colors]
    return image_colors
