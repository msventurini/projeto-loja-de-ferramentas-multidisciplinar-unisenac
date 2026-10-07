from ..config.connection import get_connection

class ServiceOrder:
    
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT ServiceOrder.ServiceID, PowerTool.PowerToolMarketingName, Brand.BrandName, ServiceOrder.ServiceDescription, ServiceOrder.Price, ServiceOrder.CheckInDate, ServiceOrder.CheckOutDate, Customer.FirstName FROM ServiceOrder INNER JOIN Customer USING (CustomerGovID) INNER JOIN PowerTool USING (PowerToolID) INNER JOIN Brand USING (BrandID)') 
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def get_by_service_id(service_id: int):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ServiceOrder.ServiceID, PowerTool.PowerToolMarketingName, Brand.BrandName, ServiceOrder.ServiceDescription, ServiceOrder.Price, ServiceOrder.CheckInDate, ServiceOrder.CheckOutDate, Customer.FirstName FROM ServiceOrder INNER JOIN Customer USING (CustomerGovID) INNER JOIN PowerTool USING (PowerToolID) INNER JOIN Brand USING (BrandID) WHERE ServiceID = %s", (service_id,)) 
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def insert_new_order(order_data):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO ServiceOrder(ServiceID, ServiceDescription, PowerToolID, CustomerGovID, Price, CheckInDate, CheckOutDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        order_values = (order_data.get('ServiceID'), order_data.get('ServiceDescription'), order_data.get('PowerToolID'), order_data.get('CustomerGovID'), order_data.get('Price'), order_data.get('CheckInDate'), order_data.get('CheckOutDate'))
        cursor.execute(sql, order_values)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id

    @staticmethod
    def update_order(service_id, order_data):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE ServiceOrder set ServiceDescription=%s, PowerToolID=%s, CustomerGovID=%s, Price=%s, CheckInDate=%s, CheckOutDate=%s WHERE ServiceID=%s"
        order_values = (order_data.get('ServiceDescription'), order_data.get('PowerToolID'), order_data.get('CustomerGovID'), order_data.get('Price'), order_data.get('CheckInDate'), order_data.get('CheckOutDate'), service_id)
        cursor.execute(sql, order_values)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0

    @staticmethod
    def delete_order(service_id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM ServiceOrder WHERE ServiceID = %s"
        valores = (service_id,)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0