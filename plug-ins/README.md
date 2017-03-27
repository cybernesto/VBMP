Retro dither Plug-In for the GIMP
=================================
Python plug-in for color reduction of low resolution images for displaying on retro computers.

Introduction
============
This plug-in adds some dithering algorithms intended for converting images into a format that can be displayed on the low resolution graphic modes of old computers like the Apple II.

Installation
============
* Copy the file retro-dither.py to the GIMP plug-ins directory. This directory can be changed so check first what is configured under the folders category of the GIMP settings dialog.

* On mac or linux the plug in must be made executable. For this use the context menu of your favorite file browser or from the console use following command: 
chmod +x  retro-dither.py

* Copy your preferred palettes into the GIMP palettes directory. For converting color images you should choose a palette that matches the system that will be used to display them. Some sample palettes have been included in the palettes directory. 

* Restart GIMP. After this the plug-in will appear under the Colors menu as "Dither..."


Usage
=====
* Load the picture you would like to convert. Depending on the mode you want to use it would make sense to resize and/or crop the picture to match the resolution you intend to use.

* Select the mode. In monochrome mode, the plug-in will automatically convert a color image into a BW image. In color mode you should select a palette. Which palette is the best will depend if your system is NTSC/PAL and the color calibration of your TV set/ monitor so you should experiment with different palettes to see which works best for your setup.

* Select the dithering algorithm. Which one to choose depends on the image you are converting and your personal taste so make sure to try which one works best.

Dither algorithms
=================
The algorithms implemented here are based on the excellent explanation from Tanner Helland:
<http://www.tannerhelland.com/4660/dithering-eleven-algorithms-source-code/>

The performance of this plug-in is limited by the fact that is written in python and surely some optimizations could still be done. For the low resolutions of the retro computers this is not critical so expandability and simplicity was preferred over a compiled plug-in. 


