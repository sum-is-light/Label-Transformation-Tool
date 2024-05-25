import tkintertools as tkt
from .left_widget import LeftWidget
from .right_widget import RightWidget


class MainWidget(tkt.Canvas):
    """主窗口控件"""
    def __init__(self, master, width, height, x, y) -> None:
        super(MainWidget, self).__init__(master, width, height, x, y)
        self.initWidgets()

    def initWidgets(self):
        """初始化所有子控件"""
        self.__left_widget = LeftWidget(self.master, 300, self.master.getHeight(), 0, 0, background="#BEE7E9")
        self.__right_widget = RightWidget(
            self.master, self.master.getWidth() - 300, self.master.getHeight(), 300, 0, background="#F5F5F5"
        )
        
    
