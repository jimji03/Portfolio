#Jim Ji
#TheOfficePaint - Jim.py

from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

root = Tk()
root.withdraw()

screen = display.set_mode((1000,725))

init()
song = mixer.music.load("Songs/The Office Theme.mp3")
mixer.music.play(-1)

fnt = font.Font("Font/cyberbit.ttf",15)
small_fnt = font.Font("Font/cyberbit.ttf",12)

#Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
light_brown = (205,133,63)
gray = (112,138,144)
drawColour = (0,0,0)
colours_list = [red,green,blue,yellow,white,black,gray,light_brown]


#Background
behind_background1 = image.load("Pictures/worldsbestboss.jpg")
screen.blit(behind_background1,(0,0))
behind_background2 = image.load("Pictures/worldsbestboss.jpg")
screen.blit(behind_background2,(0,20))
background = image.load("Pictures/worldsbestboss.jpg") #Three backgrounds were added because there was a water mark at the bottom corner. They were added behind the
background_rect = screen.blit(background,(35,20))      #last background so that it would blend in since it was not blitted at (0,0)

office_sign = image.load("Pictures/officepaintsign.png")
screen.blit(office_sign,(400,15))

########
#Borders
########

#Border for the Color Display Square, Save and Load
for x in range(730,850,40):
    draw.rect(screen,black,(x,145,32,32))

#Tool Borders
for x in range(13,350,50):
    draw.rect(screen,black,(x,613,44,44))
    draw.rect(screen,black,(x,662,44,44))

#Stamp Borders
for x in range(380,580,60):
    draw.rect(screen,black,(x,605,50,50))
    draw.rect(screen,black,(x,665,50,50))

#Display Text Box
draw.rect(screen,black,(12,10,200,80))
draw.rect(screen,white,(15,13,194,74))

#Color Palette
draw.rect(screen,white,(730,10,245,125))
draw.rect(screen,black,(730,10,245,125),3)

colorpalette_pic = image.load("Pictures/colorpalette.jpg")
colorpalette_rect = screen.blit(colorpalette_pic,(733,13))


#Canvas
canvas_border = draw.rect(screen,black,(12,97,686,456),3)
canvasrect = Rect(15,100,680,450)

def canvas():
    canvas_rect = draw.rect(screen,white,canvasrect)
    return canvas_rect
rect_canvas = canvas()

#Thickness Selection Border
draw.rect(screen,black,(914,639,79,79))

#######
#Images
#######

#Note: Variable names for pictures that end with 2, are for the colorless pictures

#Pencil

pencil_text1 = "Pencil Tool:"
pencil_text2 = "Draw anywhere on the canvas."

pencil_text_pic1 = fnt.render(pencil_text1, True, black)
pencil_text_pic2 = small_fnt.render(pencil_text2, True, black)

def text_pencil():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(pencil_text_pic1,(16,13))
    screen.blit(pencil_text_pic2,(16,35))
text_pencil() #since pencil is the default tool, the text for the tool should already be displayed when the program opens

pencil_pic1 = image.load("Pictures/pencil.jpg") 
def pencil_pics1():
    pencil_rect1 = screen.blit(pencil_pic1,(17,617))

pencil_pic2 = image.load("Pictures/pencil_colorless.jpg")
def pencil_pics2():
    pencil_rect2 = screen.blit(pencil_pic2,(17,617))
    return pencil_rect2 #This is return because it is also used outside the function
rect_pencil2 = pencil_pics2()

rect_pencil1 = pencil_pics1()#The pencil picture with color is displayed first because the tool is Pencil

#The following code is the same concept

#Eraser

eraser_text1 = "Eraser Tool:"
eraser_text2 = "Erase anything on the canvas. Scroll"
eraser_text3 = "to change the size."
eraser_text_pic1 = fnt.render(eraser_text1, True, black)
eraser_text_pic2 = small_fnt.render(eraser_text2, True, black)
eraser_text_pic3 = small_fnt.render(eraser_text3, True, black)

def text_eraser():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(eraser_text_pic1,(16,13))
    screen.blit(eraser_text_pic2,(16,35))
    screen.blit(eraser_text_pic3,(16,52))

eraser_pic1 = image.load("Pictures/eraser.png")
def eraser_pics1():
    eraser_rect1 = screen.blit(eraser_pic1,(67,617))

eraser_pic2 = image.load("Pictures/eraser_colorless.png")
def eraser_pics2():
    eraser_rect2 = screen.blit(eraser_pic2,(67,617))
    return eraser_rect2
rect_eraser2 = eraser_pics2()

#Paint Brush

paintbrush_text1 = "Paint Brush Tool:"
paintbrush_text2 = "Paint anywhere on the canvas. Scroll"
paintbrush_text3 = "to change the size."
paintbrush_text_pic1 = fnt.render(paintbrush_text1, True, black)
paintbrush_text_pic2 = small_fnt.render(paintbrush_text2, True, black)
paintbrush_text_pic3 = small_fnt.render(paintbrush_text3, True, black)

def text_paintbrush():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(paintbrush_text_pic1,(16,13))
    screen.blit(paintbrush_text_pic2,(16,35))
    screen.blit(paintbrush_text_pic3,(16,52))

paintbrush_pic1 = image.load("Pictures/paint brush.png")
def paintbrush_pics1():
    paintbrush_rect1  = screen.blit(paintbrush_pic1,(117,617))

paintbrush_pic2 = image.load("Pictures/paint brush_colorless.png")
def paintbrush_pics2():
    paintbrush_rect2 = screen.blit(paintbrush_pic2,(117,617))
    return paintbrush_rect2
rect_paintbrush2 = paintbrush_pics2()

#Eye Dropeer

eyedropper_text1 = "Eye Dropper Tool:"
eyedropper_text2 = "Click anywhwere on the the canvas"
eyedropper_text3 = "to select a colour."
eyedropper_text_pic1 = fnt.render(eyedropper_text1, True, black)
eyedropper_text_pic2 = small_fnt.render(eyedropper_text2, True, black)
eyedropper_text_pic3 = small_fnt.render(eyedropper_text3, True, black)

