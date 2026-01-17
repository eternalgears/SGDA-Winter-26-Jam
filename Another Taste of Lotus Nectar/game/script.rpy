# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hien", image = "hien", color = "#a0a82c", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define b = Character("Blair", image = "blair", color = "#9E4331", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define narrator = Character(name=None, ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define n = Character(None, kind=nvl)

# side images 
image side hien crying:
    "images/side_hien_crying.png"
    zoom 0.5
image side hien dejected:
    "images/side_hien_dejected.png"
    zoom 0.5
image side hien exhausted:
    "images/side_hien_exhausted.png"
    zoom 0.5
image side hien frustrated:
    "images/side_hien_frustrated.png"
    zoom 0.5
image side hien happy:
    "images/side_hien_happy.png"
    zoom 0.5
image side hien nervous:
    "images/side_hien_nervous.png"
    zoom 0.5
image side hien neutral glance:
    "images/side_hien_neutral_glance.png"
    zoom 0.5
image side hien neutral mouthopen:
    "images/side_hien_neutral_mouthopen.png"
    zoom 0.5
image side hien neutral:
    "images/side_hien_neutral.png"
    zoom 0.5
image side hien pleadingx2:
    "images/side_hien_pleadingx2.png"
    zoom 0.5
image side hien shocked:
    "images/side_hien_shocked.png"
    zoom 0.5
image side hien slightsmile:
    "images/side_hien_slightsmile.png"
    zoom 0.5
image side hien worried:
    "images/side_hien_worried.png"
    zoom 0.5

#transform

transform center:
    xalign 0.5
    yalign 1.0

transform centerzoom:
    xalign 0.5
    yalign 0.1
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
define sprite_dissolve = Dissolve(0.2)
define config.say_attribute_transition = sprite_dissolve
define config.side_image_same_transform = sprite_dissolve
default preferences.skip_unseen = False

## images
image white = "#fff"
image red = "#ff0000"
image black = "#000000"
image mold = Fixed(SnowBlossom("images/mold.png", count=75, xspeed=(-30,30), yspeed=(10,50), start=50))
image knife = "images/Knife.png"

# side images 
image side hien crying:
    "images/side_hien_crying.png"
    zoom 0.5
image side hien dejected:
    "images/side_hien_dejected.png"
    zoom 0.5
image side hien exhausted:
    "images/side_hien_exhausted.png"
    zoom 0.5
image side hien frustrated:
    "images/side_hien_frustrated.png"
    zoom 0.5
image side hien happy:
    "images/side_hien_happy.png"
    zoom 0.5
image side hien nervous:
    "images/side_hien_nervous.png"
    zoom 0.5
image side hien neutral glance:
    "images/side_hien_neutral_glance.png"
    zoom 0.5
image side hien neutral mouthopen:
    "images/side_hien_neutral_mouthopen.png"
    zoom 0.5
image side hien neutral:
    "images/side_hien_neutral.png"
    zoom 0.5
image side hien pleadingx2:
    "images/side_hien_pleadingx2.png"
    zoom 0.5
image side hien shocked:
    "images/side_hien_shocked.png"
    zoom 0.5
image side hien slightsmile:
    "images/side_hien_slightsmile.png"
    zoom 0.5
image side hien worried:
    "images/side_hien_worried.png"
    zoom 0.5

image blair_click:
    "images/blair default.png"
    zoom 0.7

#transforms
transform center:
    xalign 0.5
    yalign 1.0

transform alpha_dissolve: # transform for fading in/out the timer bar
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0


init: # setting timer variables in advance to avoid undefined variables
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
    $ hasKnife = False

