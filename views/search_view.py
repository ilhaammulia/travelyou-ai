from flask import Blueprint, request, jsonify, render_template
from services.search_service import SearchService

search_bp = Blueprint("search", __name__)
service = SearchService()


@search_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@search_bp.route("/api/search", methods=["POST"])
def api_search():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt required"}), 400
    places = service.search_places_from_prompt(prompt)
    print(places)
    return jsonify([p.to_dict() for p in places])