def text_eyedropper():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(eyedropper_text_pic1,(16,13))
    screen.blit(eyedropper_text_pic2,(16,35))
    screen.blit(eyedropper_text_pic3,(16,52))

dropper_pic1 = image.load("Pictures/eyedropper.jpg")
def dropper_pics1():
    dropper_rect1 = screen.blit(dropper_pic1,(167,617))

dropper_pic2 = image.load("Pictures/eyedropper_colorless.jpg")
def dropper_pics2():
    dropper_rect2 = screen.blit(dropper_pic2,(167,617))
    return dropper_rect2
rect_dropper2 = dropper_pics2()

#Bucket

bucket_text1 = "Bucket Tool:"
bucket_text2 = "Fill the canvas with the selected"
bucket_text3 = "colour."
bucket_text_pic1 = fnt.render(bucket_text1, True, black)
bucket_text_pic2 = small_fnt.render(bucket_text2, True, black)
bucket_text_pic3 = small_fnt.render(bucket_text3, True, black)

def text_bucket():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(bucket_text_pic1,(16,13))
    screen.blit(bucket_text_pic2,(16,35))
    screen.blit(bucket_text_pic3,(16,52))

bucket_pic1 = image.load("Pictures/bucket.png")
def bucket_pics1():
    bucket_rect1 = screen.blit(bucket_pic1,(217,617))

bucket_pic2 = image.load("Pictures/bucket_colorless.png")
def bucket_pics2():
    bucket_rect2 = screen.blit(bucket_pic2,(217,617))
    return bucket_rect2
rect_bucket2 = bucket_pics2() 

#Spray Can

spraycan_text1 = "Spray Can Tool:"
spraycan_text2 = "Spray paint anywhere on the canvas."
spraycan_text3 = "Scroll to change the size."
spraycan_text_pic1 = fnt.render(spraycan_text1, True, black)
spraycan_text_pic2 = small_fnt.render(spraycan_text2, True, black)
spraycan_text_pic3 = small_fnt.render(spraycan_text3, True, black)

def text_spraycan():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(spraycan_text_pic1,(16,13))
    screen.blit(spraycan_text_pic2,(16,35))
    screen.blit(spraycan_text_pic3,(16,52))

spraycan_pic1 = image.load("Pictures/spraycan.png")
def spraycan_pics1():
    spraycan_rect1 = screen.blit(spraycan_pic1,(267,617))

spraycan_pic2 = image.load("Pictures/spraycan_colorless.png")
def spraycan_pics2():
    spraycan_rect2 = screen.blit(spraycan_pic2,(267,617))
    return spraycan_rect2
rect_spraycan2 = spraycan_pics2()

#Highlighter

highlighter_text1 = "Highlighter Tool:"
highlighter_text2 = "Highlight anything on the canvas."
highlighter_text_pic1 = fnt.render(highlighter_text1, True, black)
highlighter_text_pic2 = small_fnt.render(highlighter_text2, True, black)

def text_highlighter():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(highlighter_text_pic1,(16,13))
    screen.blit(highlighter_text_pic2,(16,35))

highlighter_pic1 = image.load("Pictures/highlighter.png")
def highlighter_pics1():
    highlighter_rect1 = screen.blit(highlighter_pic1,(317,617))

highlighter_pic2 = image.load("Pictures/highlighter_colorless.png")
def highlighter_pics2():
    highlighter_rect2 = screen.blit(highlighter_pic2,(317,617))
    return highlighter_rect2
rect_highlighter2 = highlighter_pics2()

highlighter_tool = Surface((20,10),SRCALPHA)
#Highlighter Surface
draw.circle(highlighter_tool,(255,255,0,25),(10,10),10)


#Unfilled Circle

unfilledcirc_text1 = "Unfilled Circle Tool:"
unfilledcirc_text2 = "Draw an unfilled circle anywhere"
unfilledcirc_text3 = "on the canvas."
unfilledcirc_text_pic1 = fnt.render(unfilledcirc_text1, True, black)
unfilledcirc_text_pic2 = small_fnt.render(unfilledcirc_text2, True, black)
unfilledcirc_text_pic3 = small_fnt.render(unfilledcirc_text3, True, black)

def text_unfilledcirc():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(unfilledcirc_text_pic1,(16,13))
    screen.blit(unfilledcirc_text_pic2,(16,35))
    screen.blit(unfilledcirc_text_pic3,(16,52))

def unfilled_circle1():
    unfilled_circ1 = draw.ellipse(screen,red,(18,667,34,34),4)

def unfilled_circle2():
    draw.rect(screen,white,(17,666,36,36))
    unfilled_circ2 = draw.ellipse(screen,gray,(18,667,34,34),4)
    return unfilled_circ2
circ_unfilled2 = unfilled_circle2()

#Filled Circle

filledcirc_text1 = "Filled Circle Tool:"
filledcirc_text2 = "Draw a filled circle anywhere on the"
filledcirc_text3 = "canvas."
filledcirc_text_pic1 = fnt.render(filledcirc_text1, True, black)
filledcirc_text_pic2 = small_fnt.render(filledcirc_text2, True, black)
filledcirc_text_pic3 = small_fnt.render(filledcirc_text3, True, black)

def text_filledcirc():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(filledcirc_text_pic1,(16,13))
    screen.blit(filledcirc_text_pic2,(16,35))
    screen.blit(filledcirc_text_pic3,(16,52))

def filled_circle1():
    filled_circ1 = draw.ellipse(screen,red,(68,667,34,34))

def filled_circle2():
    draw.rect(screen,white,(67,666,36,36))
    filled_circ2 = draw.ellipse(screen,gray,(68,667,34,34))
    return filled_circ2
circ_filled2 = filled_circle2()

#Unfilled Rectangle

