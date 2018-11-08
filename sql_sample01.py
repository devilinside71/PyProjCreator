# -*- coding: utf-8 -*-
""" Sample SQLite3 module.
"""

import sqlite3


class MAIN():
    """ Sample SQLite3 class.
    """

    def __init__(self):
        self.database = "C:\\sqlite\\db\\pythonsqlite.db"
        self.sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

        self.sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""
        self.connection = None

    def create_connection(self, db_file):
        """ Create a database connection to the SQLite database

        Arguments:
            db_file {sqlite3 db} -- database file name

        Returns:
            various -- database connection or None
        """

        try:
            conn = sqlite3.connect(db_file)
            print('SQLite version: {0}'.format(sqlite3.version))
            return conn
        except sqlite3.Error as sql_err:
            print(sql_err)
        return None

    def create_table(self, conn, create_table_sql):
        """ Create a table from the create_table_sql statement.

        Arguments:
            conn {obj} -- Connection object
            create_table_sql {statement} -- a CREATE TABLE statement
        """

        try:
            sql_cursor = conn.cursor()
            sql_cursor.execute(create_table_sql)
        except sqlite3.Error as sql_err:
            print(sql_err)

    def create_project_data(self, conn, project_data):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?) '''
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql, project_data)
        return sql_cursor.lastrowid

    def create_task_data(self, conn, task_data):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """

        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                VALUES(?,?,?,?,?,?) '''
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql, task_data)
        return sql_cursor.lastrowid

    # create a database connection
    def execute_sql_creation(self, close_connection=False):
        """ Create database and tables.
        """

        self.connection = self.create_connection(self.database)
        if self.connection is not None:
            # create projects table
            self.create_table(self.connection, self.sql_create_projects_table)
            # create tasks table
            self.create_table(self.connection, self.sql_create_tasks_table)
            if close_connection:
                self.connection.close()
        else:
            print('Error! Cannot create the database connection.')

    def add_sample_data(self):
        """ Add sample data.
        """

        with self.connection:
            # create a new project
            project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
            project_id = self.create_project_data(self.connection, project)

            # tasks
            task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
            task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

            # create tasks
            self.create_task_data(self.connection, task_1)
            self.create_task_data(self.connection, task_2)


if __name__ == '__main__':
    MAIN_CLASS = MAIN()
    MAIN_CLASS.execute_sql_creation()
    MAIN_CLASS.add_sample_data()
