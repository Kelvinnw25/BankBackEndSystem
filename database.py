import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="atmadvance"
        )
        self.cursor = self.conn.cursor()

    def create_account(self, username, password, account_number, account_balance, pin):
        sql = "INSERT INTO accounts (username, password, account_number, account_balance, pin) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (username, password, account_number, account_balance, pin))
        self.conn.commit()

    def get_account(self, username, password):
        sql = "SELECT username, password, account_number, account_balance, pin FROM accounts WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def update_balance(self, account_number, new_balance):
        sql = "UPDATE accounts SET account_balance = %s WHERE account_number = %s"
        self.cursor.execute(sql, (new_balance, account_number))
        self.conn.commit()

    def get_account_by_number(self, account_number):
        sql = "SELECT username, password, account_number, account_balance, pin FROM accounts WHERE account_number = %s"
        self.cursor.execute(sql, (account_number,))
        return self.cursor.fetchone()