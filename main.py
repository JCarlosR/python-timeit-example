import time
import timeit

# Function to be measured
def functionTest():
    print("Starting function functionTest()")
    time.sleep(3)
    print("Function functionTest() finished")

# Since timeit results are expressed in seconds we'll use these constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR # 3600
MILLIS_PER_SECOND = 1000

# We can run the same function multiple times and the execution time will be the sum
# i.e. We could add additional logic to run multiple times and get an average execution time
NUMBER_OF_EXECUTIONS = 1

def measureExecutionTime():
    executionTime = timeit.timeit(stmt=functionTest, number=NUMBER_OF_EXECUTIONS)
    # executionTime = 325468742.10254354

    hours = int(executionTime / SECONDS_PER_HOUR)
    executionTime -= hours * SECONDS_PER_HOUR

    minutes = int(executionTime / SECONDS_PER_MINUTE)
    executionTime -= minutes * SECONDS_PER_MINUTE

    seconds = int(executionTime)
    executionTime -= seconds

    # At this point we only have the decimal part
    # e.g. 0.5 seconds = 500 milliseconds
    milliseconds = int(executionTime * MILLIS_PER_SECOND)

    print "Execution time"
    print hours, "hours"
    print minutes, "minutes"
    print seconds, "seconds"
    print milliseconds, "milliseconds"

measureExecutionTime()