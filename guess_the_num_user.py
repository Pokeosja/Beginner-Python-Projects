"""
🎯 GUESS THE NUMBER - USER VERSION
👤 Created by: Raveem Osja
🎲 User tries to guess computer's random number
"""

import random

def user_guesses():
    print("=" * 50)
    print("🎯  GUESS THE NUMBER - YOU VS COMPUTER  🎯")
    print("=" * 50)
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"\n🎮 I'm thinking of a number between 1 and 100!")
    print(f"📊 You have {max_attempts} attempts to guess it!\n")
    
    while attempts < max_attempts:
        attempts += 1
        attempts_left = max_attempts - attempts
        
        try:
            guess = int(input(f"🔢 Attempt {attempts}/{max_attempts}: "))
            
            if guess < secret_number:
                print(f"📈 Too low! {attempts_left} attempts remaining\n")
            elif guess > secret_number:
                print(f"📉 Too high! {attempts_left} attempts remaining\n")
            else:
                print("\n" + "=" * 30)
                print(f"🎉 CONGRATULATIONS! 🎉")
                print(f"✅ You guessed it in {attempts} attempts!")
                print("🏆 YOU WIN! 🏆")
                print("=" * 30)
                break
        except ValueError:
            print("❌ Please enter a valid number!\n")
            attempts -= 1
    
    else:
        print("\n" + "=" * 30)
        print("💀 GAME OVER! 💀")
        print(f"🤖 The number was: {secret_number}")
        print("=" * 30)
    
    # Play again option
    if input("\n🔄 Play again? (yes/no): ").lower() == 'yes':
        user_guesses()

if __name__ == "__main__":
    user_guesses()