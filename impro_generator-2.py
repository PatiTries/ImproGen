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
    ]
}

# Hintergrundfarbe setzen
st.markdown(
    """
    <style>
        body {
            background-color: #303030;
        }
        .filter-box {
            background-color: #61595f;
            border-radius: 5px;
            padding: 10px;
        }
        .filter-box:hover {
            border: 2px solid white;
        }
        .stButton>button {
            background-color: #61595f;
            color: white;
            border-radius: 10px;
            font-size: 18px;
        }
        .stButton>button:hover {
            border: 2px solid white;
        }
        .stButton>button:active {
            background-color: #4a1847;
        }
    </style>
    """
    , unsafe_allow_html=True
)

# Titel der App
st.markdown("<h1 style='text-align: center; color: white;'>Impro-Generator</h1>", unsafe_allow_html=True)

# Mehrfachauswahl für Kategorien
kategorien = st.multiselect("Wähle Kategorien:", list(uebungen.keys()))

# Button zum Generieren der Übung
if st.button("Übung generieren!"):
    if not kategorien:
        st.write("Bitte wähle mindestens eine Kategorie.")
    else:
        ausgewaehlte_kategorie = random.choice(kategorien)
        uebung = random.choice(uebungen[ausgewaehlte_kategorie])
        st.markdown(f"<p style='text-align: center; font-style: italic; color: #cccccc;'>{ausgewaehlte_kategorie}</p>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; font-weight: bold; color: white;'>{uebung.split(' - ')[0]}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #cccccc;'>{uebung.split(' - ')[1]}</p>", unsafe_allow_html=True)
