#!/usr/bin/env python

# Error Diffusion Dither script for the GIMP 
# Version 1.0
# Author: Mario Patino - cybernesto@gmail.com
# based on the dither script of Andy Hefner - ahefner@gmail.com
# dithering algorithms based on the information contained here:
# http://www.tannerhelland.com/4660/dithering-eleven-algorithms-source-code/
# Copyright Mario Patino, 2014

import math
from gimpfu import *
from array import array

    
def change_pixel(dim, src, x, y, px_d):
    w, h, p = dim
    if x > w:
        return       
    if y > h:
        return
    i = (x + y * w)*p
    src[i:i+p] = array("B",[max(min((a+b),255),0) for a,b in zip(px_d,src[i:i+p])])

def floyd_stein(dim, src_pixels, x, y, px_d):
    px_delta = [a*7/16 for a in px_d]
    change_pixel(dim, src_pixels, x+1, y  , px_delta)
    px_delta = [a*5/16 for a in px_d]
    change_pixel(dim, src_pixels, x  , y+1, px_delta)
    px_delta = [a*3/16 for a in px_d]
    change_pixel(dim, src_pixels, x-1, y+1, px_delta)
    px_delta = [a*1/16 for a in px_d]
    change_pixel(dim, src_pixels, x+1, y+1, px_delta)

def jarvis(dim, src_pixels, x, y, px_d):   
    px_delta = [a*7/48 for a in px_d]
    change_pixel(dim, src_pixels,x+1 ,y, px_delta)
    change_pixel(dim, src_pixels,x ,y+1, px_delta)
    px_delta = [a*5/48 for a in px_d]
    change_pixel(dim, src_pixels,x+2 ,y, px_delta)
    change_pixel(dim, src_pixels,x-1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x ,y+2, px_delta)
    px_delta = [a*3/48 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x-1 ,y+2, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+2, px_delta)
    px_delta = [a*1/48 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+2, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+2, px_delta)
    
def stucki(dim, src_pixels, x, y, px_d):
    px_delta = [a*8/42 for a in px_d]
    change_pixel(dim, src_pixels,x+1 ,y, px_delta)
    change_pixel(dim, src_pixels,x ,y+1, px_delta)
    px_delta = [a*4/42 for a in px_d]
    change_pixel(dim, src_pixels,x+2 ,y, px_delta)
    change_pixel(dim, src_pixels,x-1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x ,y+2, px_delta)
    px_delta = [a*2/42 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x-1 ,y+2, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+2, px_delta)
    px_delta = [a*1/42 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+2, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+2, px_delta)
    
def atkinson(dim, src_pixels, x, y, px_d):
    px_delta = [a*1/8 for a in px_d]
    change_pixel(dim, src_pixels,x+1 ,y, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y, px_delta)
    change_pixel(dim, src_pixels,x-1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x ,y+2, px_delta)
    
def burkes(dim, src_pixels, x, y, px_d):
    px_delta = [a*8/32 for a in px_d]
    change_pixel(dim, src_pixels,x+1 ,y, px_delta)
    change_pixel(dim, src_pixels,x ,y+1, px_delta)
    px_delta = [a*4/32 for a in px_d]
    change_pixel(dim, src_pixels,x+2 ,y, px_delta)
    change_pixel(dim, src_pixels,x-1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+1, px_delta)
    px_delta = [a*2/32 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+1, px_delta)

def sierra3(dim, src_pixels, x, y, px_d):
    px_delta = [a*5/32 for a in px_d]
    change_pixel(dim, src_pixels,x+1 ,y, px_delta)
    change_pixel(dim, src_pixels,x ,y+1, px_delta)
    px_delta = [a*4/32 for a in px_d]
    change_pixel(dim, src_pixels,x-1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+1, px_delta)
    px_delta = [a*3/32 for a in px_d]
    change_pixel(dim, src_pixels,x+2 ,y, px_delta)
    change_pixel(dim, src_pixels,x ,y+2, px_delta)
    px_delta = [a*2/42 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+1, px_delta)    
    change_pixel(dim, src_pixels,x-1 ,y+2, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+2, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+1, px_delta)    
    

