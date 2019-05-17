from sys import argv
from classes import railroad as rail
from algorithms import randomAlgo
from classes import trainlining as tl
from algorithms import advancedHillclimber as ah
from algorithms import hillclimberAlgo as ha
from algorithms import geneticAlgo as ge
from algorithms import greedyAlgo as gr
from algorithms import randomAlgo as ra
from helpers import visual
from helpers import userInterface as UI


if (len(argv) != 4):
    print("main.py, max number trajectories, max length in minutes of trajectory, type of algorithm")
    quit(1)

if (argv[1].isalpha() or argv[2].isalpha()):
    print("number of trajectories and max length should be integers")
    quit(1)

maxTrajectories = argv[1]
maxLength = argv[2]
algorithm = argv[3]

railroad = rail.Railroad()
railroad.loadStations()
totalCritical = railroad.addTotalCritical()
trainlining = tl.Trainlining(maxTrajectories, maxLength, totalCritical)

countList = []
scoreList = []

runs = 1000


if algorithm == "random":
    ra.runRandom(railroad, trainlining, runs)

if algorithm == "greedy":
    gr.runGreedy(railroad, trainlining, runs)

    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "hillclimber":
    trainlining.addTrajectories(railroad)
    counter = 0
    for i in range(10000):
        counter += 1
        ha.hillclimber(trainlining, railroad)
        score = trainlining.calculateScore()
        countList.append(counter)
        scoreList.append(score)
        if (counter % 1000) == 0:
            print(f"counter: {counter} score: {score}")
    # visual.makeGraph(countList, scoreList)

    for trajectory in trainlining.trajectories:
        print(trajectory.visitedStations)
        print("\n")

if algorithm == "genetic":
    ge.genetic(trainlining, railroad)


if algorithm == "advancedhillclimber":
    trainlining.addTrajectories(railroad)
    counter = 0
    number = 1
    for i in range(10000):
        counter += 1
        trainlining = ah.advancedHillclimber(trainlining, railroad, maxLength, number)
        if (counter % 100) == 0:
            print(len(trainlining.trajectories))
            score = trainlining.calculateScore()
            print(f"counter: {counter} score: {score}")


visual.makeCard(railroad, trainlining)
