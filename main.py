import json
from pathlib import Path

def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)

def main():
    config = load_config()

    print("🌱 GROW A PLANT EGG NOTIFIER")
    print("=" * 35)

    game = config["game"]
    print("Game:", game["name"])
    print("Place ID:", game["place_id"])

    print("\n🎯 TARGET EGGS:")

    for egg in config["target_eggs"]:
        print(f"- {egg['name']} ({egg['rarity']})")

    print("\nConfiguration loaded successfully.")
    print("Live stock detection: NOT CONNECTED YET.")

if __name__ == "__main__":
    main()
