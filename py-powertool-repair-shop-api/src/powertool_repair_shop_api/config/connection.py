from mysql import connector 

def get_connection() -> connector: # type: ignore
    return connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="",
        database="tool_repair_shop"
    ) # type: ignore
