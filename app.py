from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calleditor', methods=['GET'])
def get_endpoint_1():
    endpoint_name = request.endpoint
    return jsonify({"endpoint": endpoint_name, "branch": "dev"})

if __name__ == '__main__':
    app.run(debug=True)
