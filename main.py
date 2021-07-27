import time
import timeit

# The function took 5 hours, 4 minutes, 7 seconds y 100 milliseconds to be executed.

def function1():
    print("Starting function 1")
    time.sleep(3)
    print("Function 1 finished")

# function1()

def measureExecutionTime():
    # executionTime = timeit.timeit(stmt=function1, number=1)
    executionTime = 325468742.10254354

    # 1 min = 60 sec
    # 1 hour = 60 min = 3600 sec

    hours = int(executionTime / 3600)
    executionTime = executionTime - hours * 3600
    minutes = int(executionTime / 60)
    executionTime = executionTime - minutes * 60
    seconds = int(executionTime)
    executionTime = executionTime - seconds

    # 0.5 seconds = 500 milliseconds
    milliseconds = int(executionTime * 1000)

    print "Execution time"
    print hours, "hours"
    print minutes, "minutes"
    print seconds, "seconds"
    print milliseconds, "milliseconds"

measureExecutionTime()