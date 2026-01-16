# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hien", image = "hien", color = "#599E31", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define b = Character("Blair", image = "blair", color = "#9E4331", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define narrator = Character(name=None, image = "hien", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")

# ctc
image ctc:
    "gui/ctc_click.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

# defaults
default preferences.text_cps = 34
define slow_dissolve = Dissolve(1.0)
define medium_dissolve = Dissolve(0.7)
define sprite_dissolve = Dissolve(0.3)
define config.say_attribute_transition = sprite_dissolve
default preferences.skip_unseen = False

# images
image white = "#fff"
image black = "#000000"

# The game starts here.
label splashscreen:
    scene black
    play sound "audio/splash.wav"
    scene bg splash with dissolve
    with Pause(1.5)

    scene black with slow_dissolve

    show text "Made for the SGDA Winter '25-'26 Jam."
    with slow_dissolve
    with Pause(1.5)
    hide text with dissolve
    with Pause(1)

    return

label start:

    if persistent.endingOne == False:
        jump flashback
    elif persistent.endingOne == True:
        jump intro


label flashback:
    scene bg lotus with slow_dissolve
    play music "audio/flashback.wav" fadein 0.5 fadeout 1.0
    $ renpy.pause(2.0, hard=True)
    b "Aren’t these lotus flowers so pretty~"
    h "Mhm...."
    "The sky was painted hues of pinks and oranges, slowly shifting with the clouds."
    "Her smile outshone the red sun, setting into the pond full of lilies and lotuses."
    "In this hazy, late summer, we visited our hometown again to see the lotus flowers during their blooming season."
    "The girl across from me on the boat is Blair. {w=0.3}My everything."
    "We grew up in the same part of town, and our families were friends with each other. {w=0.2}So it was natural that we would be together a lot."
    "I had admired her for the longest time now. She was graceful, a sort of ethereal beauty."
    "Though I would have never expected in a million years to be her soulmate until this moment."
    "She dips her hand in the muddy water, probably to pick up a flower. {w=0.2}Blair always did strange things like that."
    b "Here!"
    "I look down and see a wet lotus flower in my palms."
    "The petals look a little soggy…{w=0.3} but it’s really the thought that counts!"
    "Ahhh…{w=0.2} Blair is so kind..."
    h "..."
    h "Thank you…"
    b "Hehe…"
    "Her laughter was as sweet as the honey nectar beneath the lotus petals."
    jump intro

label intro:
    stop music fadeout 1.0
    scene bg altlotus with slow_dissolve
    #start intro for first & second playthrough - Black screen for these two lines 
    "Living with Blair used to be a dream…"
    if persistent.endingOne == False:
        "Until it became one I couldn’t wake up from."
    elif persistent.endingOne == True:
        "{color=#ff0000}Until it became one I couldn't wake up from.{/color}"

    #Kitchen background
    scene black with slow_dissolve
    play music "audio/room noise.mp3" fadein 0.5 fadeout 1.0
    $ renpy.pause(2.0, hard=True)
    if persistent.endingOne == False:
        scene bg kitchen with slow_dissolve
    elif persistent.endingOne == True:
        scene bg altkitchen with slow_dissolve
    "I’m making dinner for Blair again."
    "It’s not like I don’t enjoy making food for her,{w=0.2} she just hasn’t been as grateful as she used to be."
    "A few months ago,{w=0.1} making dinner would earn me an endless shower of her affection."
    "Now I’m lucky to get a conversation out of her."
    window hide
    $ renpy.pause(2.0, hard=True)
    "I know it’s not entirely her fault though."
    "Her family plays a huge role in why she’s been acting this way."
    "But I wish she would at least tell me what goes on in her head."
    "I just wish she would tell me {i}explicitly{/i} what makes her feel the way she does…"
    "And why does she have to take it out on me?"
    "...I feel like a dog who’s waiting for their owner to come home."
    "It’s like she tied me to some pole and didn’t look back."

    if persistent.endingOne == False:
        "...{w=0.3}But that means the owner doesn’t want their dog to run away!"
        "The owner is going out of their way to make sure their dog stays by their side."
        "So I must have some sort of value…"
        "Right?"
        jump kitchen
    elif persistent.endingOne == True:
        menu:
            "Get knife.":
                "Obtained knife."
                jump kitchen
