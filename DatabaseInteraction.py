import pyodbc


class SQLServerInteractionWithPython:
    server_name = 'DESKTOP-ET98443\SQLEXPRESS'
    database_name = 'HotelManagementSystem'
    user_name = 'hrish'
    user_pass = '**my-password**'
    connection = ''
    select_query = '''select *  from HMS_Schema.Users_Table'''
    insert_query = '''insert into HMS_Schema.Users_Table values ('Hrih96', 'hrishh@11', 'DevOps', 'hrish11', '1222334454', '2122334454', 'Sion', 'hrish24@cap.com')'''
    update_query = '''query'''

    def establish_connection(self):
        try:
            self.connection = pyodbc.connect(driver='{SQL Server}', host=self.server_name, database=self.database_name,
                                             trusted_connection='Yes')
            print("MySQL Database connection successful")
        except pyodbc.Error as err:
            print(f"Error: '{err}'")
            self.connection.close()

    def get_result_from_Sql(self):
        cursor = self.connection.cursor()
        cursor.execute(self.select_query)
        rows = cursor.fetchall()
        result_of_query = []
        for row in rows:
            result_of_query.append(row)
        print(result_of_query)
        self.connection.close()

    def insert_into_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.insert_query)
            self.connection.commit()
            self.connection.close()
            print("Query inserted successfully")
        except pyodbc.Error as err:
            print(f"Error: '{err}'")
            self.connection.close()

    def update_into_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.update_query)
            self.connection.commit()
            self.connection.close()
            print("Table updated successfully")
        except pyodbc.Error as err:
            print(f"Error: '{err}'")
            self.connection.close()


Instance_of_class = SQLServerInteractionWithPython()
Instance_of_class.establish_connection()
# Instance_of_class.get_result_from_Sql()
Instance_of_class.insert_into_table()
Instance_of_class.establish_connection()
Instance_of_class.get_result_from_Sql()