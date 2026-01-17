label trueending:
        #STOP TALKING SECTION (from kitchen label)

    #stop music
    #transparent black image covering scene. Sprites and bg still visible 


    h "...."
    h "It’s no use."
    "No matter how hard I try to talk to her, she just doesn’t understand me."
    "Blair, you said you would give me the world.{w=0.2} And yet…"
    "We can’t hold each other asleep like we used to."
    "You can’t tell me that you love me,{w=0.2} because I’m always going to be spitting out those words for you."
    "We can’t even go visit our hometown and watch the lotus flowers in their bloom anymore."
    "I’ll never see you, as graceful as you are,{w=0.2} lower yourself in muddy water to pick up a soggy lotus flower for me ever again."
    "I looked at the knife.{w=0.3} Its sharp end tempts me."

    # Point and click element on Blair (if knife picked up on second playthrough)

    if hasKnife:
        call screen click_blair
    
    menu:
        "Blair":
            jump ending

    # play true ending music here

screen click_blair:
    imagebutton:
        xalign 0.5
        yalign 1.0
        idle "blair_click"
        hover "blair_click"
        action Jump("ending")

label ending:
    b "...?"
    b "Hien?"
    "I throw myself onto Blair, hugging her tight."
    "I know she doesn’t want to be this close.{w=0.3} But, please let me be selfish this time too."
    h "I’m sorry Blair…"
    b "What are you doing?!{w=0.2} Get off me!!"
    "Despite her attempts to flee from our embrace, I hold her steady."
    h "I just wanted this to work… {w=0.3}I love you, you know?"
    h "I love you so much."
    "Then as my final act of love,{w=0.2} I stabbed her from behind with the knife."
    b "AAAAAAAAGGGHHH!!!!"
    b "..Hhghk!!!"
    b "Y-you…"

    # (pause for a few seconds transition?)
    # change bg scene to lotus flowers (hide sprite)

    "Blood gushes from her back and she collapses in my arms."
    $ renpy.pause(1.0, hard=True)
    "...I pull her in for a deep kiss."
    "My poison mixed into the flesh of her tongue." 
    "The blood coughing up into my mouth tasted like nectar."
    "And her lips were reminiscent of those wet lotus petals."
    $ persistent.endingOne = False
    return



