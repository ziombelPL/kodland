meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "odpowiedż na żart",
            "SHEESH": "lekka dezprobata",
            "CREEPY": "straszny, złowieszczy",
            "AGGRO": "stać się agresywnym/zły",
            }
print("Witaj w słowniku.")
for i in range(5):
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
    word = word.upper()
    word = word.strip()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Brak słowa w bazie danych")
