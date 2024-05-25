import tkintertools as tkt


class RightWidget(tkt.Canvas):
    """ 右边详情展示控件 """
    def __init__(self, master, width, height, x, y, background=None) -> None:
        super().__init__(master, width, height, x, y, background=background)
        self.initWidgets()
        
    def initWidgets(self):
        """ 初始化所有子控件 """
        
    

