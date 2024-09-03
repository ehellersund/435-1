import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import os

#Finds leaf elements and creates a list of their bounds in a format suitable for Pillow
def get_leaf_bounds(XML):
    tree = ET.parse(XML)
    root = tree.getroot()

    def find_leaves(component):
        if len(component) == 0:
            return [component]
        leaves = []
        for child in component:
            leaves.extend(find_leaves(child))
        return leaves

    leaf_list = []
    leaves = find_leaves(root)

    for leaf in leaves:
        #Have to adjust formatting for pillow. Removes brackets & converts to tuple
        box = eval(leaf.attrib['bounds'][1:-1].replace("][", ","))
        leaf_list.append(box)
    return leaf_list

#Draws yellow bounding boxes on an image then saves it
def draw_yellow_boxes(image, bounding_boxes, output): 
    
    with Image.open(image) as im:

        draw = ImageDraw.Draw(im)
        for box in bounding_boxes:
            draw.rectangle(box, outline="yellow", width=2)
        im.save(output)

#Runs the two above functions over a list of inputs
def create_output(XMLs, images):
    bounds = []
    i = 0
    
    for XML in XMLs:
        bounds.append(get_leaf_bounds("XML/" + XML))

    for image in images:
        draw_yellow_boxes("Screenshots/" + image, bounds[i], "Outputs/" + image[:-4] + "-bounding-boxes.png")
        i += 1
    
XMLs = os.listdir("XML")
Screenshots = os.listdir("Screenshots")

create_output(XMLs, Screenshots)