
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



############## YOUSTINA - MAIN WINDOW ######################

    def create_main_window(self):
        """Window 1: Main Order Window"""
        # Top Frame
        Tops = Frame(self.root, bg=COLOR_DARK, height=80, relief=FLAT)
        Tops.pack(side=TOP, fill=X)
        
        localtime = time.asctime(time.localtime(time.time()))
        
        title_label = Label(Tops, font=('Helvetica', 24, 'bold'), 
                           text="🍽️ PREMIUM RESTAURANT MANAGEMENT SYSTEM", 
                           fg=COLOR_YELLOW, bg=COLOR_DARK)
        title_label.pack(pady=8)
        
        time_label = Label(Tops, font=('Helvetica', 11), 
                          text=f"📅 {localtime}", 
                          fg=COLOR_ORANGE, bg=COLOR_DARK)
        time_label.pack()
        
        # Control Buttons Frame
        control_frame = Frame(Tops, bg=COLOR_DARK)
        control_frame.pack(pady=8)
        
        buttons = [
            ("📊 Dashboard", self.open_dashboard, COLOR_ORANGE),
            ("📜 Order History", self.open_history, COLOR_RED),
            ("📋 Menu", self.open_menu, COLOR_YELLOW),
            ("⚙️ Settings", self.open_settings, COLOR_DARK),
            ("❌ Exit", self.exit_app, COLOR_RED)
        ]
        
        for text, cmd, color in buttons:
            btn = Button(control_frame, text=text, command=cmd, padx=12, pady=4,
                        font=('Helvetica', 10, 'bold'), bg=color, fg=COLOR_WHITE,
                        cursor="hand2", relief=RAISED, bd=2)
            btn.pack(side=LEFT, padx=3)
        
        # Main Content - Split into two parts
        main_content = Frame(self.root, bg=COLOR_LIGHT)
        main_content.pack(fill=BOTH, expand=True, padx=8, pady=8)
        
        # Left side - Order entry (expandable)
        left_frame = Frame(main_content, bg=COLOR_LIGHT)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 5))
        
        # Right side - Order summary (fixed width)
        right_frame = Frame(main_content, bg=COLOR_LIGHT, width=320)
        right_frame.pack(side=RIGHT, fill=BOTH, padx=(5, 0))
        right_frame.pack_propagate(False)
        
        self.create_order_section(left_frame)
        self.create_summary_section(right_frame)






############## Nancy Nagy - DASHBOARD ####################

    def open_dashboard(self):
        """Window 2: Dashboard Window"""
        dashboard = Toplevel(self.root)
        dashboard.title("📊 Dashboard - Statistics")
        dashboard.geometry("750x450+300+100")
        dashboard.configure(bg=COLOR_LIGHT)
        
        Label(dashboard, text="Sales Dashboard", font=('Helvetica', 20, 'bold'),
              fg=COLOR_RED, bg=COLOR_LIGHT).pack(pady=12)
        
        total_orders = len(self.orders)
        total_revenue = sum(order['total'] for order in self.orders)
        avg_order = total_revenue / total_orders if total_orders > 0 else 0
        
        stats_frame = Frame(dashboard, bg=COLOR_LIGHT)
        stats_frame.pack(pady=12)
        
        stats = [
            ("📦 Total Orders", total_orders),
            ("💰 Total Revenue", f"EGP {total_revenue:.2f}"),
            ("📊 Average Order", f"EGP {avg_order:.2f}"),
            ("🍽️ Menu Items", len(self.menu_items))
        ]
        
        for i, (label, value) in enumerate(stats):
            frame = Frame(stats_frame, bg=COLOR_WHITE, bd=2, relief=GROOVE)
            frame.grid(row=0, column=i, padx=8, pady=5)
            Label(frame, text=label, font=('Helvetica', 10, 'bold'),
                  bg=COLOR_WHITE, fg=COLOR_DARK).pack(pady=4, padx=8)
            Label(frame, text=str(value), font=('Helvetica', 14, 'bold'),
                  bg=COLOR_WHITE, fg=COLOR_RED).pack(pady=4, padx=8)
        
        Button(dashboard, text="Close", command=dashboard.destroy,
               bg=COLOR_RED, fg=COLOR_WHITE, font=('Helvetica', 10),
               cursor="hand2").pack(pady=12)
