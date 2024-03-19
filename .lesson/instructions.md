# Project: Bouncing Ball
## Background
Some of the first [video games](https://en.wikipedia.org/wiki/Early_history_of_video_games) were games where players would manipulate a ball as it bounces around the playing field. From Tennis for Two to Pong, Arkanoid, and Peggle, you will follow in their footsteps and design and program a similar game.

## Instructions

Your project is to create a game where the ball bounces around the playing field and users can interact with it.

- Make sure you have a tab open with the  [Play Documentation](https://github.com/replit/play)
- You probably want to get the ball bouncing first.
    - To get the ball to bounce off the top or bottom: `360 - angle`
    - To get the ball to bounce off the left or right: `180 - angle` 
    - After changing the angle, you should use this line of code to ensure the angle stays valid: `angle %= 360`
    - [Helpful graphic on angles](https://en.wikipedia.org/wiki/Unit_circle#/media/File:Unit_circle_angles_color.svg)
- Allow players to use either [mouse](https://github.com/replit/play#mouse-commands) or [keyboard](https://github.com/replit/play#keyboard-commands) for inputs.
    - Can use both, especially if you are making it multiplayer.
- First create the play field, then add the drawing and text objects, then put all the gameplay and logic in the `@play.repeat_forever def do()` block.
- Make sure you use variables for the play field dimensions, scores/health, and any other data you are keeping track of.


This is a wide-open assignment and you could work on it for a very long time!  Talk to your teacher about what you need to complete in order to receive credit!

---

# Examples of old games
<img src="https://cpb-eu-w2.wpmucdn.com/media.confetti.ac.uk/dist/7/112/files/2020/11/pong.gif" width="200">
<img src="https://thumbs.gfycat.com/LeafyFocusedJumpingbean-max-1mb.gif" width="200">
<img src="https://raw.githubusercontent.com/YeOldeDM/godot-breakout-example/master/break1.gif" width="200">

> [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)