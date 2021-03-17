import random
import sys
import time

ZEN_OF_PYTHON = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one and preferably only one obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea let's do more of those!
"""


def get_choice(prompt: str, options: dict) -> str:
    while (choice := input(prompt).lower()) not in options:
        print(f"Error! Your options are: {', '.join(options)}")
    return choice


def format_text(text: str) -> str:
    return "".join(c.lower() for c in text if c.isalpha())


def countdown(num: int):
    for i in range(num, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)


def generate_random_string(text: str):
    formatted_text = format_text(text)
    random_string = ""
    countdown(3)
    start_time = time.time()
    time_elapsed = 0
    text_found = False

    while time_elapsed < 120:
        random_letter = chr(random.randint(97, 122))
        print(random_letter, end="")
        random_string += random_letter
        if len(random_string) > len(formatted_text):
            random_string = random_string[1:]
        if formatted_text in random_string:
            text_found = True
            end_time = time.time()
            break
        time_elapsed = time.time() - start_time
    
    if text_found:
        print(
            f"\n\n🥳🥳🥳 THE DESIRED TEXT HAS BEEN FOUND! 🥳🥳🥳\n\nLAST RANDOMLY GENERATED TEXT:\n{random_string}\n\nYou truly have the luck of the Irish! 🍀\nThe desired text was found in {end_time - start_time} seconds!\n"
        )
    else:
        print(f"\n\nSorry, you did not find the Zen of Python! Better luck next time! 🍀")


if __name__ == "__main__":
    print("HAPPY ST. PATRICK'S DAY! 🍀 DO YOU FEEL LUCKY TODAY?")
    print(
        "Run a randomly generated string for 2 minutes and see if the text of the Zen of Python comes up! May the odds be ever in your favor!"
    )
    menu_prompt = "\nAre you ready to begin? [Y]es, [N]o: "
    choice = get_choice(menu_prompt, ["y", "n"])
    if choice == "y":
        generate_random_string(ZEN_OF_PYTHON)
