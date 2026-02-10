"""
✊ ROCK PAPER SCISSORS GAME
👤 Created by: Raveem Osja
🎮 Classic game against the computer
"""

import random

def rock_paper_scissors():
    print("=" * 50)
    print("✊  ROCK PAPER SCISSORS  ✊")
    print("=" * 50)
    
    choices = ["rock", "paper", "scissors"]
    emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\n📊 SCORE: You {user_score} - {computer_score} Computer")
        print("\nChoose your move:")
        print("1. 🪨 Rock")
        print("2. 📄 Paper")
        print("3. ✂️ Scissors")
        print("4. ⏹️ Quit")
        
        try:
            choice = input("\n🎮 Your choice (1-4): ")
            
            if choice == '4':
                print("\n👋 Thanks for playing!")
                print(f"🏁 FINAL SCORE: You {user_score} - {computer_score} Computer")
                break
            
            if choice not in ['1', '2', '3']:
                print("❌ Please choose 1, 2, 3, or 4!")
                continue
            
            user_choice = choices[int(choice) - 1]
            computer_choice = random.choice(choices)
            
            print(f"\n👤 You chose: {emojis[user_choice]} {user_choice}")
            print(f"🤖 Computer chose: {emojis[computer_choice]} {computer_choice}")
            
            # Determine winner
            if user_choice == computer_choice:
                print("🤝 IT'S A TIE!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("🎉 YOU WIN THIS ROUND!")
                user_score += 1
            else:
                print("🤖 COMPUTER WINS THIS ROUND!")
                computer_score += 1
            
            # Check for game win
            if user_score == 3:
                print("\n" + "=" * 30)
                print("🏆 YOU WIN THE GAME! 🏆")
                print("=" * 30)
                break
            elif computer_score == 3:
                print("\n" + "=" * 30)
                print("💀 COMPUTER WINS THE GAME! 💀")
                print("=" * 30)
                break
                
        except:
            print("❌ Invalid input! Try again.")

if __name__ == "__main__":
    rock_paper_scissors()