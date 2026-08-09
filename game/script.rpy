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
    
    show news:
        xsize 500
        ysize 1005
        align (0.5, 0.5)
    anchor "The planetary decline has accelerated overnight."
    anchor "Authorities are urging all citizens to remain calm."
    anchor "Scientists continue searching for a solution."

    scene bg science lab:
        fit "cover"
    
    narrator "A scientist looks at a monitor."
    show male scientist talk:
        xsize 400
        ysize 1010
        align(0.5, 0.0)
    scientist1 "Planetary Stability is 32%%"
    scientist1 "We have seventy-two hours."
    hide male scientist talk
    show female scientist idle:
        xsize 400
        ysize 1010
        align(0.5, 0.5)
    narrator "*Another scientist looks up*"
    hide female scientist idle
    show female scientist talk:
        xsize 400
        ysize 1010
        align(0.5, 0.5)
    scientist2 "And after that?"
    hide female scientist talk
    narrator "Silence."
    show male scientist talk:
        xsize 400
        ysize 1010
        align(0.5, 0.5)
    scientist1 "There won't be an Astraea to save."
    hide male scientist talk

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
                jump choice_evacuate
        
        #you chose the magic 8 ball again
        label decision_yes:
            You"..."
            You"How do I save Astraea...My once beautiful home?"
            hide mc talking
            narrator"..."
            narrator"WHAT IS TAKEN MUST BE RETURNED."
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
            narrator"You put the 8-ball back down."
            hide mc talking
            narrator"..."
            narrator"All of a sudden, the 8-ball shifts on your desk."
            show mc talking:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            You"...?"
            You"Locations?"
            narrator"The magic 8-ball has given you several locations to visit. These locations will give you clues as to why Astraea is dying."
            narrator"Which place do you visit first?"

        menu:
            "The forest":
                jump forest
            "The city":
                jump city
            "The abandoned research lab":
                jump research
        
        label forest:
            scene bg black
            narrator"You enter the forest."
            show mc talking:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            You"Why would it tell me to go through here..."
            hide mc talking
            show mc sad:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            narrator"As you go through the forest, a glow of light glimmers between the leaves of the trees."
            narrator"You pause."
            hide mc sad
            show mc regular:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            You"What was that?"
            narrator"As you push through Till the End, you start to notice more of these glimmering showers of light almost as if it was following you."
            narrator"You make your way to..."
        menu:
            "The city":
                jump city

            "The abandoned research lab":
                jump research
        
        label city:
            scene bg black
            narrator"The city. Its bustling with Aastraeans, though not as busy ever since that day."
            narrator"From observation and investigation, you learn that Astraea's energy grid is connected directly to the planetary core."
            narrator"Although, you can't get that shimmering light off your head."
            show mc talking:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            You"Where was that light coming from...?"
            narrator"You decide to hit all three locations at once, heading towards the..."
        
        menu: 
            "The abandoned research lab":
                jump research
        
        label research:
            scene bg black
            hide mc talking
            show mc regular:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            narrator"You walk through messy hallways filled with paperwork, and stumble upon a room."
            hide mc regular
            show mc talking:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"Could a clue be here?"
            hide mc talking
            narrator"You decide to go through the paperwork."
            show mc talking:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"Ugh, it's been an hour already..."
            hide mc talking
            narrator"When all of a sudden, an old computer turns on and lights up the dark room."
            show mc talking:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            You"...?"
            You"Is this the clue that I've been looking for?"
            hide mc talking
            show mc regular:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            narrator"You watch the computer, and wait."
            narrator"..."
            narrator"After a few minutes, a file appears, adding colour to the empty white screen."
            narrator"PROJECT: LAST LIGHT"
            narrator"Do you open the file?"
        menu:
            "Yes":
                jump yeah
            "No":
                jump choice_evacuate
        label yeah:
            narrator"As you open the file, text begins to flash."
            narrator"Astraea does not produce energy."
            narrator"..."
            narrator"Astraea recieves it."
            narrator"Just then, another file appears and opens on it's own."
            hide mc regular
            show mc talking:
                xsize 400
                ysize 1005
                align (0.5, 0.5)
            You"What...?"
            narrator"Planetary energy must eventually return to the stellar cycle."
            hide mc talking
            show mc sad:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"..."
            hide mc sad
            show mc talking:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"What did we do..?"
            narrator"We took too much."
            narrator"..."
            narrator"The computer shuts down and dims the entire room."
            hide mc talking
            show mc sad:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            narrator"..."
            hide mc sad
            show mc talking:
                xsize 400
                ysize 1005
                align(0.5, 0.5)
            You"The energy..."
            You"We took it."

        narrator"You return home."
        show mc sad:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        narrator"You go to your room, and pick up the magic 8-ball."
        hide mc sad
        show mc talking:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        You"What is taken...must be returned."
        hide mc talking
        show mc sad:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        narrator"You shake the 8-ball."
        narrator"YES."
        hide mc sad
        show mc talking:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        You"But how?"
        hide mc talking
        show mc sad:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        narrator"..."
        narrator"RETURN THE LIGHT."
        hide mc sad
        narrator"Astraea isn't simply dying. It's energy cycle is being interrupted."
        narrator"The planet has been giving everything it has.."
        narrator"and recieving nothing in return."
        narrator"...The player looks through the window."
        narrator"Stardust drifts through the dark sky."
        show mc talking:
            xsize 400
            ysize 1005
            align(0.5, 0.5)
        You"Every answer...begins as stardust."

    return

    label nah:
        narrator"You go back home."
        narrator"You decide that you're too tired to deal with this, and decide to sleep on it."
        scene bg black
        narrator"You failed to save Astraea."
    return
    

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
