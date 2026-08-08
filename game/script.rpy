# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define You = Character("mc regular")
define narrator = Character(None)
define scientist1 = Character("Scientist 1") 
define scientist2 = Character("Scientist 2")
define anchor = Character("News Anchor")


# The game starts here.


label start:

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

    scene bg news
    
    narrator "The planetary decline has accelerated overnight."
    narrator "Authorities are urging all citizens to remain calm."
    narrator "Scientists continue searching for a solution."
#Continue with the rest of the story here... 
return
