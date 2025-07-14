import pandas as pd
import glob
import os
import math

# Alle passenden Dateien finden
dateien = sorted(glob.glob("*_datei.csv"))
anzahl_dateien = len(dateien)
print(f"Anzahl gefundener Dateien: {anzahl_dateien}")

for dateiname in dateien:
    print(f"\nVerarbeite Datei: {dateiname}")

    # CSV-Datei einlesen (hier Komma als Trennzeichen, ggf. ';' verwenden)
    df = pd.read_csv(dateiname, sep=',')

    # Spalte, für die die Varianz berechnet werden soll
    spaltenname = 'Absatz'
    spaltenname2 = 'Produkt'
    artikelnummer = df[spaltenname2].iloc[0]
    
    if spaltenname in df.columns:
        varianz = df[spaltenname].var(ddof=0)  # Populationsvarianz
        standardabweichung = math.sqrt(varianz)

        # Fallunterscheidung je nach Höhe der Standardabweichung
        if standardabweichung <= 30:
            zustand = "X"
        elif 30 < standardabweichung <= 60:
            zustand = "Y"
        else:
            zustand = "Z"

    with open("output.csv", "a") as datei:
      datei.write("{artikelnummer};{standardabweichung:.2f};{zustand}\n")
      datei.write("Zeile 2\n") 
        
    print(f"Standardabweichung in '{spaltenname}' (Datei: {dateiname}):{artikelnummer}, {standardabweichung:.2f}, Zustand: {zustand}")
else:
        print(f"⚠️ Spalte '{spaltenname}' nicht in Datei {dateiname} gefunden.")
