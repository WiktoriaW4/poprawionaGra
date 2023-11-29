from komponenty.wstep import wstepGry
from komponenty.galeria import galeria
from komponenty.bagaz import bagaz
from komponenty.lotnisko import lotnisko
from komponenty.pogoda import pogoda
from komponenty.atrakcjePierwszegoDnia import wyboryPierwszegoDnia
from komponenty.atakRekina import atakRekina
from komponenty.atrakcjeTrzeciegoDnia import wyboryTrzeciegoDnia
from komponenty.atakLwa import atakLwa
from komponenty.wylot import wylot
from komponenty.tabliczkaMnozenia import tabliczkaMnozenia
from komponenty.koniec import koniec



imie = ""
pieniadze = 100000
(imie, pieniadze) = wstepGry()
(pieniadze) = galeria(pieniadze)
bagaz()
lotnisko()
pogoda()
wyboryPierwszegoDnia()
atakRekina(pieniadze)
wyboryTrzeciegoDnia(imie)
atakLwa()
wylot()
tabliczkaMnozenia()
koniec()