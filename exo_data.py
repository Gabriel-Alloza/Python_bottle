from dataclasses import dataclass
from typing import List

@dataclass
class Contact:
    Telephone: str
    AdresseMail: str

@dataclass
class AdressePostale:
    Adresse: str
    CodePostal: int
    Ville: str

@dataclass
class Personnes:
    Nom: str
    Prenom: str
    DateNaissance: str
    Contact: Contact
    AdressePostale: AdressePostale

@dataclass
class Repertoire:
    Personnes: List[Personnes]


Contact1 = Contact(
    Telephone="06078369895623",
    AdresseMail="adresse.mail@bablanaka.fr",
)

Adresse1 = AdressePostale(
    Adresse="25 rue de gpadidé",
    CodePostal=74000,
    Ville="Annecy"
)

Personne1 = Personnes(
    Nom="Dupont",
    Prenom="Jean",
    DateNaissance="06/07/1392",
    Contact=Contact1,
    AdressePostale=Adresse1
)

Contact2 = Contact(
    Telephone="06355555485895623",
    AdresseMail="adresse.mail@bfdfdfdfdfd.fr",
)

Adresse2 = AdressePostale(
    Adresse="23 rue de gpadidé",
    CodePostal=38000,
    Ville="Grenoble"
)

Personne2 = Personnes(
    Nom="Dupond",
    Prenom="Joseph",
    DateNaissance="06/07/2056",
    Contact=Contact2,
    AdressePostale=Adresse2
)

Repertoire = Repertoire(
    Personnes = [Personne1, Personne2]
)

print(Repertoire)

