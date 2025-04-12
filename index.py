from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="../templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_player_info', methods=['POST'])
def get_player_info():
    uid = request.form.get('uid')
    if not uid:
        return jsonify({'status': 'error', 'message': 'UID is required'}), 400

    api_url = f"https://karan-info-c91h.vercel.app/api/player-info?id={uid}"
    try:
        response = requests.get(api_url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def handler(request):
    return app(request.environ, start_response=None)
