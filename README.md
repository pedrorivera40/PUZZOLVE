# PUZZOLVE

## Indroduction
Learning how to program may be a difficult task, especially for students who have not developed problem solving skills [1]. This is in part because popular programming languages lack of simple and intuitive syntax for novice users. Other important aspect to consider is that it is difficult to find a programming language that adjusts to different learning styles.

Educators are implementing more novel and interactive teaching techniques into their curriculums, such as surveying and educational video games. This is with the purpose to engage and motivate students to learn [2]. These initiatives, especially educational video games have shown effectiveness in motivating students to learn, because it provides an interface for different learning styles such as: visual, auditory, read and writing, learn by doing, associative, and others depending on the video game features. It also represents a platform for a constructivist approach to education.

With this in mind, it is proposed the creation and implementation of PUZZOLVE, an educational programming language. The main goals for such programming language are the following:
Implement simple and intuitive syntax.
  -Provide a responsive visual aided programming interface.
  -Provide video-game-like user experience.
  -Simplify learning programming.
  -Develop problem solving skills.
The main idea behind this programming language is provide the user with a game-like experience in which the user is able to create puzzles or maps. Each map might have different objects, such as buildings, trees, etc. In addition to the map creation, the user will be able to script the solution of these maps and run these solutions through the programming language. The user would have track of each command via a responsive graphical user interface (GUI) which would respond in real-time line by line.

## Project Demo
<iframe width="560" height="315" src="https://www.youtube.com/embed/-zGL0RrC-sw" frameborder="0" allowfullscreen></iframe>

## Language features

### Educational
The programming language was designed to facilitate the teaching problem solving skills as well as making it easy for educators to develop problem sets.

It does this by facilitating the design of puzzles for teachers and it provides an intuitive syntax for students to solve such puzzles with the use of commands, all in a single platform.

### Simple and Easy to Learn Syntax
 As a programming language that was built for the purpose of teaching kids programming. The language is designed with an intuitive and simple syntax. The main purpose of the programming language is to encourage children to solve problems and convey to them  they can achieve great things.

### Interactive Mode
Puzzolve contains an interactive mode, also known as Read-Eval-Print-Loop in many programming languages, as its main “development” environment. Interactive Mode restricts the user to input a single expression and returning its corresponding output.

This allows for easier debugging (catching errors quickly as they happen) and allows for step-by-step approach to create and  solve puzzles within the programming language.

### Imperative and Object Oriented
The programming language follows an imperative style of programming. Each expression is executed once in the programming language.

The programming language several predefined functions that allow the user to create, solve and check solutions for puzzles. Such predefined functions can be used to create different combination of actions.

Data Types in the programming language are interpreted.

### Free and Open Source
 Puzzolve will be free and open source such that students or developers  can play with the language and add other features to it.
### Example program

            create map named Erangel
            set start at 0 0
            set end at 7 6
            add tree at 1 1
            add tree at 1 2
            add tree at 1 3
            add tree at 4 4
            add tree at 5 4
            add tree at 6 2
            add tree at 2 6
            add tree at 2 5
            add tree at 3 0
            add tree at 3 1
            add tree at  7 3
            build map erangel
            create solution named Shroud
            move down 4
            move right
            move right 2
            move down 2
            move left 4
            move right 5
            build solution shroud
            run shroud


## Implementation and Requirement tools.
###  Python 3.6 -
To be used as intermediate code.
### PLY (Python Lex and Yacc)-
To develop language and interpreter components like the scanner and parser for our programming language.
### Pygame -
To create the responsive visual aided programming interface.

## Project plan and timeline
![projectplan](https://i.imgur.com/iOvjWqM.png)

## Final Report
Final report can be found here: https://www.scribd.com/document/380496243/Puzzolve-Report

## Media Resources Used
Sprites: Sithjester

Music: https://www.bensound.com
