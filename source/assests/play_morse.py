import winsound
import time

DOT = 100          # milliseconds
DASH = DOT * 3
LETTER_GAP = DOT * 3
WORD_GAP = DOT * 7
FREQ = 800         # Hz

def play_morse(code):
    for symbol in code:
        if symbol == ".":
            winsound.Beep(FREQ, DOT)
        elif symbol == "-":
            winsound.Beep(FREQ, DASH)
        elif symbol == "/":
            time.sleep(WORD_GAP / 1000)
            continue

        # normal gap between symbols inside a letter
        time.sleep(DOT / 1000)

    # optional: small pause at end
    time.sleep(LETTER_GAP / 1000)


