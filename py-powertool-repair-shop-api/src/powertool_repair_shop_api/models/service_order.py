from ..config.connection import get_connection

class ServiceOrder:
    
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT PowerTool.PowerToolMarketingName, Brand.BrandName, ServiceOrder.ServiceDescription, ServiceOrder.Price, ServiceOrder.CheckInDate, ServiceOrder.CheckOutDate, Customer.FirstName FROM ServiceOrder INNER JOIN Customer USING (CustomerGovID) INNER JOIN PowerTool USING (PowerToolID) INNER JOIN Brand USING (BrandID)') 
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
