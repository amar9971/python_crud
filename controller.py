
from mysql.connector.errors import Error
import db

def isTableEmpty(mCursor) : 
    rows=mCursor.execute("SELECT * FROM school_db.STUDENT")
    data=mCursor.fetchall()
    if len(data)==0: 
        return True; 
    else: 
        return False


# call when table is empty
def enterData(mCursor) :
    print("Enter student entry")
    student_no = input ("Enter Student Roll no : ")
    student_name = input ("Enter Student name : ")
    student_dob = input ("Enter Student Date of Birth  (YYYY-MM-DD) :")
    student_doj = input ("Enter Student Date of Joining  (YYYY-MM-DD) :")
    try :
        query = "INSERT INTO school_db.STUDENT(`STUDENT_NO`, `STUDENT_NAME`, `STUDENT_DOB`, `STUDENT_DOJ`) VALUES (%s, %s, %s, %s)"
        data = (student_no, student_name, student_dob, student_doj)
        mCursor.execute(query, data)
        db.conn.commit()
        print("Data inserted successfully....")
    except(Exception, Error) as error:
        print(error)
        print("Data not inserted please try again later")
    



#provide option to manipulate student table
def option(value):
    if int(value) == 1 :
        enterData(db.mCursor)
    elif int(value) == 2:
        id = input ("Enter student No to update data : ")
        updateByStudentNo(id)       
    elif int(value) == 3:
        id = input ("Enter student No to delete data : ")
        deleteByStudentNo(id)
    elif int(value) == 4:
        getAllData()
    elif int(value) == 5:
       print("Good bye...")
    else :
        print("Invalid option")
        info()
        value = input ("Choose your option : ")
        option(value)



 
def info():
    print("===============================================================================")
    print("1.  Add data to student table")
    print("2.  Update data in student table")
    print("3.  delete data from the student table")
    print("4.  Get list of student")
    print("5.  Exit")
    print("===============================================================================")



#get all data from table
def getAllData():
    if isTableEmpty(db.mCursor) :
        print("data not available")
        value = input ("Choose your option")
        option(value)
    else :
        query = 'SELECT * FROM school_db.STUDENT;'
        db.mCursor.execute(query)
        data = db.mCursor.fetchall()
        for i in data:
            print('     {}      |       {}      |       {}      |       {}'.format(i[0], i[1], i[2], i[3]))



#delete data by student no
def deleteByStudentNo(studentId):
    query = 'SELECT * FROM school_db.STUDENT WHERE STUDENT_NO = %s;'
    db.mCursor.execute(query, [studentId])
    size = len(db.mCursor.fetchone())
    if size == 0:
        print("Data not available please choose correct student no...")
    else :
        delete = 'DELETE FROM school_db.STUDENT WHERE STUDENT_NO = %s;'
        if isTableEmpty(db.mCursor) :
            print("Data not available for deletion...")
        else :
            db.mCursor.execute(delete, [studentId])
            db.conn.commit()
            print("Data deleted successfully...")
    info()
    value = input ("Choose your option : ")
    option(value)





    
#update data by student no
def updateByStudentNo(studentId):
    query = 'SELECT * FROM school_db.STUDENT WHERE STUDENT_NO = %s;'
    db.mCursor.execute(query, [studentId])
    qData = db.mCursor.fetchone()
    size = len(qData)
    if size == 0:
        print("Data not available please choose correct student no...")
    else :
        student_name = input ("Enter Student name : ")
        student_dob = input ("Enter Student Date of Birth  (YYYY-MM-DD) :")
        student_doj = input ("Enter Student Date of Joining  (YYYY-MM-DD) :")
        if student_name is None:
            student_name = qData[1]
        if student_dob is None:
            student_dob = qData[2]
        if student_doj is None:
            student_doj = qData[3]
        db.mCursor.execute("UPDATE school_db.STUDENT SET STUDENT_NAME=%s, STUDENT_DOB=%s, STUDENT_DOJ=%s WHERE STUDENT_NO = %s",(student_name, student_dob, student_doj, studentId))
        db.conn.commit()
        print("Data updated successfully...")
    info()
    value = input ("Choose your option : ")
    option(value)
