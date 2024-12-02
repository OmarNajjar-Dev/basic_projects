import random

# الأدوات الأساسية في اللعبة
words = ["cabbage", "lettuce", "dolphin", "octopus", "angry", "happy"]
guessed_letters = []
lives = 7  # عدد المحاولات
hangman_index = 0  # لطباعة الرسمة المناسبة لكل عدد من المحاولات
hangman_stages = [
    """\n
  +---+
      |
      |
      |
      |
      |
=========\n""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========\n""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========\n""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========\n""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========\n""",
    """
  +---+
  |   |
  O   |
 /|\  |      
      |
      |
=========\n""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========\n""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\n""",
]

# مقدمة + رسالة ترحيب
input(
    "Welcome to Hangman. You have only 7 tries.\nLet's play the game!\n\nPress Enter to continue:"
)

# إنشاء كلمة عشوائية
random_word = random.choice(words)

# إنشاء وطباعة مسافات بنفس عدد أحرف الكلمة
display = ["_"] * len(random_word)
print(hangman_stages[0])  # طباعة رسمة البداية
print(" ".join(display))

# طلب من المستخدم تخمين حرف
while "_" in display and lives > 0:
    guessed = input("Please guess a letter: ").lower()
    print()

    # التحقق من التخمين (صح أم خطأ)
    # تخمين خاطئ
    if guessed not in random_word and guessed not in guessed_letters:
        guessed_letters += guessed
        lives -= 1  # خسارة محاولة، ناتجة عن التخمين الخاطئ
        hangman_index += (
            1  # مع كل تخمين خاطئ يرتكبه المستخدم، اطبع له الرسمة التي تليها
        )
        print(hangman_stages[hangman_index])

    # تخمين مكرر
    elif guessed in guessed_letters:
        print("Oops! You have already entered this letter.")
        print(f"You have {lives} tries remaining.")
        continue

    # تخمين صحيح
    else:
        for position in range(len(random_word)):
            if guessed == random_word[position]:
                display[position] = guessed
                guessed_letters += guessed

    # إضافة الحرف المخمن إلى قائمة الأحرف المخمنة اذا كان التخمين صحيحا
    if guessed not in guessed_letters:
        guessed_letters += guessed

    # خسارة المستخدم
    if lives == 0:
        print("You lose!")
        break

    # فوز المستخدم
    elif "_" not in display:
        print(" ".join(display))
        print("Congratulations! You Win! 🎉🎉🎉")

    # عرض التفاصيل للمستخدم
    if "_" in display:
        print(" ".join(display))
        print(f"You have {lives} tries remaining.")
