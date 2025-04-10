# **TicTacToe AI Game**

## **Description**  
A simple yet entertaining game offering different playing modes : play against a human or play against an AI player, through a Command Line Interface (CLI) or Graphic User Interface (GUI). 
## **Table of Contents**  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)
- [How to run](#How-to-run)
- [Game rules](#game-rules)
- [How to play](#How-to-paly)

## **Features**  
- Possibility to **choose your opponent between an AI player or human player**.  
- Possibility to **play through a Command Line Interface (CLI) or Graphical User Interface (GUI)**.  
- **AI player** powered by a **Minimax algorithm**.

## **Requirements**  
- **Python 3**  
- **Tkintker**

## **Installation**  
1. Clone or download the repository
<pre> git clone  https://github.com/Alicia105/TicTacToe.git </pre>
2. Navigate to the project directory
<pre> cd TicTacToe/src</pre>
3. Make sure the Tkintker library is installed (it's normaly included in Python standar library)
<pre> sudo apt-get install python3-tk </pre>

## **How to run** 
- Make sure you are in the good directory 
<pre> cd TicTacToe/src</pre>
- If you want to run the command line interface (CLI)
<pre>python main.py</pre>
- I you want to run the graphic user interface (GUI). 
<pre>python tictactoeGUI.py</pre>

## **Game rules**
The rules are simple :
- You have a 3x3 grid
- The first to complete a full line or diagonal wins
- The first to start is the one having the 'X' and the other player has the 'O'
- Players take turns to place their mark on empty cells .
- The game ends when one player wins or when the board is full (a draw).

## **How to play**
If you chose the CLI option :
- The rules will explained to you fron the start
- You have to choose the number corresponding to the cell you want to fill
- You first have to choose your opponent (Human or AI)
You'll end up with the following result in your terminal :
![CLI gameplay](images/terminal.jpg)

If you chose the CLI option :
- You first have to choose your opponent (Human or AI) in the following window to be able to play


![Choose opponent window](images/choose.jpg)
- You just have to click on the cell you want to fill
- If you chose the AI opponent, you will automaticly be the one to start
- The grid is updated automaticly as following


![GUI window gameplay](images/GUI.jpg)
- when the game is over a window opens with the result


![Result window gameplay](images/result.jpg)


