shopping = [("piekarnia", ["chleb", "bułki", "pączek"]), ("warzywniak", ["marchew", "seler", "rukola"])]

print("Lista zakupów")

for shop, item in shopping:
    print(f"Idę do {shop.capitalize()} i kupuję tam {item} ")

shopping_new = dict(shopping)

print(f"W sumie kupuję {len(shopping_new.get("piekarnia")) + len(shopping_new.get("warzywniak"))} produktów")

