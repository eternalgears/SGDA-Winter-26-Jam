label argument:
    play music "<volume 0.8>audio/fight.wav" fadein 1.0 fadeout 0.5
    scene bg altdinner with slow_dissolve
    pause
    show blair glare at center with sprite_dissolve:
        zoom 0.7
    h pleadingx2 "Why are you being so adamant on straying away from me?"
    h dejected "Didn't you WANT to stay together?"
    b annoyed "I just need you to give me some time."
    h exhausted "Blair, I’ve given you nothing but all the time in the world."
    with hpunch
    b enraged "Well I’d appreciate it if you'd get off my back about every little thing I do wrong!"
    h worried "..."
    h neutral "...It’s okay if you’re mean to me sometimes,{w=0.2} or even most of the time.{w=0.2} I don’t care."
    show blair acknowledging at center with sprite_dissolve:
        zoom 0.7
    $ renpy.pause(1.0, hard=True)
    h worried "I’ll be okay if you can show me some affection every once in a while."
    show blair glance at center with sprite_dissolve:
        zoom 0.7
    "Blair says nothing and looks away."
    h nervous "I just want you to affirm your love for me."
    b frustrated "..."
    h pleadingx2 "Can you do that?"
    b bored "Hm…"
    b default "Are you asking for reassurance, then?"
    h crying "Yes…"
    #The following line appears only in the 2nd playthrough
    if persistent.endingOne == False:
        $ renpy.pause(1.0, hard=True)
    elif persistent.endingOne == True:
        "{color=#ff0000}I catch a glimpse of light reflecting off of something sharp in Blair's hand.{/color}"
        $ renpy.pause(1.0, hard=True)

    b annoyed2 "..."
    b annoyed "But…"
    b "I’ve told you…{w=0.2} countless times that you didn’t need to worry about it."
    stop music fadeout 0.5
    b angry "{cps=15}Do I always have to tell you that {color=#ff0000}\"I love you\"{/color} to believe me…?{/cps}"
    show red:
        alpha 0.6
    hide hien
    show blair enraged at centerzoom with sprite_dissolve:
        zoom 0.9
    "{cps=40}{i}Without giving me time to think, Blair rushed at me with a look in her eye I’d never seen before.{i}{nw}{/cps}"
    # Choices for 2nd playthrough only

    #Menu Choices
    menu:
        "Fight":
            jump fight
        "Do nothing":
            jump nothing  
    
    #1. FIGHT SECTION
    # jaden note: i have like no clue how i am going to polish this

label fight:
    hide red
    hide blair
    show black with vpunch
    b "Ghk…!"
    "I manage to catch her off balance and knock her to the ground before she can get too close."
    "She lets go of the knife and I kick it across the floor, far from her reach."
    h "Blair……?"
    play music "<volume 0.6>audio/gameover.mp3" fadein 1.0 fadeout 5.0
    show black with slow_dissolve:
        alpha 0.7
    "Huh?"
    "What’s happening?"
    "Did Blair just…{w=0.2} try to kill me?"
    hide black with slow_dissolve
    show blair crying at center with slow_dissolve:
        zoom 0.7
    "I look up and see that she’s crying. This is the first time in months that I’m seeing her express vulnerability."
    show white with sprite_dissolve:
        alpha 0.4
    show blair sobbing at centerzoom with sprite_dissolve:
        zoom 0.9
    with hpunch
    "She throws her arms around my body."
    b "I’m sorry.{w=0.2} I’m sorry.{w=0.2} I’m sorry."
    show white with slow_dissolve:
        alpha 1.0
    hide blair
    "I’m not sure if I can comfort her as well as I used to, but I try anyway."
    h exhausted "It’s okay…"
    "I can hear her muttering other apologies into my shoulder as I stroke her hair."
    "I let her cry for a while, but then I pull away from her and look her straight in the eyes."
    hide white with slow_dissolve
    show blair crying at center with sprite_dissolve:
        zoom 0.7
    h worried "Are we going to be okay?"
    show blair sobbing with sprite_dissolve
    "She nods profusely, hiccuping sobs into my chest."

    # Fade to black screen
    hide blair
    show red:
        alpha 0.6
    with medium_dissolve

    "Will we actually be okay…?"
    "I look down at this crying girl whom I don’t recognize anymore."
    "If I didn’t push her to the ground, {color=#ff0000}would I have wound up dead?{/color}"
    show red with sprite_dissolve:
        alpha 0.7
    "{cps=20}Within those months of her indifference, was she plotting to kill me this whole time?{/cps}"
    show red with sprite_dissolve:
        alpha 0.8
    "{cps=20}Was asking you to give me kindness too much to ask for?{/cps}"
    show red with sprite_dissolve:
        alpha 0.9
    "...{w=0.3}How could you."
    show red with sprite_dissolve:
        alpha 1.0
    "{cps=18}We were supposed to be soulmates, Blair.{/cps}"

    "{b}Bad Ending 1: Cycle.{/b}"
    "Please try again."
    $ persistent.endingOne = True
    return

label nothing:
    # Fade to red?
    show red with sprite_dissolve:
        alpha 1.0
    with vpunch
    "..!!"
    "{cps=30}I feel something…sharp at the side of my stomach.{/cps}"
    play music "<volume 0.3>audio/gameover.mp3" fadein 1.0 fadeout 5.0
    scene bg altdinner:
        blur 16
    show red:
        alpha 0.5
    with slow_dissolve
    pause
    "{cps=20}In the blur of my vision, I see a pool of blood gushing from where I am.{/cps}"
    "{cps=15}Blair...{w=0.5} How could you?{/cps}"
    b "Don’t worry."
    b "No one can hurt you now."
    b "Not even me."
    show red with medium_dissolve:
        alpha 1.0
    $ renpy.pause(1.0, hard=True)
    "{b}Bad Ending 2: Unresolved.{/b}"
    "Please try again."
    $ persistent.endingOne = True
    return