def sierra2(dim, src_pixels, x, y, px_d):
    px_delta = [a*4/16 for a in px_d]
    change_pixel(dim, src_pixels,x+1 ,y, px_delta)    
    px_delta = [a*3/16 for a in px_d]
    change_pixel(dim, src_pixels,x+2 ,y, px_delta)    
    change_pixel(dim, src_pixels,x ,y+1, px_delta)
    px_delta = [a*2/16 for a in px_d]
    change_pixel(dim, src_pixels,x-1 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+1 ,y+1, px_delta)
    px_delta = [a*1/16 for a in px_d]
    change_pixel(dim, src_pixels,x-2 ,y+1, px_delta)
    change_pixel(dim, src_pixels,x+2 ,y+1, px_delta)   
    
def sierra1(dim, src_pixels, x, y, px_d):
    px_delta = [a*2/4 for a in px_d]
    change_pixel(dim, src_pixels, x+1, y  , px_delta)
    px_delta = [a*1/4 for a in px_d]
    change_pixel(dim, src_pixels, x  , y+1, px_delta)
    change_pixel(dim, src_pixels, x-1, y+1, px_delta)
    
def px_dist(p1,p2):
    return sum([(a-b)**2 for a,b in zip(p1,p2)])

def retro_dither(timg, tdrawable, mode, palette, alg):
    dither = {0 : floyd_stein,
           1 : jarvis,
           2 : stucki,
           3 : atkinson,
           4 : burkes,
           5 : sierra3,
           6 : sierra2,
           7 : sierra1,
    }
    pdb.gimp_image_undo_group_start(timg)
    try:
        layer = tdrawable.copy()
        timg.add_layer(layer, 0)
        width = layer.width
        height = layer.height
        px_size = pdb.gimp_drawable_bpp(tdrawable)
        dim = width, height, px_size
        rgn = layer.get_pixel_rgn(0, 0, width, height, TRUE, FALSE)
        src_pixels = array("B", rgn[0:width, 0:height])        
        
        i=0
        total=px_size*width*height
        if mode == 1:
            num_colors, colors = pdb.gimp_palette_get_colors(palette)
            for y in range(height):
                for x in range(width):
                    pixel = src_pixels[i:i+px_size]
                    dist = [px_dist(colors[c],pixel) for c in range(num_colors)]                
                    nearest = colors[dist.index(min(dist))][0:px_size]
                    src_pixels[i:i+px_size] = array("B",nearest)
                    px_delta = [(a-b) for a,b in zip(pixel,src_pixels[i:i+px_size])]
                    dither[alg](dim, src_pixels, x, y, px_delta)
                    gimp.progress_update(i*1.0/total)
                    i = i + px_size
            
            rgn[0:width, 0:height] = src_pixels.tostring()
            layer.flush()
            layer.update(0,0,width,height)
            pdb.gimp_image_convert_indexed(timg, NO_DITHER, CUSTOM_PALETTE, 0, FALSE, FALSE, palette)
        else:
            white = [255] * px_size
            black = [0] * px_size
            for y in range(height):
                for x in range(width):
                    pixel = src_pixels[i:i+px_size]
                    dist = sum(pixel)/px_size
                    if dist > 127:
                        nearest = white
                    else:
                        nearest = black
                    src_pixels[i:i+px_size] = array("B",nearest)
                    px_delta = [(a-b) for a,b in zip(pixel,src_pixels[i:i+px_size])]
                    dither[alg](dim, src_pixels, x, y, px_delta)
                    gimp.progress_update(i*1.0/total)
                    i = i + px_size
                    
            rgn[0:width, 0:height] = src_pixels.tostring()
            layer.flush()
            layer.update(0,0,width,height)
            pdb.gimp_image_convert_indexed(timg, NO_DITHER, MONO_PALETTE, 0, FALSE, FALSE, palette)
        
        pdb.gimp_image_undo_group_end(timg)

    except Exception, err:
        pdb.gimp_message("ERR: " + str(err))
        pdb.gimp_image_undo_group_end(timg)

register(
        "retro_dither",
        "Error-diffusion dithering algorithms to create low resolution pictures in B&W or with a limited palette",
        "Error-diffusion dithering algorithms",
        "Mario Patino",
        "Mario Patino",
        "2014",
        "<Image>/Colors/Dither...",
        "RGB*, GRAY*",
        [
          (PF_RADIO, "mode", "Dithering mode:", 0, (("Monochrome",0),("Color", 1))),
          (PF_PALETTE, "palette", "Palette:", "Default"),
          (PF_OPTION,"alg",   "Dithering algorithm:", 0, ["Floyd-Steinberg","Jarvis, Judice, and Ninke","Stucki","Atkinson", "Burkes", "Sierra", "Two-Row Sierra", "Sierra Lite"])
        ],
        [],
       retro_dither)

main()