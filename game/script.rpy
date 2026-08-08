# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character(None)
define scientist1 = Character("Scientist 1") 
define scientist2 = Character("Scientist 2")
define anchor = Character("News Anchor")
define astraean = Character("Astraean")


# The game starts here.


label start:

    python:
        name=renpy.input("What is your name?")
        name=name.strip()

    define You = Character("[name]")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg astrea:
        fit "cover"

    narrator "This is Astraea." 

    scene bg astrea p3:
        fit "cover"

    narrator "A planet once covered in vast oceans and luminous forests." 

    scene bg astrea p2:
        fit "cover"

    narrator "A planet of thousands of cities." 

    scene bg astrea p4:
        fit "cover"


    narrator "A planet of millions of people." 

    scene bg astrea p5:
        fit "cover"

    narrator "A planet called home." 

    scene bg black

    narrator "It disappears into the distance."
    narrator "People."
    narrator "Families gather around televisions."
    narrator "Children look toward a darkening sky." 
    narrator "Scientists stare at monitors."

    scene bg news:
        fit "cover"
    
    anchor "The planetary decline has accelerated overnight."
    anchor "Authorities are urging all citizens to remain calm."
    anchor "Scientists continue searching for a solution."

    scene bg science lab:
        fit "cover"
    
    narrator "A scientist looks at a monitor."
    scientist1 "Planetary Stability is 32%%"
    scientist1 "We have seventy-two hours."
    narrator "*Another scientist looks up*"
    scientist2 "And after that?"
    narrator "Silence."
    scientist1 "There won't be an Astraea to save."

    scene bg bedroom:
        fit "cover"

    narrator"The broadcast ends."
    narrator"You sit alone in your room."
    narrator"Outside the window, Astraea's sky is unusually dark."
    narrator"On the desk sits an old object."
    narrator"A black 8 ball."
    narrator"It belonged to someone in your family."
    narrator"No one knows where it came from though."

    show mc sad:
        xsize 400
        ysize 1005
        align (0.5, 0.5)
        

    narrator"You find a notification pop up on your cellphone."
    narrator"AVAILABLE TASKS: 1. Use the magic 8 ball 2. Evacuate the people"
    hide mc sad
    show mc talking:
        xsize 400
        ysize 1005
        align(0.5, 0.5)
    You "?"
    narrator "A timer then mysteriously appears."
    narrator "72:00:00."
    hide mc talking
    show mc sad:
        xsize 400
        ysize 1005
        align(0.5, 0.5)
    narrator "There isn't enough time to do everything. You must decide where to begin."

    menu:
        "Use magic 8 ball":
            jump choice_ball
        
        "Evacuate the people":
            jump choice_evacuate
    
    #chose to use 8-ball
    label choice_ball:
        scene bg bedroom:
            fit "cover"
        narrator"You pick up the 8-ball."
        show mc talking:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        You"Since when did I have this...?"
        hide mc talking
        narrator"As you shake it, the message in the middle of the little circle displays"
        narrator"ASK ME ANYTHING"
        show mc regular:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        You"..."
        hide mc regular
        show mc talking:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        You"What's happening to this planet?"
        narrator"The 8-ball swishes..."
        narrator"THE ANSWER BEGINS AS STARDUST."
        narrator"..."
        narrator"Silence."
        You"What?"
        You"What does that even mean?"
        narrator"Ask another question?"
        menu:
            "Yes":
                jump decision_yes
            "No":
                jump decision_no
        label decision_yes:
            You"..."
            You"How do I save Astraea...My once beautiful home?"
            hide mc talking
            narrator"..."
            narrator"THE ANSWER LIES IN STARDUST."
            show mc sad:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"...???"
            hide mc sad
            show mc talking:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"Whatever. This stupid thing is broken, or something."
            narrator"You're tired, but don't feel like sleeping. What should you do?"
        menu:
            "Research on Stardust?":
                jump research_yus
            
            "Sleep anyway? There's nothing enjoyable to do":
                jump lame_noo
    #chose to evacute people
    label choice_evacuate:

        scene bg city hall:
            fit "cover"
        narrator"People crowd the streets."
        narrator"Emergency messages flash across enormous screens, reading"
        narrator"ALL CITIZENS OF ASTRAEA MUST REPORT TO THE EASTERN LAUNCH STATION."
        narrator"A child clenches their parents' hand."
        narrator"One person looks back at the city."
        astraean"Are we really leaving?"
        narrator"Before a chance to answer, they head into the space launch."
        narrator"Preparing for a journey, that has no end."
    label end:
        scene bg black
        narrator"You failed to save Astraea."



return
