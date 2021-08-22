import db
import controller
if controller.isTableEmpty(db.mCursor) : 
    controller.enterData(db.mCursor)
else : 
    controller.info()
    value = input ("Choose your option : ")
    controller.option(value)