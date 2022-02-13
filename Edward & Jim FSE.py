#Jim Ji and Edward Yang
#Pokemon Battle Game
#This game allows for a player to customize a 6 pokemon team out of 20 pokemons, once the team has been assembled,
#the player will battle against a bot with a randomized 6 pokemon team. During the battle the player can choose to
#switch out the active pokemon for another, or can attack the opposite active pokemon with one of their pokemon's
#4 moves. The team that defeats all the pokemon of their opponent is deemed the winner. After a winner is decided,
#the game will restart and the player can choose to assemble another team to battle again.


from pygame import *
from random import *
from math import *
import glob
init()
screen = display.set_mode((1000,600))

#COLOURS#
red = (255,0,0)
green = (0,255,0)
blue = (30,144,255)
yellow = (255,255,0)
orange = (255,140,0)
gray = (128,128,128)
white = (255,255,255)
purple = (148,0,211)
dark_purple = (128,0,128)
light_purple = (123,104,238)
gold = (218,165,32)
black = (0,0,0)
crimson = (178,34,34)
gray = (112,138,144)
darkGray = (66,71,86)

p1_col = white
p2_col = white
##################

#FONTS#
newyorkfont = font.Font("Font/newyorkescape.ttf",25)
smallfont = font.Font("Font/newyorkescape.ttf",20)
pokenamefont = font.Font("Font/newyorkescape.ttf",30)
########

#LISTS#
rect_lst = []
rect_lst_x = []
rect_lst_y = []

select_rect_lst = []
select_rect_lst_x = []
select_rect_lst_y = []

select_rect_lst_2 = []
select_rect_lst_2_x = []
select_rect_lst_2_y = []


poke_name_x = [60,85,84,75,92,76,15,35,60,80,25,90,97,99,13,98,85,80,50,90]

poke_sprite_x = [35,20,40,70,140,60,80,110,90,110,70,80,70,95,40,75,65,80,65,75]
poke_sprite_y = [325,340,285,330,400,365,330,330,315,365,320,300,300,330,320,330,300,330,310,330]
poke_name_col = [red,blue,blue,light_purple,yellow,gray,gold,blue,crimson,orange,crimson,
                 green,gray,yellow,blue,purple,gray,yellow,yellow,blue]
########################

#TEXT#
ready_txt = newyorkfont.render(("ENTER TO"),True,white)
ready_txt_2 = newyorkfont.render(("START!"), True, gold)

single_play_white = newyorkfont.render("SINGLE PLAYER",True,white)



back_white = smallfont.render("BACK",True,white)

single_play_blue = newyorkfont.render("SINGLE PLAYER",True,blue)


player1_txt = newyorkfont.render(("Player 1"), True, p1_col)
player2_txt = newyorkfont.render(("Player 2 (B0T)"), True, p2_col)

vs_txt = newyorkfont.render(("VS"), True, red)
##########################


#RECTS#
statsRect = (15,285,318,305)
p1Rect = (340,285,312,130)
p2Rect = (340,460,312,130)
back_rect = Rect(5,5,80,40)


p1_checkmarkRect = Rect(598,258,25,25)



p1_xRect = Rect(628,258,25,25)


startRect = Rect(410,380,200,86)

quitRect = Rect(460,500,100,43)

single_play_rect = Rect(380,200,275,65)
###################################
player = 1

p1_lst = []
p2_lst = []




#TRANSPARENT RECTS AND SURFACES#
transp_rect = Surface((60,60),SRCALPHA)      
transp_rect.fill((148,0,211,150))

transp_rect_2 = Surface((318,305),SRCALPHA)      
transp_rect_2.fill((148,0,211,150))

transp_rect_3 = Surface((312,130),SRCALPHA)      
transp_rect_3.fill((148,0,211,150))

transp_rect_4 = Surface((25,25),SRCALPHA)
transp_rect_4.fill((148,0,211,150))

transp_rect_5 = Surface((300,100),SRCALPHA)
transp_rect_5.fill((148,0,211,150))

transp_rect_6 = Surface((25,25),SRCALPHA)
transp_rect_6.fill((148,0,211,150))
###########################
mx,my = mouse.get_pos()

mode = "none"

f = 0
player = 1


def sprites_load(folder):
    pics = glob.glob("%s/*.gif" % (folder))
    imgs = []
    for i in range(len(pics)):
        yo = image.load(pics[i])
        imgs.append(yo)
    return imgs

