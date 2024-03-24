

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="votre_base_de_donnees"
)

# Création d'un curseur
cursor = conn.cursor()

# Définition d'une requête SQL d'insertion
sql = "INSERT INTO Users (username, email) VALUES (%s, %s)"
values = ("john_doe", "john@example.com")

# Exécution de la requête SQL
cursor.execute(sql, values)

# Valider la transaction
conn.commit()

# Fermer le curseur et la connexion
cursor.close()
conn.close()
