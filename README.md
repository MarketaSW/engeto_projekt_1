# Textový analyzátor
První projekt v Python akademii Engeto

Úkolem bylo vytvořit program, který umí projít libovolný text a získat o něm různé informace.

### Co umí?

- vyžádat si jméno a heslo a ověřit registraci
- pokud je uživatel registrovaný, pozdraví a umožní analýzu textů
- pokud uživatel není registrovaný, upozorní jej a ukončí se

![welcome text](/assets/welcome.png)

![unregistered user](/assets/unregistered.png)

- program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:

(Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.)

Pro vybraný text spočítá následující statistiky:

počet slov,
počet slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.
Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu

![statistics from analyzed text](/assets/stats.png)
