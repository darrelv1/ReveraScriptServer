from ..models import Report
#from ...BaseReports.Users import Accountant

def build():
    Report.objects.create(title="testing build", entityID=2000, creator="Harry", is_Current=False)
    Report.objects.create(title="build is being tested", entityID=1011, creator="Nicole", is_Current=False) 

def buildTranslog():
    
    pass
