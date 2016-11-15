# This Python file uses the following encoding: utf-8

# The order of words in this list is important.  The longer words that contain other words from the list (such as PRONOUN and VERB-ED), need listed before the shorter words.  For example, PLURALNOUN needs to be before NOUN, not after.  Else, the longer word won't be detected.
parts_of_speech  = ["PLACE", "PERSON", "PRONOUN", "PLURALNOUN", "DETERMINER", "ADVERB", "PREPOSITION", "CONJUNCTION","NUMBER","ANIMAL","NOISE","VERB-ED","VERB-ING","LIQUID","OCCUPATION","EMOTION", "VERB", "ADJECTIVE", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

import random
import time

# random_madlibs From http://www.madglibs.com/
random_madlibs =[
    "Be kind to your NOUN-footed PLURALNOUN For a duck may be somebody`s NOUN, Be kind to your PLURALNOUN in PLACE Where the weather is always ADJECTIVE. You may think that this is the NOUN, Well it is.",
    "Two PLURALNOUN, both alike in dignity, In fair PLACE, where we lay our scene, From ancient NOUN break to new mutiny, Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes A pair of star-cross`d PLURALNOUN take their life; Whole misadventured piteous overthrows Do with their NOUN bury their parents` strife. The fearful passage of their ADJECTIVE love, And the continuance of their parents` rage, Which, but their children`s end, nought could VERB, Is now the NUMBER hours` traffic of our stage; The which if you with ADJECTIVE NOUN attend, What here shall VERB, our toil shall strive to mend.",
    "ADJECTIVE Macdonald had a NOUN, E-I-E-I-O and on that NOUN he had an ANIMAL, E-I-E-I-O with a NOISE NOISE here and a NOISE NOISE there, here a NOISE, there a NOISE, everywhere a NOISE NOISE, ADJECTIVE Macdonald had a NOUN, E-I-E-I-O.",
    "I enjoy long, ADJECTIVE walks on the beach, getting VERB-ED in the rain and serendipitous encounters with PLURAL. I really like piña coladas mixed with LIQUID, and romantic, candle-lit PLURALNOUN. I am well-read from Dr. Seuss to PERSON. I travel frequently, especially to PLACE, when I am not busy with work. (I am a OCCUPATION.) I am looking for NOUN and beauty in the form of a NATIONALITY goddess. She should have the physique of PERSON and the NOUN of PERSON. I would prefer if she knew how to cook, clean, and wash my PLURALNOUN. I know I’m not very attractive in my picture, but it was taken NUMBER days ago, and I have since become more ADJECTIVE.",
    "Dear PERSON, You are extremly ADJECTIVE and I VERB you! I want kiss your NOUN NUMBER times. You make my NOUN burn with desire. When I first saw you, I ADVERB stared at you and fell in love. Will you VERB out with me? Don`t let your parents discourage you, PRONOUN are just jealous. Yours forever, PERSON",
    "It was during the battle of NOUN when I was running through a NOUN when a NOUN went off right next to my platoon. Our OCCUPATION yelled for us to VERB to the nearest PLACE we could find. When we got to the PLACE we VERB-ED to start a fire. As we were starting the fire the enemy saw the NOUN from the fire and started VERB-ING PLURALNOUN at us. we all quickly ducked behind the NOUN at the PLACE and returned fire. we quickly eliminated the enemy and were EMOTION that we had won the battle.",
    "Look, I guarantee there`ll be ADJECTIVE times. I guarantee that at some NOUN, NUMBER or both of us is gonna want to get out of this NOUN. But I also guarantee that if I don`t ask you to be ADJECTIVE, I`ll VERB it for the rest of my NOUN, because I know, in my NOUN, you`re the ADJECTIVE one for me.",
    "Look at this NOUN, isn`t it neat? Wouldn`t you think my collection`s complete? Wouldn`t you think I`m the NOUN The NOUN who has everything?   Look at this NOUN, treasures untold How many wonders can one NOUN hold? VERB-ING around here, you`d think Sure, she`s got everything.  I`ve got PLURALNOUN and PLURALNOUN a-plenty I`ve got who`s-its and what`s-its galore You VERB thing-a-mabobs? I`ve got NUMBER But who cares? No ADJECTIVE deal. I VERB more.  I wanna be where the PLURALNOUN are I wanna see, wanna see `em VERB-ING walkin` around on those Whaddya call `em? Oh, feet.  VERB-ING your fins, you don`t get too far Legs are required for VERB-ING, dancin` Strollin` along down the What`s that word again? NOUN Up where PLURALNOUN VERB Up where PLURALNOUN run Up where PLURALNOUN stay all day in the sun Wanderin` free, wish I could be Part of that PLACE.  What would I give if I could live Outta these PLURALNOUN? What would I pay to spend a day Warm on the sand?  Betcha on PLACE they understand Bet they don`t reprimand their PLURALNOUN Bright young women, sick of VERB-ING Ready to stand.  And ready to know what the NOUN know Ask `em ADJECTIVE questions and get some answers What`s a NOUN, and why does it What`s the word? VERB.  When`s it my turn? Wouldn`t I VERB? VERB to explore that NOUN up above Out of ADJECTIVE NOUN, wish NOUN could be VERB of that NOUN"]

user_madlib = ""

log = open("log.txt", "a")

def word_in_pos(word):
    global parts_of_speech
    for pos in parts_of_speech:
        if pos in word.upper():
            return pos
    return None

def play_game(ml_string):
    global parts_of_speech
    global log
    replaced = []
    replaced = ml_string.split()
    index = -1
    for word in replaced:
        index += 1
        pos = word_in_pos(word)
        if pos == None:
            pass
        elif pos in parts_of_speech:
            if word == pos:
                replaced[index] = raw_input("Type in a " + pos.lower() + " > ")
            else:
                replaced[index] = word[:word.index(pos)] + raw_input("Type in a " + pos.lower() + " > ") + word[word.index(pos) + len(pos):]
        else:
            print "Unexpected result"
            log.write("\n" +time.strftime("%c") + " | E | " + pos)
    log.write("\n" + time.strftime("%c") + " | S | " + " ".join(replaced))
    return " ".join(replaced)

def add_upper(user_ml):
    global parts_of_speech
    global log
    replaced = []
    replaced = user_ml.split()
    index = -1
    for word in replaced:
        index += 1
        pos = word_in_pos(word)
        if pos == None:
            pass
        elif pos in parts_of_speech:
            if word == pos:
                pass
            else:
                replaced[index] = word.upper()
                # replaced[index] = word[:word.index(pos)] + pos + word[word.index(pos) + len(pos):]
        else:
            print "Unexpected result"
            log.write("\n" +time.strftime("%c") + " | E | " + pos)
    return " ".join(replaced)

def create_madlib():
    print "Next, type in your own Mad Lib framework using the names of different parts of speech for input locations.  For example: I VERB to the NOUN.  These are the available parts of speech keywords that you can use:\n"
    print parts_of_speech
    user_madlib = raw_input("> ")
    user_madlib = add_upper(user_madlib)
    global log
    log.write("\n" + time.strftime("%c") + " | U | " + user_madlib) # save user_madlib to log
    return user_madlib

def user_input():
    toggle = True
    while toggle:
        answer = raw_input("Shall we play a game?\n")
        answer = answer.lower()
        if answer in ("y", "yes", "yeah", "sure", "affirmative", "yup", "okay", "ok"):
            print "Great! Let's play Mad Libs."
            toggle = True
            while toggle:
                answer2 = raw_input("Would you like to type in your own Mad Lib? If no it will use a random one\n")
                answer2 = answer2.lower()
                if answer2 in ("n", "no", "nah", "nope", "negative", "nix"):
                    return play_game(random_madlibs[random.randint(0,len(random_madlibs))])
                    toggle = False
                elif answer2 in ("y", "yes", "yeah", "sure", "affirmative", "yup", "okay", "ok"):
                    return play_game(create_madlib())
                    toggle = False
                else:
                    print 'Your response was not recognized as a "Yes" or "No", please try again.'
            toggle = False
        elif answer in ("n", "no", "nah", "nope", "negative", "nix"):
            while True:
                print "Okay. Your loss..."
                return
            toggle = False
        elif answer == "Oh!":
            print "http://www.imdb.com/title/tt0086567/quotes"
        else:
            print 'Your response was not recognized as a "Yes" or "No", please try again.'

print user_input()
