from flask import Flask, request
from flasgger import Swagger, swag_from
from ..controllers.brand_controller import BrandController

# from config.swagger


app = Flask(__name__)


@app.route('/brands', methods=['GET'])
def list_all_power_tool_brands():
    return BrandController.show_all()