VBMP
====

BMP Viewer for the Apple II

Introduction
============
This project is based on the work of Arnaud Cocquière and his hommage to Steve Jobs.

<http://www.ctrl-pomme-reset.fr/2011/10/11/hommage/>

Unlike most images shown on the Apple II, the image displayed is actually a BMP file 
without additional conversion. The disk includes the sources for the BMP viewer, so I
decided to study it and learn a bit of 6502 assembly and graphics programming on the
Apple II.
Since my Apple IIc supports DHGR graphics I started playing with it to add support to
16 color BMPs and monochrome pictures in Double High-Res. I thought this could be useful
for someone else so I asked Arnaud for permission to publish it in GitHub.

Usage
=====
The code uses the Merlin Assembler syntax. Just load it in Merlin on the Apple II and it 
should compile without problems.
To load BMPs in the DSK Image I recommend Apple Commander, but Cider Press might do as
well. Just import the BMP as a Raw binary file.
Using Applesoft you can load the image with the following commands
BLOAD IMAGE.BMP,A$4000
BRUN DISPLAY

Supported formats
=================
The viewer supports BMP Images with the following resolutions and color depths
* Monochrome (1bit color depth) 280 x 192 px
* Monochrome (1bit color depth) 560 x 192 px
* 16 Color (4bit color depth) 140 x 192 px
The formats are automatically detected based on the horizontal resolution. Using different
formats as the ones listed may lead to unexpected results since the format check has been
kept as simple as possible.

