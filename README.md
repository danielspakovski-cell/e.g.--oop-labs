<p align="center">
  <h1 align="center"><b>BIRTHDAY REMINDER</b></h1>
</p>

---

## 📋 Įžanga
Mano kursinio darbo kodas tai **Python** programa, skirta gimtadienių sekimui ir priminimų siuntimui. Joje naudojami objektinio programavimo (**OOP**) principai, kurie leidžia padaryti taip, kad sistema būtų lanksti ir lengvai plečiama.

Mano programa leidžia sukurti vartotojus, pridėti prie jų draugų ar artimųjų gimtadienius ir automatiškai išsaugoti informaciją į `.txt` failą. Programa siunčia pranešimus, jei šiandien yra kieno nors gimtadienis. Pranešimus galima siųsti į skirtingus kanalus (el. paštu arba SMS žinute), naudojant **Factory Method** projektavimo šabloną, kuris įgyvendintas `NotificationFactory`, `EmailFactory` ir `SMSFactory` klasėse. Šio šablono naudojimas leidžia lengvai pridėti naujus pranešimų būdus, nekeičiant pagrindinės logikos.

### 🛠️ Kaip naudoti
Norint panaudoti kodą savo poreikiams, reikėtų keisti `run_app()` funkciją:
1. Sukurti vartotoją: `asmuo = User("Asmuo")`
2. Pridėti gimtadienius: `asmuo.add_birthday(Birthday("Vardas", "YYYY-MM-DD"))`
3. Pasirinkti pranešimo būdą: `EmailFactory()` arba `SMSFactory()`.

Paleidus kodą terminale, `.txt` failai susikurs automatiškai, o komandinėje eilutėje matysis pranešimai, jei šiandienos data sutampa su gimtadienio data.

---

## 🔍 **Analizė**
Programa yra suskirstyta į 3 pagrindinius failus:
* `services.py` – atsako už pranešimų logiką.
* `models.py` – aprašyti gimtadieniai ir vartotojai.
* `main.py` – atsako už valdymą ir visų funkcijų apjungimą.
* *Pastaba: `test_notification_system.py` skirtas kodo testavimui.*

**Panaudoti principai:**
* **Enkapsulacija:** paslepia gimtadienio duomenis ir elgseną.
* **Abstrakcija:** `NotificationService` klasei nesvarbu techninis siuntimo būdas, ji tik kviečia `.send()`.
* **Factory:** įgyvendintas per specializuotas kalses lengvam plečiamumui.

---

## ⚙️ **Reikalavimų įgyvendinimas**



* **Birthday klasė:** Saugo vardą ir datą. Tekstinė data konvertuojama į `datetime` objektą tiksliems skaičiavimams.
* **User klasė:** Kiekvienas vartotojas turi savo sąrašą (`self.birthdays = []`). Metodai `add_birthday` ir `remove_birthday` valdo šį sąrašą.
* **Duomenų saugojimas:** Metodas `save_birthdays_to_txt` sukuria unikalų failą kiekvienam vartotojui ir surašo duomenis tvarkingu formatu.
* **Priminimų logika:** Metodas `notify_birthdays` palygina šiandienos datą su sąraše esančiomis datomis. Naudojama `NotificationService` abstrakcija, leidžianti sistemai lanksčiai pasirinkti tarp `EmailNotification` ir `SMSFactory` tarnybų.
* **Multi-vartotojų palaikymas:** `main.py` faile sukurti atskiri objektai (pvz., Jonas ir Marija) veikia nepriklausomai, nes kiekviena instancija turi savo atmintį ir failus.

---

## 🚀 **Rezultatai ir apibendrinimas**
Ši programa sėkmingai sukuria pamatus lanksčiai ir plečiamai gimtadienių priminimų sistemai. Kodas sėkmingai išsprendė duomenų atskyrimo, duomenų išsaugojimo ir automatizacijos problemas.

**Pasiekti rezultatai:**
1.  **Fiziniai failai:** Sukuriami tekstiniai dokumentai su suformatuota informacija.
2.  **Vartotojo sąsaja:** Terminale simuliuojamas pranešimų siuntimas ir informavimas apie išsaugojimą.

### 💡 Ateities perspektyvos
* Sukurti grafinę vartotojo sąsają (GUI) arba Web versiją.
* Integruoti realias el. pašto ir SMS siuntimo bibliotekas.
* Pakeisti `.txt` failus į duomenų bazes (SQL) didesniam efektyvumui.
* Pridėti amžiaus skaičiavimą bei priminimus likus kelioms dienoms iki šventės.

**Apibendrinant**, šis kodas yra tvirtas skeletas, demonstruojantis teisingą objektinio programavimo taikymą praktikoje.

