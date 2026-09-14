import json
import os
import random2

# ============================================================
# NEXORA — STAGE 12
# EXPLICATIONS INTELLIGENTES
# ============================================================

APP_NAME = "NEXORA"
AI_NAME = "Nexora AI"
VERSION = "1.2"

FICHIER_PROFIL = "profil_nexora.json"


# ============================================================
# UTILITAIRES
# ============================================================

def ligne():
    print("=" * 60)


def titre(texte):
    ligne()
    print(texte.center(60))
    ligne()


def pause():
    input("\nAppuie sur Entrée pour continuer...")


def nettoyer(texte):
    return str(texte).strip()


# ============================================================
# PROFIL
# ============================================================

def charger_profil():
    if os.path.exists(FICHIER_PROFIL):
        try:
            with open(FICHIER_PROFIL, "r", encoding="utf-8") as fichier:
                profil = json.load(fichier)

            if isinstance(profil, dict):
                return profil

        except Exception:
            print("⚠️ Impossible de lire le profil.")

    return {
        "prenom": "",
        "nom": "",
        "age": 15,
        "niveau": "Débutant",
        "objectif": "Améliorer mes résultats scolaires",
        "matieres": [],
        "points_forts": [],
        "difficultes": [],
        "progression": {}
    }


def sauvegarder_profil(profil):
    try:
        with open(FICHIER_PROFIL, "w", encoding="utf-8") as fichier:
            json.dump(profil, fichier, ensure_ascii=False, indent=4)

        return True

    except Exception:
        return False


# ============================================================
# BASE DE CONNAISSANCES
# ============================================================

EXPLICATIONS = {

    "mathématiques": {
        "explication":
            "Les mathématiques consistent à utiliser des règles, "
            "des nombres et un raisonnement logique pour résoudre "
            "des problèmes.",

        "retenir":
            "Il faut comprendre la méthode avant de mémoriser "
            "les formules.",

        "conseil":
            "Commence par un exercice simple, puis augmente "
            "progressivement la difficulté."
    },

    "maths": {
        "explication":
            "Les mathématiques développent le raisonnement logique "
            "et permettent de résoudre des problèmes.",

        "retenir":
            "Comprendre les étapes est plus important que mémoriser "
            "mécaniquement.",

        "conseil":
            "Écris toutes les étapes de ton raisonnement."
    },

    "français": {
        "explication":
            "Le français demande de comprendre les textes, "
            "d'utiliser correctement la langue et de construire "
            "des phrases claires.",

        "retenir":
            "Pour progresser, il faut travailler la compréhension, "
            "le vocabulaire et la grammaire.",

        "conseil":
            "Lis régulièrement et note les nouveaux mots."
    },

    "anglais": {
        "explication":
            "L'anglais repose principalement sur le vocabulaire, "
            "la grammaire, la compréhension et la pratique.",

        "retenir":
            "La régularité est essentielle pour apprendre une langue.",

        "conseil":
            "Apprends quelques nouveaux mots chaque jour et "
            "utilise-les dans des phrases."
    },

    "physique": {
        "explication":
            "La physique cherche à expliquer les phénomènes "
            "naturels grâce à des lois, des mesures et des modèles.",

        "retenir":
            "Il faut comprendre les relations entre les grandeurs "
            "avant d'utiliser une formule.",

        "conseil":
            "Identifie toujours les données, la formule et "
            "l'unité avant de calculer."
    },

    "chimie": {
        "explication":
            "La chimie étudie la matière, ses propriétés et "
            "les transformations qu'elle peut subir.",

        "retenir":
            "Les symboles et les équations chimiques permettent "
            "de représenter les transformations.",

        "conseil":
            "Apprends progressivement les symboles et les règles."
    },

    "informatique": {
        "explication":
            "L'informatique consiste notamment à représenter, "
            "traiter et automatiser l'information avec des systèmes "
            "et des programmes.",

        "retenir":
            "Programmer consiste à décomposer un problème en étapes "
            "logiques qu'un ordinateur peut exécuter.",

        "conseil":
            "Pratique avec de petits projets et analyse tes erreurs."
    },

    "programmation": {
        "explication":
            "La programmation consiste à écrire des instructions "
            "permettant à un ordinateur d'effectuer une tâche.",

        "retenir":
            "Un bon programme commence par un problème clairement "
            "défini.",

        "conseil":
            "Découpe ton projet en petites fonctionnalités."
    },

    "histoire": {
        "explication":
            "L'histoire étudie les événements du passé et cherche "
            "à comprendre leurs causes et leurs conséquences.",

        "retenir":
            "Les dates sont utiles, mais il faut surtout comprendre "
            "les relations entre les événements.",

        "conseil":
            "Construis des chronologies pour organiser les événements."
    },

    "géographie": {
        "explication":
            "La géographie étudie les territoires, les populations, "
            "les ressources et leurs interactions.",

        "retenir":
            "Il faut relier les informations aux espaces concernés.",

        "conseil":
            "Utilise des cartes et des schémas pour mémoriser."
    },

    "biologie": {
        "explication":
            "La biologie étudie les êtres vivants, leur fonctionnement "
            "et leurs interactions avec leur environnement.",

        "retenir":
            "Comprendre les mécanismes permet de mieux retenir "
            "les informations.",

        "conseil":
            "Utilise des schémas pour représenter les processus."
    }
}


