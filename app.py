from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/echo', methods=['POST'])
def echo():
    try:
        json_data = request.json
        return jsonify(json_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
