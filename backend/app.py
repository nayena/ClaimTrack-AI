from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a database for quick development
users = []
resources = [
    {"id": 1, "subject": "Math", "link": "https://khanacademy.org"},
    {"id": 2, "subject": "Science", "link": "https://coursera.org"},
]

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User registered successfully!", "user": data}), 201

@app.route('/study-plan/<int:user_id>', methods=['GET'])
def generate_study_plan(user_id):
    user = users[user_id]
    # Simple rule-based plan (can be replaced with ML later)
    plan = [res for res in resources if res['subject'] in user['subjects']]
    return jsonify({"study_plan": plan})

if __name__ == "__main__":
    app.run(debug=True)