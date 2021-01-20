# coding: utf-8
from application import db




class FoodStockChangeLog(db.Model):
    __tablename__ = 'food_stock_change_log'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, nullable=False, index=True, info='商品id')
    unit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='变更多少')
    total_stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='变更之后总量')
    note = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='备注字段')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