unfilledrect_text1 = "Unfilled Rectangle Tool:"
unfilledrect_text2 = "Draw an unfilled rectangle"
unfilledrect_text3 = "anywhere on the canvas."
unfilledrect_text_pic1 = fnt.render(unfilledrect_text1, True, black)
unfilledrect_text_pic2 = small_fnt.render(unfilledrect_text2, True, black)
unfilledrect_text_pic3 = small_fnt.render(unfilledrect_text3, True, black)

def text_unfilledrect():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(unfilledrect_text_pic1,(16,13))
    screen.blit(unfilledrect_text_pic2,(16,35))
    screen.blit(unfilledrect_text_pic3,(16,52))

def unfilled_rectangle1():
    unfilled_rectangle_rect1 = draw.rect(screen,white,(117,666,36,36))
    unfilled_rect1 = draw.rect(screen,red,(121,673,28,22),3)

def unfilled_rectangle2():
    unfilled_rectangle_rect2 = draw.rect(screen,white,(117,666,36,36))
    unfilled_rect2 = draw.rect(screen,gray,(121,673,28,22),3)
    return unfilled_rectangle_rect2, unfilled_rect2
unfilled_rect_rectangle2, rect_unfilled2 = unfilled_rectangle2()

#Filled Rectangle

filledrect_text1 = "Filled Rectangle Tool:"
filledrect_text2 = "Draw a filled rectangle anywhere"
filledrect_text3 = "on the canvas."
filledrect_text_pic1 = fnt.render(filledrect_text1, True, black)
filledrect_text_pic2 = small_fnt.render(filledrect_text2, True, black)
filledrect_text_pic3 = small_fnt.render(filledrect_text3, True, black)

def text_filledrect():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(filledrect_text_pic1,(16,13))
    screen.blit(filledrect_text_pic2,(16,35))
    screen.blit(filledrect_text_pic3,(16,52))

def filled_rectangle1():
    filled_rectangle_rect1 = draw.rect(screen,white,(167,666,36,36))
    filled_rect1 = draw.rect(screen,red,(171,673,28,22))

def filled_rectangle2():
    filled_rectangle_rect2 = draw.rect(screen,white,(167,666,36,36))
    filled_rect2 = draw.rect(screen,gray,(171,673,28,22))
    return filled_rectangle_rect2, filled_rect2
filled_rect_rectangle2, rect_filled2 = filled_rectangle2()

#Line

line_text1 = "Line Tool:"
line_text2 = "Draw a straight line anywhere"
line_text3 = "on the canvas"
line_text_pic1 = fnt.render(line_text1, True, black)
line_text_pic2 = small_fnt.render(line_text2, True, black)
line_text_pic3 = small_fnt.render(line_text3, True, black)

def text_line():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(line_text_pic1,(16,13))
    screen.blit(line_text_pic2,(16,35))
    screen.blit(line_text_pic3,(16,52))
    
def line1():
    line_rect1 = draw.rect(screen,white,(217,666,36,36))
    colored_line = draw.line(screen,red,(221,697),(247,670),5)

def line2():
    line_rect2 = draw.rect(screen,white,(217,666,36,36))
    uncolored_line = draw.line(screen,gray,(221,697),(247,670),5)
    return line_rect2, uncolored_line
rect_line2, line_2 = line2()

#Polygon

polygon_text1 = "Polygon Tool:"
polygon_text2 = "Right click to select a set of points"
polygon_text3 = "Left click to connect the dots."
polygon_text_pic1 = fnt.render(polygon_text1, True, black)
polygon_text_pic2 = small_fnt.render(polygon_text2, True, black)
polygon_text_pic3 = small_fnt.render(polygon_text3, True, black)

def text_polygon():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(polygon_text_pic1,(16,13))
    screen.blit(polygon_text_pic2,(16,35))
    screen.blit(polygon_text_pic3,(16,52))

poly_points = [(270,669),(300,672),(296,694),(300,699),(270,699),(277,692)]
def polygon1():
    polygon_rect1 = draw.rect(screen,white,(267,666,36,36))
    polygon_pic1 = draw.polygon(screen,red,poly_points,2)

def polygon2():
    polygon_rect2 = draw.rect(screen,white,(267,666,36,36))
    polygon_pic2 = draw.polygon(screen,gray,poly_points,2)
    return polygon_rect2, polygon_pic2
rect_polygon2,pic_polygon2 = polygon2()

#Sprinkles

sprinkle_text1 = "Sprinkles Tool:"
sprinkle_text2 = "Click on the canvas to draw"
sprinkle_text3 = "sprinkles. Scroll to change the size."
sprinkles_text_pic1 = fnt.render(sprinkle_text1, True, black)
sprinkles_text_pic2 = small_fnt.render(sprinkle_text2, True, black)
sprinkles_text_pic3 = small_fnt.render(sprinkle_text3, True, black)

def text_sprinkles():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(sprinkles_text_pic1,(16,13))
    screen.blit(sprinkles_text_pic2,(16,35))
    screen.blit(sprinkles_text_pic3,(16,52))

sprinkles_pic1 = image.load("Pictures/sprinkles.png")
def sprinkles_pics1():
    sprinkles_rect1 = screen.blit(sprinkles_pic1,(317,666))

sprinkles_pic2 = image.load("Pictures/sprinkles_colorless.png")
def sprinkles_pics2():
    sprinkles_rect2 = screen.blit(sprinkles_pic2,(317,666))
    return sprinkles_rect2
rect_sprinkles2 = sprinkles_pics2()

#Save
save_pic1 = image.load("Pictures/save.png")
def save1():
    save_rect1 = screen.blit(save_pic1,(773,148))
    return save_rect1
rect_save1 = save1()

save_pic2 = image.load("Pictures/save_colorless.png")
def save2():
    save_rect2 = screen.blit(save_pic2,(773,148))
    return save_rect2
rect_save2 = save2()

