from flask import jsonify
from ..models.service_order import ServiceOrder

class ServiceOrderController:

    @staticmethod
    def show_all():
        orders = ServiceOrder.get_all()
        return jsonify(orders)