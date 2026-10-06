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