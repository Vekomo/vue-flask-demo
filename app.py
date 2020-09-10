import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, resources={r'/*': {'origins': '*'}})

from models import*

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add_tech")
def add_tech():
    technology_name=request.args.get('technology_name')
    tech_dependant_tags=request.args.get('tech_dependant_tags')
    stack_description=request.args.get('stack_description')
    try:
        tech_master=Technology_Master(
            technology_name=technology_name,
            tech_dependant_tags=tech_dependant_tags,
            stack_description=stack_description
        )
        db.session.add(tech_master)
        db.session.commit()
        return "Tech added to technology master via add_tech! tech technology_id={}".format(tech_master.technology_id)
    except Exception as e:
	    return(str(e))

@app.route("/add_os")
def add_os():
    OS_technology_name=request.args.get('OS_technology_name')
    OS_tech_dependant_tags=request.args.get('OS_tech_dependant_tags')
    OS_tech_description=request.args.get('OS_tech_description')
    try:
        os_tech_master=OS_Tech_Master(
            OS_technology_name=OS_technology_name,
            OS_tech_dependant_tags=OS_tech_dependant_tags,
            OS_tech_description=OS_tech_description
        )
        db.session.add(os_tech_master)
        db.session.commit()
        return "OS added to OS_Tech_Master via add_os! OS technology_id={}".format(OS_Tech_Master.technology_id)
    except Exception as e:
	    return(str(e))

@app.route("/add_data")
def add_data():
    Data_technology_name=request.args.get('Data_technology_name')
    Data_tech_dependant_tags=request.args.get('Data_tech_dependant_tags')
    Data_tech_description=request.args.get('Data_tech_description')
    try:
        data_tech_master=Data_Tech_Master(
            Data_technology_name=Data_technology_name,
            Data_tech_dependant_tags=Data_tech_dependant_tags,
            Data_tech_description=Data_tech_description
        )
        db.session.add(data_tech_master)
        db.session.commit()
        return "Data added to Data_Tech_Master via add_data! Data technology_id={}".format(Data_Tech_Master.technology_id)
    except Exception as e:
	    return(str(e))

@app.route("/add_app")
def add_app():
    App_technology_name=request.args.get('App_technology_name')
    App_tech_dependant_tags=request.args.get('App_tech_dependant_tags')
    App_tech_description=request.args.get('App_tech_description')
    try:
        app_tech_master=App_Tech_Master(
            App_technology_name=App_technology_name,
            App_tech_dependant_tags=App_tech_dependant_tags,
            App_tech_description=App_tech_description
        )
        db.session.add(app_tech_master)
        db.session.commit()
        return "App added to App_Tech_Master via add_app! App technology_id={}".format(App_Tech_Master.technology_id)
    except Exception as e:
	    return(str(e))
@app.route("/getall")
def get_all():
    try:
        techs=Technology_Master.query.all()
        techs+=OS_Tech_Master.query.all()
        techs+=Data_Tech_Master.query.all()
        techs+=App_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/get_tech_master", methods=['GET'])
def get_tech_master():
    try:
        techs=Technology_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/get_os_master", methods=['GET'])
def get_os_master():
    try:
        techs=OS_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))
@app.route("/get_data_master", methods=['GET'])
def get_data_master():
    try:
        techs=Data_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))
@app.route("/get_app_master", methods=['GET'])
def get_app_master():
    try:
        techs=App_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.hello()
