from flask import Flask, request
from flasgger import Swagger, swag_from
from ..controllers.brand_controller import BrandController
from ..controllers.service_order_controller import ServiceOrderController

# from config.swagger


app = Flask(__name__)


@app.route('/brands', methods=['GET'])
def list_all_power_tool_brands():
    return BrandController.show_all()

@app.route('/orders', methods=['GET'])
def list_all_service_orders():
    return ServiceOrderController.show_all()

@app.route('/orders/<int:service_id>', methods=['GET'])
def get_order_by_id(service_id: int):
    return ServiceOrderController.mostrar_por_id(service_id)

@app.route('/orders', methods=['POST'])
def create_new_order():
    order_data = request.json
    return ServiceOrderController.register_new_order(order_data=order_data)


@app.route('/orders/<int:service_id>', methods=['PUT'])
def update_order(service_id):
    order_data = request.json
    return ServiceOrderController.update_order(service_id=service_id, order_data=order_data)

@app.route('/orders/<int:service_id>', methods=['DELETE'])
def delete_order(service_id):
    return ServiceOrderController.delete_order(service_id)