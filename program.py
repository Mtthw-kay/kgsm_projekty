class AmiFrancais:

    def __init__(self, Antoine, JeNeTravaillePas, francaise, langues, Étudient):
        self.Antoine = Antoine
        self.JeNeTravaillePas = JeNeTravaillePas
        self.chocolate = ["le chocolat"]
        self.naime_pas = ["les champignons"]
        self.francaise = francaise
        self.langues = langues
        self.Étudient = Étudient

    def answer_question(self, question):
        q = question.lower()

        if "sappele" in q or "appelle" in q or "nom" in q:
            return f"Je m'appelle {self.Antoine}."
        
        if "travailles" in q or "travaille" in q or "travail" in q:
            return f"Je {self.JeNeTravaillePas}."

        if "aime" in q:
            return f"J'aime {', '.join(self.chocolate)}."

        if "nationalite" in q or "nationallite" in q:
            return f"Je suis {self.francaise}."
        
        if "parle" in q or "langue" in q:
            return f"Je parle {', '.join(self.langues)}."

        if "fais" in q or "fait" in q or "profession" in q:
            return f"Je suis {self.Étudient}."

        if "ou" in q or "où" in q or "kgsm" in q:
            return "Je travaille à KGŠM."

        return "Désolé, je ne comprends pas la question."

    def introduce(self):
        return f"Bonjour ! Je m'appelle Antoine. Avez-vous des questions à me poser ?"
    
    def start_conversation(self):
        """Metóda pre interaktívnu konverzáciu"""
        print(self.introduce())
        
        while True:
            question = input("\nVotre question (alebo 'quit' pre ukončenie): ")
            
            if question.lower() in ['quit', 'exit', 'au revoir', 'bye']:
                print("Au revoir !")
                break
            
            print(self.answer_question(question))
   

# Najprv vytvor inštanciu triedy s potrebnými parametrami
antoine = AmiFrancais(
    Antoine="Antoine",
    JeNeTravaillePas="ne travaille pas",
    francaise="français",
    langues=["français", "anglais", "Turkische"],
    Étudient="étudiant"
)
antoine.start_conversation()


