from flask import jsonify
from ..models.brand import BrandModel

class BrandController:

    @staticmethod
    def show_all():
        brands = BrandModel.get_all()
        return jsonify(brands)