import sqlite3


def execute_sql_script(filepath: str, connection: sqlite3.Connection):
    with open(filepath, "r") as sql_file:
        sql_script = sql_file.read()
    cursor = connection.cursor()
    cursor.executescript(sql_script)
    cursor.close()


def execute_query(query: str, connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute(query)
    objects = cursor.fetchall()
    cursor.close()
    return objects


def main():
    with sqlite3.connect(":memory:") as sqlite_connection:
        execute_sql_script("./db_script.txt", sqlite_connection)
        query_1 = """
            SELECT * FROM article
            LEFT JOIN comment ON article.id = comment.article_id
            WHERE comment.id is NULL
        """
        articles = execute_query(query_1, sqlite_connection)
        assert [article[0] for article in articles] == [2, 3]
        query2 = """
            SELECT * FROM article
            WHERE article.id NOT IN (
                SELECT DISTINCT article_id FROM comment
            )
            """
        articles = execute_query(query2, sqlite_connection)
        assert [article[0] for article in articles] == [2, 3]


if __name__ == "__main__":
    main()
