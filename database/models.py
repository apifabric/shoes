# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 31, 2024 10:23:40
# Database: sqlite:////tmp/tmp.kT4Db2I6Yn/shoes/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Stores customer information.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    RatingList : Mapped[List["Rating"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Stores employee data working at the store.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    StoreList : Mapped[List["Store"]] = relationship(back_populates="manager")



class Product(SAFRSBaseX, Base):
    """
    description: Represents products available in the store.
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    ProductPromotionList : Mapped[List["ProductPromotion"]] = relationship(back_populates="product")
    RatingList : Mapped[List["Rating"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")
    ShipmentList : Mapped[List["Shipment"]] = relationship(back_populates="product")



class Promotion(SAFRSBaseX, Base):
    """
    description: Manages promotions available for products.
    """
    __tablename__ = 'promotions'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductPromotionList : Mapped[List["ProductPromotion"]] = relationship(back_populates="promotion")



class Supplier(SAFRSBaseX, Base):
    """
    description: Stores supplier information for products.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="supplier")



class Inventory(SAFRSBaseX, Base):
    """
    description: Details about product inventory per supplier.
    """
    __tablename__ = 'inventories'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    supplier_id = Column(ForeignKey('suppliers.id'), nullable=False)
    quantity_supplied = Column(Integer, nullable=False)
    supply_date = Column(DateTime, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents customer orders.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class ProductPromotion(SAFRSBaseX, Base):
    """
    description: Connects promotions to products.
    """
    __tablename__ = 'product_promotions'
    _s_collection_name = 'ProductPromotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    promotion_id = Column(ForeignKey('promotions.id'), nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductPromotionList"))
    promotion : Mapped["Promotion"] = relationship(back_populates=("ProductPromotionList"))

    # child relationships (access children)



class Rating(SAFRSBaseX, Base):
    """
    description: Records product ratings from customers.
    """
    __tablename__ = 'ratings'
    _s_collection_name = 'Rating'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(String)
    rating_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("RatingList"))
    product : Mapped["Product"] = relationship(back_populates=("RatingList"))

    # child relationships (access children)



class Store(SAFRSBaseX, Base):
    """
    description: Contains store locations details.
    """
    __tablename__ = 'stores'
    _s_collection_name = 'Store'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    manager_id = Column(ForeignKey('employees.id'))

    # parent relationships (access parent)
    manager : Mapped["Employee"] = relationship(back_populates=("StoreList"))

    # child relationships (access children)
    ShipmentList : Mapped[List["Shipment"]] = relationship(back_populates="store")



class OrderItem(SAFRSBaseX, Base):
    """
    description: Details each item within an order.
    """
    __tablename__ = 'order_items'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    item_price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)



class Shipment(SAFRSBaseX, Base):
    """
    description: Tracks product shipments to stores.
    """
    __tablename__ = 'shipments'
    _s_collection_name = 'Shipment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    store_id = Column(ForeignKey('stores.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    shipped_quantity = Column(Integer, nullable=False)
    shipment_date = Column(DateTime)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ShipmentList"))
    store : Mapped["Store"] = relationship(back_populates=("ShipmentList"))

    # child relationships (access children)