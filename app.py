from db_operations import (
    add_seasonal_flavor, add_ingredient, add_customer_suggestion, 
    add_allergen, search_flavors, add_to_cart, view_cart
)

def main():
    while True:
        print("\nWelcome to the Ice Cream Parlor!")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. Add Allergen")
        print("5. Search Flavors")
        print("6. Add to Cart")
        print("7. View Cart")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            description = input("Enter flavor description: ")
            ingredients = input("Enter ingredients (comma separated): ")
            add_seasonal_flavor(name, description, ingredients)
            print("Seasonal flavor added!")
        elif choice == '2':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            add_ingredient(name, quantity)
            print("Ingredient added!")
        elif choice == '3':
            name = input("Enter your name: ")
            suggested_flavor = input("Enter suggested flavor: ")
            allergy_concern = input("Enter any allergy concerns: ")
            add_customer_suggestion(name, suggested_flavor, allergy_concern)
            print("Customer suggestion added!")
        elif choice == '4':
            name = input("Enter allergen name: ")
            add_allergen(name)
            print("Allergen added!")
        elif choice == '5':
            keyword = input("Enter search keyword: ")
            results = search_flavors(keyword)
            if results:
                print("Search Results:")
                for result in results:
                    print(f"ID: {result[0]}, Name: {result[1]}, Description: {result[2]}, Ingredients: {result[3]}")
            else:
                print("No results found.")
        elif choice == '6':
            flavor_id = int(input("Enter flavor ID to add to cart: "))
            add_to_cart(flavor_id)
            print("Flavor added to cart!")
        elif choice == '7':
            cart_items = view_cart()
            if cart_items:
                print("Cart Items:")
                for item in cart_items:
                    print(f"- {item[0]}")
            else:
                print("Cart is empty.")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
