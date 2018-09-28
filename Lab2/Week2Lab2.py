from flask import Flask, request ,jsonify
from flask_pymongo import PyMongo
import datetime

AUTHENTICATION_STATE=0



app = Flask(__name__)
app.config['MONGO_DBNAME']='restfuldb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restfuldb'
mongo = PyMongo(app)


# student = mongo.db.students.insert({"name":"Peter",
# 				"studentId":"1005074"})


@app.route('/student', methods = ['GET'])
def one_of_student():
	try:
		data=request.get_json()
		name=data['name']
		student = mongo.db.students
		s = student.find_one({'name' : name})
		if s:
			output = {'name':s['name'],'studentId':s['studentId']}
		else:
			output = "No Such Student with Json"
	except:
		data=request.data
		name=data.decode("utf-8") 
		student = mongo.db.students
		s = student.find_one({'name' : name})
		if s:
			output = {'name':s['name'],'studentId':s['studentId']}
		else:
			output = "No Such Student with plain"
	return jsonify({'result': output})


@app.route('/admin' ,methods = ['GET'])
def get_all_students():
	if AUTHENTICATION_STATE ==1:
		student = mongo.db.students
		output = []
		for s in student.find():
			output.append({'name':s['name'],'studentId':s['studentId']})
		return jsonify({'result':output})
	else: return jsonify({'Authentication': 'Failed'})


@app.route('/admin', methods = ['POST'])
def add_student():
	if AUTHENTICATION_STATE ==1:
		student = mongo.db.students
		name = request.json['name']
		studentId = request.json['studentId']
		student_entity = student.insert({'name': name, 'studentId':studentId})
		new_student = student.find_one({'_id' : student_entity})
		output = {'name':new_student['name'],'studentId':new_student['studentId']}
		return jsonify({'result':output})
	else: return jsonify({'Authentication': 'Failed'})


@app.route('/admin/<path:name>' , methods = ['DELETE'])
def delete_student(name):
	if AUTHENTICATION_STATE ==1:
		student = mongo.db.students
		s = student.find_one({'name' : name})
		if s:
			output = name +" removed from database"
			student.remove({'name':s['name'],'studentId':s['studentId']})
		else:
			output = "No Such Student"
		return jsonify({'result': output})
	else: return jsonify({'Authentication': 'Failed'})


@app.route('/admin' , methods = ['DELETE'])
def delete_All():
	if AUTHENTICATION_STATE ==1:
		count = mongo.db.students.count()
		mongo.db.students.delete_many({})
		output =  ("{0}. entries deleted.".format(count))
		return jsonify({'result':output})
	else: return jsonify({'Authentication': 'Failed'})


@app.route('/login' , methods = ['POST'])
def authenticate():
	global AUTHENTICATION_STATE
	username = request.json['username']
	password = request.json['password']
	if username == "iamfast"and password == "checkmeoff":
		output = ("{0}. Welcome Back!.".format(username))
		AUTHENTICATION_STATE=1
	else:
		output = "failed to login!"
	return jsonify({username:output})

@app.route('/admin' , methods = ['PUT'])
def alterationId():
	if AUTHENTICATION_STATE ==1:
		student = mongo.db.students
		data = request.get_json()
		name = data['name']
		studentId = data['studentId']
		s = student.find_one({'name' : name})
		if s:
			output = name +" modified"
			student.update({'name': name}, {'$set':{'studentId': studentId}})
		else:
			output = "No Such Student"
		return jsonify({'result': output})
	else: return jsonify({'Authentication': 'Failed'})
	

@app.route('/student', methods =['NOTICE'])
def notice():
	return jsonify({'about':"This is the admin database for student and their assigned student ID, you can check your assigned student ID here",'Instruction':'You can GET your student ID by GET request with your studentId'})


if __name__ == '__main__':
	app.run(debug = True)
