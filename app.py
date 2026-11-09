from flask import Flask, render_template, request
import main2

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():

    budget = int(request.form["budget"])
    season = request.form["season"]
    interest = request.form["interest"]
    days = int(request.form["days"])

    recommended_places = []

    for place in main2.destinations:

        if place["budget"] <= budget:

            score = 0

            if place["interest"] == interest:
                score += 40

            if place["season"] == season:
                score += 30

            budget_score = (
                1 - place["budget"] / budget
            ) * 30

            score += budget_score

            place["recommendation_score"] = round(score)

            place["similar"] = main2.recommend_similar_destinations(
                place["name"]
            )

            place["reason"] = (
                f"This destination matches your "
                f"{interest} interest and {season} travel preference."
                if place["interest"] == interest
                and place["season"] == season
                else "This destination is recommended based on "
                     "your travel preferences and available budget."
            )

            recommended_places.append(place)

    recommended_places.sort(
        key=lambda x: x["recommendation_score"],
        reverse=True
    )

    return render_template(
        "results.html",
        results=recommended_places,
        budget=budget,
        season=season,
        interest=interest,
        days=days
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
