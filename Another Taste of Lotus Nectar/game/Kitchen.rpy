label kitchen:
    h "I made some spaghetti…"
    h "Here you go."
    b "Thanks."

    "There it is again. {w=0.2}That bland attitude."
    "Where is the \"Oh em gee!! Hien made me dinner!\"?"
    "\"Hien, I could die happy!\""
    "I’ve asked her about the sudden personality change before, {w=0.2}but she said it’s just that sometimes, people can change."
    "And soulmates have to love every side of each other."
    "Even the boring Blair is someone I’ll have to love as well."
    "But, {w=0.2}it can’t kill her to be nice to me once in a while."

    "..."
    "I rolled up some spaghetti onto the fork and lifted it up to my lips to eat it."
    "I put a lot of love into this spaghetti.{w=0.2} I used that tomato sauce with the right consistency,{w=0.1} noodles that are moist,{w=0.1} and meatballs with the right spices in it."
    "I wonder if she’s enjoying her food…"
    b "..."
    "Oh… she looks bored."
    "Maybe I really messed up the spaghetti. I’ll make it right next time."
    ".........."
    "......................."

    "The sound of metal forks screeching the bottoms of our plates followed by silence."
    "God,{w=0.1} I hate that she’s so quiet now."
    "We used to talk a lot here at some point."
    "Once we had a conversation about how annoying her coworkers were."
    "They would always push the workload onto Blair, and the HR did nothing to save her!"
    "As dreadful and irritating it was to her,{w=0.2} I felt relieved that she felt safe enough to vent to me."
    "She must’ve felt relieved to let that off her chest too."
    "Perhaps it could be any conversation that can fill the room at this point, I don’t care."
    "I can be comforting if you let me."
    "Just say something and I’ll help you."

    b "......"
    h "......"

    "Is it normal for people to become distant with their partner because of family trauma?"
    "I only got vague bits and pieces of what happened to Blair.{w=0.2} It must’ve been really hard for her."
    "She’s probably too tired to start the conversation."
    "Uuuu…{w=0.1} but I’ve been the one talking first for a while now…"
    "It’s not that I am bad at talking to people, it’s just that she isn’t even {i}trying{/i} to talk to me."
    "Or maybe I am bad at talking?{w=0.2} And the topics I choose to talk about probably bore her to death."
    ".............Okay screw it."
    "I hate initiating the conversation.{w=0.1} But I’ll have to do it for us."

    h "..."
    # nervous sprite here
    h "Hey Blair!"
    b "Hm?"
    h "..Er.{w=0.1} How have you been?"
    h "I noticed you haven’t been saying anything lately."
    b "(Sigh...)"
    b "This again?"
    b "....I’m fine."

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
    h "Are you sure?"
    h "If you want to talk about anything, I’m here for you."
    b "...Seriously? Ugh."
    b "Like I said, I’m fine."
    b "You don’t have to ask me all the time. I’m just like this."
    h "But- you weren’t always like this!"
    # blair angry sprite?
    b "..."
    h "You’ve been…inconsiderate lately."
    # blair is still stoic while asking questions here
    b "How so?"
    h "Huh?"
    b "When have I ever been ‘inconsiderate’?"
    h "Well… whenever I try to communicate with you, you always shut it down."
    b "How am I shutting it down?"

    # menu choices (all choices in this menu have no effect on the ending)
    menu: 
        "Be specific":
            jump specific
        "Tell her your frustrations":
            jump frustrations

    # --
    # BE SPECIFIC choice
label specific:
    h "Right now."
    h "You used to be open about telling your problems to me."
    h "Now you don’t tell me anything."
    b "Just because we are dating doesn’t mean that I have to tell you everything."
    b "I am entitled to my own life. Just like you."
    h "I’m not saying you have to tell me everything that goes on in your life."
    h "This just… feels different to what you used to be like."
    b "…I’ll come back to you on my own time."
    b "Does that satisfy you?"
    "Does that satisfy you? What?"
    "You’re acting like I am a chore that you have to finish."
    jump argument

    # FRUSTRATIONS choice
label frustrations:
    h "Why do I have to spell everything out for you??"
    h "I’m trying to understand you right now and you can’t even give me the time of day!"
    b "You…"
    "Her face scrunches up to something unreadable."
    "Is she shocked? Hurt?"
    b "Then, despite all that…"
    b "Why are you still dating me?"
    h "..."
    "What?"
    "This was supposed to be the part where you apologize and say you are going to try harder for the both of us."
    "Now you are questioning the nature of our relationship??"
    jump argument

    # end of PRESS FURTHER SECTION
    # ______________
