from __future__ import print_function

try:
    input = raw_input
except NameError:
    pass

TEMPL = "your name is {}, you are {} years old, and your username is {}"

if __name__ == "__main__":
    name = input("What is your name?\n")
    age = input("What is your age?\n")
    reddit_username = input("What is your reddit username?\n")
    with open("DP_easy_1.txt", 'a') as f:
        f.write("\t".join((name, age, reddit_username)) + "\n")
    print(TEMPL.format(name, age, reddit_username))
