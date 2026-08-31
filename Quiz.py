from flask import Flask, render_template, request, jsonify

Quiz = Flask(__name__)

questions = [
    {
        "id": "q1",
        "text": "You have a completely free Sunday, what are you doing?",
        "options": [
            {"label": "1. Spending me time with Coffee", "tag": "Pothos"},
            {"label": "2. Go somewhere fun and explore", "tag": "Jade"},
            {"label": "3. Quietly do your own thing", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q2",
        "text": "What kind of friend are you?",
        "options": [
            {"label": "1. Adaptable and down for anything friend", "tag": "Pothos"},
            {"label": "2. Chill and Independent friend", "tag": "Jade"},
            {"label": "3. Sensitive and caring friend", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q3",
        "text": "Pick your favourite spot in a park",
        "options": [
            {"label": "1. Under a big shady tree", "tag": "Pothos"},
            {"label": "2. A white bench on side of the park", "tag": "Jade"},
            {"label": "3. By the fountain", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q4",
        "text": "Someone gives you a plant. Your first thought is…",
        "options": [
            {"label": "1. Can I propagate it?", "tag": "Pothos"},
            {"label": "2. Cute! Where will it look best?", "tag": "Jade"},
            {"label": "3. Please don't die because of me 😭", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q5",
        "text": "Pick a compliment:",
        "options": [
            {"label": "1. You always seem to be growing.", "tag": "Pothos"},
            {"label": "2. You're effortlessly cool", "tag": "Jade"},
            {"label": "3. You're mysterious", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q6",
        "text": "Pick your ideal rainy-day activity:",
        "options": [
            {"label": "1. Hot drink + window watching", "tag": "Pothos"},
            {"label": "2. Reading under a blanket", "tag": "Jade"},
            {"label": "3. Going outside anyway", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q7",
        "text": "You discover a tiny door at the bottom of a tree. What do you do?",
        "options": [
            {"label": "1. Open it immediately", "tag": "Pothos"},
            {"label": "2. Assume fairies live there", "tag": "Jade"},
            {"label": "3. Absolutely NOT", "tag": "Peace Lily"},
        ]
    },
        {
        "id": "q8",
        "text": "Pick a magical companion:",
        "options": [
            {"label": "1. A tiny glowing butterfly", "tag": "Pothos"},
            {"label": "2. A grumpy frog", "tag": "Jade"},
            {"label": "3. A chaotic fairy", "tag": "Peace Lily"},
        ]
    },
        {
        "id": "q9",
        "text": "If you were a tiny creature living in someone's garden, you'd be…",
        "options": [
            {"label": "1. A fairy", "tag": "Pothos"},
            {"label": "2. A tiny mushroom that may or may not be magical", "tag": "Jade"},
            {"label": "3. A butterfly", "tag": "Peace Lily"},
        ]
    },
    {
        "id": "q10",
        "text": "You receive a package with no return address. Inside is…",
        "options": [
            {"label": "1. A pressed flower", "tag": "Pothos"},
            {"label": "2. A tiny mirror", "tag": "Jade"},
            {"label": "3. A tiny key", "tag": "Peace Lily"},
        ]
    }
    
]

results = {
    "Pothos": {
        "title":"Pothos",
        "emoji":"hehe",
        "image": "pothos.gif"
        "description":"You are evergreesn, evergrowing and very adaptable, You can settle in any situation and make the best out of it!",
    },
    "Jade": {
        "title":"Jade",
        "emoji":"hehe",
        "image": "jade.gif"
        "description":"You are very strong, kind and very resilient. You are very independent and need almost little to no help to bloom into your best self",
    },
    "Peace Lily": {
        "title":"Peace Lily",
        "emoji":"hehe",
        "image": "peacelily.gif"
        "description":"You can be a bit dramatic at times but a little drama hurt no one! if given the right circumstances you can bloom very beautifully. You can also be very prortective of your loved ones and can go to any length to protect them.",
    }
}

def score_quiz(answers):
    tags = list(answers.values())
    winner = max(set(tags), key=tags.count)  # whichever tag appears most
    return winner

@Quiz.route("/")
def home():
    # Sends the QUESTIONS list to the HTML template, which loops
    # over it to build the buttons.
    return render_template("index.html", questions=questions)


@Quiz.route("/score", methods=["POST"])
def score():
    # request.get_json() reads the answers the browser sent us.
    answers = request.get_json()
    result = score_quiz(answers)
    winner = results.get(result, {
        "title": "Mystery Result",
        "emoji": "❓",
        "description": "We couldn't quite place you — try again?",
    })
    # jsonify sends it back as JSON, which script.js reads.
    return jsonify(winner)


if __name__ == "__main__":
    Quiz.run(debug=True, port=5000)
