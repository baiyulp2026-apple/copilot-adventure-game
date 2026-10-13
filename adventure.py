#!/usr/bin/env python3
# adventure.py - A single-file choose-your-own-adventure command-line game

import sys
import time

def slow(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def choose(prompt, options):
    opt_keys = {str(i+1): v for i, v in enumerate(options)}
    opt_display = "  ".join(f"[{i}] {v}" for i, v in opt_keys.items())
    while True:
        slow(f"\n{prompt}\n{opt_display}\n> ", delay=0)
        choice = input().strip()
        if choice in opt_keys:
            return int(choice) - 1
        # allow matching by full text (case-insensitive)
        for i, v in opt_keys.items():
            if choice.lower() == v.lower():
                return int(i) - 0  # returns int(i)-0 => index
        print("I didn't understand that. Choose a number or the option text.")

def ending(text):
    slow("\n" + "="*50 + "\n")
    slow(text)
    slow("\nTHE END.\n")
    slow("="*50 + "\n")
    return play_again()

def play_again():
    while True:
        r = input("Play again? (y/n) > ").strip().lower()
        if r in ('y', 'yes'):
            return True
        if r in ('n', 'no'):
            slow("Thanks for playing. Goodbye!")
            return False
        print("Please answer y or n.")

def opening():
    slow("You are a courier in the kingdom of Linvale, carrying a mysterious sealed parcel.")
    slow("On your route you face a choice of paths to deliver it before sundown.")
    first = ["Follow the riverside trail (safe, longer)", "Cut through the Whispering Woods (short, risky)", "Climb the Old Stone Pass (steep, shortcut)"]
    return choose("Which route do you take?", first)

def riverside_branch():
    slow("The riverside is calm. Fishermen nod as you pass. But dusk brings fog.")
    second = ["Accept a fisherman's offer to share a lantern", "Keep moving alone", "Investigate a strange light on the riverbank"]
    i = choose("A small decision could change your fate:", second)
    if i == 0:
        slow("The lantern reveals old runes on the parcel's seal. The fisherman hums a song that wards misfortune.")
        return ending("You arrive at the destination. The parcel is accepted; you are paid handsomely and celebrated for your caution.")
    if i == 1:
        slow("You hurry on. Fog thickens. A pack of shadowhounds crosses your path.")
        third_choice = ["Stand your ground and shout", "Throw a piece of rations to distract them"]
        j = choose("You must act quickly:", third_choice)
        if j == 0:
            slow("Your shout startles the hounds, but also attracts a patrol who mistake you for a thief.")
            return ending("After a tense explanation, the patrol escorts you to the lord's hall. The parcel is safe; your story becomes local legend.")
        else:
            slow("The rations divert them. You slip away, but the parcel was torn slightly. Inside, a sealed scroll is damp.")
            return ending("Despite the damage, the message reaches the recipient. They forgive the courier for the torn seal and reward honesty.")
    else:
        slow("The light is a will-o'-wisp. It circles you and points downstream, faster than you walk.")
        return ending("Following it, you discover a hidden boat and reach the city before sundown. The sealed parcel is delivered — and the will-o'-wisp vanishes like a blessing.")

def woods_branch():
    slow("The Whispering Woods are alive with murmurs. Trees seem to lean in to listen.")
    second = ["Whisper back to the trees", "Move silently and avoid interaction", "Climb a tree to scout"]
    i = choose("How do you approach the whispers?", second)
    if i == 0:
        slow("You whisper a simple greeting. The trees answer with directions, but ask for a favor.")
        third = ["Promise to return a lost trinket (agree)", "Refuse and press on (refuse)"]
        j = choose("The trees ask you to recover a child's music box deep in the grove. Do you:", ["Agree to help", "Refuse and continue"])
        if j == 0:
            slow("You find the music box tangled in roots and return it. The trees soften and gift you a safe path.")
            return ending("Guided through hidden glades, you deliver the parcel and gain a charm from the trees. Your luck is forever altered for the better.")
        else:
            slow("You refuse. The woods close ranks and your path becomes labyrinthine.")
            return ending("Lost until dawn, you stumble into a market where a merchant recognizes the parcel and claims the delivery fee. You're late, but alive.")
    if i == 1:
        slow("Silence is your ally. You pass unseen, but hear voices arguing near the path.")
        third = ["Eavesdrop to learn more", "Walk away quietly"]
        j = choose("Do you listen in?", ["Eavesdrop", "Leave it be"])
        if j == 0:
            slow("You learn of bandits planning an ambush ahead. You reroute and avoid danger.")
            return ending("Your caution pays off; you arrive safely and are commended for averting an ambush.")
        else:
            slow("You avoid trouble but walk into a bandit trap anyway — they wanted silent prey.")
            return ending("You are relieved of the parcel but spared severe harm. The kingdom reimburses you for your trouble, though your pride is bruised.")
    else:
        slow("From the tree you spot a ruined tower with a faint light: someone is signaling.")
        third = ["Climb down and approach the tower", "Ignore it and keep to the road"]
        j = choose("Do you investigate the tower?", ["Investigate", "Ignore it"])
        if j == 0:
            slow("Inside the tower you find an injured scholar who recognizes the parcel's seal.")
            return ending("They reveal the parcel contains a treaty; grateful, they help you complete the delivery and thank you with knowledge and a map.")
        else:
            slow("You bypass the tower and run into a messenger who offers to buy the parcel (suspicious).")
            return ending("You refuse. Later you learn the messenger was corrupt; you made the right choice by not trusting the stranger.")

def pass_branch():
    slow("The Old Stone Pass is harsh: winds bite and rocks shift.")
    second = ["Ride a rented mule for speed", "Climb on foot for control", "Wait out a storm in a cave"]
    i = choose("How will you handle the pass?", second)
    if i == 0:
        slow("The mule is sure-footed, but balks at a narrow ledge.")
        third = ["Calm the mule with a song", "Force it forward"]
        j = choose("Do you soothe or push?", ["Soothe it", "Force it"])
        if j == 0:
            slow("The mule calms, carrying you safely. A shepherd at the top gifts you dried fruit.")
            return ending("Thanks to gentleness, you cross the pass and deliver the parcel while keeping a new companion in the mule.")
        else:
            slow("The mule stumbles, you tumble, and the parcel skids toward the edge.")
            return ending("A traveler catches it at the last moment. You're bruised but alive; the recipient is annoyed but pays a smaller fee.")
    if i == 1:
        slow("On foot you find a narrow ledge with a carved rune.")
        third = ["Touch the rune", "Ignore the rune and continue"]
        j = choose("Do you touch the rune?", ["Touch it", "Ignore it"])
        if j == 0:
            slow("The rune flares and a gust grants you a brief blessing of speed.")
            return ending("You bound down the far side and arrive early. The parcel's contents avert a crisis; the kingdom rewards you.")
        else:
            slow("You pass safely but slowly. At the mountain's base, you see smoke — the city is under siege.")
            return ending("Because you arrived slowly, you are conscripted to help the city's defense and miss delivering the parcel on time, yet you find purpose in service.")
    else:
        slow("You shelter in a cave and meet an old hermit who offers tea and a choice of paths on an old map.")
        third = ["Accept the hermit's hidden path", "Take the well-worn road when storm clears"]
        j = choose("Which path do you take?", ["Hermit's path", "Well-worn road"])
        if j == 0:
            slow("The hidden path uses carved stone steps and bypasses all blockades.")
            return ending("The secret route delivers you in safety — but the hermit asks that you someday return the favor to another traveler.")
        else:
            slow("The well-worn road is crowded with refugees; you help them and come late.")
            return ending("Though late, your compassion is remembered. Years later you're called to aid in a council — the parcel's late arrival is forgiven.")

def main():
    slow("Welcome to 'Parcel of Linvale' — a short choose-your-own-adventure.\n", delay=0.01)
    while True:
        first = opening()
        if first == 0:
            again = riverside_branch()
        elif first == 1:
            again = woods_branch()
        else:
            again = pass_branch()
        if not again:
            break

if __name__ == "__main__":
    main()