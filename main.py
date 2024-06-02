import sys
from solution import Solution

if __name__ == "__main__":
    try:
        days = int(input("enter the number of total days for university: "))
        if days<1:
            print("The value must be greater than 0 days.")
            sys.exit(0)
    except ValueError:
        print("days should only be of type 'int'")
    else:
        solution = Solution(days)
        print("Answer of ({}) days {}".format(days, solution.probability_to_miss_gradution_ceremony()))