def drawSprite(lst,frame,d,x,y):
    screen.blit(lst[frame//d%len(lst)],(x,y))

background = sprites_load("Frames/Select_screen_background_frames")

#MOVE DATA
#move = ["move name",sprite,"type",damage,accuracy,"special conditions"]
darkestLariat = ["Darkest Lariat",sprites_load("Move Frames/dark_effect_frames"),"Dark",85,100,"None"]
flareBlitz = ["Flare Blitz",sprites_load("Move Frames/fire frames"),"Fire",120,100,"Recoil Damage of 1/3 inflicted damage"]
earthquake = ["Earthquake",sprites_load("Move Frames/earth frames"),"Ground",100,100,"None"]
crossChop = ["Cross Chop",sprites_load("Move Frames/earth frames"),"Fighting",100,80,"None"]
scald = ["Scald",sprites_load("Move Frames/blizzard_frames"),80,100,"None"]
iceBeam = ["Ice Beam",sprites_load("Move Frames/blizzard_frames"),"Ice",90,100,"None"]
darkPulse = ["Dark Pulse",sprites_load("Move Frames/dark 2 frames"),"Dark",90,100,"None"]
extrasensory = ["Extrasensory",sprites_load("Move Frames/energy blast frames"),"Psychic",80,100,"None"]
dragonClaw = ["Dragon Claw",sprites_load("Move Frames/dark_effect_frames"),"Dragon",80,100,"None"]
rockSlide = ["Rock Slide",sprites_load("Move Frames/earth frames"),"Rock",70,90,"None"]
ironHead = ["Iron Head",sprites_load("Move Frames/star attack frames"),"Iron",80,100,"None"]
auraSphere = ["Aura Sphere",sprites_load("Move Frames/flash frames"),"Fighting",80,100,"None"]
extremeSpeed = ["Extreme Speed",sprites_load("Move Frames/flash frames"),"Normal",80,100,"Priority"]
closeCombat = ["Close Combat",sprites_load("Move Frames/star attack frames"),"Fighting",120,100,"None"]
bulletPunch = ["Bullet Punch",sprites_load("Move Frames/flash frames"),"Steel",40,100,"Priority"]
thunderPunch = ["Thunder Punch",sprites_load("Move Frames/thunder frames"),"Electric",75,100,"None"]
hurricane = ["Hurricane",sprites_load("Move Frames/star attack frames"),"Flying",110,70,"None"]
uTurn = ["U-Turn",sprites_load("Move Frames/star attack frames"),70,100,"Switchs Out"]
highJumpKick = ["High Jump Kick",sprites_load("Move Frames/earth frames"),"Fighting",130,90,"If miss, its 1/2 of HP"]
knockOff = ["Knock Off",sprites_load("Move Frames/dark_effect_frames"),"Dark",65,100,"None"]
thunderBolt = ["Thunder Bolt",sprites_load("Move Frames/thunder frames"),"Electric",90,100,"None"]
shadowBall = ["Shadow Ball",sprites_load("Move Frames/dark 2 frames"),"Ghost",80,100,"None"]
hiddenPower = ["Hidden Power",sprites_load("Move Frames/blizzard_frames"),"Ice",60,100,"None"]
braveBird = ["Brave Bird",sprites_load("Move Frames/flash frames"),"Flying",120,100,"Recoil Damage of 1/3 inflicted damage"]
psychic = ["Psychic",sprites_load("Move Frames/energy blast frames"),"Psychic",90,100,"None"]
focusBlast = ["Focus Blast",sprites_load("Move Frames/energy blast frames"),"Fighting",120,70,"None"]
crunch = ["Crunch",sprites_load("Move Frames/dark_effect_frames"),"Dark",80,100,"None"]
gigaImpact = ["Giga Impact",sprites_load("Move Frames/energy blast frames"),"Normal",150,90,"Needs to recharge"]
hyperBeam = ["Hyper Beam",sprites_load("Move Frames/star attack frames"),"Normal",150,90,"Needs to recharge"]

#POKEMON DATA
#pokemon name = ["pokename",icon_img,poke_f_lst,poke_b_lst,[move lst],[stats lst -> Speed],type]
#                    0          1        2         3          4                  5          6        

incineroar = ["Incineroar",image.load("Icon/Incineroar_icon.png"),sprites_load("Frames/Incineroar_front_frames"),sprites_load("Frames/Incineroar_back_frames"),
              [darkestLariat,flareBlitz,earthquake,crossChop],[60],["Fire","Dark"]]

greninja = ["Greninja",image.load("Icon/Greninja_icon.png"),sprites_load("Frames/Greninja_front_frames"),sprites_load("Frames/Greninja_back_frames"),
            [scald,iceBeam,darkPulse,extrasensory],[122],["Water,","Dark"]]

garchomp = ["Garchomp",image.load("Icon/Garchomp_icon.png"),sprites_load("Frames/Garchomp_front_frames"),sprites_load("Frames/Garchomp_back_frames"),
            [earthquake,dragonClaw,rockSlide,ironHead],[102],["Dragon","Ground"]]

mLucario = ["M Lucario",image.load("Icon/mLucario_icon.png"),sprites_load("Frames/mLucario_front_frames"),sprites_load("Frames/mLucario_back_frames"),
            [auraSphere,extremeSpeed,closeCombat,bulletPunch],[112],["Fighting","Steel"]]

mCharizardx = ["M Charizard X",image.load("Icon/mCharizardx_icon.png"),sprites_load("Frames/mCharizardx_front_frames"),sprites_load("Frames/mCharizardx_back_frames"),
               [flareBlitz,dragonClaw,thunderPunch,earthquake],[100],["Fire","Dragon"]]

articuno = ["Articuno",image.load("Icon/Articuno_icon.png"),sprites_load("Frames/Articuno_front_frames"),sprites_load("Frames/Articuno_back_frames"),
            [iceBeam,hurricane,psychic,uTurn],[500,85],["Ice","Flying"]]

mBlaziken = ["M Blaziken",image.load("Icon/mBlaziken_icon.png"),sprites_load("Frames/mBlaziken_front_frames"),sprites_load("Frames/mBlaziken_back_frames"),
             [flareBlitz,highJumpKick,earthquake,knockOff],[300],["Fire","Fighting"]]

jolteon = ["Jolteon",image.load("Icon/Jolteon_icon.png"),sprites_load("Frames/Jolteon_front_frames"),sprites_load("Frames/Jolteon_back_frames"),
           [thunderBolt,shadowBall,uTurn,hiddenPower],[130],["Electric"]]

skarmory = ["Skarmory",image.load("Icon/Skarmory_icon.png"),sprites_load("Frames/Skarmory_front_frames"),sprites_load("Frames/Skarmory_back_frames"),
            [braveBird,gigaImpact,darkPulse,rockSlide],[70],["Steel","Flying"]]

mAlakazam = ["M Alakazam",image.load("Icon/mAlakazam_icon.png"),sprites_load("Frames/mAlakazam_front_frames"),sprites_load("Frames/mAlakazam_back_frames"),
             [psychic,shadowBall,focusBlast,hiddenPower],[150],["Psychic"]]

tyrantrum = ["Tyrantrum",image.load("Icon/Tyrantrum_icon.png"),sprites_load("Frames/Tyrantrum_front_frames"),sprites_load("Frames/Tyrantrum_back_frames"),
             [earthquake,dragonClaw,rockSlide,crunch],[71],["Rock","Dragon"]]

magikarp = ["Lord Magikarp",image.load("Icon/Magikarp_icon.png"),sprites_load("Frames/Magikarp_front_Frames"),sprites_load("Frames/Magikarp_back_frames"),
            [earthquake,dragonClaw,gigaImpact,hyperBeam],[120],["Water"]]

electabuzz = ["Electabuzz",image.load("Icon/Electabuzz_icon.png"),sprites_load("Frames/Electabuzz_front_frames"),sprites_load("Frames/Electabuzz_back_frames"),
              [thunderBolt,hiddenPower,knockOff,crossChop],[105],["Electric"]]

gengar = ["Gengar",image.load("Icon/Gengar_icon.png"),sprites_load("Frames/Gengar_front_frames"),sprites_load("Frames/Gengar_back_frames"),
          [shadowBall,psychic,focusBlast,hiddenPower],[110],["Ghost","Poison"]]

machamp = ["Machamp",image.load("Icon/Machamp_icon.png"),sprites_load("Frames/Machamp_front_frames"),sprites_load("Frames/Machamp_back_frames"),
           [earthquake,crossChop,closeCombat,thunderPunch],[55],["Fighting"]]

meowth = ["Meowth",image.load("Icon/Meowth_icon.png"),sprites_load("Frames/Meowth_front_frames"),sprites_load("Frames/Meowth_back_frames"),
          [hyperBeam,gigaImpact,uTurn,hiddenPower],[90],["Normal"]]

ninetales = ["Ninetales",image.load("Icon/Ninetales_icon.png"),sprites_load("Frames/Ninetales_front_frames"),sprites_load("Frames/Ninetales_back_frames"),
            [flareBlitz,psychic,shadowBall,auraSphere],[109],["Fire"]]

snorlax = ["Snorlax",image.load("Icon/Snorlax_icon.png"),sprites_load("Frames/Snorlax_front_frames"),sprites_load("Frames/Snolax_back_frames"),
           [earthquake,rockSlide,gigaImpact,knockOff],[80],["Normal"]]

steelix = ["Steelix",image.load("Icon/Steelix_icon.png"),sprites_load("Frames/Steelix_front_frames"),sprites_load("Frames/Steelix_back_frames"),
           [earthquake,crunch,gigaImpact,focusBlast],[80],["Steel","Ground"]]

zygarde = ["Zygarde",image.load("Icon/Zygarde_icon.png"),sprites_load("Frames/Zygarde_front_frames"),sprites_load("Frames/Zygarde_back_frames"),
           [earthquake,dragonClaw,extremeSpeed,gigaImpact],[95],["Dragon","Ground"]]


moveTest = sprites_load("Move Frames/blizzard_frames")

fonts = [font.Font("Font/newyorkescape.ttf",10),font.Font("Font/newyorkescape.ttf",12),font.Font("Font/newyorkescape.ttf",15)]

terrain = image.load("Pictures/battle.jpg")

pokemon = [incineroar,greninja,articuno,garchomp,jolteon,skarmory,mAlakazam,mLucario,tyrantrum,magikarp,mBlaziken,zygarde,
               steelix,meowth,mCharizardx,gengar,machamp,ninetales,electabuzz,snorlax]

shuff_pokemon = pokemon[:]
shuffle(shuff_pokemon)

ready_pic = sprites_load("Frames/Ready_frames")

checkmark_pic = image.load("Icon/Checkmark_icon.png")
x_pic = image.load("Icon/X_icon.png")
pokemon_title = image.load("Icon/Pokemon_title_icon.png")



title_image = image.load("TITLE/Pictures/pokemon advanced.png")

second = image.load("TITLE/Pictures/second page.png")
title_background = image.load("TITLE/Pictures/sunset_background.png")

start_black = image.load("TITLE/Pictures/start_black.png")
start_red = image.load("TITLE/Pictures/start_red.png")

quit_black = image.load("TITLE/Pictures/quit_black.png")
quit_blue = image.load("TITLE/Pictures/quit_blue.png")



t_effect = sprites_load("Frames/Title_page_opener_frames")
pikagun = sprites_load("Frames/pikagun")
pokelogo = sprites_load("Frames/pokelogo")
loading = sprites_load("Frames/loading_frames")




def singleplayLayout():
    
    
    
    draw.rect(screen,purple,statsRect,3)
    
    screen.blit(transp_rect_2, (15,285))
    draw.rect(screen,light_purple,statsRect,4)
    
    screen.blit(transp_rect_3, (340,285))
    screen.blit(transp_rect_3, (340,460))
    
    draw.rect(screen,light_purple,p1Rect,3)
    draw.rect(screen,light_purple,p2Rect,3)

    
    screen.blit(transp_rect_4,(628,258))
    draw.rect(screen,dark_purple,p1_xRect,2)
    
    
    screen.blit(x_pic,(631,261))

    screen.blit(pokemon_title,(230,5,100,100))
    
    screen.blit(vs_txt, (475,423,312,130))
    draw.rect(screen,blue,back_rect,3)
    screen.blit(back_white,(10,12))
    if back_rect.collidepoint(mx,my):
        screen.blit(back_blue,(10,12))
            

        
           
    for x in range(100,900,80):
        for y in range(80,260,100):
            draw.rect(screen,light_purple,(x,y,60,60),4)
            draw.rect(screen,light_purple,(x,y,60,60),4)
            screen.blit(transp_rect, (x,y))
    for x in range(380,680,100):
        for y in range(320,365,44):
            draw.rect(screen,white,(x,y,30,30),2)
            draw.rect(screen,white,(x,y+175,30,30),2)
            draw.rect(screen,light_purple,(x,y,30,30),3)
            draw.rect(screen,light_purple,(x,y+175,30,30),3)
            


def readyMode():
        
    screen.blit(transp_rect_5,(675,390))
    screen.blit(ready_txt,(750,410))
    screen.blit(ready_txt_2,(780,440))
    



    

def introScreen(page):

    f = 0
    g = 0
  
    
        
    def title():
       
        screen.blit(title_background,(0,0))
        screen.blit(title_image,(220,5))
        
        screen.blit(start_black,(410,380))
        if startRect.collidepoint(mx,my):
            screen.blit(start_red,(410,380))
        screen.blit(quit_black,(460,500))
        if quitRect.collidepoint(mx,my):
            screen.blit(quit_blue,(460,500))
        

    
    def gameSelect():
        global page
        
        second_page = screen.blit(second,(0,0))
        screen.blit(single_play_white,(385,217))
        
        screen.blit(back_white,(10,12))
        
        
        draw.rect(screen,white,single_play_rect,3)
        
        draw.rect(screen,white,back_rect,3)

        if single_play_rect.collidepoint(mx,my):
            screen.blit(single_play_blue,(385,217))
            draw.rect(screen,blue,single_play_rect,3)
        
        if back_rect.collidepoint(mx,my):
            
            draw.rect(screen,blue,back_rect,3)
        
        
        
        drawSprite(pikagun,f,2,225,245)
        drawSprite(pokelogo,f,5,250,0)
    
    def themeSong():
        mixer.music.load("TITLE/theme.wav")
        mixer.music.play(-1) #-1 loops the music 
    

    mode = "none"
    running  = True
    
    while running:
        click = False
        for evt in event.get():
            if evt.type== QUIT:
                running=False
                page = "quit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
            if evt.type == KEYDOWN:
                if evt.key == K_RETURN and mode == "p2_ready":
                    page = "battle"
                    
                
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()

        
            
        #drawSprite(loading,f,10,0,0)
        ##g += 1
            
        #if g >= 500:
        title()
        
        
        
                
        if click and startRect.collidepoint(mx,my):                                
                page = "game select"
                themeSong()
        if page == "game select":
            gameSelect()
            

            if click and back_rect.collidepoint(mx,my):
                page = "intro"
                
            if click and single_play_rect.collidepoint(mx,my):
                page = "single player"
                for i in range(6):
                    
                    
                    if len(p1_lst) > i:
                        p2_lst.append(shuff_pokemon[i])
                        screen.blit(p2_lst[i][1],(select_rect_lst_2_x[i]-5,select_rect_lst_2_y[i]-4))

                running = False
               
            if click and back_rect.collidepoint(mx,my):
                page = "intro"
        if click and quitRect.collidepoint(mx,my):           
            quit()
                
            
        

        f += 1
        display.flip()
        time.wait(10)
        
    return page

def singleSelect(page):

    

    p1_lst = []
    p2_lst = []

    f = 0
    player = 1
    
    
    for x in range(100,900,80):
        for y in range(80,260,100):
            pokemon_rect = Rect(x,y,60,60)
            rect_lst.append(pokemon_rect)
            rect_lst_x.append(x)
            rect_lst_y.append(y)

    for x in range(380,680,100):
        for y in range(320,365,44):
            
            pokemon_select = Rect(x,y,30,30)
            pokemon_select_2 = Rect(x,y+175,30,30)
            
            select_rect_lst.append(pokemon_select)
            select_rect_lst_x.append(x)
            select_rect_lst_y.append(y)

            select_rect_lst.append(pokemon_select_2)
            select_rect_lst_2_x.append(x)
            select_rect_lst_2_y.append(y+175)
                        
    def readyMode():
        
        screen.blit(transp_rect_5,(675,390))
        
        screen.blit(ready_txt,(750,410))
        screen.blit(ready_txt_2,(780,440))
       

    def selectPokes():
        
        
        for i in range(20):
            
            if rect_lst[i].collidepoint(mx,my):
                draw.rect(screen,white,(rect_lst_x[i],rect_lst_y[i],60,60),2)
                drawSprite(pokemon[i][2],f,15,poke_sprite_x[i],poke_sprite_y[i])
                pokemon_txt = pokenamefont.render((pokemon[i][0]), True, poke_name_col[i])
                screen.blit(pokemon_txt,(poke_name_x[i],540))
                
            if mb[0] == 1 and rect_lst[i].collidepoint(mx,my):
                draw.rect(screen,white,(rect_lst_x[i],rect_lst_y[i],60,60),2)
            
            if rect_lst[i].collidepoint(mx,my) and click:
                p1_lst.append(pokemon[i])
                if len(p1_lst) >= 6:
                    player = 2
                    
            screen.blit(pokemon[i][1],(rect_lst_x[i]+12,rect_lst_y[i]+9))
    
    running=True
    

    mode = "none"
    
    while running:
        click = False
        enter = False
        battle = False
        for evt in event.get():
            if evt.type== QUIT:
                running=False
                page = "quit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
            if evt.type == KEYDOWN:
                if evt.key == K_RETURN and mode == "ready":
                    page = "battle"
                    running = False
                    
                    
                    
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        
        drawSprite(background,f,25,0,0)


        singleplayLayout()
        
        selectPokes()

        if player == 1:
            p1_col = gold
            p2_col = white

        screen.blit(player1_txt, (421,287,312,130))
        screen.blit(player2_txt, (370,462,312,130))    

        

        
        
        if len(p1_lst) >= 6:
            screen.blit(transp_rect_4,(598,258))
            screen.blit(checkmark_pic,(602,261))
            draw.rect(screen,dark_purple,p1_checkmarkRect,2)

            
            if p1_checkmarkRect.collidepoint(mx,my):
                draw.rect(screen,white,p1_checkmarkRect,2)
            if click and p1_checkmarkRect.collidepoint(mx,my):
                mode = "ready"

        if back_rect.collidepoint(mx,my):
            draw.rect(screen,purple,back_rect,3)
            if click:
                mode = "back"
                
       
        if p1_xRect.collidepoint(mx,my):
            draw.rect(screen,white,p1_xRect,2)
        
        if p1_xRect.collidepoint(mx,my) and click:
            p1_lst = []

        for i in range(6):
            if len(p1_lst) > i:
                screen.blit(p1_lst[i][1],(select_rect_lst_x[i]-5,select_rect_lst_y[i]-4))
            shuffle(shuff_pokemon)
            p2_lst.append(shuff_pokemon[i])
            screen.blit(p2_lst[i][1],(select_rect_lst_2_x[i]-5,select_rect_lst_2_y[i]-4))

        if mode == "ready":
            drawSprite(ready_pic,f,20,665,285)
            readyMode()
        if mode == "back":
            p1_lst = []
            
            page = "game select"
            introScreen()
            mode = "none"
        if mode == "battle":
            page = "battle"
            
        
        f += 1
        display.flip()
        
    return p1_lst, p2_lst, page
def singleBattle(team1,team2,page):
    running = True
    
    f = 0 #frame variable for sprites
    turn = 1 
    active1 = team1[0]
    active2 = team2[0]

    #These lists keep track of the health of the pokemon (All pokemon start with 500 HP)
    team1HP = [500,500,500,500,500,500]
    team2HP = [500,500,500,500,500,500]
    
    def layout():
        screen.fill(gray)

        draw.rect(screen,black,(0,0,708,428))
        draw.line(screen,black,(705,424),(705,600),4)
        draw.line(screen,black,(705,300),(1000,300),4)
        
        screen.blit(terrain,(4,4)) #THE BATTLE FIED PICTURE

        #Turn Number Display
        screen.blit(fonts[2].render("Turn #%d" % (turn),True,black),(715,10))

        #Player Team Displays
        screen.blit(fonts[1].render("Player 1 Team",True,black),(722,310))
        screen.blit(fonts[1].render("Player 2 Team",True,black),(722,453))

        y = 0
        #Boxes for P1 Team
        for y in range(334,395,60):
            for x in range(723,904,90):
                draw.rect(screen,black,(x,y,80,50),4)
        #Boxes for P2 Team
        for y in range(475,536,60):
            for x in range(723,904,90):
                draw.rect(screen,black,(x,y,80,50),4)

        #Following Code displays the pokemon of P1 on the botton right section of the screen
        j = 0
        k = 3
        for i in range(743,924,90):
            screen.blit(team1[j][1],(i,339))
            screen.blit(team1[k][1],(i,399))
            j += 1
            k += 1
        #Following Code displays the pokemon of P2 on the botton right section of the screen
        j = 0
        k = 3
        for i in range(743,924,90):
            screen.blit(team2[j][1],(i,480))
            screen.blit(team2[k][1],(i,540))
            j += 1
            k += 1

        active1Check()
        active2Check()
        
        #Health Bars
        #active1
        draw.rect(screen,gray,(398,308,250,70))
        draw.rect(screen,black,(395,305,250,75),4) #Border
        screen.blit(fonts[0].render(active1[0],True,black),(405,314))
        draw.rect(screen,darkGray,(422,340,195,12))
        if team1HP[team1.index(active1)] > 0:
            draw.rect(screen,green,(422,340,int((team1HP[team1.index(active1)]/500)*195),12)) #Green Health Bar
        draw.rect(screen,black,(420,338,199,16),3)#Green Health Bar Border
        
        
        #active2
        draw.rect(screen,gray,(60,40,250,70))
        draw.rect(screen,black,(57,37,255,75),4) #Border
        screen.blit(fonts[0].render(active2[0],True,black),(67,46))
        draw.rect(screen,darkGray,(87,72,195,12))
        if team2HP[team2.index(active2)] > 0:
            draw.rect(screen,green,(87,72,int((team2HP[team2.index(active2)]/500)*195),12)) #Green Health Bar
        draw.rect(screen,black,(85,70,199,16),3)#Green Health Bar Border

    def active1Check():
        if active1 == incineroar:
            drawSprite(incineroar[3],f,3,90,200)
            if t == "p1 wait":
                drawMove(incineroar[4])
        if active1 == greninja:
            drawSprite(greninja[3],f,3,70,230)
            if t == "p1 wait":
                drawMove(greninja[4])
        if active1 == garchomp:
            drawSprite(garchomp[3],f,3,70,180)
            if t == "p1 wait":
                drawMove(garchomp[4])
        if active1 == mLucario:
            drawSprite(mLucario[3],f,3,70,180)
            if t == "p1 wait":
                drawMove(mLucario[4])
        if active1 == mCharizardx:
            drawSprite(mCharizardx[3],f,3,60,190)
            if t == "p1 wait":
                drawMove(mCharizardx[4])
        if active1 == articuno:
            drawSprite(articuno[3],f,3,60,150)
            if t == "p1 wait":
                drawMove(articuno[4])
        if active1 == jolteon:
            drawSprite(jolteon[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(jolteon[4])
        if active1 == electabuzz:
            drawSprite(electabuzz[3],f,3,85,210)
            if t == "p1 wait":
                drawMove(electabuzz[4])
        if active1 == gengar:
            drawSprite(gengar[3],f,3,110,190)
            if t == "p1 wait":
                drawMove(gengar[4])
        if active1 == machamp:
            drawSprite(machamp[3],f,3,110,160)
            if t == "p1 wait":
                drawMove(machamp[4])
        if active1 == mAlakazam:
            drawSprite(mAlakazam[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(mAlakazam[4])
        if active1 == mBlaziken:
            drawSprite(mBlaziken[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(mBlaziken[4])
        if active1 == meowth:
            drawSprite(meowth[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(meowth[4])
        if active1 == ninetales:
            drawSprite(ninetales[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(ninetales[4])
        if active1 == skarmory:
            drawSprite(skarmory[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(skarmory[4])
        if active1 == snorlax:
            drawSprite(snorlax[3],f,3,110,200)
            if t == "p1 wait":
                drawMove(snorlax[4])
        if active1 == steelix:
            drawSprite(steelix[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(steelix[4])
        if active1 == tyrantrum:
            drawSprite(tyrantrum[3],f,3,80,210)
            if t == "p1 wait":
                drawMove(tyrantrum[4])
        if active1 == zygarde:
            drawSprite(zygarde[3],f,3,110,230)
            if t == "p1 wait":
                drawMove(zygarde[4])
        if active1 == magikarp:
            drawSprite(magikarp[3],f,3,110,200)
            if t == "p1 wait":
                drawMove(magikarp[4])

    def active2Check():
        if active2 == mBlaziken:
            drawSprite(mBlaziken[2],f,3,450,20)
        if active2 == jolteon:
            drawSprite(jolteon[2],f,3,530,80)
        if active2 == skarmory:
            drawSprite(skarmory[2],f,3,450,50)
        if active2 == mAlakazam:
            drawSprite(mAlakazam[2],f,3,470,20)
        if active2 == tyrantrum:
            drawSprite(tyrantrum[2],f,3,470,20)
        if active2 == magikarp:
            drawSprite(magikarp[2],f,3,470,40)
        if active2 == incineroar:
            drawSprite(incineroar[2],f,3,420,40)
        if active2 == articuno:
            drawSprite(articuno[2],f,3,420,40)
        if active2 == electabuzz:
            drawSprite(electabuzz[2],f,3,420,40)
        if active2 == garchomp:
            drawSprite(garchomp[2],f,3,420,40)
        if active2 == gengar:
            drawSprite(gengar[2],f,3,420,40)
        if active2 == greninja:
            drawSprite(greninja[2],f,3,420,40)
        if active2 == machamp:
            drawSprite(machamp[2],f,3,420,40)
        if active2 == mCharizardx:
            drawSprite(mCharizardx[2],f,3,420,40)
        if active2 == meowth:
            drawSprite(meowth[2],f,3,420,40)
        if active2 == mLucario:
            drawSprite(mLucario[2],f,3,420,40)
        if active2 == ninetales:
            drawSprite(ninetales[2],f,3,420,40)
        if active2 == snorlax:
            drawSprite(snorlax[2],f,3,420,40)
        if active2 == steelix:
            drawSprite(steelix[2],f,3,420,40)
        if active2 == zygarde:
            drawSprite(zygarde[2],f,3,420,40)

    
    #writes the move names down in the boxes
    def drawMove(lst):
        one = screen.blit(fonts[0].render(lst[0][0],True,black),(35,482))
        two = screen.blit(fonts[0].render(lst[1][0],True,black),(209,482))
        three = screen.blit(fonts[0].render(lst[2][0],True,black),(383,482))
        four = screen.blit(fonts[0].render(lst[3][0],True,black),(557,482))
        return [one,two,three,four]

    def p1Move():
        #To see which Player is going
        #screen.blit(fonts[1].render("Turn of Player %d" % (player_turn),True,black),(25,438))

        drawMove(active1[4])
        #Pokemon Team
        j = 0
        for i in range(55,606,110):
            screen.blit(team1[j][1],(i,540))
            j += 1

        #Move Rectangle 
        for i in range(25,645,174):
            draw.rect(screen,black,(i,465,130,50),4)

        #Team Rectangle 
        for i in range(25,645,110):
            draw.rect(screen,black,(i,535,100,50),4)

        #Turning Move Rects to Yellow when mouse hovering over
        for i in range(4):
            if move_rect_lst[i].collidepoint(mx,my):
                draw.rect(screen,yellow,(move_rect_lst_qu[i],465,130,50),4)
                
        #Turning Pokemon Icon Rects to Yellow when mouse hovering over
        for i in range(6):
            if team_rect_lst[i].collidepoint(mx,my):
                draw.rect(screen,yellow,(team_rect_lst_qu[i],535,100,50),4)
    
    #Team Rectangles
    team_rect_lst = []
    team_rect_lst_qu = []

    for i in range(25,645,110):
        team_rect = draw.rect(screen,black,(i,520,100,50),4)
        team_rect_lst.append(team_rect)
        team_rect_lst_qu.append(i)
   
    #Move Rectangles
    move_rect_lst = []
    move_rect_lst_qu = []

    for i in range(25,645,174):
        move_rect = draw.rect(screen,black,(i,450,130,50),4)
        move_rect_lst.append(move_rect)
        move_rect_lst_qu.append(i)

    def typeCheck(moves,index,active): #This function checks if the moves is supereffective
        if len(moves) != 0 and moves[1] == "":
            if moves[index][2] == "Fairy":
                if "Fighting" in active[6] or "Dragon" in active[6] or "Dark" in active[6]:
                    return True

            elif moves[index][2] == "Steel":
                if "Ice" in active[6] or "Rock" in active[6] or "Fairy" in active[6]:
                    return True
                
            elif moves[index][2] == "Dark":
                if "Psychic" in active[6] or "Ghost" in active[6]:
                    return True

            elif moves[index][2] == "Dragon":
                if "Dragon" in active[6]:
                    return True
                
            elif moves[index][2] == "Ghost":
                if "Psychic" in active[6] or "Ghost" in active[6]:
                    return True

            elif moves[index][2] == "Rock":
                if "Fire" in active[6] or "Ice" in active[6] or "Flying" in active[6] or "Bug" in active[6]:
                    return True

            elif moves[index][2] == "Bug":
                if "Grass" in active[6] or "Psychic" in active[6] or "Dark" in active[6]:
                    return True

            elif moves[index][2] == "Psychic":
                if "Fight" in active[6] or "Poison" in active[6]:
                    return True

            elif moves[index][2] == "Flying":
                if "Grass" in active[6] or "Fighting" in active[6] or "Bug" in active[6]:
                    return True

            elif moves[index][2] == "Ground":
                if "Fire" in active[6] or "Electric" in active[6] or "Poison" in active[6] or "Rock" in active[6] or "Steel" in active[6]:
                    return True
                
            elif moves[index][2] == "Poison":
                if "Grass" in active[6] or "Fairy":
                    return True

            elif moves[index][2] == "Fighting":
                if "Normal" in active[6] or "Ice" in active[6] or "Rock" in active[6] or "Dark" in active[6] or "Ice" in active[6]:
                    return True

            elif moves[index][2] == "Ice":
                if "Grass" in active[6] or "Ground" in active[6] or "Flying" in active[6] or "Dragon" in active[6]:
                    return True

            elif moves[index][2] == "Grass":
                if "Water" in active[6] or "Ground" in active[6] or "Rock" in active[6]:
                    return True

            elif moves[index][2] == "Electric":
                if "Water" in active[6] or "Flying" in active[6]:
                    return True
            
            elif moves[index][2] == "Water":
                if "Fire" in active[6] or "Ground" in active[6] or "Rock" in active[6]:
                    return True

            elif moves[index][2] == "Fire":
                if "Grass" in active[6] or "Ice" in active[6] or "Bug" in active[6] or "Steel" in active[6]:
                    return True 
        
    def hitCheck(moveLst,index):
        #MOVE HIT PERCENTAGE
        #0 means the move hit
        #1 means the opponent's pokemon avoided the move
        seventyP= [1,1,1,0,0,0,0,0,0,0]
        eightyP = [1,1,0,0,0,0,0,0,0,0]
        ninetyP = [1,0,0,0,0,0,0,0,0,0]

        if moveLst[index][4] == 70:
            shuffle(seventyP)
            if seventyP[0] == 0:
                return True
            else:
                return False
            
        if moveLst[index][4] == 80:
            shuffle(eightyP)
            if eightyP[0] == 0:
                return True
            else:
                return False
            
        if moveLst[index][4] == 90:
            shuffle(ninetyP)
            if ninetyP[0] == 0:
                return True
            else:
                return False
            
        if moveLst[index][4] == 100:
            return True

    def moveSprites(x,y,z,moves): #This function draws the moves at a specified location
        if moves[z] == darkestLariat:
            drawSprite(darkestLariat[1],mf,3,x,y)
        if moves[z] == flareBlitz:
            drawSprite(flareBlitz[1],mf,3,x,y)
        if moves[z] == earthquake:
            drawSprite(earthquake[1],mf,3,x,y)
        if moves[z] == crossChop:
            drawSprite(crossChop[1],mf,3,x,y)
        if moves[z] == scald:
            drawSprite(scald[1],mf,3,x,y)
        if moves[z] == iceBeam:
            drawSprite(iceBeam[1],mf,3,x,y)
        if moves[z] == darkPulse:
            drawSprite(darkPulse[1],mf,3,x,y)
        if moves[z] == extrasensory:
            drawSprite(extrasensory[1],mf,3,x,y)
        if moves[z] == dragonClaw:
            drawSprite(dragonClaw[1],mf,3,x,y)
        if moves[z] == rockSlide:
            drawSprite(rockSlide[1],mf,3,x,y)
        if moves[z] == ironHead:
            drawSprite(ironHead[1],mf,3,x,y)
        if moves[z] == auraSphere:
            drawSprite(auraSphere[1],mf,3,x,y)
        if moves[z] == extremeSpeed:
            drawSprite(extremeSpeed[1],mf,3,x,y)
        if moves[z] == closeCombat:
            drawSprite(closeCombat[1],mf,3,x,y)
        if moves[z] == bulletPunch:
            drawSprite(bulletPunch[1],mf,3,x,y)
        if moves[z] == thunderPunch:
            drawSprite(thunderPunch[1],mf,3,x,y)
        if moves[z] == hurricane:
            drawSprite(hurricane[1],mf,3,x,y)
        if moves[z] == uTurn:
            drawSprite(uTurn[1],mf,3,x,y)
        if moves[z] == highJumpKick:
            drawSprite(highJumpKick[1],mf,3,x,y)
        if moves[z] == knockOff:
            drawSprite(knockOff[1],mf,3,x,y)
        if moves[z] == thunderBolt:
            drawSprite(thunderBolt[1],mf,3,x,y)
        if moves[z] == shadowBall:
            drawSprite(shadowBall[1],mf,3,x,y)
        if moves[z] == hiddenPower:
            drawSprite(hiddenPower[1],mf,3,x,y)
        if moves[z] == braveBird:
            drawSprite(braveBird[1],mf,3,x,y)
        if moves[z] == psychic:
            drawSprite(psychic[1],mf,3,x,y)
        if moves[z] == focusBlast:
            drawSprite(focusBlast[1],mf,3,x,y)
        if moves[z] == crunch:
            drawSprite(crunch[1],mf,3,x,y)
        if moves[z] == gigaImpact:
            drawSprite(gigaImpact[1],mf,3,x,y)
        if moves[z] == hyperBeam:
            drawSprite(hyperBeam[1],mf,3,x,y)
        
    def p1Fainted(): #This function runs when p1's poke faints and p1 chooses a new one to switch in
        #Team Rectangle 
        for i in range(25,645,110):
            draw.rect(screen,black,(i,535,100,50),4)
        #Pokemon Team
        j = 0
        for i in range(55,606,110):
            screen.blit(team1[j][1],(i,540))
            j += 1
        #Turning Pokemon Icon Rects to Yellow when mouse hovering over
        for i in range(6):
            if team_rect_lst[i].collidepoint(mx,my):
                draw.rect(screen,yellow,(team_rect_lst_qu[i],535,100,50),4)
        screen.blit(fonts[0].render("Select the next pokemon:",True,black),(25,510))

    #These variables are lists so that all the activity that is going on can be diplayed on the screen
    #for the entire turn
    moves = []
    mf = 0
    t = ["p1 wait"]
    hCheck = []
    battleLst = []
    fainted = []
    lose1 = 0
    lose2 = 0
    
    #battleLst Index OrderL 0.p1 Successful/Unsuccessful attack 1. p2 Opponent is alive or fainted 2.counter
    #3.p2 Successful/Unsuccessful attack 4. p1 Opponent Health 5.counter
    def gamePlay(t,mf,moves,hCheck,battleLst,team1HP,team2HP,active1,active2,fainted,turn,lose1,lose2):
        #Variable 'moves' Index Order: 0.Move1 1.Switch1 2.Old1 3.Move2
        if t[0] == "p1 wait":
            p1Move()
            #Following code is for p1 to select a move
            for i in range(4):
                if click and move_rect_lst[i].collidepoint(mx,my):
                    moves = [team1[team1.index(active1)][4][i],"",""]
                    t.append("p2 wait")
                    mf = 0

            #Following code is for when p1 selects to switch out active1 for a new pokemon
            for i in range(6):
                if click and team_rect_lst[i].collidepoint(mx,my):
                    if team1HP[team1.index(team1[i])] > 0:
                        moves = ["",team1[i],active1]
                        if moves[1] != moves[2]: #To make sure that p2 is not switching out active1 for the same pokemon
                            t.append("p2 wait")
                            mf = 0
                            screen.blit(fonts[0].render("Return, %s!" % (moves[2][0]),True,black),(715,40))
        if len(t) == 2:
            if t[1] == "p2 wait":
                moves.append(team2[team2.index(active2)][4][randint(0,3)])
                mf = 0
                if moves[1] == "": #This checks if p1 selected a move
                    #Special Cases
##                    if moves[0][0] == "Bullet Punch" or moves[0][0] == "Extreme Speed":
##                        t = ["p1 go first"]
##                    if moves[3][0] == "Bullet Punch" or moves[3][0] == "Extreme Speed":
##                        t = ["p2 go first"]
                    #If there are no special cases, it then checks speeds
                    if team1[team1.index(active1)][5] > team2[team2.index(active2)][5]:
                        t = ["p1 go first"]
                    if team1[team1.index(active1)][5] < team2[team2.index(active2)][5]:
                        t = ["p2 go first"]
                    if team1[team1.index(active1)][5] == team2[team2.index(active2)][5]:
                        t = ["p1 go first"]
                if moves[0] == "": #This checks if p1 chose to switch out their pokemon
                    t = ["p1 go switch"]

        if t[0] == "p1 go first":
            if mf == 0:
                hCheck = [hitCheck(moves,0)]
            #Move Was Successful
            if hCheck[0] == True: 
                screen.blit(fonts[0].render("%s used %s" % (active1[0],moves[0][0]),True,black),(715,40))
                if len(t) == 1:
                    if mf < 200: #Move is displaying on the screen
                        moveSprites(400,20,0,moves)
                    if mf == 200: #Move stops
                        battleLst = [typeCheck(moves,0,active2)]
                        if battleLst[0] == True: #Move was super effective
                            team2HP[team2.index(active2)] = team2HP[team2.index(active2)] - moves[0][3] - 80 #Health
                        if battleLst[0] == None: #
                            team2HP[team2.index(active2)] = team2HP[team2.index(active2)] - moves[0][3]
                        if team2HP[team2.index(active2)] == 0 or team2HP[team2.index(active2)] < 0:
                            battleLst.append("Fainted") #Means the opponent fainted
                            lose2 += 1
                        if team2HP[team2.index(active2)] > 0:
                            battleLst.append("Alive") #Means the the opponent is still alive 
                if len(battleLst) > 1:
                    if battleLst[0] == True:
                        screen.blit(fonts[0].render("It was super effective!",True,black),(715,60))
                    if battleLst[1] == "Alive":
                        if len(t) == 1:
                            if mf == 250:
                                t.append("p2 go second")
                                mf = 0
                    if battleLst[1] == "Fainted":
                        if len(t) == 1:
                            #The following code choses a random poke from team2 that has an
                            #HP over 0
                            if fainted == []:
                                fainted = [active2]
                                fainted.append(team2[randint(0,5)])
                                if team2HP[team2.index(fainted[1])] > 0:
                                    active2 = fainted[1]
                                    battleLst.append(mf)
                                if team2HP[team2.index(fainted[1])] < 0 or team2HP[team2.index(fainted[1])] == 0:
                                    fainted = []
                        if len(fainted) > 1:
                            screen.blit(fonts[0].render("%s fainted!" % (fainted[0][0]),True,black),(715,120))
                            screen.blit(fonts[0].render("Player 2 sent out %s!" % (fainted[1][0]),True,black),(715,140))
                            #Resets
                            if len(t) == 1:
                                if mf - 200 == battleLst[2]:
                                    t = ["p1 wait"]
                                    turn += 1
                                    fainted = []
                                    mf = 0
                                    battleLst = []
                                    hCheck = []
                                    fainted = []
            #Move was unsuccessful                    
            if len(hCheck) != 0:
                if hCheck[0] == False:
                    screen.blit(fonts[0].render("%s used %s" % (active1[0],moves[0][0]),True,black),(715,40))
                    screen.blit(fonts[0].render("%s dodged the attack!" % (active2[0]),True,black),(715,60))
                    if len(hCheck) == 1:
                        if len(t) == 1:
                            if mf == 50:
                                mf = 0
                                t.append("p2 go second")
                                battleLst = ["",""] #Because the next step is expecting the list to have 2 items

        if t[0] == "p2 go first":
            if mf == 0:
                hCheck = [hitCheck(moves,3)]
            #Move Was Successful
            if hCheck[0] == True: 
                screen.blit(fonts[0].render("%s used %s" % (active2[0],moves[3][0]),True,black),(715,40))
                if len(t) == 1:
                    if mf < 200: #Move is displaying on the screen
                        moveSprites(70,200,3,moves)
                    if mf == 200: #Move stops
                        battleLst = [typeCheck(moves,3,active1)]
                        if battleLst[0] == True: #Move was super effective
                            team1HP[team1.index(active1)] = team1HP[team1.index(active1)] - moves[3][3] - 80 #Health
                        if battleLst[0] == None: #
                            team1HP[team1.index(active1)] = team1HP[team1.index(active1)] - moves[3][3]
                        if team1HP[team1.index(active1)] == 0 or team1HP[team1.index(active1)] < 0:
                            battleLst.append("Fainted")
                            lose1 += 1
                        if team1HP[team1.index(active1)] > 0:
                            battleLst.append("Alive")
                if len(battleLst) > 1:
                    if battleLst[0] == True:
                        screen.blit(fonts[0].render("It was super effective!",True,black),(715,60))
                    if battleLst[1] == "Alive":
                        if len(t) == 1:
                            if mf == 250:
                                t.append("p1 go second")
                                mf = 0
                    if battleLst[1] == "Fainted":
                        if len(t) == 1:
                            if len(battleLst) == 2:
                                p1Fainted()
                            if len(fainted) == 0:
                                fainted = [active1]
                            screen.blit(fonts[0].render("%s fainted!" % (fainted[0][0]),True,black),(715,120))
                            for i in range(6):
                                if click and team_rect_lst[i].collidepoint(mx,my):
                                    if team1HP[team1.index(team1[i])] > 0:
                                        fainted.append(team1[i])
                                        battleLst.append(mf)
                            if len(battleLst) == 3:
                                screen.blit(fonts[0].render("Player1 sent out %s" % (fainted[1][0]),True,black),(715,140))
                                active1 = fainted[1]
                                if mf - 50 == battleLst[2]:
                                    t = ["p1 wait"]
                                    turn += 1
                                    mf = 0
                                    battleLst = []
                                    hCheck = []
                                    fainted = []
            #Move was unsuccessful
            if len(hCheck) != 0:
                if hCheck[0] == False:
                    screen.blit(fonts[0].render("%s used %s" % (active2[0],moves[3][0]),True,black),(715,40))
                    screen.blit(fonts[0].render("%s dodged the attack!" % (active1[0]),True,black),(715,60))
                    if len(hCheck) == 1:
                        if len(t) == 1:
                            if mf == 50:
                                mf = 0
                                t.append("p1 go second")
                                battleLst = ["",""] #Because the next step is expecting the list to have 2 items            

        if t[0] == "p1 go switch":
            screen.blit(fonts[0].render("Return, %s!" % (moves[2][0]),True,black),(715,40))
            if len(t) == 1:
                if mf == 20:
                    active1 = moves[1] #Pokemon Switches out here
                    battleLst = [""]
            if len(battleLst) > 1:
                screen.blit(fonts[0].render("Its your turn, %s !" % (active1[0]),True,black),(715,60))
            if len(t) == 1:
                if mf == 30:
                    mf = 0
                    t.append("p2 go second")
                    battleLst.append("") #To add another index because the list is expected to have 2 items in the next step
                    hCheck = [""]
                    
        if len(t) == 2:
            if t[1] == "p1 go second":
                if mf == 0:
                    hCheck.append(hitCheck(moves,0))
                if hCheck[1] == True:
                    screen.blit(fonts[0].render("%s used %s" % (active1[0],moves[0][0]),True,black),(715,120))
                    if mf < 200:
                        moveSprites(400,20,0,moves)
                    if mf == 200:
                        battleLst.append(typeCheck(moves,0,active2))
                        if battleLst[2] == True:
                            team2HP[team2.index(active2)] = team2HP[team2.index(active2)] - moves[0][3] - 80
                        if battleLst[2] == None:
                            team2HP[team2.index(active2)] = team2HP[team2.index(active2)] - moves[0][3]
                        if team2HP[team2.index(active2)] == 0 or team2HP[team2.index(active2)] < 0:
                            battleLst.append("Fainted")
                            lose2 += 1
                        if team2HP[team2.index(active2)] > 0:
                            battleLst.append("Alive")
                    if len(battleLst) > 3:
                        if battleLst[2] == True:
                            screen.blit(fonts[0].render("It was super effective!",True,black),(715,140))
                        if battleLst[3] == "Alive":
                            if mf == 250:
                                t = ["p1 wait"]
                                turn += 1
                                mf = 0
                                battleLst = []
                                hCheck = []
                                fainted = []
                        if len(battleLst) != 0: #Makes sure that program does not crash when battleLst is reset
                            if battleLst[3] == "Fainted":
                                if fainted == []:
                                    fainted = [active2]
                                    fainted.append(team2[randint(0,5)])
                                    if team2HP[team2.index(fainted[1])] > 0:
                                        active2 = fainted[1]
                                        battleLst.append(mf)
                                    if team2HP[team2.index(fainted[1])] < 0 or team2HP[team2.index(fainted[1])] == 0:
                                        fainted = []
                                if len(fainted) > 1:
                                    screen.blit(fonts[0].render("%s fainted!" % (fainted[0][0]),True,black),(715,190))
                                    screen.blit(fonts[0].render("Player 2 sent out %s!" % (fainted[1][0]),True,black),(715,210))
                                    if mf - 50 == battleLst[4]:
                                        t = ["p1 wait"]
                                        turn += 1
                                        fainted = []
                                        mf = 0
                                        battleLst = []
                                        hCheck = []
                                        fainted = []

                if len(hCheck) != 0:
                    if hCheck[1] == False:
                        screen.blit(fonts[0].render("%s used %s" % (active1[0],moves[0][0]),True,black),(715,120))
                        screen.blit(fonts[0].render("%s dodged the attack!" % (active2[0]),True,black),(715,140))
                        if mf == 50:
                            t = ["p1 wait"]
                            turn += 1
                            mf = 0
                            battleLst = []
                            hCheck = []
                            fainted = []
                                    
        if len(t) == 2:
            if t[1] == "p2 go second":
                if mf == 0:
                    hCheck.append(hitCheck(moves,3))
                if hCheck[1] == True:
                    screen.blit(fonts[0].render("%s used %s" % (active2[0],moves[3][0]),True,black),(715,120))
                    if mf < 200:
                        moveSprites(70,200,3,moves)
                    if mf == 200:
                        battleLst.append(typeCheck(moves,3,active1))
                        if battleLst[2] == True:
                            team1HP[team1.index(active1)] = team1HP[team1.index(active1)] - moves[3][3] - 80
                        if battleLst[2] == None:
                            team1HP[team1.index(active1)] = team1HP[team1.index(active1)] - moves[3][3]
                        if team1HP[team1.index(active1)] == 0 or team1HP[team1.index(active1)] < 0:
                            battleLst.append("Fainted")
                            lose1 += 1
                        if team1HP[team1.index(active1)] > 0:
                            battleLst.append("Alive")
                    if len(battleLst) > 3:
                        if battleLst[2] == True:
                            screen.blit(fonts[0].render("It was super effective!",True,black),(715,140))
                        if battleLst[3] == "Alive":
                            if mf == 250:
                                t = ["p1 wait"]
                                turn += 1
                                mf = 0
                                battleLst = []
                                hCheck = []
                                fainted = []
                        if len(battleLst) != 0: #Makes sure that program does not crash when battleLst is reset
                            if battleLst[3] == "Fainted":
                                if len(battleLst) == 4:
                                    p1Fainted()
                                    if len(fainted) == 0:
                                        fainted = [active1]
                                    screen.blit(fonts[0].render("%s fainted!" % (fainted[0][0]),True,black),(715,190))
                                    #Following code is for when p1 selects to switch out active1 for a new pokemon
                                    for i in range(6):
                                        if click and team_rect_lst[i].collidepoint(mx,my):
                                            if team1HP[team1.index(team1[i])] > 0:
                                                fainted.append(team1[i])
                                                battleLst.append(mf)
                                if len(battleLst) == 5:
                                    screen.blit(fonts[0].render("%s fainted!" % (fainted[0][0]),True,black),(715,190))
                                    screen.blit(fonts[0].render("Player 1 sent out %s" % (fainted[1][0]),True,black),(715,210))
                                    active1 = fainted[1]
                                    if mf - 50 == battleLst[4]:
                                        t = ["p1 wait"]
                                        turn += 1
                                        mf = 0
                                        battleLst = []
                                        hCheck = []
                                        fainted = []
                if len(hCheck) != 0:
                    if hCheck[1] == False:
                        screen.blit(fonts[0].render("%s used %s" % (active2[0],moves[3][0]),True,black),(715,120))
                        screen.blit(fonts[0].render("%s dodged the attack!" % (active1[0]),True,black),(715,140))
                        if mf == 50:
                            t = ["p1 wait"]
                            turn += 1
                            mf = 0
                            battleLst = []
                            hCheck = []
                            fainted = []
        
                

       
            
        
        return t,mf,moves,hCheck,battleLst,team1HP,team2HP,active1,active2,fainted,turn,lose1,lose2
    yo1 = 0
    yo2 = 0    
    while running:
        click = False
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                page = "quit"
            if evt.type == MOUSEBUTTONDOWN:
                click = True
        #-------------------------------------------------------------------------------------------------------------------------------------------
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()    
        
        layout()
        t,mf,moves,hCheck,battleLst,team1HP,team2HP,active1,active2,fainted,turn,lose1,lose2 = gamePlay(t,mf,moves,hCheck,battleLst,team1HP,team2HP,active1,active2,
                                                                                                        fainted,turn,lose1,lose2)
        #RESTART WHEN A TEAM IS DEFEATED
        if lose2 == 6:
            mf = 0
            lose2 += 1
        if lose2 == 7:
            screen.blit(fonts[0].render("Player 1 WON !!!!!!!",True,black),(715,200))
            if mf == 100:
                running = False
                page = "intro"
        if lose1 == 6:
            mf = 0
            lose += 1
        if lose1 == 7:
            screen.blit(fonts[0].render("Player 2 WON !!!!!!!",True,black),(715,200))
            if mf == 100:
                running = False
                page = "intro"
        #------------------------------------------------------------
        mf += 1
        f += 1
        display.flip()
        time.wait(10)
    return page
             


running = True

page = "intro"
f = 0
g = 0
team1 = []
team2 = []
while running:
    
    click = False
    
    if page == "intro":
    
       page = introScreen(page)
       if startRect.collidepoint(mx,my) and click:
           
           page == "game select"
       
    if page == "quit":
        running = False
    if page == "game select":
        
        gameSelect()
        team1,team2,page = singleSelect(page)
    if page == "single player":
        team1,team2,page = singleSelect(page)

    if page == "battle":
        page = singleBattle(team1,team2,page)
        
        
quit()





































