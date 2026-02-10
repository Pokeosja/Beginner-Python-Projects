"""
🎭 MADLIBS GAME
📝 Created by: Raveem Osja
✨ A fun word game where users input words to generate a story
"""

def madlibs_game():
    print("=" * 50)
    print("🎭  WELCOME TO MADLIBS GAME!  🎭")
    print("=" * 50)
    print("📝 Please enter the following words:\n")
    
    # Get user inputs
    adjective1 = input("🔤 Adjective: ")
    noun1 = input("🔤 Noun: ")
    verb1 = input("🔤 Verb (past tense): ")
    adverb1 = input("🔤 Adverb: ")
    adjective2 = input("🔤 Another adjective: ")
    noun2 = input("🔤 Another noun: ")
    noun3 = input("🔤 One more noun: ")
    adjective3 = input("🔤 Final adjective: ")
    verb2 = input("🔤 Verb: ")
    
    # Create the story
    story = f"""
    ✨✨✨ YOUR MADLIB STORY ✨✨✨
    
    Once upon a time, there was a {adjective1} {noun1} who {verb1} {adverb1} 
    through the enchanted forest. Suddenly, a {adjective2} {noun2} appeared!
    
    "Oh no!" exclaimed the {noun1}. "I must find the magical {noun3}!"
    
    After a {adjective3} journey, our hero finally managed to {verb2} 
    the treasure and save the kingdom!
    
    🏆 THE END 🏆
    """
    
    print("\n" + "=" * 50)
    print(story)
    print("=" * 50)
    
    # Play again option
    play_again = input("\n🔄 Play again? (yes/no): ").lower()
    if play_again == 'yes':
        madlibs_game()

# Run the game
if __name__ == "__main__":
    madlibs_game()