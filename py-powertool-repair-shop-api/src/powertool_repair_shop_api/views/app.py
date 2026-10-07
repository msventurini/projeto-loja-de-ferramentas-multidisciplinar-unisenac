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

@app.route('/series', methods=['POST'])
def create_new_order():
    order_data = request.json
    return ServiceOrderController.register_new_order(order_data=order_data)
