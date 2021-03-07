from dto.discounts_dto import DiscountDTO
from flask import Blueprint
from flask.wrappers import Request
from flask import request
from entity.discount_entity import DiscountEntity
import json
from utils.utils import ObjetJson


discount_bp = Blueprint('discount', __name__)


@discount_bp.route('/new/discount', methods=['POST'])
def new_discount_json():
    if Request.is_json:
        j = request.get_json()
        discountDTO = DiscountDTO()
        discountEntity = DiscountEntity(**j)
        sales = ObjetJson.to_json(discountDTO.new_discount(discountEntity))
        return sales, 200


@discount_bp.route('/edit/discount/<discount_id>', methods=['GET', 'POST'])
def update_discount_json(discount_id):
    if Request.is_json:
        j = request.get_json()
        discountDTO = DiscountDTO()
        discountEntity = DiscountEntity(**j)
        discount = ObjetJson.to_json(
            discountDTO.update_discount(discount_id, discountEntity))
        return discount, 200
