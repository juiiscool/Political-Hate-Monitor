import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load dataset
df = pd.read_excel("dataset/comments.xlsx")


@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    keyword = ""
    toxicity_score = None
    toxicity_level = None
    total_comments = 0
    hate_speech_count = 0
    negative_count = 0

    if request.method == "POST":

        keyword = request.form["keyword"].strip()

        comments = df["Comment i Pastruar"].fillna("").astype(str)

        results = df[
            comments.str.contains(
                keyword,
                case=False,
                na=False,
                regex=False
            )
        ]

        # Calculate toxicity
        total_comments = len(results)

        hate_speech_count = (
            results["Hate Speech"]
            .astype(str)
            .str.lower()
            .eq("true")
            .sum()
        )

        negative_count = (
            results["Sent. Anal. Category"]
            .astype(str)
            .str.lower()
            .eq("negative")
            .sum()
        )

        if total_comments > 0:

            hate_rate = hate_speech_count / total_comments
            negative_rate = negative_count / total_comments

            toxicity_score = (
                hate_rate * 0.70 +
                negative_rate * 0.30
            ) * 100

        else:
            toxicity_score = 0

        # Determine toxicity level
        if toxicity_score >= 67:
            toxicity_level = "HIGH"

        elif toxicity_score >= 34:
            toxicity_level = "MEDIUM"

        else:
            toxicity_level = "LOW"

    return render_template(
        "index.html",
        results=results,
        keyword=keyword,
        toxicity_score=toxicity_score,
        toxicity_level=toxicity_level,
        total_comments=total_comments,
        hate_speech_count=hate_speech_count,
        negative_count=negative_count
    )


if __name__ == "__main__":
    app.run(debug=True)