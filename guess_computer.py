"""
🔢 GUESS THE NUMBER - COMPUTER VERSION
🎯 Created by: Raveem Osja
🤖 Computer tries to guess YOUR number!
"""

import random
import time

def computer_guesses():
    print("=" * 50)
    print("🤖  COMPUTER GUESS THE NUMBER  🤖")
    print("=" * 50)
    print("\n🎯 Think of a number between 1 and 100!")
    print("📝 I'll try to guess it in minimum attempts.\n")
    
    input("🤔 Ready? Press Enter when you have your number...")
    
    low = 1
    high = 100
    attempts = 0
    feedback = ''
    
    print("\n" + "=" * 30)
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
            
        attempts += 1
        
        print(f"\n🤖 Computer guesses: {guess}")
        feedback = input("📊 Is it (H)igh, (L)ow, or (C)orrect? ").lower()
        
        if feedback == 'h':
            high = guess - 1
            print("📉 Too high! Let me think...")
        elif feedback == 'l':
            low = guess + 1
            print("📈 Too low! Let me think...")
        elif feedback != 'c':
            print("❌ Please enter H, L, or C!")
    
    print(f"\n🎉 COMPUTER WINS! 🎉")
    print(f"✅ Your number was: {guess}")
    print(f"🎯 Guessed in {attempts} attempts!")
    
    # Play again option
    if input("\n🔄 Play again? (yes/no): ").lower() == 'yes':
        computer_guesses()

if __name__ == "__main__":
    computer_guesses()