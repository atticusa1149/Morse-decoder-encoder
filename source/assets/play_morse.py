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
            time.sleep(DOT / 1000)  # gap between symbols
        elif symbol == "-":
            winsound.Beep(FREQ, DASH)
            time.sleep(DOT / 1000)  # gap between symbols
        elif symbol == "/":
            # we've already had a DOT gap after the last symbol,
            # so only add the extra needed to reach WORD_GAP
            time.sleep((WORD_GAP - DOT) / 1000)

    # optional: small pause at end
    time.sleep(LETTER_GAP / 1000)
