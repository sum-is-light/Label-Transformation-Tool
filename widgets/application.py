import tkintertools as tkt
from .main_widget import MainWidget


class Application(tkt.Tk):
    """应用程序类，定义全局属性"""
    def __init__(self) -> None:
        super(tkt.Tk, self).__init__()
        self.__size = (1024, 800)
        super(Application, self).__init__(
            title="Label Transformation Tool——便捷的标签转换工具",
            width=self.getWidth(),
            height=self.getHeight(),
        )
        self.initWidgets()
    
    def initWidgets(self):
        self.__main_widget = MainWidget(self, self.getWidth(), self.getHeight(), 0, 0)

    def getWidth(self) -> int:
        """获取窗口宽度"""
        return self.__size[0]

    def getHeight(self) -> int:
        """获取窗口高度"""
        return self.__size[1]


if __name__ == "__main__":
    root = Application()
    root.mainloop()  # 根窗口进入消息事件循环
