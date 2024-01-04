import calendar
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000/"}})

@app.route('/shedule', methods=['POST', 'GET'])
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])
def shedule():
    try:
        current_date = datetime.date.today()
        year = current_date.year
        month = current_date.month
        days = calendar.monthrange(year, month)[1]
        month_in_word = calendar.month_name[month]
        return jsonify({"Year": year, "Month": month, "Days": days, "Month_in_word": month_in_word})
        
    except Exception as e:
        print(f"Error retrieving the date: {str(e)}")
        return jsonify({"message": "error"})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
