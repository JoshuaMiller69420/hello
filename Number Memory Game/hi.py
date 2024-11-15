import json
import os
import time
import random
import msvcrt

def load_json_file():
    with open("high_scores.json", "r") as file:
        data = json.load(file)
        return data


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def game(data, user_name):
    round = 1
    level = 3
    score = 0
    while True:
        
        rand_num = "".join([str(random.randint(0,9))
                                  for _ in range(level)])
        print(f"Remember the following numbers: {rand_num}")
        start_time = time.time()
        pause = time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Round {round}")
        guess_input = str(input("Enter the numbers you just saw: "))
        if guess_input == rand_num:
            response_time = time.time() - start_time
            score += int(100/response_time)
            print(f"Good Job! - Current score: {score}")
            level += 1
            round += 1
        elif guess_input != rand_num:
            print("Too bad!")
            print(f"You completed {
                  round} rounds with a final score of {score}.")
            print("Updated High Scores: ")
            add_score(data, user_name, score)
            save_score(data)
            print_scores(data)
            try_again(data, user_name)


def try_again(data, user_name):
    play_again = input("Play again?(y/n): ")
    if play_again == "y":
        print("Have fun!")
        game(data, user_name)
    elif play_again == "n":
        print("That's to bad. Have a good day!")
        quit()
    else:
        print("That's not yes or no silly, try again.")


def print_scores(data):
    sorted_data = sorted(data, key=lambda x: x["score"], reverse=True)
    for index, cust in enumerate(sorted_data, start=1):
        print(f"{index}. {cust["name"]} - {cust["score"]}")


def add_score(data, user_name, score):
    data.append({"name": user_name, "score": score})
    data.sort(key=lambda x: x['score'], reverse=True)
    if len(data) > 5:
        data.pop()
    return data


def save_score(data):
    with open("high_scores.json", "w") as f: 
        json.dump(data, f, indent=4) 


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