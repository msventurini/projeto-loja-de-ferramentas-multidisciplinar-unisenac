from flask import jsonify
from ..models.service_order import ServiceOrder

class ServiceOrderController:

    @staticmethod
    def show_all():
        orders = ServiceOrder.get_all()
        return jsonify(orders)

    @staticmethod
    def mostrar_por_id(service_id: int):
        order = ServiceOrder.get_by_service_id(service_id)
        if order:
            return jsonify(order)
        return jsonify({"erro": "order not found"}), 404

    @staticmethod
    def cadastrar(order_data):
        new_data_id = ServiceOrder.insert_new_order(order_data=order_data)
        return jsonify({"mensagem": "Série criada com sucesso", "id": new_data_id}), 201
