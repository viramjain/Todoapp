import psycopg2
class DatabaseConnection(object):
    def __init__(self):
        global con
        try:
            con = psycopg2.connect(host="localhost", database="Data", user="postgres", password="1234")


            with con:
                cur=con.cursor()
                cur.execute("' CREATE TABLE Course(Id INT  SERIAL , name TEXT ,"
                            " description TEXT, price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1,PRIMARY KEY (Id)"'')

                print("Table created successfully")
        except Exception:
            print("Unable to create db")
    def insert(self,data):
        try:
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO Course(name,description,price,is_private) values(?,?,?,?),",data)
                return True
        except Exception:
            return False
    def fetchall(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT  * FROM Course")
                return cur.fetchall()
        except Exception:
            return False
    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql="DELETE FROM Course WHERE id=?"
                cur.execute(sql,[id])
                return True
        except Exception:
            return False
def main():
    print("*\n"*40)
    print("\n::Course Management :: \n")
    print("*\n"*40)
    print("\n")
    db=DatabaseConnection()
    print("#"*40)
    print("\n :: User Manaual ::\n")
    print("#"*40)
    print("\nPress !.Insert a new Course")
    print("\nPress 2.Show all Courses")
    print('\nPress 3.Delete a Course(need Id of Course)\n')
    print("#"*40)
    print("\n")
    choice=input("\nenter a choice:")
    if choice=='1':
        name=input("\nenter course name:")
        description=input("\nenter course description:")
        price=input("\n enter course price:")
        private=input("\nIs this course private (0/1):")
        if db.insert([name,description,price,private]):
            print("\ncourse added successfully")
        else:
            print("\nSomething is Wrong")
    elif choice=='2':
        print('\n:: Course List::')
        for index,item in enumerate(db.fetchall()):
            print("\n Sl no :: "+str(index+1))
            print("\n Course Id :: " + str(index[0]))
            print("\n Course name :: " + str(index[1]))
            print("\n Course description  :: " + str(index[2]))
            print("\n Course Price :: " + str(index[3]))
            private="Yes" if item[4] else 'No'
            print("\nIS Private:"+private)
            print("\n")
    elif choice=='3':
        record_id=input("enter the course id :")
        if db.delete_data(record_id):
            print("\nCourse was deleted ")
        else:
            print("\nSomething went wrong")
    else:
        print("\nBad Choice")
if __name__=='__main__':
    main()





