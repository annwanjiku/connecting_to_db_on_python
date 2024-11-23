import mysql.connector
from config import host, user, password


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=host,
        password=password,
        username=user,
        port=3306,
        database=db_name,
        auth_plugin="mysql_native_password"

    )
    return cnx


def do_something():
    db_connection = None

    try:
        db_name = "bakery"
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        print("\nConnection successful to %s database \n" % db_name)

        query = """SELECT * from SWEET"""
        cursor.execute(query)
        result = cursor.fetchall()

        for each in result:
            print(each)

        return result

    except Exception as e:
        print(f"Exception {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("\nDatabase connection closed!")


def main():
    do_something()


if __name__ == "__main__":
    main()
