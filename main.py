
from tkinter import *
from tkinter import ttk, messagebox
import random
import time
from datetime import datetime
import json
import os

# Color Scheme
COLOR_DARK = "#003049"
COLOR_RED = "#D62828"
COLOR_ORANGE = "#F77F00"
COLOR_YELLOW = "#FCBF49"
COLOR_LIGHT = "#EAE2B7"
COLOR_WHITE = "#FFFFFF"

class RestaurantSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x650+50+50")
        self.root.resizable(1, 1)
        self.root.title("Restaurant Management System - Premium Version")
        self.root.configure(bg=COLOR_DARK)
        
        # Data storage
        self.orders = []
        self.current_order = {}
        self.discount_code = None
        
        # Enhanced menu items with more details
        self.menu_items = {
            "Fries Meal": {"price": 25, "category": "Appetizers", "icon": "🍟", "description": "Crispy golden fries"},
            "Chicken Wings": {"price": 45, "category": "Appetizers", "icon": "🍗", "description": "Spicy BBQ wings"},
            "Caesar Salad": {"price": 28, "category": "Salads", "icon": "🥗", "description": "Fresh Caesar salad"},
            "Burger Meal": {"price": 35, "category": "Main Course", "icon": "🍔", "description": "Double beef burger"},
            "Cheese Burger": {"price": 30, "category": "Main Course", "icon": "🧀", "description": "With cheddar cheese"},
            "Lunch Meal": {"price": 40, "category": "Main Course", "icon": "🍱", "description": "Complete lunch box"},
            "Pizza Meal": {"price": 50, "category": "Main Course", "icon": "🍕", "description": "Margherita pizza"},
            "Drinks": {"price": 35, "category": "Beverages", "icon": "🥤", "description": "Soft drinks"},
            "Coffee": {"price": 15, "category": "Beverages", "icon": "☕", "description": "Fresh brewed coffee"},
            "Ice Cream": {"price": 20, "category": "Desserts", "icon": "🍦", "description": "Vanilla ice cream"}
        }
        
        self.load_data()
        self.create_main_window()
    
    def load_data(self):
        """Load saved orders from file"""
        if os.path.exists("restaurant_data.json"):
            try:
                with open("restaurant_data.json", "r") as f:
                    data = json.load(f)
                    self.orders = data.get("orders", [])
            except:
                self.orders = []
    
    def save_data(self):
        """Save orders to file"""
        data = {"orders": self.orders}
        with open("restaurant_data.json", "w") as f:
            json.dump(data, f, indent=4)

