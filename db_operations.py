import sqlite3

def add_seasonal_flavor(name, description, ingredients):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO SeasonalFlavors (name, description, ingredients) VALUES (?, ?, ?)''', (name, description, ingredients))
    conn.commit()
    conn.close()

def add_ingredient(name, quantity):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Ingredients (name, quantity) VALUES (?, ?)''', (name, quantity))
    conn.commit()
    conn.close()

def add_customer_suggestion(name, suggested_flavor, allergy_concern):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO CustomerSuggestions (name, suggested_flavor, allergy_concern) VALUES (?, ?, ?)''', (name, suggested_flavor, allergy_concern))
    conn.commit()
    conn.close()

def add_allergen(name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Allergens (name) VALUES (?)''', (name,))
    conn.commit()
    conn.close()

def search_flavors(keyword):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM SeasonalFlavors WHERE name LIKE ? OR description LIKE ?''', ('%' + keyword + '%', '%' + keyword + '%'))
    results = cursor.fetchall()
    conn.close()
    return results

def add_to_cart(flavor_id):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Cart (flavor_id) VALUES (?)''', (flavor_id,))
    conn.commit()
    conn.close()

def view_cart():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT SeasonalFlavors.name FROM Cart JOIN SeasonalFlavors ON Cart.flavor_id = SeasonalFlavors.id''')
    results = cursor.fetchall()
    conn.close()
    return results
