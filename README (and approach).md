# CSCI435 Assignment 1
Created by Evan Hellersund in Python 3.10
### How to use
Simply clone the repository and run `outliner.py` to generate the images with bounding boxes into the `Outputs` folder (which is where they are on GitHub, too). There is no need to move files into different folders.
Theoretically, different XML files and images may be added, so long as both files fall into the same place alphabetically when considering the other XML/image pairings and they are added to the correct folders.

Please make sure you have the below libraries and modules installed, as well.
### Libraries/modules used
- xml.etree.ElementTree
- Pillow
- os

I will get into why I used these in the next section.
### My Solution
I chose to use Python as I have little to no experience working with XML files or image editing. 
I think my solution is logical and reasonably elegant but ultimately my code is based heavily on the fact that Googling "python xml parser" and "python image drawing" turns up the sites for ElementTree and Pillow first.
I began by attempting to parse the XML files as I recognized that the bounds for the yellow boxes were a component of the XML files, so I created a function to do that.
Then, I figured out how to draw shapes with Pillow, creating another function. I tried to then use the bounds from parsing the XML files to draw the boxes on one screenshot, but they were formatted wrong. 

After I got that down, I got to creating a master function that would iterate through the directories of the XMLs and screenshots, as that would save me from having to hardcode the file names in
(and also allowing for other images and XML files to be used). I chose to write to a separate directory and modify the output filenames slightly for workspace cleanliness.
### Note
If there was a way to work around the missing `</node>` in `com.apalon.ringtones.xml`, I did not find it. I assumed that error was due to the
XML files being captured from Android using the dump feature of the uiautomator framework.
### References
https://docs.python.org/3/library/xml.etree.elementtree.html

https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
