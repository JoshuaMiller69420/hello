import json
import os
import time
import random


def load_json_file():
    with open("high_scores.json", "r") as file:
        data = json.load(file)
        return data


def game(data, user_name):
    round_num = 3
    score = 0
    while True:
        print(f"Round {round_num - 2}")
        rand_num = "".join([str(random.randint(0,9))
                                  for _ in range(round_num)])
        for x in range (0,5):
            b = (f"Remember this number -> {rand_num}")
            print (b, end="\r")
            time.sleep(0.3)
        user_in = str(input("Guess the number: "))
        round_num += 1
        #if user_in == rand_num:
            
        #start_time = time.time()
        #prompt for input here
        #response_time = time.time() - start_time
        break


def add_score():
    pass


def main():
    #loading things
    #for x in range (0,5):  
    #    b = "Loading" + "." * x
    #    print (b, end="\r")
    #    time.sleep(1)
    
    data = load_json_file()
    print("Welcome to the memory game!")
    user_name = str(input("Enter your name: "))
    
    print("High Scores:")
    sorted_data = sorted(data, key=lambda x: x["score"], reverse=True)
    for index, cust in enumerate(sorted_data, start=1):
        print(f"{index}. {cust["name"]} - {cust["score"]}")
    
    user_in = str(input("Press Enter to start or q to quit: ")).lower()
    if user_in == "q":
        quit()
    elif user_in == "":
        game(data, user_name)
    else:
        print("Invalid input. Try again.")


if __name__ == "__main__":
    main()


#with open("high_scores.json", "w") as f: 
#    json.dump(high_scores, f, indent=4) 