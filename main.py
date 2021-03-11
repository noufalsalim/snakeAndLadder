# import necessary packages
import numpy as np
import pandas as pd

def diceroll(value):
    """
    add value which is obtained by rolling dice randomly to the current value,
    if the value exceeds the end value(100) reduce the current dice value to keep it in the current position
    """
    dice = np.random.choice(np.arange(1,7), p=distribution)
    value += dice
    if value > end_square:
        value -= dice
    return value

def valuecheck(value):
    """
    check the current value has any ladders or snakes and replace the current value with resulting value
    """
    value = sl_values[value-1]
    return value

def main(number_of_players):
    """
    initialize the values and roll the dice to increase the value, 
    check the value for any snakes and ladders and update,
    write the value to a file
    """
    df = pd.DataFrame()
    number_of_steps = []

    for _ in range(0, number_of_players):
        current_value = init_square
        out = [current_value, ]
        
        while current_value < end_square:
            result = diceroll(current_value)
            result = valuecheck(result)
            current_value = result
            out.append(int(current_value))
        
        number_of_steps.append(len(out)) # find number of steps taken for each player to each end, for calculating average
        df = df.append(pd.Series(out), ignore_index=True) 

    df.transpose().to_csv("out.csv", sep=",")

    print("Average number of steps taken by all {} players are: {}".format(number_of_players, np.mean(number_of_steps)))



if __name__ == "__main__":
    """
    Read the SL.csv file and initialize the values and call main function
    """
    global init_square
    global end_square
    global sl_values
    global distribution
    
    number_of_games = 50
    number_of_players = 10
    # distribution = [0.05,0.05,0.05,0.05,0.05,0.75]
    # distribution = [4/12, 1/12, 1/12, 3/12, 1/12, 2/12]
    distribution = [1/12, 2/12, 2/12, 3/12, 1/12, 3/12]

    with open("SL.csv", "r") as fr:
        csv = fr.readlines()
        out = [int(out.split("\n")[0]) for out in csv]

    init_square = 1
    end_square = out[0]
    sl_values = out[1:]

    main(number_of_players)