"""
Interface en ligne de commande (CLI) pour tester le jeu 2048.

Ce fichier permet de vérifier le bon fonctionnement de la logique
sans interface graphique.
"""

import os
import argparse

from sl29.games._2048 import (
    nouvelle_partie,
    jouer_coup,
)
def afficher_score(score:int) -> None:
    """
    Affiche le score du jeu dans le terminal.

    :param score: Le score.
    """
    print(f"SCORE : {score}")

def afficher_plateau(plateau: list[list[int]]) -> None:
    """
    Affiche le plateau de jeu dans le terminal.

    :param plateau: La grille actuelle.
    """
    print()
    for ligne in plateau:
        for valeur in ligne:
            if valeur == 0:
                print(".", end="\t")
            else:
                print(valeur, end="\t")
        print()
    print()


def demander_commande() -> str:
    """
    Demande une commande à l'utilisateur.

    :return: La commande saisie.
    """
    print("Commandes :")
    print("  g = gauche | d = droite | h = haut | b = bas | q = quitter")
    return input("Votre choix : ").strip().lower()


def _clear_terminal() -> None:
    """Efface le terminal en utilisant les codes d'échappement ANSI."""
    # \033[H : place le curseur en haut à gauche
    # \033[2J : efface l'écran complet
    os.system("clear")

def jouer() -> None:
    """
    Lance une partie de 2048 en mode texte.
    """
    plateau, score = nouvelle_partie()

# Le clear est maintenant activé par défaut
    clear = True
    try:
        parser = argparse.ArgumentParser(add_help=False)
        # On change l'argument pour permettre de désactiver le nettoyage
        parser.add_argument("--no-clear", action="store_true", help="Désactiver le nettoyage du terminal")
        args, _ = parser.parse_known_args()

        # Si --no-clear est présent, clear devient False
        if args.no_clear:
            clear = False
    except Exception:
        # En cas d'erreur, on reste sur True par sécurité
        clear = True
    while True:
        if clear:
            _clear_terminal()
        afficher_score(score)
        afficher_plateau(plateau)

        commande = demander_commande()
        if commande in ('g', 'd', 'b', 'h'):
            plateau, points, fini = jouer_coup(plateau, commande)
            score += points
            if fini:

                if clear:
                    _clear_terminal()
                afficher_score(score)
                afficher_plateau(plateau)
                print("Plus de place ni de fusion possible : Fin de la partie.")
                break
        elif commande == 'q':
            print("Je quitte le jeu.")
            break
        else:
            print("Entree incorrecte.")


if __name__ == "__main__":
    jouer()

