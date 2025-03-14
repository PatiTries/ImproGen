import random
import streamlit as st

# Kategorien & Übungen
uebungen = {
    "Stimme & Sprache": [
        "Echo-Spiel - Eine Person spricht eine Zeile, die andere wiederholt sie mit Variationen.",
        "Fantasiesprache - Spieler erfinden eine Sprache und kommunizieren damit in einer Szene.",
        "Stimm-Modulation - Eine kurze Szene wird mit verschiedenen Stimmfarben gespielt."
    ],
    "Körperarbeit & Bewegung": [
        "Raumlauf mit Status - Spieler durchqueren den Raum mit einer vorgegebenen Statusstufe.",
        "Spiegel-Spiel - Zwei Spieler spiegeln sich gegenseitig und wechseln unauffällig die Führung.",
        "Energie-Level-Wechsel - Eine Szene beginnt auf niedriger Energie und steigert sich bis zum Maximum."
    ],
    "Emotion & Ausdruck": [
        "Emotionskarussell - Eine Szene wird mehrfach gespielt, jedes Mal mit einer anderen Emotion.",
        "Inneres vs. äußeres Gefühl - Spieler stellen eine Emotion dar, sprechen aber mit einer anderen.",
        "Gefühlswechsel auf Signal - Eine Szene läuft, ein Außenstehender gibt Signale, woraufhin die Emotion wechselt."
    ],
    "Improvisation & Spontane Szenen": [
        "Ja, und... - Spieler akzeptieren jedes Angebot und bauen darauf auf.",
        "Freeze & Switch - Während einer Szene ruft jemand 'Freeze!', friert das Spiel ein und ersetzt einen Spieler.",
        "Requisiten-Impro - Spieler erhalten eine zufällige Requisite und müssen sie in die Szene einbauen."
    ],
    "Szenen & Rollenarbeit": [
        "Figuren-Wechsel - Jeder Spieler wechselt innerhalb einer Szene mehrfach seine Rolle.",
        "Monolog vs. Dialog - Eine Szene wird als Monolog begonnen und dann in einen Dialog überführt.",
        "Beziehungstest - Zwei Charaktere interagieren ohne Worte, nur über Körpersprache."
    ],
    "Storytelling & Dramaturgie": [
        "Heldenreise in 3 Minuten - Die Spieler improvisieren eine klassische Heldenreise.",
        "Genre-Wechsel - Eine Szene beginnt in einem Genre und wechselt plötzlich in ein anderes.",
        "Erzähler vs. Spieler - Einer erzählt, die anderen spielen das Gesagte aus."
    ],
    "Wahrnehmung & Präsenz": [
        "Augenkontakt-Impro - Eine Szene, in der die Spieler sich nicht aus den Augen lassen dürfen.",
        "Bühnenfokus setzen - Spieler müssen bewusst mit Aufmerksamkeit im Raum arbeiten.",
        "Still-Impro - Eine Szene ohne Worte, rein über Bewegung und Ausdruck."
    ],
    "Spaß & Extra": [
        "Gegenteilszene - Spieler spielen eine Szene mit komplett gegenteiligen Reaktionen.",
        "Impro-Song - Eine normale Szene, aber jeder Satz muss gesungen werden.",
        "Übertriebene Emotionen - Alles wird maximal dramatisch oder übertrieben lustig gespielt."
    ]
}

def zufaellige_uebung(kategorie=None):
    if kategorie and kategorie in uebungen:
        return random.choice(uebungen[kategorie])
    else:
        gesamt_liste = sum(uebungen.values(), [])
        return random.choice(gesamt_liste) if gesamt_liste else "Keine Übungen vorhanden"

# Streamlit App
st.title("🎭 Impro-Übungsgenerator")

# Kategorie Auswahl
kategorie = st.selectbox("Wähle eine Kategorie:", ["Alle"] + list(uebungen.keys()))

if st.button("Übung generieren! 🎲"):
    if kategorie == "Alle":
        st.write("**Zufällige Übung:**", zufaellige_uebung())
    else:
        st.write(f"**Zufällige Übung aus {kategorie}:**", zufaellige_uebung(kategorie))
