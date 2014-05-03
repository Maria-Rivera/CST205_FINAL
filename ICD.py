#########################################################################
# File Name:IDC.py                                                      #               
# Summary:  Program will collect the pixels of images of cells and      #
#           it will determine what parts of the cells are infected.     #
#           The infected areas will be identified by a square around    #
#           them.                                                       #
# User Input:  N/A                                                      #
# Output:   Image of cells will be displayed with infected areas        #
#           identified.                                                 #                              
#                                                                       #              
# Authors: Maria Rivera & Adilene Constante                             #              
# Date created: April 9, 2014                                           #                                   
#                                                                       #
# Course Name: CST-205                                                  #
# Instructor: Sathya Narayanan                                          #
# Assignment: Final Project                                             #
#########################################################################
from PIL import Image
import ImageStat
import math
import ImageDraw

image1 = Image.open("TestCase.jpg")
#more test case images:
#image1 = Image.open("Case330_B.jpg")
#image1 = Image.open("malaria5.jpg")

pixels = [] #array will hold the image's pixels
greatestPixels = [] # array wil hold pixels with darkest luminance
xLocation = [] #array will hold pixels' x location
yLocation = [] #array will hold pixels' y location

# Precondition: Function call
# Postcondition: Appends pixels to array
def getPixels():
    for xPixel in range(300):
        for yPixel in range(300):
            pix = image1.load()
            pixels.append(pix[xPixel, yPixel])

# Precondition: Function call
# Postcondition: Returns image's overall luminance
def OverallLuminance():
   stat = ImageStat.Stat(image1)
   gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) #overall luminance formula
         for r,g,b in image1.getdata())
   return sum(gs)/stat.count[0]

# Precondition: Function call
# Postcondition: Returns pixel with darkest luminance
def greatestPixelBrightness():
    darkestPixel = 240
    overall = OverallLuminance()
    image = image1.convert ( 'RGB' )
    for X in range (300):
        for Y in range (300) :
           #get RGB
            pixelRGB = image.getpixel((X,Y))
            R,G,B = pixelRGB
            pixelLuminance = ( 0.2126*R) + ( 0.7152*G ) + ( 0.0722*B)
            if ( pixelLuminance < darkestPixel):
                darkestPixel = pixelLuminance
    return darkestPixel

# Precondition: greatest individual pixel luminance and
#               overall picture luminance be passed in
# Postcondition: Returns average luminance
def controlLuminance(greatest, overall):
    return (greatest + overall) / 2

# Precondition: average luminance passed in
# Postcondition: prints pixels' location and luminance
def comparePixels(control):
    count = 0 
    image = image1.convert ( 'RGB' )
    for X in range (300):
        for Y in range (300) :
           #get RGB
            pixelRGB = image.getpixel((X,Y))
            R,G,B = pixelRGB
            luminance = ( 0.2126*R) + ( 0.7152*G ) + ( 0.0722*B)
            if ( luminance <= control):
                greatestPixels.append(luminance)
                xLocation.append(X)
                yLocation.append(Y)
                count += 1
                print ( "Pixel Location: " ,X,Y, luminance)
        
# Precondition: pixels with lowest luminance identified 
# Postcondition: draws a rectangle around infected site
def idInfection():
    draw = ImageDraw.Draw(image1)
    # STILL WORKING ON ALGORITHM
##    for x in range(len(greatestPixels)):
##        draw.line((122, 120) + (166, 120), fill = 0)
##    image1.show()
            
def main():
    getPixels()
    lum = OverallLuminance()
    brightest = greatestPixelBrightness()
    control = controlLuminance(brightest, lum)
    comparePixels(control)
    idInfection()
    
main()
