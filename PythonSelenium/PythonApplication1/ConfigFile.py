
class config():
    def __init__(self):
        #Driver and site configuration
        self.url = "https://sap-sta.paws.com/"
        self.service = "C:\\SeleniumProjects\\WebDrivers\\msedgedriver.exe"
        self.headless = False

        #Account configuration
        self.email_prefix = "705d2182d0-b54e92"
        self.domain = "@inbox.mailtrap.io"