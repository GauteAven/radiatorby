class Lyspære:
    def __init__(self, identifikator, enhet, modellnavn, produsent):
        self.identifikator = identifikator
        self.enhet = enhet
        self.modellnavn = modellnavn
        self.produsent = produsent
        self.er_på = False

    def slå_på(self):
        self.er_på = True
        print("Lyspæren er slått på.")

    def slå_av(self):
        self.er_på = False
        print("Lyspæren er slått av.")


# Opprett en instans av lyspæren
lys = Lyspære(
    identifikator="6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28",
    enhet="Light Bulp",
    modellnavn="Lumina Glow 4000",
    produsent="Elysian Tech"
)

# Test lyspæren
if __name__ == "__main__":
    print("Identifikator:", lys.identifikator)
    print("Enhet:", lys.enhet)
    print("Modellnavn:", lys.modellnavn)
    print("Produsent:", lys.produsent)

    # Slå på lyspæren
    lys.slå_på()

    # Sjekk om lyspæren er på
    if lys.er_på:
        print("Lyspæren er på.")
    else:
        print("Lyspæren er av.")

    # Slå av lyspæren
    lys.slå_av()

    # Sjekk om lyspæren er av
    if not lys.er_på:
        print("Lyspæren er av.")
    else:
        print("Lyspæren er på.")
