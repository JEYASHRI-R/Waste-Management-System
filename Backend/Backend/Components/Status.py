import sys
sys.path.append('..')
from Resource.imports import *
from Resource.config import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000/"}})

@app.route('/status', methods=['POST', 'GET'])
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])
def register():
    try:
        df = pd.read_csv(COLLECTION_STATUS)
        json_data = df.to_json(orient='records')  # Convert DataFrame to JSON
        return jsonify({"data": json_data})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
