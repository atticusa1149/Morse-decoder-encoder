from colorama import Fore,Style # type: ignore
from source.assests.dict import morse_letters,morse_dict
from source.assests.play_morse import play_morse
def translate(text):
    """Convert text to Morse code."""
    text = text.lower()
    return ' '.join(morse_letters.get(char, "") for char in text if char in morse_letters)

def morse_to_text(morse_code):
    """Convert Morse code to text."""
    words = morse_code.split(" / ")  # Split Morse code words
    decoded_text = []

    for word in words:
        letters = word.split(" ")  # Split Morse code letters
        decoded_word = "".join(morse_dict.get(letter, "") for letter in letters if letter in morse_dict)
        decoded_text.append(decoded_word)

    return " ".join(decoded_text)

while True:
    choice = input("Type 'morse' to convert text to Morse code, or 'text' to convert Morse code to text: ").strip().lower()
    if choice == "morse":
        word_to_morse = input("Enter a phrase (only letters and numbers, spaces allowed): ").strip()
        morse_phrase = translate(word_to_morse)
        print(Fore.YELLOW+f"Your Morse code: {morse_phrase}"+Style.RESET_ALL)
        sound_put=input("If you would like to here the audio for the output type yes, else, type anything else")

        if sound_put=="yes":
            play_again=True
            while play_again:
                play_morse(morse_phrase)
                play_again = input("If you would like to listen to the audio again type yes: ").strip().lower() == "yes"

    elif choice == "text":
        morse_to_word = input("Enter Morse code (use spaces between letters and '/' between words): ").strip()
        word_phrase = morse_to_text(morse_to_word)
        print(Fore.YELLOW+f"Your translated text: {word_phrase}"+Style.RESET_ALL)

    else:
        print('invalid choice')
