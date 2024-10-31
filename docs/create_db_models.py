# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    """description: Stores customer information."""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)

class Product(Base):
    """description: Represents products available in the store."""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

class Supplier(Base):
    """description: Stores supplier information for products."""
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)

class Inventory(Base):
    """description: Details about product inventory per supplier."""
    __tablename__ = 'inventories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    quantity_supplied = Column(Integer, nullable=False)
    supply_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

class Order(Base):
    """description: Represents customer orders."""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    total_amount = Column(Float, default=0.0)

class OrderItem(Base):
    """description: Details each item within an order."""
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    item_price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)

class Employee(Base):
    """description: Stores employee data working at the store."""
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    hire_date = Column(DateTime, default=datetime.datetime.utcnow)

class Store(Base):
    """description: Contains store locations details."""
    __tablename__ = 'stores'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String, nullable=False)
    manager_id = Column(Integer, ForeignKey('employees.id'), nullable=True)

class Shipment(Base):
    """description: Tracks product shipments to stores."""
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    shipped_quantity = Column(Integer, nullable=False)
    shipment_date = Column(DateTime, default=datetime.datetime.utcnow)

class Promotion(Base):
    """description: Manages promotions available for products."""
    __tablename__ = 'promotions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

class ProductPromotion(Base):
    """description: Connects promotions to products."""
    __tablename__ = 'product_promotions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    promotion_id = Column(Integer, ForeignKey('promotions.id'), nullable=False)

class Rating(Base):
    """description: Records product ratings from customers."""
    __tablename__ = 'ratings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(String, nullable=True)
    rating_date = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sample Data Insertion
session.add_all([
    Customer(name="Alice", email="alice@example.com", address="123 Apple St"),
    Customer(name="Bob", email="bob@example.com", address="456 Birch St"),
    Product(name="Running Shoes", category="Footwear", price=50.0, stock_quantity=100),
    Product(name="Sandals", category="Footwear", price=30.0, stock_quantity=50),
    Supplier(name="Shoe Supplier A", contact_info="contact@supplierA.com"),
    Supplier(name="Shoe Supplier B", contact_info="contact@supplierB.com"),
    Inventory(product_id=1, supplier_id=1, quantity_supplied=50, supply_date=datetime.datetime(2023, 9, 10)),
    Inventory(product_id=2, supplier_id=2, quantity_supplied=40, supply_date=datetime.datetime(2023, 9, 11)),
    Order(customer_id=1, order_date=datetime.datetime(2023, 10, 1), total_amount=80.0),
    OrderItem(order_id=1, product_id=1, quantity=1, item_price=50.0, amount=50.0),
    OrderItem(order_id=1, product_id=2, quantity=1, item_price=30.0, amount=30.0),
    Employee(name="Charlie", position="Manager", hire_date=datetime.datetime(2023, 1, 1)),
    Store(location="Downtown", manager_id=1),
    Shipment(store_id=1, product_id=1, shipped_quantity=20, shipment_date=datetime.datetime(2023, 10, 2)),
    Promotion(name="Holiday Sale", discount_percentage=10, start_date=datetime.datetime(2023, 12, 1), end_date=datetime.datetime(2023, 12, 31)),
    ProductPromotion(product_id=1, promotion_id=1),
    Rating(product_id=1, customer_id=1, rating=5, review="Very comfortable!", rating_date=datetime.datetime(2023, 10, 5)),
])

session.commit()
