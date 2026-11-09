from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 

destinations=[
    {
    "name": "Goa",
    "state": "Goa",
    "budget": 18000,
    "season": "Winter",
    "interest": "Beach",
    "description": "Goa is a popular beach destination in India, known for its vibrant nightlife, beautiful beaches, and Portuguese heritage. Visitors can enjoy water sports, explore historic churches, and indulge in Goan cuisine.",
    "attractions": [
        "Calangute Beach",
        "Baga Beach",
        "Dudhsagar Falls",
        "Se Cathedral"
    ]
},
{
    "name": "Manali",
    "state": "Himachal Pradesh",
    "budget": 25000,
    "season": "Summer",
    "interest": "Adventure",
    "description": "Manali is a scenic hill station in Himachal Pradesh, known for its snow-capped mountains, lush valleys, and adventure sports. It is a popular destination for skiing, paragliding, and trekking.",
    "attractions": [
        "Rohtang Pass",
        "Vashisht Hot Springs",
        "Hadimba Temple",
        "Marhi Viewpoint"
    ]
},
{
    "name": "Ooty",
    "state": "Tamil Nadu",
    "budget": 12000,
    "season": "Summer",
    "interest": "Nature",
    "description": "Ooty, also known as Udhagamandalam, is a popular hill station in the Nilgiri Hills of Tamil Nadu. It is known for its scenic landscapes, tea plantations, and pleasant climate. Visitors can enjoy boating in Ooty Lake, exploring the Botanical Gardens, and taking a ride on the Nilgiri Mountain Railway.",
    "attractions":[
                       "Ooty Lake",
                       "Botanical Gardens",
                       "Doddabetta Peak",
                       "Nilgiri Mountain Railway"
                  ] 
},
{
    "name": "Coorg",
    "state": "Karnataka",
    "budget": 14000,
    "season": "Monsoon",
    "interest": "Nature",
    "description": "Coorg is a beautiful hill station in Karnataka, known for its coffee plantations, rivers, and lush greenery. It is a perfect destination for nature lovers and adventure seekers.",
    "attractions":[
                       "Abbey Falls",
                       "Raja's Seat",
                       "Dubare Elephant Camp",
                       "Nisargadhama"
                  ]
},
{
    "name": "Rishikesh",
    "state": "Uttarakhand",
    "budget": 16000,
    "season": "Winter",
    "interest": "Adventure",
    "description": "Rishikesh is a spiritual town in Uttarakhand, known for its yoga and meditation centers, gurus, and the holy Ganges River. It is a popular destination for those seeking inner peace and spiritual growth.",
    "attractions": [
        "Triveni Ghat",
        "Laxman Jhula",
        "Ram Jhula"
    ]
},
{
    "name": "Udaipur",
    "state": "Rajasthan",
    "budget": 22000,
    "season": "Winter",
    "interest": "Culture",
    "description": "Udaipur is a historic city in Rajasthan, known for its beautiful palaces, lakes, and rich cultural heritage. It is a popular destination for those interested in history and architecture.",
    "attractions": [
        "Lake Pichola",
        "City Palace",
        "Saheliyon ki Badi"
    ]
},
{
    "name": "Andaman",
    "state": "Andaman and Nicobar Islands",
    "budget": 35000,
    "season": "Winter",
    "interest": "Beach",
    "description": "Andaman is a group of islands in the Bay of Bengal, known for their pristine beaches, coral reefs, and diverse marine life. It is a paradise for water sports enthusiasts.",
    "attractions": [
        "Havelock Island",
        "Neil Island",
        "Radhanagar Beach"
    ]
},
{
    "name": "Varkala",
    "state": "Kerala",
    "budget": 10000,
    "season": "Winter",
    "interest": "Beach",
    "description": "Varkala is a coastal town in Kerala, known for its beautiful beaches, cliffs, and Ayurvedic spas. It is a popular destination for those seeking relaxation and wellness.",
    "attractions": [
        "Varkala Beach",
        "Kappil Beach",
        "Ayurvedic Spas"
    ]
},
{
    "name": "Mysore",
    "state": "Karnataka",
    "budget": 8000,
    "season": "Winter",
    "interest": "Culture",
    "description": "Mysore is a historic city in Karnataka, known for its palaces, temples, and rich cultural heritage. It is a popular destination for those interested in history and architecture.",
    "attractions": [
        "Mysore Palace",
        "Chamundi Hill",
        "Brindavan Gardens"
    ]
},
{
    "name": "Darjeeling",
    "state": "West Bengal",
    "budget": 20000,
    "season": "Summer",
    "interest": "Nature",
    "description": "Darjeeling is a hill station in West Bengal, famous for its tea plantations and the iconic Darjeeling Himalayan Railway. It offers breathtaking views of the Himalayas and a serene atmosphere.",
    "attractions": [
        "Darjeeling Himalayan Railway",
        "Tiger Hill",
        "Padmaja Naidu Himalayan Zoological Park"
    ]
},
{
    "name": "Leh",
    "state": "Ladakh",
    "budget": 40000,
    "season": "Summer",
    "interest": "Adventure",
    "description": "Leh is a scenic town in Ladakh, known for its stunning mountain landscapes, monasteries, and vibrant culture. It is a popular destination for those seeking adventure and cultural experiences.",
    "attractions": [
        "Shanti Stupa",
        "Thiksey Monastery",
        "Leh Palace"
    ]
},
{
    "name": "Pondicherry",
    "state": "Puducherry",
    "budget": 13000,
    "season": "Winter",
    "interest": "Beach",
    "description": "Pondicherry is a former French colony in India, known for its colonial architecture, beautiful beaches, and tranquil atmosphere. It is a popular destination for those seeking a peaceful retreat.",
    "attractions": [
        "Auroville",
        "Promenade Beach",
        "Basilica of the Sacred Heart of Jesus"
    ]
},
{
    "name": "Varanasi",
    "state": "Uttar Pradesh",
    "budget": 12000,
    "season": "Winter",
    "interest": "Culture",
    "description": "Varanasi is a sacred city in Uttar Pradesh, known for its ancient temples, ghats, and rich cultural heritage. It is a popular destination for those interested in spirituality and history.",
    "attractions": [
        "Kashi Vishwanath Temple",
        "Dashashwamedh Ghat",
        "Sarnath"
    ]
},
{
    "name": "Shimla",
    "state": "Himachal Pradesh",
    "budget": 22000,
    "season": "Summer",
    "interest": "Nature",
    "description": "Shimla is a hill station in Himachal Pradesh, known for its scenic beauty, colonial architecture, and pleasant climate. It is a popular destination for those seeking a peaceful retreat.",
    "attractions": [
        "Victoria Park",
        "The Ridge",
        "Christ Church"
    ]
},
{
    "name": "Hampi",
    "state": "Karnataka",
    "budget": 9000,
    "season": "Winter",
    "interest": "Culture",
    "description": "Hampi is a UNESCO World Heritage site in Karnataka, known for its ancient ruins, temples, and rich cultural heritage. It is a popular destination for those interested in history and archaeology.",
    "attractions": [
        " Hampi Archaeological Site",
        "Virupaksha Temple",
        "Vittala Temple"
    ]
}
]

