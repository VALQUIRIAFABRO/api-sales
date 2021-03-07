from controller.sales_controller import sales_bp
from controller.discount_controller import discount_bp


def make_rout(app):
    app.register_blueprint(sales_bp)
    app.register_blueprint(discount_bp)
    return app
    