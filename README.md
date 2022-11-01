# Simulierter Patientenmonitor
 Da simulierte Patientenmonitore immer mit enormen Kosten verbunden sind, möchte ich eine kostengünstige Alternative schaffen. Welche
 man sich selber zusammen bauen kann.
 Der Monitor wird über eine drahtlose Verbindung mit der Trainer App kommunizieren. Dies soll auch ohne Internetverbindung möglich sein.

 # Monitor
 Der Patientenmonitor soll später auf einem RPI mit Touchscreen laufen und wird im späteren Verlauf auch darauf optimiert.

 # Trainer App
 Die Trainer App soll, wie der Name es vermuten lässt, auf grundsätzlich jedem aktuellen Android-Handy laufen.

 # Roadmap
| x.x | Ziel                         | Status              |
| --- | ---------------------------- | ------------------- |
| 0.1 | Funktionsfähiges GUI         | :heavy_check_mark:  |
| 0.2 | Kommunikationsready          | :heavy_check_mark:  |
| 0.3 | Einbindung Kurven            | :x:                 |
| 0.4 | 1. praktische Umsetztung     | :x:                 |
| 0.5 | 2. praktische Umsetzung      | :x:                 |
| 0.6 | Einbindung AED Algorhytmus   | :x:                 |
| 0.7 | Einbindung Sounds            | :x:                 |
| 0.8 | 3. praktische Umsetztung     | :x:                 |

## ToDo der aktuellen Version
- [] Beschaffung weiterer EKG Kurven
- [] Organisation der Kurven Datenbank
- [X] HF messen und darstellen
- [] Kurven automatisch in richtiger Geschwindigkeit darstellen
- [] HF Sound

# How to run
## Requirements
Python >=3.7

## Run
```
pip install -r requirements-dev.txt
python src/main.py
```
# Genutzte Bibliotheken
## Python Heart Rate Analysis Toolkit
https://github.com/paulvangentcom/heartrate_analysis_python
