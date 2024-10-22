class HashiraBot:
    def __init__(self, name):
        self.name = name
        self.genres = ["Action", "Adventure", "Fantasy", "Romance", "Slice of Life", "Comedy", "Drama", "Horror", "Sci-Fi"]
        self.statuses = ["Ongoing", "Completed"]
        self.animes = {
            "Shounen": ["Naruto", "Attack on Titan", "Demon Slayer", "My Hero Academia", "One Piece"],
            "Isekai": ["Re:Zero", "Sword Art Online", "No Game No Life", "Overlord", "That Time I Got Reincarnated as a Slime"],
            "Slice of Life": ["Your Lie in April", "Clannad", "March Comes in Like a Lion", "Barakamon", "K-On!"],
            "Romance": ["Toradora!", "Your Name", "A Silent Voice", "Fruits Basket", "Horimiya"],
            "Fantasy": ["Fullmetal Alchemist: Brotherhood", "The Rising of the Shield Hero", "Made in Abyss", "Magi", "Hunter x Hunter"]
        }
        self.ratings = {}  # Store ratings and reviews

    def get_introduction(self):
        return f"Hello! I'm {self.name}, your anime recommendation chatbot."
    
    def get_category_preference(self):
        while True:
            category_preference = input("HashiraBot: Which category of anime do you prefer? (Shounen, Isekai, Slice of Life, Romance, Fantasy): ").title()
            if category_preference in self.animes:
                return category_preference
            else:
                print("HashiraBot: Please enter a valid category.")

    def get_genre_preference(self):
        print("HashiraBot: Which genres are you interested in?")
        for i, genre in enumerate(self.genres, start=1):
            print(f"{i}. {genre}")

        user_choices = input("Enter the numbers of your preferred genres (e.g., 1 3): ")
        chosen_genres = [self.genres[int(choice) - 1] for choice in user_choices.split()]
        return chosen_genres

    def get_status_preference(self):
        print("HashiraBot: What is the status of the anime you want to watch?")
        for i, status in enumerate(self.statuses, start=1):
            print(f"{i}. {status}")

        user_choices = input("Enter the numbers of your preferred statuses (e.g., 1 2): ")
        chosen_statuses = [self.statuses[int(choice) - 1] for choice in user_choices.split()]
        return chosen_statuses

    def recommend_animes(self, category, genres, statuses):
        recommended_animes = []
        for genre in genres:
            recommended_animes += self.animes[category]
        
        print("HashiraBot: Here are some recommended animes:")
        for i, anime in enumerate(recommended_animes, start=1):
            print(f"{i}. {anime}")

        return recommended_animes

    def get_anime_details(self, animes):
        anime_number = int(input("HashiraBot: Enter the number of the anime you want to know more about: ")) - 1
        selected_anime = animes[anime_number]
        anime_details = {
            "title": selected_anime,
            "story": "This is a great anime with an amazing story.",
            "rating": "8.5/10",
            "episode_number": "24",
            "year": "2022"
        }
        return anime_details

    def rate_anime(self, anime_title):
        if anime_title in self.ratings:
            print("HashiraBot: You have already rated this anime.")
            return
        
        rating = input(f"HashiraBot: How would you rate '{anime_title}' (1-10)? ")
        review = input("HashiraBot: Write a short review: ")
        self.ratings[anime_title] = {"rating": rating, "review": review}
        print("HashiraBot: Thank you for your rating and review!")

    def search_anime_by_title(self, title):
        found_animes = []
        for category, animes in self.animes.items():
            for anime in animes:
                if title.lower() in anime.lower():
                    found_animes.append(anime)
        return found_animes

    def random_recommendation(self, category):
        import random
        recommended_anime = random.choice(self.animes[category])
        return recommended_anime

    def list_recent_recommendations(self):
        # You can add a mechanism to store recent recommendations and display them here
        pass

def main():
    bot_name = "HashiraBot"
    chatbot = HashiraBot(bot_name)
    
    print(chatbot.get_introduction())

    category_preference = chatbot.get_category_preference()
    chosen_genres = chatbot.get_genre_preference()
    chosen_statuses = chatbot.get_status_preference()

    recommended_animes = chatbot.recommend_animes(category_preference, chosen_genres, chosen_statuses)

    anime_details = chatbot.get_anime_details(recommended_animes)
    print(f"HashiraBot: Anime Details -\nTitle: {anime_details['title']}\nStory: {anime_details['story']}\nRating: {anime_details['rating']}\nEpisode Number: {anime_details['episode_number']}\nYear: {anime_details['year']}")

    rate_anime_option = input("HashiraBot: Would you like to rate an anime? (yes/no): ").lower()
    if rate_anime_option == "yes":
        anime_to_rate = input("HashiraBot: Enter the title of the anime you want to rate: ")
        chatbot.rate_anime(anime_to_rate)

    search_title = input("HashiraBot: Do you want to search for an anime by title? (yes/no): ").lower()
    if search_title == "yes":
        title_to_search = input("HashiraBot: Enter the title or keyword to search for: ")
        found_animes = chatbot.search_anime_by_title(title_to_search)
        if found_animes:
            print(f"HashiraBot: Found animes matching '{title_to_search}':")
            for i, anime in enumerate(found_animes, start=1):
                print(f"{i}. {anime}")
        else:
            print("HashiraBot: No matching animes found.")

    random_recommendation_option = input("HashiraBot: Would you like a random anime recommendation? (yes/no): ").lower()
    if random_recommendation_option == "yes":
        random_recommended_anime = chatbot.random_recommendation(category_preference)
        print(f"HashiraBot: Randomly recommended anime: {random_recommended_anime}")

    print("HashiraBot: Thanks for using the HashiraBot chatbot!")
    user_response = input("You: ")
    if "welcome" in user_response.lower():
        print("HashiraBot: Goodbye!")
    else:
        print("HashiraBot: Goodbye!")

if __name__ == "__main__":
    main()
