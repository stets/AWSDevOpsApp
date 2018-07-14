from flask import Flask, jsonify

app = Flask(__name__)

output = [
	{
	'id': 1,
	'name': 'Stetson', 
	'Car': 'Scion'
	}

]

@app.route('/api', methods=['GET'])
def get_tasks():
		return jsonify({'output': output})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')