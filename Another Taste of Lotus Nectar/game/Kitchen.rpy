label kitchen:
    play music "<volume 0.38>audio/dinner.wav" fadein 1.0 fadeout 1.0
    scene bg dinner with slow_dissolve
    if persistent.endingOne == True:
        show mold
    h happy "I made some spaghetti..."
    h slightsmile "Here you go."
    show blair default at center with sprite_dissolve:
        zoom 0.7
    b "Thanks."
    show blair glance at center with sprite_dissolve:
        zoom 0.7
    show black:
        alpha 0.4
    n "There it is again. {w=0.2}That bland attitude."
    n "Where is the \"Oh em gee!! Hien made me dinner!\"?"
    n "\"Hien, I could die happy!\""
    narrator worried "I've asked her about the sudden personality change before, {w=0.2}but she said it's just that sometimes, people can change."
    narrator nervous "And soulmates have to love every side of each other."
    "Even the boring Blair is someone I'll have to love as well."
    narrator frustrated "But, {w=0.2}it can't kill her to be nice to me once in a while."
    hide black with slow_dissolve
    $ renpy.pause(2.0, hard=True)
    narrator neutral "..."
    narrator neutral mouthopen "I rolled up some spaghetti onto the fork and lifted it up to my lips to eat it."
    t "I put a lot of love into this spaghetti.{w=0.2} I used that tomato sauce with the right consistency,{w=0.1} noodles that are moist,{w=0.1} and meatballs with the right spices in it."
    narrator neutral glance "I wonder if she's enjoying her food..."
    b bored "..."
    narrator nervous"Oh... she looks bored."
    narrator worried "Maybe I really messed up the spaghetti. I'll make it right next time."
    $ renpy.pause(2.0, hard=True)
    show blair glance at center with sprite_dissolve:
        zoom 0.7
    ".........."
    "......................."
    play sound "<volume 0.1>audio/forkscrape.wav" fadeout 0.2
    t "The sound of metal forks screeching the bottoms of our plates followed by silence."
    narrator exhausted "God,{w=0.1} I hate that she's so quiet now."
    "We used to talk a lot here at some point."
    show black:
        alpha 0.4
    nvl clear
    n "Once we had a conversation about how annoying her coworkers were."
    n "They would always push the workload onto Blair, and the HR did nothing to save her!"
    nvl clear
    n "As dreadful and irritating it was to her,{w=0.2} I felt relieved that she felt safe enough to vent to me."
    nvl clear
    narrator neutral glance "She must've felt relieved to let that off her chest too."
    show black:
        alpha 0.7
    narrator worried "Perhaps it could be any conversation that can fill the room at this point, I don't care."
    narrator nervous "I can be comforting if you let me."
    show black:
        alpha 0.8
    "Just say something and I'll help you."
    hide black with slow_dissolve
    $ renpy.pause(2.0, hard=True)
    show blair bored at center with sprite_dissolve:
        zoom 0.7
    b "......"
    h neutral "......"
    show black:
        alpha 0.4
    n "Is it normal for people to become distant with their partner because of family trauma?"
    n "I only got vague bits and pieces of what happened to Blair.{w=0.2} It must've been really hard for her."
    n "She's probably too tired to start the conversation."
    nvl clear
    n "Uuuu...{w=0.1} but I've been the one talking first for a while now..."
    nvl clear
    n "It's not that I am bad at talking to people, it's just that she isn't even {i}trying{/i} to talk to me."
    n "Or maybe I am bad at talking?{w=0.2} And the topics I choose to talk about probably bore her to death."
    nvl clear
    show black:
        alpha 0.8
    n ".............Okay screw it."
    nvl clear
    n "I hate initiating the conversation.{w=0.1} But I'll have to do it for us."
    $ renpy.pause(1.0, hard=True)
    hide black with slow_dissolve
    nvl clear
    h "..."
    # nervous sprite here
    h nervous "Hey Blair!"
    b default "Hm?"
    h "..Er.{w=0.1} How have you been?"
    h dejected "I noticed you haven't been saying anything lately."
    b annoyed2 "(Sigh...)"
    show cg annoy with medium_dissolve
    b "This again?"
    b "....I'm fine."

    # menu choices
    if persistent.endingOne == False:
        menu:
            "Press further.":
                jump pressfurther
    elif persistent.endingOne == True:
        menu:
            "Press further.":
                jump pressfurther
            "Stop talking.":
                jump trueending

    # choice 2: "Stop talking." (if game over <= 1, this choice appears. this choice should lead to the true ending. There is a in-game mechanic renpy allows to show a menu choice, but not let the user pick it unless a certain switch is on)

    # ________________________________
    # 1. PRESS FURTHER SECTION . this leads to the first game over (with the argument)

label pressfurther:
    hide cg annoy with medium_dissolve
    h neutral mouthopen "Are you sure?"
    h slightsmile "If you want to talk about anything, I'm here for you."
    b annoyed "...Seriously? Ugh."
    b glance "Like I said, I'm fine."
    b default "You don't have to ask me all the time. I'm just like this."
    h pleadingx2 "But- you weren't always like this!"
    # blair angry sprite?
    b frustrated "..."
    h worried "You've been...inconsiderate lately."
    # blair is still stoic while asking questions here
    b annoyed2 "How so?"
    h shocked "Huh?"
    b default "When have I ever been ‘inconsiderate'?"
    h nervous "Well... whenever I try to communicate with you, you always shut it down."
    b annoyed "How am I shutting it down?"

    # menu choices (all choices in this menu have no effect on the ending)
    menu:
        "Be specific":        
            jump specific
        "Tell her your frustrations":
            jump frustrations
    # --
    # BE SPECIFIC choice
label specific:
    scene cg disinterest with slow_dissolve
    h frustrated "Right now."
    h worried "You used to be open about telling your problems to me."
    h dejected "Now you don't tell me anything."
    scene cg annoy with medium_dissolve
    b "Just because we are dating doesn't mean that I have to tell you everything."
    b "I am entitled to my own life. Just like you."
    h worried "I'm not saying you have to tell me everything that goes on in your life."
    h nervous "This just... feels different to what you used to be like."
    
    scene bg dinner
    show blair annoyed2 at center:
        zoom 0.7
    with medium_dissolve

    b "...I'll come back to you on my own time."
    b annoyed "Does that satisfy you?"
    show black:
        alpha 0.4
    stop music fadeout 1.0
    t "Does that satisfy you? What?"
    narrator worried "You're acting like I am a chore that you have to finish."
    narrator dejected "Why are you so cold...?"
    jump argument

    # FRUSTRATIONS choice
label frustrations:
    h frustrated "Why do I have to spell everything out for you??"
    h shocked "I'm trying to understand you right now and you can't even give me the time of day!"

    show cg shocked with medium_dissolve
    $ renpy.pause(0.5, hard=True)
    b acknowledging "You..."
    narrator worried "Her face scrunches up to something unreadable."
    "Is she shocked? Hurt?"

    hide cg shocked with sprite_dissolve
    b acknowledging "Then, despite all that..."
    b glare "Why are you still dating me?"
    h nervous "..."
    show black:
        alpha 0.4
    stop music fadeout 1.0
    t "What?"
    narrator worried "This was supposed to be the part where you apologize and say you are going to try harder for the both of us."
    narrator pleadingx2 "Now you are questioning the nature of our relationship??"
    hide cg annoy

    jump argument

    # end of PRESS FURTHER SECTION
    # ______________
