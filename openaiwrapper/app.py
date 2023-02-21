"""
App module.
"""
import openai
from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


if not openai.api_key:
    raise ValueError("Must set `OPENAI_API_KEY` in environment variables")


@app.route("/api/completions", methods=["POST"])
def completions():
    """
    Text completions endpoint.
    """
    params = request.json

    if not params.get("prompt"):
        return jsonify({"error": "Missing param 'prompt'"}), 400
    if not params.get("engine"):
        return jsonify({"error": "Missing param 'engine'"}), 400

    result = openai.Completion.create(**params)
    messages = [choice.text.strip() for choice in result.choices]

    return {"response": result.choices, "messages": messages}


@app.route("/api/image", methods=["POST"])
def image():
    """
    Image creation endpoint.
    """
    params = request.json

    result = openai.Image.create(**params)
    if not params.get("prompt"):
        return jsonify({"error": "Missing param 'prompt'"}), 400

    urls = [item["url"] for item in result["data"]]

    return {"response": result["data"], "urls": urls}
