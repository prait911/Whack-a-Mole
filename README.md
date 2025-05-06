# Mängu üldine idee ja eesmärk
Mängutüüp:
Reaktsioonimäng.

Üldine idee:
Mängija peab hiireklõpsuga kiiresti tabama ekraanil juhuslikult ja lühiajaliselt ilmuvaid “mutte” (moles).

Mängija:
hiir.

Mängu eesmärk:
Teenida võimalikult palju punkte enne mängu lõppu, tabades võimalikult palju mutte võimalikult kiiresti.


# Peamised funktsionaalsed osad
Muti ilmumine juhuslikult: Iga kord juhuslikus asukohas.

Tabamine hiireklõpsuga: Mängija klõpsab muti peale.

Punktide kogumine: Tabamuse korral lisatakse punktid. Võibolla on ka halvad mutid, kes võtavad punkte maha.

Taimeri kasutamine: Mäng kestab kindla aja (nt 60 sekundit).

Stseenide vahetus: Algusmenüü → Mäng → Mäng läbi.

Heliefektid: Tabamise ja halva muti tabamise heli.

Tulemuste kuvamine: Mängu ajal kuvatakse skoor ning pärast mängu kuvatakse lõplik skoor.


# Rakenduse arhitektuur
🎮 Mängutsükli ülesehitus
Kasutatakse Pygame'i tavapärast tsüklit:

update(): uuendab mängu loogikat.

draw(): joonistab uue kaadri.

🧍‍♂️ Mängija ja objektide käitumine
Muttide käitumine: ilmuvad suvaliselt, on nähtaval piiratud aja.

Mängija käitumine: sihib ja klõpsab mutti.

Reeglid: ainult nähtav mutt annab punkte ja halvad mutid võtavad punkte maha.

⌨️ Sisendite haldus
Pygame event loop tuvastab MOUSEBUTTONDOWN sündmused ja kontrollib, kas mutt on tabatud.

🏆 Punktisüsteem ja mängu tulemus
Tabatud mutt: +mingi punktisumma

Mänguaeg: nt 60 sekundit

Lõpptulemus: kuvatakse peale mängu lõppu

🔄 Stseenide või olekute vahetus
StartScene → GameScene → GameOverScene

SceneManager kontrollib olekut ja vahetab stseene vastavalt sündmustele.

📦 Ressursside haldamine
Kõik pildid ja helid laetakse resource_loader.py kaudu.


# Failide ja moodulite esialgne jaotus
/Whack-A-Mole/
main.py
settings.py
game_functions.py
game_stats.py
player.py
button.py
scoreboard.py


# Visualiseerimine: komponentide diagramm
main.py
  └── SceneManager
        ├── StartScene
        ├── GameScene
        │     ├── Mole
        │     ├── InputHandler
        │     └── ScoreManager
        └── GameOverScene
  └── ResourceLoader


# Selgitus
See struktuur sobib meie mängu jaoks, sest see on kasutaja sõbralik ning hetkel oskame ainult Pygame'is mängu teha.
