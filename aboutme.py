# about_luki.py

class Luki:
    def __init__(self):
        self.name = "Luki"
        self.age = 14
        self.skills = {
            "Python": 90,
            "JavaScript": 75,
            "C++": 15,
            "Lua": 40
        }
        self.tools = {
            "Discord Bot Development": 95,
            "Git": 80,
            "Web Development": 65,
            "UI/UX Design": 60
        }
        self.projects = [
            "PYTHYKON ESPORTS",
            "LukiSOFTWARE",
            "BronnikoFyut",
            "LukiMoneda"
        ]
        self.discord_bots = [
            "PYTHYKON BOT",
            "Brawniverse System",
            "Mega Tours Bot",
            "Paella Tours Bot"
        ]
        self.gaming = {
            "FNAF": "⭐ Favorite",
            "Roblox": "🎮 Active Player (Forsaken)",
            "Fortnite": "🏆 Competitive",
            "GTA V": "🌆 Story Completed",
            "Doki Doki Literature Club": "📚 Completed"
        }

    def introduce(self):
        print(f"👋 Hello! I'm {self.name}, a passionate dev creating futuristic apps.")
        print("🚀 Let's build something amazing together!\n")

    def show_skills(self):
        print("🧠 Skills:")
        for lang, level in self.skills.items():
            print(f"  - {lang}: {level}%")

    def show_tools(self):
        print("\n🛠 Tools & Technologies:")
        for tool, level in self.tools.items():
            print(f"  - {tool}: {level}%")

    def show_projects(self):
        print("\n🌍 Projects:")
        for project in self.projects:
            print(f"  - {project}")

    def show_bots(self):
        print("\n🤖 Discord Bots:")
        for bot in self.discord_bots:
            print(f"  - {bot}")

    def show_gaming(self):
        print("\n🎮 Gaming Interests:")
        for game, status in self.gaming.items():
            print(f"  - {game}: {status}")


if __name__ == "__main__":
    luki = Luki()
    luki.introduce()
    luki.show_skills()
    luki.show_tools()
    luki.show_projects()
    luki.show_bots()
    luki.show_gaming()
