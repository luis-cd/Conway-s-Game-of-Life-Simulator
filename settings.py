class Settings():

    def __init__(self):
        '''Initialize setting class'''

        #screen settings.

        self.width=1000
        self.height=1000
        self.bg=(25,25,25)

        #cell settings.

        self.numberx=25
        self.numbery=25

        #game settings.

        self.timeSleep=0.2
        self.pauseState=False