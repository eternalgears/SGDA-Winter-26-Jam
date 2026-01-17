label kitchen:
    scene bg dinner with slow_dissolve
    h happy "I made some spaghetti…"
    h "Here you go."
    show blair default at center with sprite_dissolve:
        zoom 0.7
    b "Thanks."

    narrator nervous "There it is again. {w=0.2}That bland attitude."
    narrator frustrated "Where is the \"Oh em gee!! Hien made me dinner!\"?"
    "\"Hien, I could die happy!\""
    narrator worried "I’ve asked her about the sudden personality change before, {w=0.2}but she said it’s just that sometimes, people can change."
    narrator nervous "And soulmates have to love every side of each other."
    "Even the boring Blair is someone I’ll have to love as well."
    narrator frustrated "But, {w=0.2}it can’t kill her to be nice to me once in a while."

    narrator neutral "..."
    narrator neutral mouthopen "I rolled up some spaghetti onto the fork and lifted it up to my lips to eat it."
    narrator slightsmile "I put a lot of love into this spaghetti.{w=0.2} I used that tomato sauce with the right consistency,{w=0.1} noodles that are moist,{w=0.1} and meatballs with the right spices in it."
    narrator neutral glance "I wonder if she’s enjoying her food…"
    b bored "..."
    narrator nervous"Oh… she looks bored."
    narrator worried "Maybe I really messed up the spaghetti. I’ll make it right next time."
    ".........."
    "......................."

    narrator neutral "The sound of metal forks screeching the bottoms of our plates followed by silence."
    narrator exhausted "God,{w=0.1} I hate that she’s so quiet now."
    "We used to talk a lot here at some point."
    narrator neutral "Once we had a conversation about how annoying her coworkers were."
    narrator dejected "They would always push the workload onto Blair, and the HR did nothing to save her!"
    narrator slightsmile "As dreadful and irritating it was to her,{w=0.2} I felt relieved that she felt safe enough to vent to me."
    narrator neutral glance "She must’ve felt relieved to let that off her chest too."
    narrator worried "Perhaps it could be any conversation that can fill the room at this point, I don’t care."
    narrator nervous "I can be comforting if you let me."
    "Just say something and I’ll help you."

    b "......"
    h neutral "......"

    narrator worried "Is it normal for people to become distant with their partner because of family trauma?"
    narrator neutral mouthopen "I only got vague bits and pieces of what happened to Blair.{w=0.2} It must’ve been really hard for her."
    "She’s probably too tired to start the conversation."
    narrator exhausted "Uuuu…{w=0.1} but I’ve been the one talking first for a while now…"
    narrator frustrated "It’s not that I am bad at talking to people, it’s just that she isn’t even {i}trying{/i} to talk to me."
    narrator neutral glance "Or maybe I am bad at talking?{w=0.2} And the topics I choose to talk about probably bore her to death."
    narrator worried ".............Okay screw it."
    narrator neutral "I hate initiating the conversation.{w=0.1} But I’ll have to do it for us."

    h "..."
    # nervous sprite here
    h nervous "Hey Blair!"
    b default "Hm?"
    h "..Er.{w=0.1} How have you been?"
    h "I noticed you haven’t been saying anything lately."
    b annoyed2 "(Sigh...)"
    b "This again?"
    b glance "....I’m fine."

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
    h neutral mouthopen "Are you sure?"
    h slightsmile "If you want to talk about anything, I’m here for you."
    b annoyed "...Seriously? Ugh."
    b glance "Like I said, I’m fine."
    b default "You don’t have to ask me all the time. I’m just like this."
    h pleadingx2 "But- you weren’t always like this!"
    # blair angry sprite?
    b frustrated "..."
    h worried "You’ve been…inconsiderate lately."
    # blair is still stoic while asking questions here
    b annoyed2 "How so?"
    h shocked "Huh?"
    b default "When have I ever been ‘inconsiderate’?"
    h nervous "Well… whenever I try to communicate with you, you always shut it down."
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
    h frustrated "Right now."
    h worried "You used to be open about telling your problems to me."
    h dejected "Now you don’t tell me anything."

    show cg disinterest with sprite_dissolve

    b "Just because we are dating doesn’t mean that I have to tell you everything."
    b "I am entitled to my own life. Just like you."
    h worried "I’m not saying you have to tell me everything that goes on in your life."
    h nervous "This just… feels different to what you used to be like."

    hide cg disinterest

    b glance "…I’ll come back to you on my own time."
    b bored "Does that satisfy you?"
    narrator shocked "Does that satisfy you? What?"
    narrator frustrated "You’re acting like I am a chore that you have to finish."
    jump argument

    # FRUSTRATIONS choice
label frustrations:
    h frustrated "Why do I have to spell everything out for you??"
    h shocked "I’m trying to understand you right now and you can’t even give me the time of day!"

    show cg shocked with sprite_dissolve
    b "You…"
    narrator worried "Her face scrunches up to something unreadable."
    "Is she shocked? Hurt?"

    show cg annoy with sprite_dissolve
    b "Then, despite all that…"
    b "Why are you still dating me?"
    h shocked "..."
    narrator shocked "What?"
    narrator worried "This was supposed to be the part where you apologize and say you are going to try harder for the both of us."
    narrator pleadingx2 "Now you are questioning the nature of our relationship??"
    hide cg annoy

    jump argument

    # end of PRESS FURTHER SECTION
    # ______________
