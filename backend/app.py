import os
import sys

from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

sys.path.insert(0, os.path.dirname(__file__))
from astrology import generate_report

app = Flask(__name__)
CORS(app)

@app.route('/api/report', methods=['POST'])
def report():
    data = request.get_json() or {}
    try:
        report = generate_report(data)
        return jsonify(report), 200
    except Exception as e:
        # For expected input problems, return a 400 with the message so the frontend can show it
        if isinstance(e, ValueError):
            return jsonify({'message': str(e)}), 400
        tb = traceback.format_exc()
        app.logger.error('Error generating report: %s', tb)
        # Return a generic message to the client while logging full traceback server-side
        return jsonify({'message': 'Internal server error. Check server logs.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
