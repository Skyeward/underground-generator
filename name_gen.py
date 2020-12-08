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
#_____ Docks <<< SKIPPED
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
#Names that already exist on the map << don't do this?
#Names that are over X length
#Names that are on the real tube map?
#Where one word in the phrase is contained in the other word
#within a syllable, ban *x__*x (eg. brofr, pleagl)
#within a syllable, ban x*___x* eg. (bob, dreds)


import json
import random


class WordData():
    def __init__(self, raw_word_data):
        self.particles = raw_word_data["particles"]
        self.template_words = raw_word_data["words"]
        self.phonemes = raw_word_data["phonemes"]

        self.consonants = []
        self.vowels = []
        self.starting_consonants = []
        self.starting_vowels = []


    def get_consonants(self):
        if len(self.consonants) > 0:
            return self.consonants

        for consonant in self.phonemes["consonants"]:
            if consonant["only_start"] == False:
                self.starting_consonants.append(consonant)

        self.consonants = self.phonemes["consonants"]
        return self.consonants


    def get_vowels(self):
        if len(self.vowels) > 0:
            return self.vowels

        self.vowels = self.phonemes["vowels"]
        return self.vowels


    def get_starting_consonants(self):
        if len(self.starting_consonants) > 0:
            return self.starting_consonants
    
        for consonant in self.phonemes["consonants"]:
            if consonant["only_start"] == True or consonant["available_at_start"] == True:
                self.starting_consonants.append(consonant)

        return self.starting_consonants


    def get_starting_vowels(self):
        if len(self.starting_vowels) > 0:
            return self.starting_vowels
    
        for vowel in self.phonemes["vowels"]:
            if vowel["allowed_at_start"] == True:
                self.starting_vowels.append(vowel)

        return self.starting_vowels


def main():
    word_data = load_word_data()
    generate_random_word(word_data)


def load_word_data():
    try:
        with open("word_bank.json", "r") as word_bank_file:
            raw_word_data = json.load(word_bank_file)
    except:
        print("Problem loading json") 
        exit()
    
    word_data = WordData(raw_word_data)

    return word_data


def generate_random_word(word_data):
    VOWELS = "aeiou"
    random_particle = random.choice(word_data.particles)
    particle = random_particle["text"]
    is_monosyllabic = random.choice([True, False])

    if random_particle["prefix"] == True:
        if random_particle["suffix"] == True:
            particle_is_prefix = random.choice([True, False])
        else:
            particle_is_prefix = True
    else:
        particle_is_prefix = False

    print(particle)

    if particle_is_prefix == True and particle[-1] in VOWELS:
        consonants_and_vowels, random_word = generate_syllable(word_data, True, is_monosyllabic, True, False)
        print("True, False")
    elif particle_is_prefix == False and particle[0] in VOWELS:
        consonants_and_vowels, random_word = generate_syllable(word_data, True, is_monosyllabic, False, True)
        print("False, True")
    else:
        consonants_and_vowels, random_word = generate_syllable(word_data, True, is_monosyllabic, False, False)
        print("False, False")

    if is_monosyllabic == False:
        requires_consonant_start = (consonants_and_vowels[-1] == "vowels")

        if particle_is_prefix == False and particle[0] in VOWELS:
            requires_consonant_end = True
        else:
            requires_consonant_end = False

        consonants_and_vowels, addition_to_random_word = generate_syllable(word_data, False, True, requires_consonant_start, requires_consonant_end)
        random_word += addition_to_random_word

    if particle_is_prefix == True:
        random_word = particle + random_word
    else:
        random_word = random_word + particle

    print(random_word)
    return random_word


def generate_syllable(word_data, is_first_syllable, is_last_syllable, requires_consonant_start, requires_consonant_end):
    consonants_and_vowels = choose_consonants_and_vowels(requires_consonant_start, requires_consonant_end)
    phonemes = []

    for item in consonants_and_vowels:
        if is_first_syllable == True:
            if item == "consonants":
                random_phoneme = random.choice(word_data.get_starting_consonants())
            else:
                random_phoneme = random.choice(word_data.get_starting_vowels())
        else:
            if item == "consonants":
                random_phoneme = random.choice(word_data.get_consonants())
            else:
                random_phoneme = random.choice(word_data.get_vowels())
        
        phonemes.append(random_phoneme["text"])

    print(consonants_and_vowels)
    print("".join(phonemes))
    return consonants_and_vowels, "".join(phonemes)


def choose_consonants_and_vowels(requires_consonant_start, requires_consonant_end):
    choices = ["consonants", "vowels"]
    choice_indexes = [0, 1]
    first_phoneme_weightings = [9, 1]
    consonant_and_vowel_indexes = []
    consonants_and_vowels = []

    if requires_consonant_start == True:
        consonant_and_vowel_indexes.append(0)
        consonant_and_vowel_indexes.append(1)
    else:
        random_choice = random.choices(choice_indexes, first_phoneme_weightings)[0]
        consonant_and_vowel_indexes.append(random_choice)
        consonant_and_vowel_indexes.append((random_choice + 1) % 2)

    if requires_consonant_end == True and choice_indexes[-1] == 1:
        consonant_and_vowel_indexes.append(0)
    elif requires_consonant_end == False and random.randrange(0, 2) == 0:
        consonant_and_vowel_indexes.append((choice_indexes[-1] + 1) % 2)

    for i in consonant_and_vowel_indexes:
        consonants_and_vowels.append(choices[i])

    return consonants_and_vowels


if __name__ == "__main__":
    main()