import time
import random
import sys

mirrors = [
    "You glance at the mirror. Your reflection blinks a moment after you.",
    "A cold draft brushes your neck. In the mirror, you see a dark shape move behind you.",
    "Your reflection grins—your own mouth stays still.",
    "The lights flicker. In one flash, your reflection is missing from the glass.",
    "You hear your name whispered, but your reflection mouths something else.",
    "A handprint appears on the inside of the mirror.",
    "You look away, but feel watched. The reflection is still staring at you.",
    "The mirror shows a room that isn’t yours. Someone is standing in the corner.",
    "Your breath fogs the glass. A word appears: 'RUN.'",
    "The reflection starts to move on its own, reaching toward the glass."
]

def slow_print(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def scare_jump():
    slow_print("\nA sudden bang rattles the mirror! Your reflection SCREAMS, its face twisted and inhuman!\n", 0.02)
    time.sleep(1)
    slow_print("You stumble back, heart pounding...", 0.04)
    time.sleep(1)

def subtle_scare():
    slow_print(random.choice(mirrors), 0.04)
    time.sleep(1)

def intro():
    slow_print("SPECTROPHOBIA", 0.07)
    slow_print("A short horror experience. Press Enter to begin...")
    input()
    slow_print("You wake up in a dimly lit house. All is quiet except for your own breathing.")
    slow_print("A hallway stretches before you. At the end, an old mirror stands.")

def ending():
    slow_print("\nYou reach out to the mirror. Your reflection does not move.", 0.04)
    slow_print("A hand bursts through the glass and grabs you.", 0.04)
    slow_print("Everything goes black.", 0.07)
    slow_print("\nTHE END.", 0.15)

def main():
    intro()
    steps = 0
    while steps < 5:
        slow_print("\nDo you walk closer to the mirror? (yes/no)", 0.03)
        choice = input("> ").strip().lower()
        if choice == "yes":
            if random.random() < 0.3:
                subtle_scare()
            else:
                slow_print("You take a cautious step forward...", 0.04)
            steps += 1
        elif choice == "no":
            slow_print("You stand frozen, but the mirror seems closer than before...", 0.04)
            steps += 1
        else:
            slow_print("You hesitate, unable to decide...", 0.04)
    # Final sequence
    scare_jump()
    ending()

if __name__ == "__main__":
    main()