#Load
load_pic1 = image.load("Pictures/load.png")
def load1():
    load_rect1 = screen.blit(load_pic1,(813,148))
    return load_rect1
rect_load1 = load1()

load_pic2 = image.load("Pictures/load_colorless.png")
def load2():
    load_rect2 = screen.blit(load_pic2,(813,148))
    return load_rect2
rect_load2 = load2()

#Eraser All
eraserall_border = draw.rect(screen,black,(12,550,32,32))

eraseall_pic1 = image.load("Pictures/erase-all.png")
def eraseall_pics1():
    eraseall_rect1 = screen.blit(eraseall_pic1,(15,553))
    return eraseall_rect1
rect_eraseall1 = eraseall_pics1()

eraseall_pic2 = image.load("Pictures/erase-all_colorless.png")
def eraseall_pics2():
    eraseall_rect2 = screen.blit(eraseall_pic2,(15,553))
    return eraseall_rect2
rect_eraseall2 = eraseall_pics2()

#Undo
undo_border = draw.rect(screen,black,(41,550,32,32))

undo_pic1 = image.load("Pictures/undo.png")
def undo_pics1():
    undo_rect1 = screen.blit(undo_pic1,(44,553))
    return undo_rect1
rect_undo1 = undo_pics1()

undo_pic2 = image.load("Pictures/undo_colorless.png")
def undo_pics2():
    undo_rect2 = screen.blit(undo_pic2,(44,553))
    return undo_rect2
rect_undo2 = undo_pics2()

#Redo
redo_border = draw.rect(screen,black,(70,550,32,32))

redo_pic1 = image.load("Pictures/redo.png")
def redo_pics1():
    redo_rect1 = screen.blit(redo_pic1,(73,553))
    return redo_rect1
rect_redo1 = redo_pics1()

redo_pic2 = image.load("Pictures/redo_colorless.png")
def redo_pics2():
    redo_rect2 = screen.blit(redo_pic2,(73,553))
    return redo_rect2
rect_redo2 = redo_pics2()

##########################
#Play, Pause, Stop Buttons
##########################

#Play, Pause, Stop Borders
for x in range(793,910,40):
    draw.rect(screen,black,(x,686,32,32))

play_pic = image.load("Pictures/Button_Play.jpg")
play_rect = screen.blit(play_pic,(796,689))

pause_pic = image.load("Pictures/Button_Pause.jpg")
pause_rect = screen.blit(pause_pic,(836,689))

stop_pic = image.load("Pictures/Button_Stop.jpg")
stop_rect = screen.blit(stop_pic,(876,689))

#######
#Stamps
#######

#Michael
michael_stamp = image.load("Stamps/Michael Stamp.png")

mike_text1 = "Michael Scott:"
mike_text2 = "The former Regional Manager of"
mike_text3 = "Dunder Mifflin Sabre, Scranton."
mike_text_pic1 = fnt.render(mike_text1, True, black)
mike_text_pic2 = small_fnt.render(mike_text2, True, black)
mike_text_pic3 = small_fnt.render(mike_text3, True, black)

def text_mike():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(mike_text_pic1,(16,13))
    screen.blit(mike_text_pic2,(16,35))
    screen.blit(mike_text_pic3,(16,52))

mike_pic1 = image.load("Pictures/Michael_Head.png")
def mike1():
    mike_rect1 = screen.blit(mike_pic1,(383,608))

mike_pic2 = image.load("Pictures/Michael_Head_colorless.png")
def mike2():
    mike_rect2 = screen.blit(mike_pic2,(383,608))
    return mike_rect2
rect_mike2 = mike2()

#Dwight
dwight_stamp = image.load("Stamps/Dwight Stamp.png")

dwight_text1 = "Dwight Schrute:"
dwight_text2 = "The current Regional Manager of"
dwight_text3 = "Dunder Mifflin Sabre, Scranton."
dwight_text_pic1 = fnt.render(dwight_text1, True, black)
dwight_text_pic2 = small_fnt.render(dwight_text2, True, black)
dwight_text_pic3 = small_fnt.render(dwight_text3, True, black)

def text_dwight():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(dwight_text_pic1,(16,13))
    screen.blit(dwight_text_pic2,(16,35))
    screen.blit(dwight_text_pic3,(16,52))

dwight_pic1 = image.load("Pictures/dwight_head.png")
def dwight1():
    dwight_rect1 = screen.blit(dwight_pic1,(443,608))

dwight_pic2 = image.load("Pictures/dwight_head_colorless.png")
def dwight2():
    dwight_rect2 = screen.blit(dwight_pic2,(443,608))
    return dwight_rect2
rect_dwight2 = dwight2()

#Angela
angela_stamp = image.load("Stamps/Angela Stamp.png")

angela_text1 = "Angela Schrute:"
angela_text2 = "A senior accountant at Dunder"
angela_text3 = "Mifflin Sabre, Scranton."
angela_text_pic1 = fnt.render(angela_text1, True, black)
angela_text_pic2 = small_fnt.render(angela_text2, True, black)
angela_text_pic3 = small_fnt.render(angela_text3, True, black)

def text_angela():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(angela_text_pic1,(16,13))
    screen.blit(angela_text_pic2,(16,35))
    screen.blit(angela_text_pic3,(16,52))

angela_pic1 = image.load("Pictures/Angela_head.png")
def angela1():
    angela_rect1 = screen.blit(angela_pic1,(503,608))

angela_pic2 = image.load("Pictures/Angela_head_colorless.png")
def angela2():
    angela_rect2 = screen.blit(angela_pic2,(503,608))
    return angela_rect2
rect_angela2 = angela2()

#Stanley
stanley_stamp = image.load("Stamps/Stanley Stamp.png")

stanley_text1 = "Stanley Hudson:"
stanley_text2 = "A senior sales representative"
stanley_text3 = "at Dunder Mifflin Sabre, Scranton."
stanley_text_pic1 = fnt.render(stanley_text1, True, black)
stanley_text_pic2 = small_fnt.render(stanley_text2, True, black)
stanley_text_pic3 = small_fnt.render(stanley_text3, True, black)

