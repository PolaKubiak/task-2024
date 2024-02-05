shopping = [("piekarnia", ["chleb", "bułki", "pączek"]), ("warzywniak", ["marchew", "seler", "rukola"])]
#testowanie edycji kodu zdalnie aaaaaaa
#usunięte - poprawka nr 2

for shop, item in shopping:
    print(f"Idę do {shop.capitalize()} i kupuję tam {item} ")
#kolejny testttttttttttttt
shopping_new = dict(shopping)

print(f"W sumie kupuję {len(shopping_new.get("piekarnia")) + len(shopping_new.get("warzywniak"))} produktów")
print("Działa, czy nie działa?")

#czy działa? do commitu nr 2 