destination_df = pd.DataFrame(destinations)

ml_data = destination_df[
    ["name", "description", "attractions", "interest", "season"]
].copy()

ml_data["features"] = (
    ml_data["description"] + " " +
    ml_data["attractions"].apply(lambda x: " ".join(x)) + " " +
    ml_data["interest"] + " " +
    ml_data["season"]
)

tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(ml_data["features"])

similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend_similar_destinations(destination_name):

    matches = ml_data[
        ml_data["name"].str.lower() == destination_name.lower()
    ]

    if matches.empty:
        return []

    destination_index = matches.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[destination_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores:

        if index != destination_index:

            recommendations.append({
                "name": ml_data.iloc[index]["name"],
                "score": round(float(score), 3)
            })

    return recommendations[:3]


######
def view_saved_trips():

    try:
        file = open("saved_trips.txt", "r")

        print("\n----- Previously Saved Trips -----")
        print(file.read())

        file.close()

    except FileNotFoundError:
        print("No saved trips found.")

def delete_saved_trips():

    try:
        with open("saved_trips.txt", "r") as file:
            content = file.read()

        if content == "":
            print("\nNo saved trips to delete.")
            return

        confirmation = input(
            "\nAre you sure you want to delete all saved trips? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            with open("saved_trips.txt", "w") as file:
                file.write("")

            print("\nAll saved trips deleted successfully!")

        else:
            print("\nDeletion cancelled.")

    except FileNotFoundError:

        print("\nNo saved trips found.")

def view_all_destinations():

    print("\n===== ALL AVAILABLE DESTINATIONS =====")

    for i, place in enumerate(destinations, start=1):

        print("\n", i, ".", place["name"])
        print("State:", place["state"])
        print("Budget: ₹", place["budget"])
        print("Interest:", place["interest"])
        print("Best Season:", place["season"])

def search_destination():

    search = input("\nEnter destination name: ").strip().lower()

    found = False

    for place in destinations:

        if search in place["name"].lower():

            show_destination(place)
            show_description(place)

            found = True

    if found == False:

        print("Sorry! Destination not found.")

def get_trip_details():

    while True:
        try:
            budget = int(input("Enter your total travel budget: "))

            if budget > 0:
                break
            else:
                print("Budget must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    interests = ["nature", "adventure", "culture", "beach"]

    while True:
        interest = input("Enter your interest (Nature/Adventure/Culture/Beach): ").strip().lower()

        if interest in interests:
            break
        else:
            print("Invalid interest. Please try again.")

    seasons = ["summer", "winter", "monsoon"]

    while True:
        season = input("Enter your preferred season (Summer/Winter/Monsoon): ").strip().lower()

        if season in seasons:
            break
        else:
            print("Invalid season. Please try again.")

    while True:
        try:
            days = int(input("How many days do you want to travel? "))

            if days > 0:
                break
            else:
                print("Days must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    return budget, interest, season, days


def daily_budget(budget, days):
    if days > 0:
     return budget / days
    else:
        print("Number of days cannot be negative.")
        return 0

def show_daily_budget(per_day_budget):
    print("Your daily budget for the trip is:", per_day_budget)

def show_destination(place):
    print("----------------------------")
    print("Destination:", place["name"])
    print("State:", place["state"])
    print("Estimated Budget:", place["budget"])
    print("Best Season:", place["season"])
    print("----------------------------")

def show_description(place):
    print("Description:", place.get("description", "Description not available."))

def show_itinerary(place, days):

    attractions = place.get("attractions", [])

    print("\n----- Travel Itinerary -----")

    if len(attractions) == 0:
        print("Itinerary not available.")
        return

    for i in range(days):

        print("\nDay", i + 1)

        first = i * 2
        second = first + 1

        if first < len(attractions):
            print("1.", attractions[first])

        if second < len(attractions):
            print("2.", attractions[second])

        if first >= len(attractions):
            print("Free time to explore.")

def save_trip(place, days):

    file = open("saved_trips.txt", "a")

    file.write("\n----- My Saved Trip -----\n")
    file.write("Destination: " + place["name"] + "\n")
    file.write("State: " + place["state"] + "\n")
    file.write("Budget: " + str(place["budget"]) + "\n")
    file.write("Season: " + place["season"] + "\n")
    file.write("Duration: " + str(days) + " days\n")

    attractions = place.get("attractions", [])

    for i in range(days):
        file.write("\nDay " + str(i + 1) + "\n")

        first = i * 2
        second = first + 1

        if first < len(attractions):
            file.write(attractions[first] + "\n")

        if second < len(attractions):
            file.write(attractions[second] + "\n")

    file.close()

    print("\nTrip saved successfully!")

def find_destination(budget, interest, season,days):
    
    matching_places = []

    for place in destinations:
        if place["budget"] <= budget and place["interest"].lower() == interest and place["season"].lower() == season:
            matching_places.append(place)

    matching_places.sort(
         key=lambda place: (
             place["budget"],
             place["name"]
          )
    )

    if len(matching_places) > 0:

      print("\n----- Recommended Destinations -----")

      for i, place in enumerate(matching_places, start=1):
        print(i, ".", place["name"], "-", "₹", place["budget"])

      print("Total recommendations:", len(matching_places))

      while True:
        try:
          choice = int(input("Enter your destination number: "))

          if choice >= 1 and choice <= len(matching_places):
            break
          
          else:
            print("Invalid choice. Please select a number from the list.")

        except ValueError:
            print("Please enter a valid number.")

      if choice >= 1 and choice <= len(matching_places):

        selected_place = matching_places[choice - 1]

        show_destination(selected_place)
        show_description(selected_place)
        show_itinerary(selected_place, days)
        save_trip(selected_place, days)
      else:
          print("Invalid destination choice.")

    else:
       print("No matching destinations found.")


def main_menu():
    while True:
        print("\n===== TOURISM RECOMMENDATION SYSTEM =====")
        print("1. Find a Destination")
        print("2. View Saved Trips")
        print("3. View All Destinations")
        print("4. Search Destination")
        print("5. Delete Saved Trips")
        print("6. Find Similar Destinations (ML)")
        print("7. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                user_budget, user_interest, user_season, user_days = get_trip_details()

                per_day_budget = daily_budget(user_budget, user_days)
                show_daily_budget(per_day_budget)

                find_destination(
                    user_budget,
                    user_interest,
                    user_season,
                    user_days
                )

            elif choice == 2:
                view_saved_trips()

            elif choice == 3:
                 view_all_destinations()
            elif choice == 4:
                 search_destination()
            elif choice == 5:
                delete_saved_trips()

            elif choice == 6:
                destination_name = input("Enter the name of the destination you want to find similar ones for: ")
                recommend_similar_destinations(destination_name)

            elif choice == 7:
                print("Thank you for using our system!")
                break

            else:
                print("Invalid choice. Enter 1, 2, 3, 4, 5, 6 or 7.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main_menu()
