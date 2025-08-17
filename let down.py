import sys
import time

def play_lyric ():
    lyric = [
        ("You know", 0.09),
        ("You know where you are with", 0.09),
        ("You know where you are with", 0.09),
        ("Floor collapses, floating", 0.09),
        ("Bouncing back and", 0.09),
        ("One day...", 0.09),
        ("I am gonna grow wings", 0.09),
        ("A chemical reaction", 0.09),
        ("Hysterical and useless", 0.09),
        ("Hysterical and", 0.09),
        ("Let down and hanging around", 0.09),
        ("Crushed like a bug in the ground",0.09),
        ("Let down and hanging around", 0.09)
    ]

    delay = [1.8, 2.0, 2.0, 2.3, 0.3, 2.1, 2.3, 2.6, 2.6, 1.8, 1.9, 4.2, 4.2]
    print("\n=== Let Down - Radiohead === ")
    time.sleep(2)
    for i, (line, delayCharacter) in enumerate(lyric):
        for character in line :
            print(character, end='')
            sys.stdout.flush()
            time.sleep(delayCharacter)
        time.sleep(delay[i])
        print('')  
    print("// br.ainware")


play_lyric() 