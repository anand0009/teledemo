import mysql.connector
from mysql.connector import Error

try:
    print("try block")
    connection = mysql.connector.connect(host='localhost',
                                         database='jiodb',
                                         user='root',
                                         password='root')

except Error as e:
    print("Error reading data from MySQL table", e)

cursor = connection.cursor()


def finish():
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


def get_new_plan():
    sql_select_Query = "select * from new_plan"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    print("records=", records)
    # converting List data to String
    new_list=''
    for x in records:
         print(x)
         new_plan='Plan : '+str(x[0])+'| Validity : '+x[1]+'| Benefits : '+x[2]+'\n'
         new_list=new_plan+new_list
    new_list='Latest plan is :-\n'+new_list
    print("newplan=",new_list)
    return records


def get_user_plan(number):
    if given_number_user_verify(number):
        sql_select_Query = "SELECT * FROM jiodb.user_plan_details where user_phone_number=%s"
        cursor.execute(sql_select_Query, (number,))
        records = cursor.fetchall()

        # converting List data to String
        for x in records:
            user_plan='Hi '+x[4]+', your plan details :\n Plan     : '+str(x[1])+'\n Validity : '+x[6] +'\n Used     : '+str(x[2])+'\n Balance  : '+x[3]
        print("user_plan=",user_plan)

        return user_plan
    else:
        return "User is not present with this number.Please give a valid number"


def given_number_user_verify(number):
    sql_select_Query = "SELECT * FROM jiodb.user_plan_details where user_phone_number=%s"
    cursor.execute(sql_select_Query, (number,))
    if cursor.fetchone():
        print("user is present")
        return True
    else:
        print("user is not present")
        return False

#get_new_plan()

#given_number_user_verify(8921249991)
#print(get_user_plan(8921249971))
#finish()