"""Data for word categories, hints, and game content"""
WORD_CATEGORIES = {
    "ANIMALS": {
        "words": ["CAT", "DOG", "COW", "PIG", "DUCK", "FISH", "BIRD", "FROG",
                  "LION", "BEAR", "TIGER", "ZEBRA", "MONKEY", "RABBIT", "MOUSE",
                  "EAGLE", "SHARK", "WHALE", "SNAKE", "DEER"],
        "icon": "🐱",
        "hint_prefix": "This is an animal that "
    },
    "COLORS": {
        "words": ["RED", "BLUE", "GREEN", "YELLOW", "BLACK", "WHITE", "PINK",
                  "PURPLE", "ORANGE", "BROWN", "GRAY"],
        "icon": "🎨",
        "hint_prefix": "This is a color that "
    },
    "FOOD": {
        "words": ["CAKE", "MILK", "BREAD", "RICE", "SOUP", "EGGS", "MEAT",
                  "APPLE", "MANGO", "GRAPE", "LEMON", "HONEY", "PIZZA", "BURGER"],
        "icon": "🍕",
        "hint_prefix": "This is a food item that "
    },
    "NATURE": {
        "words": ["SUN", "MOON", "STAR", "SKY", "CLOUD", "RAIN", "SNOW",
                  "WIND", "TREE", "FLOWER", "GRASS", "LEAF", "ROCK", "OCEAN"],
        "icon": "🌿",
        "hint_prefix": "This is a nature-related word that "
    },
    "HOME": {
        "words": ["BED", "CUP", "PEN", "BOOK", "BALL", "TOY", "HAT", "SHOE",
                  "DOOR", "WINDOW", "TABLE", "CHAIR", "LAMP", "CLOCK"],
        "icon": "🏠",
        "hint_prefix": "This is something you might find at home that "
    },
    "ACTIONS": {
        "words": ["RUN", "JUMP", "SING", "DANCE", "READ", "WRITE", "EAT", "SLEEP",
                  "LAUGH", "CRY", "SMILE", "PLAY", "WORK", "STUDY"],
        "icon": "⚡",
        "hint_prefix": "This is an action that means to "
    }
}

# Easy mode categories (simpler words)
EASY_CATEGORIES = {
    "ANIMALS": {
        "words": ["CAT", "DOG", "COW", "PIG", "DUCK", "FISH", "BIRD", "FROG"],
        "icon": "🐱",
        "hint_prefix": "This animal "
    },
    "COLORS": {
        "words": ["RED", "BLUE", "GREEN", "YELLOW", "BLACK", "WHITE", "PINK"],
        "icon": "🎨",
        "hint_prefix": "This color "
    },
    "FOOD": {
        "words": ["CAKE", "MILK", "BREAD", "RICE", "SOUP", "EGGS", "APPLE"],
        "icon": "🍕",
        "hint_prefix": "This food "
    },
    "OBJECTS": {
        "words": ["CAR", "BUS", "HAT", "CUP", "BED", "PEN", "BOOK", "TOY", "BALL"],
        "icon": "📦",
        "hint_prefix": "This object "
    }
}

# Hard mode categories (challenging words)
HARD_CATEGORIES = {
    "PROGRAMMING": {
        "words": ["PYTHON", "PROGRAM", "DEVELOPER", "COMPUTER", "ALGORITHM",
                  "FUNCTION", "VARIABLE", "DICTIONARY", "DATABASE", "NETWORK"],
        "icon": "💻",
        "hint_prefix": "This programming term "
    },
    "TECHNOLOGY": {
        "words": ["SECURITY", "APPLICATION", "INTERFACE", "SOFTWARE", "HARDWARE",
                  "JAVASCRIPT", "TERMINAL", "COMMAND", "PROCESSOR", "MEMORY"],
        "icon": "🔧",
        "hint_prefix": "This technology term "
    },
    "COMPLEX_ANIMALS": {
        "words": ["ELEPHANT", "GIRAFFE", "KANGAROO", "DOLPHIN", "PENGUIN"],
        "icon": "🦒",
        "hint_prefix": "This animal "
    }
}

# Detailed hints for specific words
SPECIFIC_HINTS = {
    "CAT": "🐱 says 'meow' and loves milk",
    "DOG": "🐕 says 'woof' and is called man's best friend",
    "COW": "🐄 gives us milk",
    "PIG": "🐷 says 'oink' and loves mud",
    "DUCK": "🦆 says 'quack' and loves water",
    "FISH": "🐟 lives in water and has fins",
    "BIRD": "🐦 has wings and can fly",
    "FROG": "🐸 jumps and says 'ribbit'",
    "LION": "🦁 The king of the jungle",
    "BEAR": "🐻 A large furry animal that loves honey",
    "RED": "🔴 The color of apples and fire trucks",
    "BLUE": "🔵 The color of the sky and ocean",
    "CAKE": "🎂 A sweet dessert often eaten at birthdays",
    "MILK": "🥛 A white drink from cows",
    "SUN": "☀️ The star that gives us light and heat",
    "MOON": "🌙 The object that glows at night",
}

def get_word_with_category(category_dict, category_name):
    """Get a random word and its category info"""
    import random
    category_data = category_dict[category_name]
    word = random.choice(category_data["words"])
    return word, category_name, category_data["icon"], category_data["hint_prefix"]

def get_hint_for_word(word, hint_prefix, category_name):
    """Get a hint for a specific word"""
    if word in SPECIFIC_HINTS:
        return f"💡 HINT: {SPECIFIC_HINTS[word]}"
    else:
        return f"💡 HINT: {hint_prefix}has {len(word)} letters and starts with '{word[0]}'"