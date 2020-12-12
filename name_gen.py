#WORD TEMPLATES:
#_____
#_____all
#_____bank
#Black_____
#_____borough
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
#_____thorpe
#_____ton
#_____tree
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
#Coronation
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
#Jubilee
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

#LONG VOWELS NEED TO BE FOLLOWED BY A CONSONANT THAT'S ALLOWED AT THE START
#WHERE THERE ARE DOUBLE CONSONANTS, THE IT MUST BE NON-START+START << PROBBLY WRONG, TRY NEXT LINE
#WHERE THERE ARE DOUBLE CONSONANTS, THE IT MUST BE "(REQ VOWEL AFTER = FALSE) + START" 
#IF THIS SEQUENCE IS "_x + _x", REMOVE ONE x

import json
import random


class WordData():
    def __init__(self, raw_word_data):
        self.particles = raw_word_data["particles"]
        self.template_words = raw_word_data["words"]
        self.phonemes = raw_word_data["phonemes"]

        self.consonants = []
        self.vowels = []
        
        self.get_consonants()
        self.get_vowels()

        self.starting_consonants = []
        self.starting_vowels = []
        self.long_vowels = []
        self.short_vowels = []
        self.consonants_available_at_start = []
        self.consonants_not_available_at_start = []


    def get_consonants(self):
        if len(self.consonants) > 0:
            return self.consonants

        for consonant in self.phonemes["consonants"]:
            if consonant["only_start"] == False:
                self.consonants.append(consonant)


    def get_vowels(self):
        if len(self.vowels) > 0:
            return self.vowels

        self.vowels = self.phonemes["vowels"]


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


    def get_long_vowels(self):
        if len(self.long_vowels) > 0:
            return self.long_vowels

        for vowel in self.phonemes["vowels"]:
            if vowel["long_vowel"] == True:
                self.long_vowels.append(vowel)
        
        return self.long_vowels


    def get_short_vowels(self):
        if len(self.short_vowels) > 0:
            return self.short_vowels

        for vowel in self.phonemes["vowels"]:
            if vowel["long_vowel"] == False:
                self.short_vowels.append(vowel)
        
        return self.short_vowels


    def get_consonants_available_at_start(self):
        if len(self.consonants_available_at_start) > 0:
            return self.consonants_available_at_start

        for consonant in self.phonemes["consonants"]:
            if consonant["available_at_start"] == True:
                self.consonants_available_at_start.append(consonant)

        return self.consonants_available_at_start


    def get_consonants_not_available_at_start(self):
        if len(self.consonants_not_available_at_start) > 0:
            return self.consonants_not_available_at_start

        for consonant in self.phonemes["consonants"]:
            if consonant["available_at_start"] == False:
                self.consonants_not_available_at_start.append(consonant)

        return self.consonants_not_available_at_start
    

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
    VOWEL_CHARACTERS = "aeiou"
    random_particle = random.choice(word_data.particles)
    particle = random_particle["text"]

    if random_particle["prefix"] == True:
        if random_particle["suffix"] == True:
            particle_is_prefix = random.choice([True, False])
        else:
            particle_is_prefix = True
    else:
        particle_is_prefix = False

    print(particle)

    #generate syllables

    if particle_is_prefix == True:
        random_word = particle + random_word
    else:
        random_word = random_word + particle

    print(random_word)
    return random_word


def generate_syllables(word_data, requires_consonant_start, requires_consonant_end):
    consonants_and_vowels = choose_consonants_and_vowels(requires_consonant_start, requires_consonant_end)
    phonemes = []

    vowels = word_data.vowels 
    starting_consonants = word_data.get_starting_consonants()
    starting_vowels = word_data.get_starting_vowels()
    short_vowels = word_data.get_short_vowels()
    long_vowels = word_data.get_long_vowels()
    consonants_available_at_start = word_data.get_consonants_available_at_start()
    consonants_not_available_at_start = word_data.get_consonants_not_available_at_start()

    # while len(phonemes) < phoneme_count:
    #     if len(phonemes) == 0:
    #         if consonants_and_vowels[0] == "vowel":
    #             potential_phonemes = starting_vowels
    #         else:
    #             potential_phonemes = starting_consonants

    #         random_phoneme = random.choice(potential_phonemes)
    #         phonemes.append(random_phoneme)
    #     elif len(phonemes) < (phoneme_count - 1):
    #         if consonants_and_vowels[len(phonemes)] == "consonant" and consonants_and_vowels[len(phonemes) + 1] == "consonant":
    #             #add two consonants
    #             pass
    #     elif len(phonemes) == (phoneme_count - 1):
    #         pass
    #     else:
    #         previous_phoneme = phonemes[-1]
    #         previous_is_vowel = ("long_vowel" in previous_phoneme)

    #         if previous_is_vowel == True:
    #             random_consonant = random.choice(consonants)
    #         else:

    for phoneme in consonants_and_vowels:
        if phoneme == "V":
            phonemes.append(random.choice(starting_vowels))
        if phoneme == "C":
            phonemes.append(random.choice(starting_consonants))
        if phoneme == "v":
            phonemes.append(random.choice(vowels))
        if phoneme == "s":
            phonemes.append(random.choice(short_vowels))
        if phoneme == "l":
            phonemes.append(random.choice(long_vowels))
        if phoneme == "c":
            phonemes.append(random.choice(consonants_available_at_start))
        if phoneme == "r":
            phonemes.append(random.choice(consonants_not_available_at_start))


    print(consonants_and_vowels)
    print("".join(phonemes))
    return consonants_and_vowels, "".join(phonemes)


def choose_consonants_and_vowels(requires_consonant_start, requires_consonant_end):
    # consonant_to_consonant = ["cvc", "cvcvc"]
    # consonant_to_vowel = ["cv", "cvcv", "cvccv"]
    # vowel_to_consonant = ["vc", "vcvc", "vccvc"]
    # vowel_to_vowel = ["vcv", "vccv", "vcvcv"]

    consonant_to_consonant = ["Csr", "Csrsr", "Cvcsr"]
    consonant_to_vowel = ["Cl", "Cvcl", "Csrl", "Csrcl"]
    vowel_to_consonant = ["Vr", "Vcsr", "Vrsr", "Vrcsr"]
    vowel_to_vowel = ["Vcl", "Vrl", "Vrcl", "Vcvcl", "Vrsrl", "Vcsrl", "Vrvcl", "Vcvcl"]

    #V = start vowel
    #C = start consonant
    #l = long vowel
    #s = short vowel
    #v = vowel
    #r = consonant not available at start
    #c = consonant available at start

    if requires_consonant_start == True and requires_consonant_end == True:
        return random.choice(consonant_to_consonant)
    elif requires_consonant_start == True:
        return random.choice(consonant_to_consonant + consonant_to_vowel)
    elif requires_consonant_end == True:
        if random.randrange(0, 10) == 0:
            return random.choice(vowel_to_consonant)
        else:
            return random.choice(consonant_to_consonant)
    else:
        if random.randrange(0, 10) == 0:
            return random.choice(vowel_to_consonant + vowel_to_vowel)
        else:
            return random.choice(consonant_to_consonant + consonant_to_vowel)


if __name__ == "__main__":
    main()