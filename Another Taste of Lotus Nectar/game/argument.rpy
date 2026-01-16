label argument:
    scene bg altdinner with slow_dissolve
    
    h "Why are you being so adamant on straying away from me?"
    h "Don’t you WANT to stay together?"
    b "I just need you to give me some time."
    h "Blair, I’ve given you nothing but all the time in the world."
    b "Well I’d appreciate it if you'd get off my back about every little thing I do wrong!"
    h "..."
    h "...It’s okay if you’re mean to me sometimes,{w=0.2} or even most of the time.{w=0.2} I don’t care."
    h "I’ll be okay if you can show me some affection every once in a while."
    "Blair says nothing and looks away."
    h "I just want you to affirm your love for me."
    h "..."
    h "Can you do that?"
    b "Hm…"
    b "Are you asking for reassurance, then?"
    h "Yes…"
    #The following line appears only in the 2nd playthrough 
    "I catch a glimpse of light reflecting off of something sharp in Blair's hand."

    h "..."
    b "But…"
    b "I’ve told you…{w=0.2} countless times that you didn’t need to worry about it."
    b "{cps=20}Do I always have to tell you that \"I love you\" to believe me…?{/cps}"
    "Without giving me time to think Blair rushed at me with a look in her eye I’d never seen before."
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
    b "Ghk…!"
    "I manage to catch her off balance and knock her to the ground before she can get too close."
    "She lets go of the knife and I kick it across the floor, far from her reach."
    h "Blair……?"
    "What’s happening? Huh??"
    "Did Blair just…{w=0.2} try to kill me?"
    "I look up and see that she’s crying. This is the first time in months that I’m seeing her express vulnerability."
    "She throws her arms around my body."
    b "I’m sorry.{w=0.2} I’m sorry.{w=0.2} I’m sorry."

    "I’m not sure if I can comfort her as well as I used to, but I try anyway."
    h "It’s okay…"
    "I can hear her muttering other apologies into my shoulder as I stroke her hair."
    "I let her cry for a while, but then I pull away from her and look her straight in the eyes."
    h "Are we going to be okay?"
    "She nods profusely, hiccuping sobs into my chest."

    # Fade to black screen
    "Will we actually be okay…?"
    "I look down at this crying girl whom I don’t recognize anymore."
    "If I didn’t push her to the ground, would I have wound up dead?"
    "Within those months of her indifference, was she plotting to kill me this whole time?"
    "Was asking you to give me kindness too much to ask for?"
    "...{w=0.3}How could you."
    "We were supposed to be soulmates, Blair."

    "{b}Bad Ending 1: Cycle.{/b}"
    "Please try again."
    $ persistent.endingOne = True
    return

label nothing:
    # Fade to red?
    "I feel something…sharp at the side of my stomach."
    "In the blur of my vision, I see a pool of blood gushing from where I am."
    "Blair…"
    "How could you?"
    b "Don’t worry."
    b "No one can hurt you now."
    b "Not even me."

    "{b}Bad Ending 2: Unresolved.{/b}"
    "Please try again."
    $ persistent.endingOne = True
    return

