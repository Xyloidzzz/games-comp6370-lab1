# TWIXT Board Simulator

*(Adjusted as an Impartial Normal Play Game)*

## Import Quirks

- **graphics** is required for the GUI. It can be installed via pip using ***pip install `pip install graphics.py`.
- **win32gui** is required for the screenshot functionality. It can be installed via pip using `pip install pywin32`.
- **PIL** is also required for the screenshot functionality. It can be installed via pip using `pip install pillow`.

## Controls

- Click twice on a cell to place a peg.
- Click once on a cell then again on another cell to place two pegs (if not there) and a link.

## Menu Bar Options

- **Actions**
  - **Take Screenshot**: Takes a screenshot of the current game state and saves it to ./Screenshots.
  - **Change Peg Color**: Changes the color of the pegs between black and red. (Used mostly for demonstration purposes, linking between red and black is buggy.)
  - **Clear Board**: Clears the board of all pegs and links.
  - **Exit**: Exit the game.
