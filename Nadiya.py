import time
import random

 
war_emotions = ["fear", "grief", "hopelessness", "anger", "displacement", "anxiety", "resilience"]


emotion_tips = {
    "fear": [
        "Focus on what you can control right now, even if it's small.",
        "Try grounding techniques like deep breathing or naming objects around you.",
        "Reach out to someone close to talk about your fears."
    ],
    "grief": [
        "Allow yourself to feel without judgment. It's okay to mourn losses.",
        "Create a memory ritual, like lighting a candle or writing a message.",
        "You are not alone—many share this pain and support is out there."
    ],
    "hopelessness": [
        "Even in darkness, small acts of kindness matter. Try one today.",
        "Write down one thing you're grateful for—it can shift your focus.",
        "Remember that healing can start from just one step."
    ],
    "anger": [
        "Channel anger into something constructive like writing, art, or movement.",
        "Take deep breaths or walk away briefly to cool down.",
        "It's okay to feel angry—what matters is how you cope with it."
    ],
    "displacement": [
        "Try to create a small sense of routine wherever you are.",
        "Connect with others who share your experience—it builds strength.",
        "Remember, home can be found in people and moments, not just places."
    ],
    "anxiety": [
        "Breathe slowly—inhale for 4 counts, hold, exhale for 4.",
        "Limit exposure to distressing news if it overwhelms you.",
        "Talk to someone—it often eases anxious thoughts."
    ],
    "resilience": [
        "Your strength is powerful—acknowledge how far you've come.",
        "Keep a small journal to note moments of courage each day.",
        "Inspiring others with your resilience is a quiet act of resistance."
    ]
}


all_affirmations = [
    "You are not alone; help and hope exist.",
    "Even on hard days, you're doing your best.",
    "Your feelings are valid and deserve space.",
    "Small steps forward are still steps.",
    "You’ve survived every difficult moment so far—you're strong.",
    "You have every right to feel what you’re feeling right now.",
    "Every sunrise is a sign of your resilience.",
    "You matter. Your experience matters.",
    "Bravery is continuing despite the fear."
]

used_affirmations = []

def get_unique_affirmation():
    global used_affirmations
    remaining = [a for a in all_affirmations if a not in used_affirmations]
    if not remaining:
        used_affirmations = []
        remaining = all_affirmations.copy()
    affirmation = random.choice(remaining)
    used_affirmations.append(affirmation)
    return affirmation

def animate_text(text, delay=0.02, bold=False):
    if bold:
        text = f"\033[1m{text}\033[0m"  
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_valid_input(prompt, allow_emotion=False, valid_responses=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["bye", "exit"]:
            animate_text("\nTake care of yourself. Goodbye.", 0.03)
            exit()
        if allow_emotion:
            if user_input in war_emotions:
                return user_input
            else:
                print("\nPlease tell me how you’re feeling using words like fear, grief, hopelessness, anger, displacement, anxiety, resilience.")
        elif valid_responses:
            if user_input in valid_responses:
                return user_input
            else:
                print(f"\nPlease choose one of the following: {', '.join(valid_responses)}")
        else:
            return user_input

def share_war_tips(emotion, used_tips):
    tips = [tip for tip in emotion_tips[emotion] if tip not in used_tips.get(emotion, [])]
    if not tips:
        return False
    tip = random.choice(tips)
    used_tips.setdefault(emotion, []).append(tip)
    animate_text(f"\n- {tip}", delay=0.03)
    return True

def main():
    used_tips = {}
    animate_text("Hope has a name. And it’s Nadiya.", delay=0.05, bold=True)
    animate_text("Hi, I’m Nadiya, your support bot.")
    animate_text("Tell me, how are you today?")

    emotion = get_valid_input("\nYou: ", allow_emotion=True)
    animate_text("\nThank you for sharing. It’s really brave to open up.", delay=0.04)
    animate_text("\nHere are a couple of things you might try:", delay=0.04)

    shared = share_war_tips(emotion, used_tips)
    if not shared:
        animate_text("\nI've shared all my tips for this feeling. Just know you're not alone.")

    affirmation = get_unique_affirmation()
    animate_text(f"\n{affirmation}")

    while True:
        animate_text("\nHow are you feeling now?", delay=0.03)
        animate_text("(You can type 'better', 'worse', 'no change', or 'bye' to exit)", delay=0.02)

        response = get_valid_input("\nYou: ", valid_responses=["better", "worse", "no change", "nochange", "same", "bye"])

        if response == "better":
            animate_text("\nThat’s wonderful to hear. Keep doing what’s helping you.", delay=0.03)
            animate_text("Would you like another tip or affirmation? (yes/no)", delay=0.02)
            reply = get_valid_input("\nYou: ", valid_responses=["yes", "no", "y", "n"])
            if reply.startswith("y"):
                if not share_war_tips(emotion, used_tips):
                    animate_text("\nI've shared all my tips for this feeling.", delay=0.03)
                animate_text(f"\n{get_unique_affirmation()}")
            else:
                animate_text("\nThat's perfectly fine. Just remember, you're doing great.", delay=0.03)

        elif response == "worse":
            animate_text("\nI'm really sorry you're feeling this way. It's okay to have rough days.", delay=0.03)
            if not share_war_tips(emotion, used_tips):
                animate_text("\nI've shared all my tips for this feeling. Maybe talk to someone you trust?", delay=0.03)
            animate_text(f"\n{get_unique_affirmation()}")

        elif response in ["no change", "nochange", "same"]:
            animate_text("\nIt's okay to feel like this. Progress can take time.", delay=0.03)
            animate_text("Would you like some more tips or a comforting message? (yes/no)", delay=0.02)
            reply = get_valid_input("\nYou: ", valid_responses=["yes", "no", "y", "n"])
            if reply.startswith("y"):
                if not share_war_tips(emotion, used_tips):
                    animate_text("\nI've shared all my tips for this feeling.", delay=0.03)
                animate_text(f"\n{get_unique_affirmation()}")
            else:
                animate_text("\nThat's alright. You're not alone.", delay=0.03)

        animate_text("\nWould you like some more support or tips? (yes/no)", delay=0.02)
        cont = get_valid_input("\nYou: ", valid_responses=["yes", "no", "y", "n"])
        if cont.startswith("n"):
            animate_text("\nTake care of yourself. Remember, you are not alone. Goodbye.", 0.03)
            break
        else:
            animate_text("\nHow are you feeling now? Please share how you're feeling.", delay=0.03)
            emotion = get_valid_input("\nYou: ", allow_emotion=True)
            animate_text("\nThanks for opening up again.", delay=0.03)
            if not share_war_tips(emotion, used_tips):
                animate_text("\nI've shared all my tips for this feeling.", delay=0.03)
            animate_text(f"\n{get_unique_affirmation()}")

if __name__ == "__main__":
    main()
