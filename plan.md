# Quibble Race: Project Plan

## learning goals:
- unit testing
- setting up git / venvs
- learning the debugger (NO PRINT STATEMENTS)
- split rendering from code (CLI version and graphics version)

## vertical slice
- game opens w/ a menu screen, start, video options
- set the players as either player / comp / number of rounds / general game options
- generate players w/ starting moneey
- generate the racers / history
- pre race menu: 
    - quibbles, their wins and payout, and ability to bet and hinder
- news report
- race menu: watch the racers run
- earn money
- end / victory screen

## project structure:
- main
- racer
- player

## notes
- bugs suck man, they suck so bad. Here's what I'm thinking:
- sometimes you need to make bad code just to see how everything works
- THEN you look for all the pieces that have been repeated
- THEN you chop up pieces of the code to make sure you repeat as many actions as few times as possible

## bugs
- winnings doesn't work
- race render sometimes skips a row
- you can bet more money than you have
- racers maintain their position on the track
- no input validation on bet amount
- sometimes the funds become float

## planned features
- ai / expected value calculations
- runner history, stats, acceleration
- high scores / player stats / saves
- racetracks w/ random obstacles
- a more robust menu system that allows you to go do more things rather than just one thing in order (pick racer, choose bet etc)