"""
🔍 BINARY SEARCH DEMO
📚 Created by: Raveem Osja
🎯 Teaching the binary search algorithm
"""

import random
import time

def binary_search_demo():
    print("=" * 50)
    print("🔍  BINARY SEARCH ALGORITHM DEMO  🔍")
    print("=" * 50)
    
    print("\n📚 What is Binary Search?")
    print("✨ Binary search is an efficient algorithm for finding an item")
    print("   from a SORTED list of items. It works by repeatedly dividing")
    print("   the search interval in half.\n")
    
    # Generate sorted list
    print("📊 Generating a sorted list of 20 random numbers...")
    numbers = sorted(random.sample(range(1, 101), 20))
    
    print("\n📈 Sorted List:")
    for i, num in enumerate(numbers):
        print(f"{num:3}", end="  " if (i+1) % 10 != 0 else "\n")
    
    target = random.choice(numbers)
    print(f"\n🎯 Target number to find: {target}")
    
    print("\n" + "=" * 40)
    print("🔍 STARTING BINARY SEARCH")
    print("=" * 40)
    
    low = 0
    high = len(numbers) - 1
    steps = 0
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        current = numbers[mid]
        
        print(f"\n📊 Step {steps}:")
        print(f"   Low index: {low}, High index: {high}")
        print(f"   Middle index: {mid}, Value: {current}")
        
        # Visualize current state
        print("   ", end="")
        for i in range(len(numbers)):
            if i == low:
                print("[", end="")
            if i == mid:
                print(f"({numbers[i]})", end="")
            else:
                print(f" {numbers[i]} ", end="")
            if i == high:
                print("]", end="")
            if i < len(numbers) - 1:
                print(" ", end="")
        print()
        
        time.sleep(1)
        
        if current == target:
            print(f"\n✅ FOUND! Target {target} at index {mid}")
            print(f"📈 Found in {steps} steps")
            break
        elif current < target:
            print(f"   ↗️ {current} < {target}, searching RIGHT half")
            low = mid + 1
        else:
            print(f"   ↙️ {current} > {target}, searching LEFT half")
            high = mid - 1
        
        time.sleep(0.5)
    
    print("\n" + "=" * 40)
    print("📊 BINARY SEARCH COMPLETE!")
    print("=" * 40)
    
    # Compare with linear search
    print(f"\n📊 COMPARISON:")
    print(f"✅ Binary search took {steps} steps")
    
    # Simulate linear search
    linear_steps = 0
    for i, num in enumerate(numbers):
        linear_steps += 1
        if num == target:
            break
    
    print(f"📈 Linear search would take {linear_steps} steps")
    print(f"💡 Binary search is {linear_steps/steps:.1f}x faster!")
    
    # Interactive demo
    if input("\n🎮 Try with your own number? (yes/no): ").lower() == 'yes':
        try:
            user_target = int(input("🔢 Enter a number between 1-100: "))
            
            if user_target in numbers:
                # Find using binary search
                low, high = 0, len(numbers) - 1
                user_steps = 0
                
                while low <= high:
                    user_steps += 1
                    mid = (low + high) // 2
                    
                    if numbers[mid] == user_target:
                        print(f"\n✅ Found {user_target} at index {mid}")
                        print(f"📊 Took {user_steps} binary search steps")
                        break
                    elif numbers[mid] < user_target:
                        low = mid + 1
                    else:
                        high = mid - 1
            else:
                print(f"❌ {user_target} is not in the list")
                
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Run again
    if input("\n🔄 Run demo again? (yes/no): ").lower() == 'yes':
        binary_search_demo()

if __name__ == "__main__":
    binary_search_demo()