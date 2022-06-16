from stdafx import *

WHITE = (255, 255, 255)
BACKGROUND = (113, 129, 110)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



def DrawImage(ren, image, src, dst = None):
    img = image.copy()
    img = pygame.transform.scale(img, (src.width, src.height))

    if dst == None: 
        ren.blit(img, src)
    else:
        ren.blit(img, src, dst)


def DrawAALine(ren, color, point1, point2, width = 1):
    center_L1 = ((point1[0]+point2[0]) / 2, (point1[1]+point2[1]) / 2)

    length = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    angle = math.atan2(point1[1] - point2[1], point1[0] - point2[0])


    UL = (center_L1[0] + (length/2.) * math.cos(angle) - (width/2.) * math.sin(angle),
        center_L1[1] + (width/2.) * math.cos(angle) + (length/2.) * math.sin(angle))
    UR = (center_L1[0] - (length/2.) * math.cos(angle) - (width/2.) * math.sin(angle),
        center_L1[1] + (width/2.) * math.cos(angle) - (length/2.) * math.sin(angle))
    BL = (center_L1[0] + (length/2.) * math.cos(angle) + (width/2.) * math.sin(angle),
        center_L1[1] - (width/2.) * math.cos(angle) + (length/2.) * math.sin(angle))
    BR = (center_L1[0] - (length/2.) * math.cos(angle) + (width/2.) * math.sin(angle),
        center_L1[1] - (width/2.) * math.cos(angle) - (length/2.) * math.sin(angle))

    gfxdraw.aapolygon(ren, (UL, UR, BR, BL), color)
    gfxdraw.filled_polygon(ren, (UL, UR, BR, BL), color)