# ============================================================
# MINI-COURS
# ============================================================

MINI_COURS = {

    "mathématiques": [
        "1. Lis attentivement le problème.",
        "2. Identifie les données.",
        "3. Choisis la méthode adaptée.",
        "4. Effectue le calcul.",
        "5. Vérifie ton résultat."
    ],

    "anglais": [
        "1. Apprends le vocabulaire.",
        "2. Comprends la structure de la phrase.",
        "3. Observe les temps utilisés.",
        "4. Pratique avec des phrases.",
        "5. Relis tes erreurs."
    ],

    "programmation": [
        "1. Définis le problème.",
        "2. Découpe-le en petites tâches.",
        "3. Écris le code.",
        "4. Teste.",
        "5. Corrige les erreurs.",
        "6. Améliore progressivement."
    ]
}


# ============================================================
# EXPLICATION D'UNE MATIÈRE
# ============================================================

def expliquer_matiere():
    titre("NEXORA AI — EXPLICATION INTELLIGENTE")

    matiere = nettoyer(
        input("Quelle matière veux-tu comprendre ? : ")
    ).lower()

    if matiere in EXPLICATIONS:

        data = EXPLICATIONS[matiere]

        print("\n📚 MATIÈRE :", matiere.upper())

        print("\n🧠 EXPLICATION")
        print(data["explication"])

        print("\n⭐ À RETENIR")
        print(data["retenir"])

        print("\n💡 CONSEIL NEXORA")
        print(data["conseil"])

        if matiere in MINI_COURS:
            print("\n🎓 MINI-COURS")

            for etape in MINI_COURS[matiere]:
                print(etape)

    else:
        print("\n⚠️ Je n'ai pas encore de cours spécialisé pour cette matière.")

        print(
            "\nNEXORA te conseille de commencer par : "
            "définir la notion, identifier les points importants, "
            "faire un exemple puis vérifier ta compréhension."
        )

    pause()


# ============================================================
# EXPLICATION APRÈS ERREUR
# ============================================================

def analyser_erreur():
    titre("NEXORA AI — ANALYSE D'ERREUR")

    matiere = nettoyer(
        input("Matière concernée : ")
    ).lower()

    erreur = nettoyer(
        input("Explique ton erreur : ")
    )

    if not erreur:
        print("\n⚠️ Décris ton erreur pour permettre l'analyse.")
        pause()
        return

    print("\n🔎 ANALYSE DE NEXORA AI")

    print(
        "\nTon erreur peut venir d'une mauvaise compréhension "
        "de la notion, d'une étape oubliée ou d'une erreur "
        "d'application."
    )

    if matiere in EXPLICATIONS:
        print("\n📖 RAPPEL")
        print(EXPLICATIONS[matiere]["explication"])

        print("\n💡 MÉTHODE CONSEILLÉE")
        print(EXPLICATIONS[matiere]["conseil"])

    print("\n🎯 PLAN DE CORRECTION")
    print("1. Relis la question.")
    print("2. Identifie exactement l'étape où tu bloques.")
    print("3. Reprends la règle ou la notion.")
    print("4. Refais l'exercice sans regarder la réponse.")
    print("5. Compare ensuite ton résultat.")

    pause()


# ============================================================
# OBJECTIF PERSONNALISÉ
# ============================================================

def definir_objectif(profil):
    titre("OBJECTIF PERSONNEL")

    objectif = nettoyer(
        input("Quel est ton objectif scolaire ? : ")
    )

    if objectif:
        profil["objectif"] = objectif

        if sauvegarder_profil(profil):
            print("\n✅ Objectif enregistré.")
        else:
            print("\n⚠️ L'objectif n'a pas pu être sauvegardé.")

    pause()


# ============================================================
# AJOUTER UNE MATIÈRE
# ============================================================

def ajouter_matiere(profil):
    titre("AJOUTER UNE MATIÈRE")

    matiere = nettoyer(
        input("Nom de la matière : ")
    )

    if not matiere:
        print("⚠️ Nom invalide.")
        pause()
        return

    if "matieres" not in profil:
        profil["matieres"] = []

    if matiere not in profil["matieres"]:
        profil["matieres"].append(matiere)
        sauvegarder_profil(profil)

        print("\n✅ Matière ajoutée.")
    else:
        print("\nℹ️ Cette matière existe déjà.")

    pause()


# ============================================================
# PROGRESSION
# ============================================================

