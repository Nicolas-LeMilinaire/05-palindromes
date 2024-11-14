#### Fonction secondaire
"""jcvhkjhvjwh"""


def ispalindrome(p):

    """qhssgckjqshckjshckuqh"""

    p = p.lower()
    table = p.maketrans("àâéèëêîôûç", "aaeeeeiouc", " ?.,;:/!'-()[]+<>")
    p = p.translate(table)
    print(p)
    if p == p[::-1] :
        return True
    return False

#### Fonction principale


def main():
    """wqk,chkqjschvkwjdhciwuhc"""
    # vos appels à la fonction secondaire ici

    for s in ["L'ami naturel ? Le rut animal"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
