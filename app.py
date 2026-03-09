from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    produit_dict = [
        {"nom": "chaussures", "prix": 40, "images": "chossur_1.jpg"},
        {"nom": "chaussures", "prix": 45, "images": "chossur_2.jpg"},
        {"nom": "chaussures", "prix": 40, "images": "chossur_3.jpg"},
        {"nom": "chaussures", "prix": 45, "images": "chossur_4.jpg"},
        {"nom": "chaussures", "prix": 35, "images": "chossur_5.jpg"},
        {"nom": "chaussures", "prix": 40, "images": "chossur_6.jpg"},
        {"nom": "chaussures", "prix": 40, "images": "chossur_7.jpg"},
        {"nom": "chaussures", "prix": 50, "images": "chossur_8.jpg"},
        {"nom": "chaussures", "prix": 35, "images": "chossur_9.jpg"},
        {"nom": "chaussures", "prix": 45, "images": "chossur_10.jpg"},

        {"nom": "accessoir", "prix": 50, "images": "accessoir_1.jpg"},
        {"nom": "accessoir", "prix": 50, "images": "accessoir_2.jpg"},
        {"nom": "accessoir", "prix": 50, "images": "accessoire_3.jpg"},

        {"nom": "pile", "prix": 30, "images": "pile_1.jpg"},
        {"nom": "pile", "prix": 30, "images": "pile_2.jpg"},
        {"nom": "pile", "prix": 30, "images": "pile_3.jpg"},
        {"nom": "pile", "prix": 30, "images": "pile_4.jpg"},
        
        

    ]
    return render_template("index.html", produit_flask=produit_dict)

