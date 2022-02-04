from flask import Flask, jsonify, request
from final_data import   t


app = Flask(__name__)

@app.route("/get")
def get_task():
    return jsonify({
        "data": data
    })

@app.route("/planet")
def get_planet():
    name = request.args.get("planet")
    planet_data = next(i for i in data if i["name"]==name)
    return jsonify({
        "data": planet_data
    })

if __name__ == "__main__":
    app.run()