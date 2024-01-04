import sys
sys.path.append('..')
from Resource.imports import *
from Resource.config import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000/"}})
df = pd.read_csv(REGISTERED_USER)

@app.route('/login', methods=['POST', 'GET'])
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])
def login():
    try:
        data = request.get_json()
        print(data)
        
        email = data.get('email')
        password = data.get('password')
        
        user_auth = any((df['Email'] == email) & (df['Password'] == password))
        
        if user_auth == True:
            if not os.path.isfile(USER_LOGIN):
                with open(USER_LOGIN, mode="w", newline="") as log_file_obj:
                    log_writer = csv.writer(log_file_obj)
                    log_writer.writerow(["Date", "Time", "Email"])
    
            with open(USER_LOGIN, mode="a", newline="") as log_file_obj:
                log_writer = csv.writer(log_file_obj)
                log_writer.writerow([date, time, email])
        
            return jsonify({"message": "success"})
        
        else:
            return jsonify({"message": "Invalid Credentials"})
    
    except Exception as e:
        print(f"Error during registration: {str(e)}")
        return jsonify({"message": "error"})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
