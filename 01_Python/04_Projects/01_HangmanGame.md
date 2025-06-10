# Project 1: Hangman Game 🎯

## Overview
Build a complete Hangman game in Python that demonstrates your understanding of core programming concepts including data structures, control flow, functions, file handling, and object-oriented programming.

## Difficulty Level
**Beginner to Intermediate** | **Estimated Time: 8-12 hours**

---

## Problem Statement

Create a console-based Hangman game where players guess letters to reveal a hidden word. The game should be engaging, user-friendly, and demonstrate clean code practices.

### Core Requirements

#### 1. Basic Game Mechanics
- Display the word as underscores (`_ _ _ _`) initially
- Accept single letter guesses from the player
- Reveal correctly guessed letters in their positions
- Track and display incorrect guesses
- Limit incorrect guesses (typically 6-7 attempts)
- Determine win/loss conditions

#### 2. User Interface
- Clear, formatted display of game state
- Visual representation of hangman (ASCII art) that updates with wrong guesses
- Display of guessed letters (both correct and incorrect)
- Remaining attempts counter
- Input validation and error handling

#### 3. Word Management
- Minimum word list of 50+ words stored in a separate file (`words.txt`)
- Random word selection for each game
- Support for words of varying lengths (4-12 characters)
- Case-insensitive gameplay

---

## Technical Specifications

### Required Features

#### Core Functionality (70 points)
- [x] **Game Loop**: Implement main game loop with proper state management
- [x] **Word Display**: Show current state of word with guessed letters revealed
- [x] **Input Handling**: Accept and validate user input (single letters only)
- [x] **Guess Tracking**: Track correct and incorrect guesses separately
- [x] **Win/Loss Logic**: Properly detect and handle game end conditions
- [x] **File I/O**: Read word list from external file

#### User Experience (20 points)
- [x] **Visual Feedback**: ASCII hangman drawing that updates with wrong guesses
- [x] **Clear Interface**: Well-formatted display of game information
- [x] **Error Handling**: Handle invalid inputs gracefully
- [x] **Game Statistics**: Show attempts remaining and letters guessed

#### Code Quality (10 points)
- [x] **Functions**: Break code into logical, reusable functions
- [x] **Documentation**: Include docstrings and comments
- [x] **Variable Naming**: Use descriptive variable names
- [x] **Code Organization**: Clean, readable code structure

### Bonus Features (Extra 20 points)
- [ ] **Difficulty Levels**: Easy/Medium/Hard with different word lists
- [ ] **Hint System**: Provide category hints or letter frequency hints
- [ ] **Score System**: Track wins/losses across multiple games
- [ ] **Custom Word Lists**: Allow users to add their own words
- [ ] **Multiplayer Mode**: Two-player mode where one sets the word

---

## Implementation Guidelines

### Suggested Program Structure

```python
def load_words(filename):
    """Load words from file and return as list"""
    pass

def choose_random_word(word_list):
    """Select random word from list"""
    pass

def display_hangman(wrong_count):
    """Display ASCII hangman based on wrong guess count"""
    pass

def display_game_state(word, guessed_letters, wrong_letters, wrong_count):
    """Display current game state to user"""
    pass

def get_player_guess(guessed_letters):
    """Get and validate player's letter guess"""
    pass

def check_game_over(word, guessed_letters, wrong_count, max_wrong):
    """Check if game is won or lost"""
    pass

def play_hangman():
    """Main game function"""
    pass

def main():
    """Main program entry point"""
    pass

if __name__ == "__main__":
    main()
```

### Required Files Structure
```
hangman_project/
├── hangman.py          # Main game file
├── words.txt          # Word list file
├── README.md          # Project documentation
└── hangman_art.py     # ASCII art (optional separate file)
```

---

## Sample Game Flow

```
=== HANGMAN GAME ===

Word: _ _ _ _ _ _
Wrong letters: 
Attempts remaining: 6

  +---+
  |   |
      |
      |
      |
      |
=========

Enter a letter: p

Good guess!

Word: P _ _ _ _ _
Wrong letters: 
Attempts remaining: 6

Enter a letter: x

Wrong letter!

Word: P _ _ _ _ _
Wrong letters: X
Attempts remaining: 5

  +---+
  |   |
  O   |
      |
      |
      |
=========

Enter a letter: y

Good guess!

Word: P Y _ _ _ _
Wrong letters: X
Attempts remaining: 5

# ... game continues until win or loss
```

---

## Testing Checklist

Ensure your implementation handles these scenarios:

### Basic Functionality
- [ ] Game loads word list successfully
- [ ] Random word selection works
- [ ] Correct letters are revealed in proper positions
- [ ] Incorrect letters are tracked separately
- [ ] Game ends when word is complete
- [ ] Game ends when max wrong guesses reached

### Edge Cases
- [ ] Duplicate letter guesses are handled appropriately
- [ ] Invalid input (numbers, symbols, multiple letters)
- [ ] Empty input handling
- [ ] Case insensitivity (A and a treated the same)
- [ ] Words with repeated letters display correctly

### User Experience
- [ ] Clear instructions provided
- [ ] Game state is always visible and understandable
- [ ] Hangman ASCII art displays correctly
- [ ] Win/loss messages are clear

---

## Evaluation Criteria

| Criteria | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D/F) |
|----------|---------------|----------|------------------|------------------|
| **Functionality** | All features work perfectly, handles edge cases | Core features work well, minor issues | Basic functionality present | Major functionality missing |
| **Code Quality** | Clean, well-organized, excellent naming | Good structure, readable | Adequate organization | Poor structure, hard to read |
| **User Experience** | Intuitive, polished interface | Clear and functional | Basic but usable | Confusing or frustrating |
| **Error Handling** | Comprehensive validation | Good input handling | Basic error checking | Little to no validation |
| **Documentation** | Excellent comments and docstrings | Good documentation | Some documentation | Poor or missing docs |

---

## Submission Requirements

### What to Submit
1. **Source Code**: All Python files (.py)
2. **Word List**: words.txt file with 50+ words
3. **README.md**: Project documentation including:
   - How to run the program
   - Features implemented
   - Any bonus features added
   - Known limitations or bugs
4. **Screenshots**: 2-3 screenshots showing gameplay

### Submission Format
- Create a GitHub repository for your project
- Include all files in the repository
- Ensure code is well-commented
- Test thoroughly before submission

### Deadline
**[Insert your deadline here]**

---

## Getting Started Tips

1. **Start Simple**: Begin with basic word display and letter guessing
2. **Test Frequently**: Test each function as you write it
3. **Use Print Statements**: Debug by printing variable values
4. **Handle One Thing at a Time**: Don't try to implement everything at once
5. **Read Error Messages**: Python's error messages are helpful for debugging

## Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [File I/O in Python](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Random Module Documentation](https://docs.python.org/3/library/random.html)

---

## Academic Integrity
This project should be completed individually. While you may discuss general approaches with classmates, the code you submit must be your own work. Plagiarism will result in a failing grade.

**Good luck, and happy coding! 🐍**