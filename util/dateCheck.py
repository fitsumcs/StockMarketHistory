import maya
def checkDat(startDate, endDate):
    startDate = maya.parse(startDate).datetime()
    endDate = maya.parse(endDate).datetime()
    t =(startDate-endDate)
    notZero = True
    notZero = endDate - startDate
    # if endDate - startDate == 0 :
    #     notZero = False
    return   "{:%h/%m/%s}".format(t)==  '0:00:00'