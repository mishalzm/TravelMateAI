# TravelMate AI

TravelMate AI is a Flask web app that recommends Indian travel destinations from a small, locally defined destination catalog. Enter a budget, preferred season, interest, and trip length to see destinations that fit your budget, ranked by preference match and budget fit.

## Features

- Accepts a travel budget in Indian rupees, a season (Winter, Summer, or Monsoon), an interest (Beach, Nature, Adventure, or Culture), and number of travel days.
- Shows destinations whose listed estimated budget is within the submitted budget, ordered by a recommendation score.
- Builds a content-based similarity list for each recommendation using destination descriptions, attractions, interest, and season.
- Displays destination details, attractions, estimated budget, best season, and recommendation rationale.
- Provides client-side destination search and interest filtering on the results page, plus a light/dark theme toggle.

The submitted trip length is shown in the results summary; it is not currently used to filter or rank destinations. Destination data and listed budgets are maintained in `main2.py` and are illustrative catalog values.

## Recommendation approach

The app first excludes destinations whose listed budget exceeds the user's budget. For each remaining destination, it calculates a score from:

- **40 points** when the destination's interest matches the selected interest.
- **30 points** when its season matches the selected season.
- **Up to 30 points** based on how much budget remains: `(1 - destination budget / submitted budget) * 30`.

Results are sorted from highest score to lowest. The displayed rationale is a short template based on the selected preferences and does not explain the numeric score.

For “You May Also Like,” `main2.py` creates TF-IDF vectors from each destination's description, attractions, interest, and season, then compares those vectors with cosine similarity. It returns up to three other destinations with the highest similarity scores. These similar destinations are supplementary suggestions; they do not change the main results ranking.

## Requirements

- Python 3.11 or later
- pip

Dependencies are listed in `requirements.txt`: Flask, pandas, NumPy, and scikit-learn.

## Run locally

From the project root, create and activate a virtual environment, then install the dependencies and start the Flask development server:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

Open [http://localhost:5000](http://localhost:5000) in a browser. The app listens on port `5000` and binds to `0.0.0.0`; the code runs with Flask debug mode disabled.

## Run with Docker

Build the image from the project root:

```bash
docker build -t travelmate-ai .
```

Start the container and map port 5000:

```bash
docker run --rm -p 5000:5000 travelmate-ai
```

Then open [http://localhost:5000](http://localhost:5000). The included Dockerfile uses Python 3.11 slim, installs `requirements.txt`, copies the project into the image, and starts `app.py`.

## Project structure

```text
.
├── app.py               # Flask routes and preference-based ranking
├── main2.py             # Destination catalog and TF-IDF similarity model
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container build and start instructions
├── templates/
│   ├── index.html       # Trip preference form
│   └── results.html     # Recommendation results
└── static/
    ├── style.css        # Page styling
    ├── theme.js         # Theme toggle and results-page filters
    └── images/          # Destination images, when available
```

## GitHub

Clone the repository and enter its directory:

```bash
git clone https://github.com/mishalzm/TravelMateAI.git
cd TravelMateAI
```

After making local changes, stage, commit, and push them to your configured remote branch:

```bash
git add README.md
git commit -m "Add project README"
git push
```

## Notes

- Recommendations use the destination catalog and rules shipped with the project; the app does not call an external AI service or live travel data source.
- The budget is used as a single submitted amount. The app does not calculate per-day costs or validate destination availability.
- Some destination images may be absent; the results page hides an image when its file cannot be loaded.
