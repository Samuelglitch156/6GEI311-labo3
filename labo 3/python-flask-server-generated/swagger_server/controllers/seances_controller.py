import connexion
from flask import jsonify
import six

from swagger_server.models.cours import Cours  # noqa: E501
from swagger_server.models.seance import Seance  # noqa: E501
from swagger_server import util


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


seances_db = [
    # Séances pour le cours 6GEI186
    {"sigle": "6GEI186", "date": "2024-09-15", "sujet": "Introduction à l'assembleur"},
    {"sigle": "6GEI186", "date": "2024-09-22", "sujet": "Jeux de lumières - Partie 1"},
    {"sigle": "6GEI186", "date": "2024-09-29", "sujet": "Jeux de lumières - Partie 2"},
    {"sigle": "6GEI186", "date": "2024-10-06", "sujet": "Optimisation de code assembleur"},
    
    # Séances pour le cours 6GIN250
    {"sigle": "6GIN250", "date": "2024-09-20", "sujet": "Sécurité sur les chantiers"},
    {"sigle": "6GIN250", "date": "2024-09-27", "sujet": "Évaluation des risques"},
    {"sigle": "6GIN250", "date": "2024-10-04", "sujet": "Planification sécuritaire"},
    {"sigle": "6GIN250", "date": "2024-10-11", "sujet": "Normes de sécurité en construction"},

    # Séances pour le cours 6GEI300
    {"sigle": "6GEI300", "date": "2024-09-14", "sujet": "Introduction à l'électronique"},
    {"sigle": "6GEI300", "date": "2024-09-21", "sujet": "Transmission audio via infrarouge"},
    {"sigle": "6GEI300", "date": "2024-09-28", "sujet": "Conception de circuits de transmission"},
    {"sigle": "6GEI300", "date": "2024-10-05", "sujet": "Mesure des performances des circuits"},

    # Séances pour le cours 8PRO128
    {"sigle": "8PRO128", "date": "2024-09-16", "sujet": "Introduction à la programmation orientée objet"},
    {"sigle": "8PRO128", "date": "2024-09-23", "sujet": "Gestion des objets en mémoire"},
    {"sigle": "8PRO128", "date": "2024-09-30", "sujet": "Application à la gestion de garage"},
    {"sigle": "8PRO128", "date": "2024-10-07", "sujet": "Conception d'une interface utilisateur"},

    # Séances pour le cours 6GEI418
    {"sigle": "6GEI418", "date": "2024-09-12", "sujet": "Introduction aux signaux et systèmes"},
    {"sigle": "6GEI418", "date": "2024-09-19", "sujet": "Conception de filtres avec Matlab"},
    {"sigle": "6GEI418", "date": "2024-09-26", "sujet": "Simulation de systèmes linéaires"},
    {"sigle": "6GEI418", "date": "2024-10-03", "sujet": "Étude de la réponse en fréquence"},

    # Séances pour le cours 8INF334
    {"sigle": "8INF334", "date": "2024-09-13", "sujet": "Introduction à Agile Scrum"},
    {"sigle": "8INF334", "date": "2024-09-20", "sujet": "Développement orienté objet"},
    {"sigle": "8INF334", "date": "2024-09-27", "sujet": "Gestion des réservations en Agile"},
    {"sigle": "8INF334", "date": "2024-10-04", "sujet": "Collaboration en équipe"},

    # Séances pour le cours 6GEI415
    {"sigle": "6GEI415", "date": "2024-09-10", "sujet": "Méthodes de conception en électronique"},
    {"sigle": "6GEI415", "date": "2024-09-17", "sujet": "Conception d'amplificateurs"},
    {"sigle": "6GEI415", "date": "2024-09-24", "sujet": "Implémentation sur PCB"},
    {"sigle": "6GEI415", "date": "2024-10-01", "sujet": "Test et validation des amplificateurs"},

    # Séances pour le cours 6GEI435
    {"sigle": "6GEI435", "date": "2024-09-11", "sujet": "Introduction aux systèmes asservis"},
    {"sigle": "6GEI435", "date": "2024-09-18", "sujet": "Simulation de systèmes avec Matlab"},
    {"sigle": "6GEI435", "date": "2024-09-25", "sujet": "Conception de contrôleurs PID"},
    {"sigle": "6GEI435", "date": "2024-10-02", "sujet": "Application aux panneaux photovoltaïques"},

    # Séances pour le cours 6GEN105
    {"sigle": "6GEN105", "date": "2024-09-15", "sujet": "Introduction à l'ingénierie des systèmes"},
    {"sigle": "6GEN105", "date": "2024-09-22", "sujet": "Panneaux solaires et intégration"},
    {"sigle": "6GEN105", "date": "2024-09-29", "sujet": "Freinage régénératif"},
    {"sigle": "6GEN105", "date": "2024-10-06", "sujet": "Simulation des systèmes intégrés"},

    # Séances pour le cours 6GEI311
    {"sigle": "6GEI311", "date": "2024-10-05", "sujet": "Conception d'une architecture logicielle"},
    {"sigle": "6GEI311", "date": "2024-10-12", "sujet": "Gestion des bibliothèques en Python"},
    {"sigle": "6GEI311", "date": "2024-10-19", "sujet": "Patrons de conception"},
    {"sigle": "6GEI311", "date": "2024-10-26", "sujet": "Déploiement des logiciels"}
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