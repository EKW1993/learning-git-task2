#Zadanie 
print("Lista zakupów")
shopping_dict = {"piekarnia": ["chleb", "bułki", "pączek"], "warzywniak": ["marchew", "seler", "rukola", "pietruszka", "por"]} 

for shop, products in shopping_dict.items():
    products_list = [produkt.capitalize() for produkt in products] 
    shop = shop.capitalize() 
    
    print("Idę do", shop, ", kupuję tu następujące rzeczy:", products_list)

X = sum(len(products) for products in shopping_dict.values())
print("W sumie kupuję",X, "produktów.")