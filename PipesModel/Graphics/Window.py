from stdafx import *


#screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pipes model")


infoObject = pygame.display.Info()

WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h



class Window(object):

    def __init__(self, rect = None, visible = True, ID = ""):
        
        self.ID = ID

        self.visible = visible

        self.buttons = []
        self.windows = []

        self.rect = rect

        

    def Close(self):
        self.visible = False

    def Open(self):
        self.visible = True

    def OpenWindow(self, ID, close_other = False):
        if close_other:
            for window in self.windows:
                window.visible = False
                
        self.FindWindowByID(ID).Open()

    def TurnWindowVisibility(self, ID, close_other = False):
        window = self.FindWindowByID(ID)

        if window.visible:
            window.Close()
            return

        if not window.visible:
            self.OpenWindow(ID, close_other)
            return

    def TurnVisibility(self):
        self.visible = not self.visible


    
    def FindWindowByID(self, ID):
        return next(x for x in self.windows if x.ID == ID)



    def AddButton(self, button):
        self.buttons.append(button)

    def AddWindow(self, rect, visible, ID):
        self.windows.append(Window(rect, visible, ID))


    def Draw(self):

        if not self.visible:
            return
        


        if self.rect != None:
            pygame.draw.rect(screen, (240, 240, 240), self.rect)#(rect.x, rect.y, rect.w, rect.h))#(WIDTH - 215, 0, 215, HEIGHT)
            pygame.draw.rect(screen, (20, 20, 20), self.rect, width = 2)#(rect.x, rect.y, rect.w, rect.h), width = 2)

        for button in self.buttons:
            button.draw()

        for window in self.windows:
            window.Draw()



    def Loop(self, events):

        if not self.visible:
            return
        else:

            for button in self.buttons:
                button.listen(events)
            
            for window in self.windows:
                window.Loop(events)