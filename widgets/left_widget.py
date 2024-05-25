import tkintertools as tkt


class LeftWidget(tkt.Canvas):
    """ 左边功能选择控件 """
    def __init__(self, master, width, height, x, y, background=None) -> None:
        super().__init__(master, width, height, x, y, background=background)
        self.initWidgets()
        
    def initWidgets(self):
        """ 初始化所有子控件 """
        tkt.Button(self, 50, 50, 50, 30)
    

