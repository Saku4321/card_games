# 🂡 Python Card Games Collection / Zbiór gier karcianych w Pythonie

This repository contains console implementations of two classic card games written in Python:
**Blackjack** and **War (Wojna)**.  
Both projects are based on object-oriented programming (OOP) principles and feature full in-game logic, including deck management, card handling, and game flow.

To repozytorium zawiera konsolowe implementacje dwóch klasycznych gier karcianych napisanych w Pythonie:
**Blackjacka** oraz **Wojny**.  
Oba projekty wykorzystują programowanie obiektowe (OOP) i zawierają pełną logikę gry — tworzenie talii, obsługę kart oraz przebieg rozgrywki.

---

## 🎰 Blackjack

A console-based version of **Blackjack**, where the player competes against the dealer.  
The program implements betting, card drawing, hand value management, and even a **split** mechanic.

Konsolowa wersja gry **Blackjack**, w której gracz rywalizuje z krupierem.  
Program obsługuje zakłady, dobieranie kart, dynamiczną wartość asa oraz mechanikę **rozdzielenia kart (split)**.

### Features / Funkcje
- Deck and card classes (`Deck`, `Card`)
- Hand value tracking with ace adjustment
- Chip and bet system
- Split mechanic for identical opening cards
- Automatic dealer play
- Win/loss/draw logic with blackjack handling

### How to play / Jak grać
1. Run the script:
   ```bash
   python Black_jack.py
   ```
2. Enter your player name and buy chips.  
   Podaj imię gracza i kup żetony.
3. Place a bet (must be a multiple of 25).  
   Postaw zakład (wielokrotność 25).
4. Choose to take a card (`y/n`).  
   Dobieraj karty lub zatrzymaj się.
5. If possible, split your hand.  
   Jeśli masz dwie takie same karty – możesz je rozdzielić.
6. The dealer plays automatically and the winner is determined.  
   Krupier gra automatycznie, a wynik zostaje ogłoszony.

---

## ⚔️ War (Wojna)

A simple two-player **War** game simulation.  
Players flip cards from their decks, and the higher value wins the round.  
In the case of a tie, a *war* begins, where players place extra cards before comparing again.

Symulacja klasycznej gry **Wojna** dla dwóch graczy.  
Gracze odkrywają karty z własnych talii, a wyższa karta wygrywa rundę.  
W przypadku remisu rozpoczyna się *wojna* – gracze wykładają dodatkowe karty i porównują ponownie.

### Features / Funkcje
- Card and deck classes
- Shuffling and fair dealing
- Automatic comparison and "WAR" handling
- Game ends when one player runs out of cards

### How to play / Jak grać
1. Run the script:
   ```bash
   python War.py
   ```
2. Enter both players’ names.  
   Podaj imiona obu graczy.
3. Watch each round result and follow the prompts.  
   Obserwuj wynik każdej rundy.
4. Continue until one player loses all cards.  
   Gra kończy się, gdy któryś z graczy straci wszystkie karty.

---

## ⚙️ Technical Info / Informacje techniczne

Both games use:
- `random` module for shuffling
- Object-oriented design (`Card`, `Deck`, `Player`, `Hand`, etc.)
- Text-based user interaction (console input/output)
- No external libraries required

Obie gry wykorzystują:
- moduł `random` do tasowania kart,  
- podejście obiektowe (klasy `Card`, `Deck`, `Player`, `Hand`),  
- prosty interfejs konsolowy,  
- brak zewnętrznych zależności.

---

## 🚀 Possible Improvements / Możliwe ulepszenia
- Add score saving and persistent chip balance  
- Implement computer opponents or multiplayer  
- Create GUI version (e.g. with `tkinter` or `pygame`)  
- Add sound effects or animations  

---

## 👨‍💻 Author / Autor
Created as part of Python learning and programming practice with object-oriented design.  
Stworzono w ramach nauki Pythona i praktyki programowania obiektowego.
