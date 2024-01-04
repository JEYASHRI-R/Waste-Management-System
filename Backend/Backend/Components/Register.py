import sys
sys.path.append('..')
from Resource.imports import *
from Resource.config import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000/"}})

@app.route('/register', methods=['POST', 'GET'])
@cross_origin(origin='http://localhost:3000', headers=['Content-Type', 'Authorization'])
def register():
    try:
        data = request.get_json()
        print(data)
        
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        
        if(len(email)>1 and len(username)>1 and len(password)>1):      
            if not os.path.isfile(REGISTERED_USER):
                with open(REGISTERED_USER, mode="w", newline="") as log_file_obj:
                    log_writer = csv.writer(log_file_obj)
                    log_writer.writerow(["Date", "Time", "Email", "User Name", "Password"])
    
            with open(REGISTERED_USER, mode="a", newline="") as log_file_obj:
                log_writer = csv.writer(log_file_obj)
                log_writer.writerow([date, time, email, username, password])
        
            return jsonify({"message": "success"})
    
        else:
            return jsonify({"message": "Invalid Credentials"})
    
    except Exception as e:
        print(f"Error during registration: {str(e)}")
        return jsonify({"message": "error"})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