#countdown screen for timed sections
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    # ^ Countdown in 0.01 second increments until the timer hits 0
    # once 0, jump to timer_jump

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
    # ^ Timer bar

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
    show blair smile at center with sprite_dissolve:
        zoom 0.7
    b "Aren’t these lotus flowers so pretty~"
    h slightsmile "Mhm...."
    "The sky was painted hues of pinks and oranges, slowly shifting with the clouds."
    "Her smile outshone the red sun, setting into the pond full of lilies and lotuses."
    "In this hazy, late summer, we visited our hometown again to see the lotus flowers during their blooming season."
    narrator happy "The girl across from me on the boat is Blair. {w=0.3}My everything."
    "We grew up in the same part of town, and our families were friends with each other. {w=0.2}So it was natural that we would be together a lot."
    "I had admired her for the longest time now. She was graceful, a sort of ethereal beauty."
    "Though I would have never expected in a million years to be her soulmate until this moment."
    narrator neutral glance "She dips her hand in the muddy water, probably to pick up a flower. {w=0.2}Blair always did strange things like that."
    b "Here!"
    narrator neutral "I look down and see a wet lotus flower in my palms."
    narrator slightsmile "The petals look a little soggy…{w=0.3} but it’s really the thought that counts!"
    "Ahhh…{w=0.2} Blair is so kind..."
    h "..."
    h happy "Thank you…"
    b laughing "Hehe…"
    "Her laughter was as sweet as the honey nectar beneath the lotus petals."
    jump intro

label intro:
    stop music fadeout 1.0
    scene bg altlotus with slow_dissolve
    #start intro for first & second playthrough - Black screen for these two lines 
    narrator neutral "Living with Blair used to be a dream…"
    if not persistent.endingOne: #persistent.endingOne == False
        narrator worried "Until it became one I couldn’t wake up from."
    else: #elif persistent.endingOne == True
        narrator worried "{color=#ff0000}Until it became one I couldn't wake up from.{/color}"

    #Kitchen background
    scene black with slow_dissolve
    play music "audio/room noise.mp3" fadein 0.5 fadeout 1.0
    $ renpy.pause(2.0, hard=True)
    if persistent.endingOne == False:
        scene bg kitchen with slow_dissolve
    elif persistent.endingOne == True:
        scene bg altkitchen with slow_dissolve
        show mold
    narrator neutral "I’m making dinner for Blair again."
    narrator nervous "It’s not like I don’t enjoy making food for her,{w=0.2} she just hasn’t been as grateful as she used to be."
    "A few months ago,{w=0.1} making dinner would earn me an endless shower of her affection."
    narrator dejected "Now I’m lucky to get a conversation out of her."
    window hide
    $ renpy.pause(2.0, hard=True)
    narrator nervous"I know it’s not entirely her fault though."
    "Her family plays a huge role in why she’s been acting this way."
    narrator worried "But I wish she would at least tell me what goes on in her head."
    "I just wish she would tell me {i}explicitly{/i} what makes her feel the way she does…"
    narrator dejected "And why does she have to take it out on me?"
    narrator exhausted "...I feel like a dog who’s waiting for their owner to come home."
    "It’s like she tied me to some pole and didn’t look back."

    if not persistent.endingOne: #persistent.endingOne == False
        narrator slightsmile "...{w=0.3}But that means the owner doesn’t want their dog to run away!"
        "The owner is going out of their way to make sure their dog stays by their side."
        narrator neutral glance "So I must have some sort of value…"
        narrator nervous "Right?"
        jump kitchen
    else: #persistent.endingOne == True
        call screen knife_select

        screen knife_select:
            imagebutton:
                xpos 0.69235 #0.6925
                ypos 0.1954 #0.1954
                xanchor 0.5
                yanchor 0.5
                idle "cabinet1.png"
                hover "cabinet1_hover.png"
                action Jump("get_knife")
        #menu:
            #"Get knife.":
                #show knife:
                    #xalign 0.5
                    #yalign 0.5
                #narrator neutral "Obtained knife."
                #jump kitchen

label get_knife:
    show knife:
        xalign 0.5
        yalign 0.5
    narrator neutral "Obtained knife."
    $ hasKnife = True
    jump kitchen
