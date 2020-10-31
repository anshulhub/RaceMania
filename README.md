# Car-Game
This is a very Basic Car game made just for practising Python programming using pygame library and getting a GUI game.
The objective of the game is to go as long as possible without hitting another car or driving off the road.

## Controls
You control the black car at the bottom of the screen by pressing the left and right arrow keys. You must press the key in the direction 
you want to go. Holding the key will not have an effect.
![images](readme_assets/gameplay.png)

## Getting Game Over
Colliding with the other cars in any way will result in a game over.
![images](readme_assets/game_over.png)
*Hitting the car head on*

![images](readme_assets/game_over2.png)
*Completely going on top of the car*

Apart from hitting the other cars, you must also be careful not to drive off the road.
![images](readme_assets/offtheroad.png)
*Driving into the bushes*

## Dependencies
To run this project, you'll need to install [pygame](https://pypi.org/project/pygame/). This can be done with the following command:

    pip install pygame