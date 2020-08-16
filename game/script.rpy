# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e0 = Character("张 仲华")
define e1 = Character("吴 汾吟")
define e2 = Character("文 婷轩")
define e3 = Character("付 华华")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e0 "You've created a new Ren'Py game."

    e0 "Once you add a story, pictures, and music, you can release it to the world!"

    e1 "好想透你"
    # This ends the game.

    return
