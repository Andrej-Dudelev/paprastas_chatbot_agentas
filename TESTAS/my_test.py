
def paprastas_chatbot_agentas(ivedimas):
    ivedimas = ivedimas.lower() # Konvertuoti į mažąsias raides, kad būtų lengviau apdoroti

    if "labas" in ivedimas or "sveiki" in ivedimas:
        return "Labas! Kaip aš galiu jums padėti?"
    elif "kaip tau sekasi" in ivedimas or "kaip gyveni" in ivedimas:
        return "Aš esu programa, tad man sekasi puikiai! O jums?"
    elif "aciu" in ivedimas or "ačiū" in ivedimas:
        return "Nėra už ką! Džiaugiuosi galėdamas padėti."
    elif "pabaiga" in ivedimas or "iki" in ivedimas:
        return "Iki pasimatymo! Geros dienos!"
    else:
        return "Atsiprašau, nesupratau. Ar galite pakartoti?"

# Agento paleidimas
print("Sveiki, aš esu paprastas AI agentas. Įveskite 'pabaiga' norėdami išeiti.")
while True:
    naudotojo_ivedimas = input("Jūs: ")
    atsakymas = paprastas_chatbot_agentas(naudotojo_ivedimas)
    print(f"Agentas: {atsakymas}")
    if "pabaiga" in naudotojo_ivedimas.lower():
        break

