import _sqlite3

class Database:
    DB_NAME = "students.db"
    @staticmethod
    def _connect():
        return _sqlite3.connect(Database.DB_NAME)
    
    @staticmethod
    def _create_table():
        with Database._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL
                )
            """)

        @staticmethod
        def insert_student(name, email,age ,gender):
            with Database._connect() as conn:
                conn.execute("INSERT INTO students(name, email, age,gender) VALUES(?,?,?,?)", (name, email, age,gender,))
        @staticmethod
        def read_students():
            with Database._connect() as conn:
                cursor =conn.execute("SELECT * FROM students")
                return cursor.fetchall()
            
        @staticmethod
        def update_student(id, name, email, age,gender):
            with Database._connect() as conn:
                conn.execute("UPDATE students SET name = ?, email = ?, age =?,gender=? WHERE id = ?", (name, email, age,gender))
        @staticmethod
        def delete_student(id):
            with Database._connect() as conn:
                conn.execute("DELETE FROM students WHERE id = ?", (id,))
    


Database._create_table()    

