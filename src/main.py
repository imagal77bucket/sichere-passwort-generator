import random
import string

class PasswortGenerator:
    def __init__(self, länge=12, grobuchstaben=True, kleinbuchstaben=True, zahlen=True, sonderzeichen=True):
        self.länge = länge
        self.grobuchstaben = grobuchstaben
        self.kleinbuchstaben = kleinbuchstaben
        self.nzahlen = zahlen
        self.sonderzeichen = sonderzeichen

    def generiere_passwort(self):
        zeichen = ''
        if self.grobuchstaben:
            zeichen += string.ascii_uppercase
        if self.kleinbuchstaben:
            zeichen += string.ascii_lowercase
        if self.nzahlen:
            zeichen += string.digits
        if self.sonderzeichen:
            zeichen += string.punctuation

        if not zeichen:
            raise ValueError('Mindestens eine Zeichenklasse muss ausgewählt werden!')

        passwort = ''.join(random.choice(zeichen) for _ in range(self.länge))
        return passwort

if __name__ == '__main__':
    länge = int(input('Geben Sie die gewünschte Passwortlänge ein (z.B. 12): '))
    generator = PasswortGenerator(länge=länge)
    passwort = generator.generiere_passwort()
    print(f'Generiertes Passwort: {passwort}')