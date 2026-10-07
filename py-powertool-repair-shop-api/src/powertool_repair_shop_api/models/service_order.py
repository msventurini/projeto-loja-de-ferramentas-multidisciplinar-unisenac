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
        valores = (dados.get('ServiceID'), dados.get('ServiceDescription'), dados.get('PowerToolID'), dados.get('CustomerGovID'), dados.get('Price'), dados.get('CheckInDate'), dados.get('CheckOutDate'))
        cursor.execute(sql, valores)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return last_id
