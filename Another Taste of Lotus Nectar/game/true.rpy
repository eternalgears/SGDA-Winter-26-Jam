label trueending:
        #STOP TALKING SECTION (from kitchen label)

    #stop music
    #transparent black image covering scene. Sprites and bg still visible 

    stop music fadeout 1.0
    scene bg altdinner with slow_dissolve

    h neutral "...."
    h frustrated "It’s no use."
    show black:
        alpha 0.6
    play music "<volume 2.0>audio/room noise.mp3" fadein 2.0 fadeout 1.0
    n "{cps=20}No matter how hard I try to talk to her, she just doesn’t understand me.{/cps}"
    n "{cps=20}Blair, you said you would give me the world.{w=0.2} And yet…{/cps}"
    n "{cps=20}We can’t hold each other asleep like we used to.{/cps}"
    n "{cps=20}You can’t tell me that you love me,{w=0.2} because I’m always going to be spitting out those words for you.{/cps}"
    show black with sprite_dissolve:
        alpha 0.7
    n "{cps=20}We can’t even go visit our hometown and watch the lotus flowers in their bloom anymore.{/cps}"
    show black with sprite_dissolve:
        alpha 0.8
    n "{cps=16}I’ll never see you, as graceful as you are,{w=0.2} lower yourself in muddy water to pick up a soggy lotus flower for me ever again.{/cps}"
    nvl clear
    show black with sprite_dissolve:
        alpha 0.45
    n "I looked at the knife.{w=0.3} Its sharp end tempts me."

    # Point and click element on Blair (if knife picked up on second playthrough)

    menu:
        "Blair":
            jump ending

    # play true ending music here

label ending:
    hide black with sprite_dissolve
    show blair bored at center with slow_dissolve:
        zoom 0.7
    b glance "...?"
    b default "Hien?"
    stop music
    show black with vpunch
    "I throw myself onto Blair, hugging her tight."
    "I know she doesn’t want to be this close.{w=0.3} But, please let me be selfish this time too."
    play music "<volume 0.6>audio/trueending.wav" fadein 0.5 fadeout 1.5
    scene bg lotus
    show white:
        alpha 0.5
    with slow_dissolve
    show blair shock at center with slow_dissolve:
        zoom 0.7
    h crying "I’m sorry Blair…"
    with vpunch
    b enraged "What are you doing?!{w=0.2} Get off me!!"
    with hpunch
    "Despite her attempts to flee from our embrace, I hold her steady."
    h nervous "I just wanted this to work… {w=0.3}I love you, you know?"
    show blair crying at center with sprite_dissolve:
        zoom 0.7
    h pleadingx2 "I love you so much."
    show red with medium_dissolve:
        alpha 0.7
    show blair shock at center with sprite_dissolve:
        zoom 0.7
    with vpunch
    scene red with dissolve
    scene black
    "Then as my final act of love,{w=0.2} I stabbed her from behind with the knife."
    b "{cps=40}AAAAAAAAGGGHHH!!!!{/cps}"
    $ renpy.pause(0.5, hard=True)
    b "{cps=30}..Hhghk!!!{/cps}"
    $ renpy.pause(0.5, hard=True)
    b "{cps=20}Y-you...{/cps}"

    # (pause for a few seconds transition?)
    # change bg scene to lotus flowers (hide sprite)

    "She collapses into my arms as blood gushes from her back."
    $ renpy.pause(1.0, hard=True)
    scene bg altlotus2 with slow_dissolve:
        blur 10
    "...{w=0.1}I pull her in for a deep kiss."
    "{cps=20}My poison mixed{w=0.1} into the flesh of her tongue.{/cps}"
    "{cps=20}The blood{w=0.1} coughing up into my mouth{w=0.1} tasted like nectar.{/cps}"
    scene bg altlotus2 with slow_dissolve:
        blur 50
    "{cps=10}And her{w=0.1} lips were reminiscent{w=0.1} of those wet{w=0.1} lotus petals.{/cps}"
    scene bg lotus:
        blur 15
    show white:
        alpha 0.4
    with slow_dissolve
    "{cps=20}{b}True Ending: Limerance.{/b}{/cps}"
    stop music with fadeout 2.0
    scene black with slow_dissolve
    $ persistent.endingOne = False
    return



