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
    def register_new_order(order_data):
        new_data_id = ServiceOrder.insert_new_order(order_data=order_data)
        return jsonify({"mensagem": "order created successfully", "id": new_data_id}), 201

    @staticmethod
    def update_order(service_id, order_data):
        success = ServiceOrder.update_order(service_id=service_id, order_data=order_data)
        if success:
            return jsonify({"mensagem": "Order updated successful"})
        return jsonify({"erro": "Not Found", "código": "404"}), 404

    @staticmethod
    def delete_order(service_id):
        sucesso = ServiceOrder.delete_order(service_id)
        if sucesso:
            return jsonify({"mensagem": "deleted"})
        return jsonify({"erro": "not found", "código": "404"}), 404