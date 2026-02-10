"""
💀 HANGMAN GAME
👤 Created by: Raveem Osja
🔤 Word guessing game with limited tries
"""

import random

def hangman():
    print("=" * 50)
    print("💀  HANGMAN GAME  💀")
    print("=" * 50)
    
    # Word categories
    categories = {
        "Animals": ["elephant", "giraffe", "kangaroo", "penguin", "dolphin", "butterfly"],
        "Countries": ["australia", "brazil", "canada", "japan", "germany", "egypt"],
        "Fruits": ["pineapple", "strawberry", "watermelon", "blueberry", "pomegranate"]
    }
    
    # Display categories
    print("\n📂 Choose a category:")
    categories_list = list(categories.keys())
    for i, category in enumerate(categories_list, 1):
        print(f"{i}. {category}")
    
    # Get category choice
    while True:
        try:
            choice = int(input("\n🎯 Enter category number (1-3): "))
            if 1 <= choice <= 3:
                selected_category = categories_list[choice - 1]
                break
            else:
                print("❌ Please choose 1, 2, or 3!")
        except:
            print("❌ Invalid input!")
    
    # Select random word
    word = random.choice(categories[selected_category])
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    
    # Game variables
    lives = 6
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    
    print(f"\n🎮 Category: {selected_category}")
    print(f"💡 Hint: The word has {len(word)} letters")
    
    while lives > 0 and len(word_letters) > 0:
        print("\n" + hangman_stages[6 - lives])
        print(f"💔 Lives remaining: {lives}")
        
        # Show current word state
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("📝 Word: " + ' '.join(word_list))
        
        # Show used letters
        print("🔤 Used letters: " + ' '.join(sorted(used_letters)))
        
        # Get user guess
        guess = input("\n🔠 Guess a letter: ").lower()
        
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("✅ Good guess!")
            else:
                lives -= 1
                print("❌ Wrong guess!")
        elif guess in used_letters:
            print("⚠️ You already used that letter!")
        else:
            print("❌ Invalid character!")
    
    # Game over
    print("\n" + "=" * 40)
    if lives == 0:
        print(hangman_stages[6])
        print("💀 GAME OVER! You've been hanged!")
        print(f"🤖 The word was: {word}")
    else:
        print("🎉 CONGRATULATIONS! YOU WIN!")
        print(f"✅ The word was: {word}")
    print("=" * 40)
    
    # Play again
    if input("\n🔄 Play again? (yes/no): ").lower() == 'yes':
        hangman()

if __name__ == "__main__":
    hangman()