class BBreak(object):

    reg = None

    def __init__(self , reg):
        self.reg = reg

    def getTranslation(self):

        self.reg.breakIsTrue()
        return "Break"