def text_stanley():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(stanley_text_pic1,(16,13))
    screen.blit(stanley_text_pic2,(16,35))
    screen.blit(stanley_text_pic3,(16,52))

stanley_pic1 = image.load("Pictures/Stanley_head.png")
def stanley1():
    stanley_rect1 = screen.blit(stanley_pic1,(563,608))

stanley_pic2 = image.load("Pictures/Stanley_head_colorless.png")
def stanley2():
    stanley_rect2 = screen.blit(stanley_pic2,(563,608))
    return stanley_rect2
rect_stanley2 = stanley2()

#Jim
jim_stamp = image.load("Stamps/Jim Stamp.png")

jim_text1 = "Jim Halpert:"
jim_text2 = "The current Assistant to the"
jim_text3 = "Regional Manager of Dunder"
jim_text4 = "Mifflin Sabre, Scranton."
jim_text_pic1 = fnt.render(jim_text1, True, black)
jim_text_pic2 = small_fnt.render(jim_text2, True, black)
jim_text_pic3 = small_fnt.render(jim_text3, True, black)
jim_text_pic4 = small_fnt.render(jim_text4, True, black)

def text_jim():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(jim_text_pic1,(16,13))
    screen.blit(jim_text_pic2,(16,35))
    screen.blit(jim_text_pic3,(16,52))
    screen.blit(jim_text_pic4,(16,69))

jim_pic1 = image.load("Pictures/Jim_head.png")
def jim1():
    jim_rect1 = screen.blit(jim_pic1,(383,668))

jim_pic2 = image.load("Pictures/Jim_head_colorless.png")
def jim2():
    jim_rect2 = screen.blit(jim_pic2,(383,668))
    return jim_rect2
rect_jim2 = jim2()

#Pamela
pam_stamp = image.load("Stamps/Pam Stamp.png")

pam_text1 = "Pamela Halpert:"
pam_text2 = "The former secretary. Currently"
pam_text3 = "the Office Administrator for"
pam_text4 = "Dunder Mifflin Sabre, Scranton."
pam_text_pic1 = fnt.render(pam_text1, True, black)
pam_text_pic2 = small_fnt.render(pam_text2, True, black)
pam_text_pic3 = small_fnt.render(pam_text3, True, black)
pam_text_pic4 = small_fnt.render(pam_text4, True, black)

def text_pam():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(pam_text_pic1,(16,13))
    screen.blit(pam_text_pic2,(16,35))
    screen.blit(pam_text_pic3,(16,52))
    screen.blit(pam_text_pic4,(16,69))

pam_pic1 = image.load("Pictures/Pam_head.png")
def pam1():
    pam_rect1 = screen.blit(pam_pic1,(443,668))

pam_pic2 = image.load("Pictures/Pam_head_colorless.png")
def pam2():
    pam_rect2 = screen.blit(pam_pic2,(443,668))
    return pam_rect2
rect_pam2 = pam2()

#Kevin
kevin_stamp = image.load("Stamps/Kevin Stamp.png")

kevin_text1 = "Kevin Malone:"
kevin_text2 = "A former accountant at Dunder"
kevin_text3 = "Mifflin Sabre, Scranton. Currently"
kevin_text4 = "an owner of a bar."
kevin_text_pic1 = fnt.render(kevin_text1, True, black)
kevin_text_pic2 = small_fnt.render(kevin_text2, True, black)
kevin_text_pic3 = small_fnt.render(kevin_text3, True, black)
kevin_text_pic4 = small_fnt.render(kevin_text4, True, black)

def text_kevin():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(kevin_text_pic1,(16,13))
    screen.blit(kevin_text_pic2,(16,35))
    screen.blit(kevin_text_pic3,(16,52))
    screen.blit(kevin_text_pic4,(16,69))

kevin_pic1 = image.load("Pictures/Kevin_head.png")
def kevin1():
    kevin_rect1 = screen.blit(kevin_pic1,(503,668))

kevin_pic2 = image.load("Pictures/Kevin_head_colorless.png")
def kevin2():
    kevin_rect2 = screen.blit(kevin_pic2,(503,668))
    return kevin_rect2
rect_kevin2 = kevin2()

#Creed
creed_stamp = image.load("Stamps/Creed Stamp.png")

creed_text1 = "Creed Bratton:"
creed_text2 = "A former employee of Dunder Miffin"
creed_text3 = "Sabre, Scranton. Currently a fugitive"
creed_text4 = "who faked his own death."
creed_text_pic1 = fnt.render(creed_text1, True, black)
creed_text_pic2 = small_fnt.render(creed_text2, True, black)
creed_text_pic3 = small_fnt.render(creed_text3, True, black)
creed_text_pic4 = small_fnt.render(creed_text4, True, black)

def text_creed():
    draw.rect(screen,white,(15,13,194,74))
    screen.blit(creed_text_pic1,(16,13))
    screen.blit(creed_text_pic2,(16,35))
    screen.blit(creed_text_pic3,(16,52))
    screen.blit(creed_text_pic4,(16,69))

creed_pic1 = image.load("Pictures/Creed_head.png")
def creed1():
    creed_rect1 = screen.blit(creed_pic1,(563,668))

creed_pic2 = image.load("Pictures/Creed_head_colorless.png")
def creed2():
    creed_rect2 = screen.blit(creed_pic2,(563,668))
    return creed_rect2
rect_creed2 = creed2()

#Important Global Variables
colour = black
size = 10
tool = "pencil"
music = "pause"
point_lst = []
undo_list = []
copiedscreen = screen.subsurface(rect_canvas).copy() #Adds the first blank canvas into the list
undo_list.append(copiedscreen)
redo_list = []
screenshot = screen.copy
mx,my = 0,0
buttonDownLock = False 
click = False
right_click = False

running = True

