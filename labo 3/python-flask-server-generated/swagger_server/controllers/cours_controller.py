import connexion
from flask import jsonify
import six

from swagger_server.models.cours import Cours  # noqa: E501
from swagger_server.models.seance import Seance  # noqa: E501
from swagger_server import util

# Base de données simulée pour les cours
cours_db = [
    {"sigle": "6GEI186", "titre": "Architecture des ordinateurs", "description": "Cours sur la programmation en langage assembleur pour la réalisation de jeux de lumières."},
    {"sigle": "6GIN250", "titre": "Santé et sécurité au travail", "description": "Techniques de planification sécuritaire pour les projets de construction."},
    {"sigle": "6GEI300", "titre": "Electronique", "description": "Étude de la transmission audio à l'aide de la technologie infrarouge."},
    {"sigle": "8PRO128", "titre": "Programmation orientée objet", "description": "Application des principes de la programmation orientée objet pour la gestion d'un garage."},
    {"sigle": "6GEI418", "titre": "Signaux et systèmes", "description": "Conception et simulation de filtres électroniques en utilisant Matlab."},
    {"sigle": "8INF334", "titre": "Modélisation et developpement objet", "description": "Application des méthodologies Agile Scrum pour gérer les réservations d'un centre de villégiature."},
    {"sigle": "6GEI415", "titre": "Méthodes de conception en électronique", "description": "Conception d'un amplificateur audio sur une plaquette PCB."},
    {"sigle": "6GEI435", "titre": "Systèmes asservis", "description": "Conception et simulation d'un système d'inclinaison de panneaux photovoltaïques."},
    {"sigle": "6GEN105", "titre": "Ingenierie et méthodes pratiques", "description": "Projet d'intégration de panneaux solaires et de freinage régénératif dans les transports en commun."},
    {"sigle": "6GEI311", "titre": "Architecture des logiciels", "description": "Développement de concepts d'architecture logicielle et gestion des bibliothèques en utilisant Python."}
]

# Base de données simulée pour les séances
seances_db = [
    {"sigle": "6GEI186", "date": "2024-09-15", "sujet": "Introduction à l'assembleur"},
    {"sigle": "6GEI186", "date": "2024-09-22", "sujet": "Jeux de lumières - Partie 1"},
    {"sigle": "6GEI311", "date": "2024-10-05", "sujet": "Conception d'une architecture logicielle"},
    {"sigle": "6GEI311", "date": "2024-10-12", "sujet": "Gestion des bibliothèques en Python"},
    {"sigle": "6GIN250", "date": "2024-09-20", "sujet": "Sécurité sur les chantiers"},
]

def cours_get():  # noqa: E501
    """Obtenir la liste des cours

    :rtype: List[Cours]
    """
    return jsonify(cours_db), 200

def cours_sigle_delete(sigle):  # noqa: E501
    """Supprimer un cours

    :param sigle: Sigle du cours à supprimer
    :type sigle: str

    :rtype: None
    """
    global cours_db
    cours_existant = next((cours for cours in cours_db if cours["sigle"] == sigle), None)
    if cours_existant is None:
        return {"message": "Cours non trouvé"}, 404

    # Supprimer le cours de la base de données
    cours_db = [cours for cours in cours_db if cours["sigle"] != sigle]
    return '', 204

def cours_sigle_get(sigle):  # noqa: E501
    """Obtenir un cours par son sigle

    :param sigle: Sigle du cours
    :type sigle: str

    :rtype: Cours
    """
    cours = next((cours for cours in cours_db if cours["sigle"] == sigle), None)
    if cours is None:
        return {"message": "Cours non trouvé"}, 404
    return jsonify(cours), 200

def cours_sigle_put(body, sigle):  # noqa: E501
    """Mettre à jour un cours existant

    :param body: Contenu du cours à mettre à jour
    :type body: dict | bytes
    :param sigle: Sigle du cours à mettre à jour
    :type sigle: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # Parse le corps de la requête JSON
        for cours in cours_db:
            if cours["sigle"] == sigle:
                # Mettre à jour le cours existant
                cours["titre"] = body.get("titre", cours["titre"])
                cours["description"] = body.get("description", cours["description"])
                return '', 204

    return {"message": "Cours non trouvé"}, 404

def cours_post(body):  # noqa: E501
    """Ajouter un nouveau cours

    :param body: Contenu du cours à ajouter
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # Parse le corps de la requête JSON
        new_sigle = body.get("sigle", None)
        if not new_sigle:
            return {"message": "Le sigle est requis pour ajouter un nouveau cours."}, 400

        # Vérifier si le cours existe déjà
        cours_existant = next((cours for cours in cours_db if cours["sigle"] == new_sigle), None)
        if cours_existant:
            return {"message": "Un cours avec ce sigle existe déjà."}, 409

        new_cours = {
            "sigle": new_sigle,
            "titre": body["titre"],
            "description": body["description"]
        }
        cours_db.append(new_cours)
        return jsonify(new_cours), 201

    return {"message": "Format de données invalide"}, 400

def cours_sigle_seances_get(sigle):  # noqa: E501
    """Obtenir la liste des séances d'un cours

    :param sigle: Sigle du cours
    :type sigle: str

    :rtype: List[Seance]
    """
    # Récupérer les séances associées au cours par son sigle
    seances = [seance for seance in seances_db if seance["sigle"] == sigle]
    if not seances:
        return {"message": "Aucune séance trouvée pour ce cours"}, 404
    return jsonify(seances), 200
