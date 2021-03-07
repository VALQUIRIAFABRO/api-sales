from flask import Blueprint
from flask.wrappers import Request
from flask import request
from dto.sales_dto import SalesDTO
from entity.sales_entity import SalesEntity
import json
from utils.utils import ObjetJson

sales_bp = Blueprint('sales', __name__)


@sales_bp.route('/new/sales', methods=['POST']) 
def new_sales_json():
    if Request.is_json: 
        j = request.get_json()
        salesDTO = SalesDTO()
        salesEntity = SalesEntity(**j)
        sales = ObjetJson.to_json(salesDTO.new_sales(salesEntity))
        return sales, 200


@sales_bp.route('/edit/sales/<sales_id>', methods=['GET', 'POST'])
def update_sales_json(sales_id):
    if Request.is_json:
        j = request.get_json()
        salesDTO = SalesDTO()
        salesEntity = SalesEntity(**j)
        sales = ObjetJson.to_json(salesDTO.update_sales(sales_id, salesEntity))
        return sales, 200  
    
