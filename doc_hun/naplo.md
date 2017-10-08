# A L0C4L1Z3R fejlesztési naplója

## 2017.07.21
- megismerkedtem a C++ legalapvetőbb tulajdonságaival, mivel a programom megírásához túl bonyolultnak
  találtam, előbb az általam jobban ismert C#, majd később a python nyelv mellett döntöttem, mert habár
  még nem használtam, praktikusnak, átláthatónak, egyszerűnek találtam
- megismerkedtem a jelforrás pozíciójának koordinátarendszerben meghatározásának matematikai alapjaival
- készítettem egy programot ami elvégzi ezeket a számításokat

## 2017.07.22
- a koordinátarendszer méterben számíott adatait elkezdtem földrajzi koordinátákká konvertálni, felismertem,
  hogy a Föld görbülete, a hosszúsági és szélességi körök különböző kerülete, és a különböző kerületű
  szélességi körök problémát jelentenek. Mivel ezek a problémák elhanyagolható különbségeket okoznak,
  a Földet egy 10x10 km-es négyzetben síknak tekintem a mérések során. 
- elkezdtem a gps adatok átvitelét megoldani az androidos eszközről a gpsd libraryvel

## 2017.07.23
- megoldottam, hogy a program ne lépjen ki, ha nem kap gps adatot, hanem próbálkozzon lekérni azt, amíg meg nem kapja
- kerestem egy programot, ami képes az androidos eszközről a giroszkóp/gps adatokat streamelni UDP csomagokban
- utánanéztem, hogy hogyan kell a socket libraryt UDP csomagok fogadására használni
- megoldottam az UDP csomagokban érkező adatok feldolgozását

## 2017.07.24
- mivel az UDP csomagokban érkező adatokkal ugyanolyan módszerrel kaphatom meg a gps és a giroszkóp adatokat, 
  úgy döntöttem, hogy ezt használom a gps library helyett is
- felismertem, hogy a jelenlegi módszeremmel csak a tengerszint feletti 0m-es síkra vetítve tudom meghatározni
  a jelforrás pozícióját, ezért a a lineáris függvények közös pontjának meghatározását alapul véve megoldottam
  hogy térben is el tudjam helyezni a jelforrást
- megoldottam, hogy a giroszkóp adatokat a gps adatok nélkül is tudjam fogadni, mert azok gyakrabban érkeznek
- megoldottam, hogy tudjak az újabb giroszkóp adatokkal is számolni, amíg a gps adatok változatlanok
- megoldottam, hogy a bufferben felhalmozódó csomagok miatt ne lassuljon le a program
- elkezdtem megoldani az adatok beolvasását a perifériákról

## 2017.07.25
- megoldottam az adatok beolvasását a perifériákról
- könnyebbé tettem ezt scriptekkel
- megírtam ezt a naplót és a dokumentációt  


# Összegzés

## Ami működik:
- adatok beolvasása a perifériákról
- számítások elvégzése az adatok alapján

## Ami még nincs kész:
- a számított adatok pontosságának ellenőrzése