while running:
    if tool == "polygon":
        click = False
        right_click = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = mouse.get_pos()
            screenshot = screen.copy()
            if evt.button == 1:
                click = True
            if evt.button == 3:
                right_click = True
            if evt.button == 4 and size <= 30:
                size += 1
            if evt.button == 5 and size >=1:
                size -= 1
        if evt.type == MOUSEBUTTONUP:
            if click == True:
                copiedscreen = screen.subsurface(rect_canvas).copy()
                undo_list.append(copiedscreen)
            buttonDownLock = False
    #-------------------------------------------------------------------------
    #Clicking
    omx,omy = mx,my
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    screen.set_clip(None)
    draw.rect(screen,white,(918,643,71,71))
    thickness_select = draw.circle(screen,colour,(953,678),size)

    #Changing Colours on the Colour Palette
    if mb[0] == 1:
        if colorpalette_rect.collidepoint(mx,my):
            colour = screen.get_at((mx,my))

    #Colour Display Square
    draw.rect(screen,colour,(733,148,26,26))
            
    #Tool Selection
    if mb[0] == 1:
        if rect_pencil2.collidepoint(mx,my):    #When the uncolored picture is clicked, the colorled picture is blitted on top and the text display changes
            tool = "pencil"
            pencil_pics1()
            text_pencil()
        elif rect_eraser2.collidepoint(mx,my):
            tool = "eraser"
            eraser_pics1()
            size = 10
            text_eraser()
        elif rect_paintbrush2.collidepoint(mx,my):
            tool = "paintbrush"
            paintbrush_pics1()
            text_paintbrush()
        elif rect_dropper2.collidepoint(mx,my):
            tool = "dropper"
            dropper_pics1()
            text_eyedropper()
        elif rect_bucket2.collidepoint(mx,my):
            tool = "bucket"
            bucket_pics1()
            text_bucket()
        elif rect_spraycan2.collidepoint(mx,my):
            tool = "spray can"
            spraycan_pics1()
            text_spraycan()
        elif rect_highlighter2.collidepoint(mx,my):
            tool = "highlighter"
            highlighter_pics1()
            text_highlighter()
        elif circ_unfilled2.collidepoint(mx,my):
            tool = "unfilled circ"
            unfilled_circle1()
            text_unfilledcirc()
        elif circ_filled2.collidepoint(mx,my):
            tool = "filled circ"
            filled_circle1()
            text_filledcirc()
        elif rect_unfilled2.collidepoint(mx,my) or unfilled_rect_rectangle2.collidepoint(mx,my):
            tool = "unfilled rect"
            unfilled_rectangle1()
            text_unfilledrect()
        elif rect_filled2.collidepoint(mx,my) or filled_rect_rectangle2.collidepoint(mx,my):
            tool = "filled rect"
            filled_rectangle1()
            text_filledrect()
        elif line_2.collidepoint(mx,my) or rect_line2.collidepoint(mx,my):
            tool = "line"
            line1()
            text_line()
        elif pic_polygon2.collidepoint(mx,my) or rect_polygon2.collidepoint(mx,my):
            tool = "polygon"
            polygon1()
            text_polygon()
        elif rect_sprinkles2.collidepoint(mx,my):
            tool = "sprinkles"
            sprinkles_pics1()
            text_sprinkles()
            size = 2
 
        #Stamp
        if rect_mike2.collidepoint(mx,my):
            tool = "michael"
            mike1()
            text_mike()
        elif rect_dwight2.collidepoint(mx,my):
            tool = "dwight"
            dwight1()
            text_dwight()
        elif rect_angela2.collidepoint(mx,my):
            tool = "angela"
            angela1()
            text_angela()
        elif rect_jim2.collidepoint(mx,my):
            tool = "jim"
            jim1()
            text_jim()
        elif rect_pam2.collidepoint(mx,my):
            tool = "pam"
            pam1()
            text_pam()
        elif rect_stanley2.collidepoint(mx,my):
            tool = "stanley"
            stanley1()
            text_stanley()
        elif rect_creed2.collidepoint(mx,my):
            tool = "creed"
            creed1()
            text_creed()
        elif rect_kevin2.collidepoint(mx,my):
            tool = "kevin"
            kevin1()
            text_kevin()
        
    #Changing Icon Colors
    if tool != "pencil":                 
        if rect_pencil2.collidepoint(mx,my):          #When mouse hovers over uncolored picture the colorled picture is blitted on top of it
            pencil_pics1()
        elif background_rect.collidepoint(mx,my):     #When the mouse hovers overs the background, the uncolored picture is blitted back on
            pencil_pics2()                            #The following code is the same concept
            
    if tool != "eraser":
        if rect_eraser2.collidepoint(mx,my):
            eraser_pics1()
        elif background_rect.collidepoint(mx,my):
            eraser_pics2()

    if tool != "paintbrush":
        if rect_paintbrush2.collidepoint(mx,my):
            paintbrush_pics1()
        elif background_rect.collidepoint(mx,my):
            paintbrush_pics2()
            
    if tool != "dropper":
        if rect_dropper2.collidepoint(mx,my):
            dropper_pics1()
        elif background_rect.collidepoint(mx,my):
            dropper_pics2()

    if tool != "bucket":
        if rect_bucket2.collidepoint(mx,my):
            bucket_pics1()
        elif background_rect.collidepoint(mx,my):
            bucket_pics2()

    if tool != "spray can":
        if rect_spraycan2.collidepoint(mx,my):
            spraycan_pics1()
        elif background_rect.collidepoint(mx,my):
            spraycan_pics2()

    if tool != "highlighter":
        if rect_highlighter2.collidepoint(mx,my):
            highlighter_pics1()
        elif background_rect.collidepoint(mx,my):
            highlighter_pics2()

    if tool != "unfilled circ":
        if circ_unfilled2.collidepoint(mx,my):
            unfilled_circle1()
        elif background_rect.collidepoint(mx,my):
            unfilled_circle2()

    if tool != "filled circ":
        if circ_filled2.collidepoint(mx,my):
            filled_circle1()
        elif background_rect.collidepoint(mx,my):
            filled_circle2()

    if tool != "unfilled rect":
        if rect_unfilled2.collidepoint(mx,my):
            unfilled_rectangle1()
        elif background_rect.collidepoint(mx,my):
            unfilled_rectangle2()

    if tool != "filled rect":
        if rect_filled2.collidepoint(mx,my):
            filled_rectangle1()
        elif background_rect.collidepoint(mx,my):
            filled_rectangle2()

    if tool != "line":
        if line_2.collidepoint(mx,my) or rect_line2.collidepoint(mx,my):
            line1()
        elif background_rect.collidepoint(mx,my):
            line2()

    if tool != "polygon":
        if pic_polygon2.collidepoint(mx,my) or rect_polygon2.collidepoint(mx,my):
            polygon1()
        elif background_rect.collidepoint(mx,my):
            polygon2()

    if tool != "sprinkles":
        if rect_sprinkles2.collidepoint(mx,my):
            sprinkles_pics1()
        elif background_rect.collidepoint(mx,my):
            sprinkles_pics2()

    #Stamps
    if tool != "stanley":
        if rect_stanley2.collidepoint(mx,my):
            stanley1()
        elif background_rect.collidepoint(mx,my):
            stanley2()

    if tool != "creed":
        if rect_creed2.collidepoint(mx,my):
            creed1()
        elif background_rect.collidepoint(mx,my):
            creed2()

    if tool != "kevin":
        if rect_kevin2.collidepoint(mx,my):
            kevin1()
        elif background_rect.collidepoint(mx,my):
            kevin2()

    if tool != "michael":
        if rect_mike2.collidepoint(mx,my):
            mike1()
        elif background_rect.collidepoint(mx,my):
            mike2()

    if tool != "dwight":
        if rect_dwight2.collidepoint(mx,my):
            dwight1()
        elif background_rect.collidepoint(mx,my):
            dwight2()

    if tool != "angela":
        if rect_angela2.collidepoint(mx,my):
            angela1()
        elif background_rect.collidepoint(mx,my):
            angela2()

    if tool != "jim":
        if rect_jim2.collidepoint(mx,my):
            jim1()
        elif background_rect.collidepoint(mx,my):
            jim2()

    if tool != "pam":
        if rect_pam2.collidepoint(mx,my):
            pam1()
        elif background_rect.collidepoint(mx,my):
            pam2()

    if rect_save2.collidepoint(mx,my):
        save1()
    elif background_rect.collidepoint(mx,my):
        save2()
    if rect_load2.collidepoint(mx,my):
        load1()
    elif background_rect.collidepoint(mx,my):
        load2()
    if rect_eraseall2.collidepoint(mx,my):
        eraseall_pics1()
    elif background_rect.collidepoint(mx,my):
        eraseall_pics2()
    if rect_undo2.collidepoint(mx,my):
        undo_pics1()
    elif background_rect.collidepoint(mx,my):
        undo_pics2()
    if rect_redo2.collidepoint(mx,my):
        redo_pics1()
    elif background_rect.collidepoint(mx,my):
        redo_pics2()

    #Paint 
    if mb[0] == 1:
        if click:

            #This allows the user to select the name of canvas image that they want to save and then it saves the image
            if rect_save1.collidepoint(mx,my):
                save_image = asksaveasfilename(defaultextension = ".png") 
                image.save(screen.subsurface(rect_canvas),save_image) 

            #This allows the user to selected an desired image, once its selected it loads the image and then blits it onto the canvas for the user to edit
            if rect_load1.collidepoint(mx,my):
                open_image = askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")]) 
                open_image_pic = image.load(open_image) 
                screen.blit(open_image_pic,(15,100)) 

        #Once this code is selected, it screenshots the canvas and adds it to undo_list, this allows the user to reaccess their last canvas if they press undo
        #It then calls on the canvas() function to draw a white rectangle the size of the canvas
        if rect_eraseall1.collidepoint(mx,my) and not buttonDownLock: #buttonDownLock only allows this code to be used once per click so that it only makes one 
            buttonDownLock = True                                     #screenshot instead of many. This concept is used in following code
            copiedscreen = screen.subsurface(rect_canvas).copy()
            undo_list.append(copiedscreen) 
            canvas() #Draws a white rectangle on top of 

        #There must be more than one item in the list for this to work, it then takes the last item on undo_list, adds it to redo_list and deletes it from undo_list
        #Then the last item on the undo_list is blitted onto the canvas
        if rect_undo1.collidepoint(mx,my):
            if len(undo_list) > 1 and not buttonDownLock: #buttonDownLock
                buttonDownLock = True 
                undo_screen = undo_list.pop()
                redo_list.append(undo_screen)
                screen.blit(undo_list[-1],(15,100))

        if rect_redo1.collidepoint(mx,my):
            if len(redo_list) > 0 and not buttonDownLock:
                buttonDownLock = True
                redo_screen = redo_list.pop()
                undo_list.append(redo_screen)
                screen.blit(undo_list[-1],(15,100))

        if play_rect.collidepoint(mx,my) and music == "pause":
            mixer.music.unpause()
        if pause_rect.collidepoint(mx,my):
            mixer.music.pause()
            music = "pause"
        if stop_rect.collidepoint(mx,my):
            mixer.music.pause()
            music = "stop"
        if play_rect.collidepoint(mx,my) and music == "stop":
            mixer.music.play()
          
    
    
    #Drawing
    if mb[0] == 1:
        dx = mx - omx
        dy = my - omy
        distance = int(sqrt(dx**2 + dy**2))
        if rect_canvas.collidepoint(mx,my):
            
            screen.set_clip(rect_canvas)
            
            if tool == "pencil":
                draw.line(screen,colour,(omx,omy),(mx,my),2)
            elif tool == "eraser":
                draw.circle(screen,white,(mx,my),size)
                for i in range (1,distance + 1):
                    draw.circle(screen,white,(int(omx + i*dx/distance),int(omy + i*dy/distance)),size)

            #This tool used the distance formula to find the distance between the starting mouse position and the next mouse possition. The loop allows circles
            #to be drawn from the starting mouse position to the next, connecting them with circles. This code is used in the following code.
            elif tool == "paintbrush":
                draw.circle(screen,colour,(mx,my),size) #When mouse is not moved, no circle is drawn so this draws a circle when the mouse is not moving 
                for i in range (1,distance + 1):
                    draw.circle(screen,colour,(int(omx + i*dx/distance),int(omy + i*dy/distance)),size)

            #This tool changes the colour variable to which colour is at the mouse position on the canvas
            elif tool == "dropper":
                colour = screen.get_at((mx,my))

            #This tool fills the entire canvas
            elif tool == "bucket":
                draw.rect(screen,colour,canvasrect)

            #This tool uses the distance formula as well, it takes an random point, then checks if the distance from that random point to the mouse position is
            #is smaller or equal to the size which is the radius of the spray paint. If the distance is smaller or equal than it draws a circle at the random point.
            elif tool == "spray can":
                for i in range(100):
                    line_x = randint(mx - size, mx + size)
                    line_y = randint(my - size, my + size)
                    dist_x = mx - line_x
                    dist_y = my - line_y
                    line_dist = int(sqrt(dist_x**2 + dist_y**2))
                    if line_dist <= size:
                        draw.circle(screen,colour,(line_x, line_y),0)

            #This tool uses the same concept as paintbrush, but draws opaque yellow circles
            elif tool == "highlighter":
                screen.blit(highlighter_tool,(mx,my))
                for i in range (1,distance + 1):
                    screen.blit(highlighter_tool,(int(omx+i*dx/distance),int(omy+i*dy/distance)))

            #This tool draws an unfilled rectangle starting at the mouse position to the the distance from the current mouse position to the starting mouse position
            elif tool == "unfilled rect":
                screen.blit(screenshot,(0,0))
                draw.rect(screen,colour,(sx,sy,mx-sx,my-sy),4)

            #This tool draws an filled rectangle starting at the mouse position to the the distance, from the current mouse position to the starting mouse position
            elif tool == "filled rect":
                screen.blit(screenshot,(0,0))
                draw.rect(screen,colour,(sx,sy,mx-sx,my-sy))

            #This tool draws an unfilled circle to at the starting position to the position of the mouse
            elif tool == "unfilled circ":
                ellipse_rect = Rect(sx,sy,mx,my)
                ellipse_rect.normalize()
                screen.blit(screenshot,(0,0))
                draw.arc(screen,colour,ellipse_rect,0,360,4)

            #This tool draws an filled circle starting at the mouse position, from the current mouse position to the current mouse position
            elif tool == "filled circ":
                ellipse_rect = Rect(sx,sy,mx-sx,my-sy)
                ellipse_rect.normalize()
                screen.blit(screenshot,(0,0))
                draw.ellipse(screen,colour,ellipse_rect)

            #This tool draws an line from the starting mouse position to the current mouse position
            elif tool == "line":
                screen.blit(screenshot,(0,0))
                draw.line(screen,colour,(sx,sy),(mx,my),5)

            #This tool takes random points in a square surrounding the mouse position and draws lines from these random points to the mouse position
            elif tool == "sprinkles":
                for i in range(2):
                    line_x = randint(mx-40,mx+40)
                    line_y = randint(my-40,my+40)
                    rand_colour = choice(colours_list)
                    draw.line(screen,rand_colour,(line_x,line_y),(mx,my),size)

            #Stamps
            #This blits the stamp where the mouse position is
            if tool == "stanley":                               
                screen.blit(screenshot,(0,0))
                screen.blit(stanley_stamp,(mx-75,my-80))                
            elif tool == "creed":
                screen.blit(screenshot,(0,0))
                screen.blit(creed_stamp,(mx-100,my-60))
            elif tool == "kevin":
                screen.blit(screenshot,(0,0))
                screen.blit(kevin_stamp,(mx-70,my-100))
            elif tool == "michael":
                screen.blit(screenshot,(0,0))
                screen.blit(michael_stamp,(mx-145,my-115))
            elif tool == "dwight":
                screen.blit(screenshot,(0,0))
                screen.blit(dwight_stamp,(mx-115,my-100))
            elif tool == "angela":
                screen.blit(screenshot,(0,0))
                screen.blit(angela_stamp,(mx-75,my-100))
            elif tool == "jim":
                screen.blit(screenshot,(0,0))
                screen.blit(jim_stamp,(mx-40,my-80))
            elif tool == "pam":
                screen.blit(screenshot,(0,0))
                screen.blit(pam_stamp,(mx-65,my-70))


            

    #Polygon Tool

    #This tool allows the user to collect  set of points and when they right click it draws lines connecting the set of points
    if tool == "polygon":
        if click:  
            if rect_canvas.collidepoint(mx,my):
                screen.set_clip(rect_canvas)
                draw.circle(screen,colour,(mx,my),2) #To show what points where selected
                point_lst.append((sx,sy))
                polygon_colour = colour #If the user changes colour when points are already selected, this ensures that the drawned polygon is the same colour as
                #the points

        if right_click and len(point_lst) > 1:  #len(point_lst) > 1 was added so that it will not allow the user to right draw a polygon before selecting points
            if rect_canvas.collidepoint(mx,my):
                screen.set_clip(rect_canvas)
                draw.polygon(screen,polygon_colour,point_lst,5)
                point_lst[:] = [] #Deletes all contents of list
                        
    #This allows for click to work only on the canvas
    if mb[0] == 1 and tool != "polygon":
        if rect_canvas.collidepoint(mx,my):
            click = True
        else:
            click = False

        
    
    omx,omy = mx,my
                            
    #-------------------------------------------------------------------------

    display.flip()
quit()



















