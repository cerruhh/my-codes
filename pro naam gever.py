naam = ['Thomas', 'Lucas', 'papa', 'toadish', 'mama', 'Je moeder']
werkwoord = ['koopt', 'rijdt', 'schopt', 'geeft', 'raakt', 'tekent', 'gooit', 'vernielt', 'knuffelt', 'bestuurt','vecht met  ',]
onderwerp = ['haha toadish go brrr', 'een koe', 'een buldozer', 'een fiets', 'een vliegtuig', 'een leeuw', 'knuffels', 'een nintendo switch', 'je moeder', 'Toadish', 'Toad', 'Pikachu',]

from random import randint

def kiesuitlijst(woorden):
    aantal_woorden = len(woorden)
    kies_een_nummer = randint(0, aantal_woorden - 1) 
    woord_gekozen = woorden[kies_een_nummer]
    return woord_gekozen

print (kiesuitlijst(onderwerp))


#print (optellen(2,3))

while True:
    print(kiesuitlijst(naam), kiesuitlijst(werkwoord), kiesuitlijst(onderwerp), end='.\n')    
    input() 



