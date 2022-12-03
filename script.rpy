"""

Creating starter with label start and this is the test version not the final
which will be in another file

"""

define Elise = Character("Estellise Albrone", color="#ffc0cb")
define n = Character("Narrator", color="#0000ff")
define edna = Character("Edna", color="#8b8000")
define Alfin = Character("Alfin Reise-Arnor", color="#ff0000")
define mik = Character("Mikleo", color="#00ffff")
define unknown = Character("Unknown", color="#A020F0")

default food_option = False
default walk_option = False
default chase_option = False
default not_chase_option = False


label start:

    unknown "Hello players doesn't this place seem like its inescapable?"
    unknown "Like there is no where to run...will you climb the stairs or...will
    you hope to put your faith in me?"
    unknown "*Laughs* Who am I? You will find out in due time. Now the butterfly
    has come. Let your journey begin."
    scene train with dissolve
    n "A young black-hiared girl with blue eyes had just gotten off of the train. The spring breeze blew her
    shiny long hair as she walked off. Her posture was elegant and perfectly straight like every
    step was calculated."
    show elise happy_4 at right
    Elise "(My name is Estellise Albrone. I'm the Princess of the
    Albrone family.)"
    show elise happy_4 at right
    Elise "(I'm currently heading back to the castle and meet
    with my group.)"
    show elise happy_4 at right
    label choices:
        Elise "(But before that what should I do first?)"
    menu:
        "Eat Food":
            jump one_food
        "Walk Around":
            "I'll wander around for a bit then head back."
            jump one_walk

    label one_food:
        "You choose to eat food"
        jump one_food_common

    label one_food_common:
        Elise "I should get food for the others too."
        Elise "Ah, I see a store right over there."
        $ food_option = True
        jump food

    label one_walk:
        "You choose to walk around"
        jump one_walk_common

    label one_walk_common:
        "Few moments later..."
        Elise "Wait...I see someone over the distance."
        $ walk_option = True
        jump walk

    label food:
        if food_option == True:
            scene cafe with dissolve
            n "Estellise entered the cafe and it was bustling inside. People were cheerfully
            chatting amongst themselves while the rabbit-like creatures hopped around the place and
            serving them food alongside the employees to entertain the customers."
            jump the_food_common

    label the_food_common:
        show elise happy_4 at left
        Elise "*Observes the menu* (What would they like? Should I call them?)"
        show edna normal at right
        waitress "What would you like sir? *Says in the most monotone voice ever*"
        jump food_scene

    label food_scene:
        show elise surprise at left
        Elise "(Wait...I recognize that voice...)"
        show elise happy_4 at left
        Elise "Edna is that you?"
        hide edna normal at right
        show edna surprise at right
        n "The yellow-haired nonchalant girl hears a familiar voice calling out. She walks towards Estellise with a
        surprised look on her face."
        edna "Oh its you Estellise. Why must you trouble me in work?"
        n "The petite girl named Edna glared at her."
        edna "If you aren't here to order food I suggest you leave."
        Elise "I'm a customer so treat me like I am one."
        show edna normal at right
        edna "*Sighs* Of course what would you like to order?"
        Elise "I would like to have chicken sandwich and fruit salad"
        edna "*Nods* Okay sit somewhere I'll be there with your order"
        n "Edna went to the counter showing the chef the order while Estellise searched
        for a place to sit."

    label walk:
        if walk_option == True:
            n "Through the distance she notices blonde hair that seemed different from the rest.
            The figure seemed to walk away."
            jump choices_part_two

    label choices_part_two:
        if walk_option == True:
            Elise "(Should I chase her?)"
            menu:
                "Yes":
                    "You choose to follow the mysterious person."
                    $ chase_option = True
                    jump chase
                "No":
                    Elise "I wouldn't gain anything from chasing that person...maybe that
                    air of familiarity was just my imagination."
                    $ not_chase_option = True
                    jump not_chase

    label chase:
        if chase_option == True:
            scene flower with dissolve
            hide elise happy_4 at right
            n "She was panting heavily as she chased the person. It seemed that the person was
            toying with her. However, that would soon end since she cornered the person. There
            weren't much places for the blonde haired girl to run."
            show elise happy_4 at right
            Elise "*Breathing heavily* I finally...caught up...to you...now why were you watching...me?"
            n "All of a sudden the girl giggled turning around making eye contact with Estellise."
            show alfin happy at left
            Alfin "Surprise Estellise. Aww you're so fun to mess with!"
            show elise surprise at right
            Elise "Why must you do this everytime? Just playing with my trust are you?"
            Alfin "*giggles* I adore you. You're my best friend!"

    label not_chase:
        if not_chase_option == True:
            show elise happy_4 at right
            n "All of sudden she noticed a familiar looking male with white hair and fair complexion
            approaching her. She runs to wards him with a bright smile."
            Elise "Mikleo were you the person that was staring at me?"
            show mikleo happy at left
            mik "No that was Alfin. Looks like you didn't fall for her tricks this time. I would
            have no reason to do such a thing."
            n "Then a girl with blonde hair and fancy red dress appeared beside Mikleo."
            hide mikleo happy at left
            show alfin happy at left
            Alfin "*Hugs Estellise* Did you miss me Elise?!"
            hide elise happy_4 at right
            hide alfin happy at left
            n "Estellise blushed madly feeling bashful. Unsure of how to react she pushed her off"
            show alfin happy at left
            show elise surprise at right
            Elise "You do know that I'm not the biggest fan of hugs right?"

    pause
return
