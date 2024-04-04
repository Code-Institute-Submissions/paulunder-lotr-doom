# **Lord of the Rings - Mount Doom**
Developed by Paul Pfister

<img src="docs/am-i-responsive.png" alt="A screenshot of Am I Responsive representation of the website">

[Link to live site](https://lotr-doom-638e78e3e24d.herokuapp.com/)

## Introduction
Lord of the Rings - Mount Doom is a text-based story game where the player takes on the role of Frodo Baggins, the player can choose between 2 paths in the beginning of the game, and the player must navigate through the game by making choices that will affect the outcome of the game. The player must reach Mount Doom and destroy the One Ring to win the game.

## Contents
* [Project Goals](#project-goals)<br>
    * [For the user](#for-the-user)
    * [For the site owner](#for-the-site-owner)
* [User Experience](#user-experience)<br>
    * [Target audience](#target-audience)
    * [User requirements](#user-requirements)
    * [User Manual](#user-manual)
    * [User Stories](#user-stories)
* [Technical Design](#technical-design)
    * [Data Models](#data-models)
    * [Flowchart](#flowchart)
* [Features](#features)
    * [App Features](#app-features)
    * [Feature Ideas for future development](#feature-ideas-for-future-development)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
* [Testing](#testing)
    * [Validation](#validation)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Bugs](#bugs)
* [Credits](#credits)

## Project Goals

### ...For the user
* Play a game that is understandable and works as expected.
* Play a game where you have some story line choices.
* To sign up with a new account.
* Log back in to an existing account.

### ...For the site owner
* Take the user by the hand and guide them through the game. - clear instructions.
* To test the user's ability to make decisions.
* To receive feedback from the user about the game.

## User Experience

### Target audience
Lord of the rings fans, that are willing to imagine some extras in the Frodo Baggin's journey to Mount Doom.

### User requirements
* A game that is understandable and works as expected.
* Log-in works as expected and incorrect details do not allow the user access to their account.
* GA win or a loss is communicated to the user

### User Manual
Click the dropdown to view the user manual:
<details>
<summary>User Manual</summary>

### Log in
When the program starts, the user will be prompted to:
* Enter their existing login.
* Sign up for a new account.
This choice is navigated by typing yes or no on the keyboard and pressing enter to submit. The credentials will then submitted or checked in the Google Sheets.

The user will then type in their details. The program will reject any incorrect or invalid details and the user will have to try again.

### Playing the game
After Log In or Sign Up, the user will be taken to the main menu. Here, the user can select the path he wants to take.
The Paths are:
1. The Path of the Ring
2. The Path of the Fellowship

#### Levels
The user will be presented with a question and if the user answers correctly, the user will see an ASCII Art Piece of happy Frodo. If the user answers incorrectly, the game ends immediatly and the user have to restart the game. 

### Completing the game
When answering all questions correctly, the user will be taken to the end of the game. The user will be presented with a message that they have completed the game and saved middle earth. Now the user can decide to play again.
</details><br>

####################

### User Stories
#### As a first time user...
(1) Sign up with a username and for the game.
(2) To have some visual ASCII Art to help understanding the game
(3) To see a visual representation of the game.
(4) To be able to sign up with a new account.
(5) To be able to make mistakes and receive feedback.
(6) To receive a win or loss message at the end of the game.

#### As a returning user...
(7) Be able to log in with my username and password.
(8) Play a different path than before.
(9) To send feedback to the site owner about the game.

#### As the site owner...
(10) Ensure that all data entered by the user is validated so as not to break the program/create bad user experience.
(11) Ensure that all user actions are given feedback in the terminal so that users feel they know what to do next in the game.


## Technical Design

### Flowchart

A flowchart was created using [Lucidchart](https://lucid.app/) to visualise the logic flow of the game.

<details>
    <summary>Flowchart</summary>
    <p>Dungeon Escape game logic:</p>
    <img src="docs/technical-design/lotr-doom-flowchart.jpg" alt="A screenshot of the flowchart of game logic">
</details><br>

### Data Models

* The game uses a google sheet to store user login data - this is simple one.
* The game uses a JSON File to store the game story, questions and answers.

## Features
The website has a single page with several features within the mock python terminal. These features are listed below.

### App Features:

<details>
    <summary>Game Title</summary>
    <p>This is what the user sees upon loading the site. The ASCII Art piece was originally from [ASCII Art Archive](https://www.asciiart.eu/). I needed to modify it to suit this piece of Art into the PYthon Code</p>
    <ul>
        <li>
            <p>Are you an existing user? (yes/no)</p>
        </li>
        <li>
            <img src="docs/features/signup.png" alt="A screenshot of the Are you an existing user? (yes/no) feature">
        </li>
        <li>
            <p>User story covered: 1, 2, 7</p>
        </li>
        <li>
            <p>Authentication - you cannot log in with an account that doesn't exist.</p>
        </li>
        <li>
            <img src="docs/features/authentication.png" alt="A screenshot of the login auth">
        </li>
        <li>
            <p>User story covered: 4, 7</p>
        </li>
        <li>
            <p>Validation - cannot sign up with invalid user data</p>
        </li>
        <li>
            <img src="docs/features/signup-validation.png" alt="A screenshot of the login auth validation">
        </li>
        <li>
            <p>User story covered: 5</p>
        </li>
    </ul>
</details><br>
