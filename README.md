# cse210-04
This repository will let us participate in the Greed game project for week 7 and week 8.

Are you exciting to play Adventure Games? Play Greed game and you might be surprised. 
The rules are simple, the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
py __main__.py 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                        (project root folder)
+-- cse210-04               (source code for game)
  +-- game                  (specific classes)
  +--- casting              (ALL THE ACTOR IN OUR GAME AND OPERATIONS)
  +---- actor.py            (the main class actor: this class will be the parent)
  +---- cast.py             (All operations appled to our actors like create, delete, get actor, etc)
  +---- gem.py              (Actor: Type of character. This class lets us win points)
  +---- rock.py             (Actor: Type of character. This class lets us lose points)
  +--- directing            (THE MAIN ACTOR)
  +---- director.py         (This class will direct all the actors)
  +--- services             (ALL SERVICES TO PLAY WITH THE GAME )
  +---- keyboard_service.py (Lets to use the Arrow key)
  +---- video_services.py   (Lets to draw graphic on the screem)
  +--- shared               (CONTROL POSITION IN THE)
  +---- color.py            (Control color of every character on the sreem)
  +---- point.py            (Control position X's and Y's¡son the sreen)
  +-- __main__.py           (program entry point)
+-- README.md               (general info)
```

## Required Technologies
---
* Python 3.9.0

## Authors
---
* Melanie Cristeche (cri21012@byui.edu)
* Carter Raymond (ray21006@byui.edu)
* Leonard Salazar (sal21034@byui.edu)
