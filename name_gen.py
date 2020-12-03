#WORD TEMPLATES:
#_____
#_____all
#_____bank
#Black_____
#_____bottom
#_____bridge (exclude "_____ Bridge" template?)
#_____bury
#_____by
#_____caster?
#_____chester?
#_____church (exclude "_____ Church" template?)
#_____combe
#_____court (exclude "_____ Court" template?)
#_____dale
#_____don
#_____end (exclude "_____ End" template?)
#_____er
#_____ey
#_____ford
#_____hall
#_____ham
#_____ing
#_____land
#_____ley
#Middle_____
#_____minster
#_____mouth
#_____ney
#_____pool
#_____ridge (exclude "_____ Ridge" template?)
#_____row
#_____sea
#_____send <<<< remove?
#_____sey
#_____side
#_____smith
#_____stall
#_____stead
#_____stone
#_____stow
#_____ton
#Up_____ <<< might not work, remove?
#_____wake
#_____wall
#_____wark <<< might not work, remove?
#_____water
#____way (exclude "_____ Way" template?)
#_____well
#_____wich
#_____wick
#_____worth
#_____wright


#PHRASE TEMPLATES:
#_____
#_____ Airport? <<< SKIPPED
#_____ Bridge
#_____ Canal
#_____ Carriageway
#_____ Central
#_____ Church
#City _____
#_____ Court
#_____ Cross
#_____ docks <<< SKIPPED
#_____ End
#_____ Exchange
#_____ Garden(s)
#Greater _____
#_____ Green
#_____ Heath
#High _____
#Higher _____
#_____ Hill
#Inner _____ <<< SKIPPED
#_____ Junction
#_____ Lane
#Little _____ <<< should be paired with blank template?
#Lower _____ <<< should be paired with blank template?
#_____ Main
#_____ Market
#Old _____ <<< should be paired with new?
#_____ Palace
#_____ Park
#_____ Quarter <<< SKIPPED
#_____ Quays
#_____ Ridge
#_____ Rise
#_____ Road
#Royal _____
#Saint _____ <<< Bespoke code that can add "'s road/street/lane" to the end of this?
#_____ Square
#_____ Street
#_____ Tower
#_____ Town
#Upper _____
#_____ Vale
#_____ Walk
#_____ Way
#_____ Wharf
#_____ Wood(s)

#_____ East (should these be location specific?)
#_____ North (these can go first or second)
#_____ South
#_____ West (should they make a different direction version likely?)

#Three [english word]s
#Four [english word]s
#Five [english word]s
#Six [english word]s
#Seven [english word]s
#Eight [english word]s


#WORD BANK
#Arch
#Avenue
#Barrow
#Bell
#Bishop
#Bluffs
#Borough
#Broadway
#Brook
#Castle
#Chapel
#Cobbles
#Corner
#Cottage
#Court
#Creek
#Deacon
#Dock(s)
#Duke 
#Estate
#Farm
#Field(s)
#Fountain
#Gallery
#Gate
#Glade
#Grange
#Grove
#Hamlet
#Harbour
#House
#King('s)
#Manor
#Meadows
#Mere
#Mile
#Mill
#Monger?
#Oak
#Oval
#Path
#Pond
#Queen('s)
#Rectory
#Regent
#Runway
#Stables
#Stadium
#Tree
#Tunnel
#Village
#Water (exclude "_____water" template?)
#Weir
#Yard


#Exclude:
#Names that already exist on the map
#Names that are over X length
#Names that are on the real tube map?
#Where one word in the phrase is contained in the other word


import json


def main():
    particles, template_words = load_word_data()
    generate_random_word(particles)


def load_word_data():
    try:
        with open("word_bank.json", "r") as word_bank_file:
            word_data = json.load(word_bank_file)
    except:
        print("Problem loading json") 
        exit()
    
    #response_json = response_json.decode('utf-8')
    particles = word_data["particles"]
    template_words = word_data["words"]

    return particles, template_words


def generate_random_word(particles):
    print(particles[0]["text"])


if __name__ == "__main__":
    main()