def enregistrer_note(profil):
    titre("SUIVI DE PROGRESSION")

    matiere = nettoyer(
        input("Matière : ")
    )

    try:
        note = float(input("Note obtenue sur 100 : "))

        if note < 0 or note > 100:
            print("⚠️ La note doit être entre 0 et 100.")
            pause()
            return

    except ValueError:
        print("⚠️ Entre une valeur numérique.")
        pause()
        return

    if "progression" not in profil:
        profil["progression"] = {}

    if matiere not in profil["progression"]:
        profil["progression"][matiere] = []

    profil["progression"][matiere].append(note)

    sauvegarder_profil(profil)

    print("\n✅ Note enregistrée.")

    if note >= 90:
        print("🌟 Excellent niveau !")
    elif note >= 75:
        print("🔥 Très bon travail !")
    elif note >= 60:
        print("📈 Tu progresses, continue !")
    else:
        print("💪 Il faut renforcer cette matière.")

    pause()


def afficher_progression(profil):
    titre("MA PROGRESSION")

    progression = profil.get("progression", {})

    if not progression:
        print("Aucune note enregistrée.")
        pause()
        return

    for matiere, notes in progression.items():

        moyenne = sum(notes) / len(notes)

        print(f"\n📚 {matiere}")
        print("Notes :", ", ".join(str(n) for n in notes))
        print(f"Moyenne : {moyenne:.2f}/100")

        if moyenne >= 90:
            print("Niveau : 🌟 Excellent")
        elif moyenne >= 75:
            print("Niveau : 🔥 Très bon")
        elif moyenne >= 60:
            print("Niveau : 📈 Correct")
        else:
            print("Niveau : 💪 À renforcer")

    pause()


# ============================================================
# PROFIL
# ============================================================

def afficher_profil(profil):
    titre("PROFIL NEXORA")

    prenom = profil.get("prenom", "")
    nom = profil.get("nom", "")

    print("👤 Nom :", f"{prenom} {nom}".strip())
    print("🎂 Âge :", profil.get("age", "Non renseigné"))
    print("🎓 Niveau :", profil.get("niveau", "Non renseigné"))
    print("🎯 Objectif :", profil.get("objectif", "Non renseigné"))

    matieres = profil.get("matieres", [])

    print("\n📚 Matières :")

    if matieres:
        for matiere in matieres:
            print("•", matiere)
    else:
        print("Aucune matière enregistrée.")

    pause()


# ============================================================
# CONSEIL INTELLIGENT
# ============================================================

def conseil_intelligent(profil):
    titre("NEXORA AI — CONSEIL INTELLIGENT")

    progression = profil.get("progression", {})

    if not progression:
        print(
            "📌 Commence par enregistrer quelques notes afin que "
            "NEXORA puisse analyser ta progression."
        )
        pause()
        return

    moyennes = {}

    for matiere, notes in progression.items():
        if notes:
            moyennes[matiere] = sum(notes) / len(notes)

    if not moyennes:
        pause()
        return

    matiere_faible = min(moyennes, key=moyennes.get)
    matiere_forte = max(moyennes, key=moyennes.get)

    print("🧠 ANALYSE DE TON PROFIL")

    print(
        f"\n📉 Matière à renforcer : {matiere_faible}"
        f" ({moyennes[matiere_faible]:.1f}/100)"
    )

    print(
        f"📈 Point fort : {matiere_forte}"
        f" ({moyennes[matiere_forte]:.1f}/100)"
    )

    print("\n🎯 RECOMMANDATION")

    print(
        f"Consacre une partie de ta prochaine séance à "
        f"{matiere_faible}."
    )

    if moyennes[matiere_faible] < 60:
        print(
            "Commence par revoir les bases avant de passer "
            "aux exercices difficiles."
        )
    elif moyennes[matiere_faible] < 75:
        print(
            "Travaille davantage les exercices d'application "
            "et analyse tes erreurs."
        )
    else:
        print(
            "Ton niveau est correct. Travaille maintenant "
            "la précision et les exercices plus complexes."
        )

    pause()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu():
    profil = charger_profil()

    while True:

        titre("NEXORA AI")
        print("Une IA consacrée aux études")
        print("Version", VERSION)

        print("\n1. 👤 Mon profil")
        print("2. 📚 Expliquer une matière")
        print("3. 🔎 Analyser une erreur")
        print("4. 🎯 Définir mon objectif")
        print("5. ➕ Ajouter une matière")
        print("6. 📝 Enregistrer une note")
        print("7. 📊 Voir ma progression")
        print("8. 🧠 Conseil intelligent")
        print("0. 🚪 Quitter")

        choix = input("\nChoisis une option : ").strip()

        if choix == "1":
            afficher_profil(profil)

        elif choix == "2":
            expliquer_matiere()

        elif choix == "3":
            analyser_erreur()

        elif choix == "4":
            definir_objectif(profil)

        elif choix == "5":
            ajouter_matiere(profil)

        elif choix == "6":
            enregistrer_note(profil)

        elif choix == "7":
            afficher_progression(profil)

        elif choix == "8":
            conseil_intelligent(profil)

        elif choix == "0":
            print("\n👋 Merci d'avoir utilisé NEXORA AI.")
            break

        else:
            print("\n⚠️ Choix invalide.")
            pause()


# ============================================================
# LANCEMENT
# ============================================================

if __name__ == "__main__":
    menu()