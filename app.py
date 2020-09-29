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

# ||||||||||| TECHNOLOGY_MASTER |||||||||||||||||||||||||||||||||||||||||||||||

@app.route("/get_tech_master", methods=['GET'])
def get_tech_master():
    try:
        techs=Technology_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/add_tech", methods=['POST'])
def add_tech():
    post_data = request.get_json()
    print(post_data)
    technology_name=post_data.get('technology_name')
    tech_dependant_tags=post_data.get('tech_dependant_tags')
    stack_description=post_data.get('stack_description')
    try:
        tech_master=Technology_Master(
            technology_name=technology_name,
            tech_dependant_tags=tech_dependant_tags,
            stack_description=stack_description
        )
        db.session.add(tech_master)
        db.session.commit()
        techs=Technology_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/update_tech", methods=['PUT'])
def update_tech_master():
    post_data = request.get_json()
    tech_id = post_data.get('technology_id')
    technology_name=post_data.get('technology_name')
    tech_dependant_tags=post_data.get('tech_dependant_tags')
    stack_description=post_data.get('stack_description')
    techs=Technology_Master.query.filter_by(technology_id=tech_id).first()
    try:
        techs.technology_name = technology_name
        techs.tech_dependant_tags = tech_dependant_tags
        techs.stack_description = stack_description
        db.session.commit()
        techs=Technology_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        return(str(e))

@app.route("/delete_tech", methods=['PUT'])
def delete_tech_master():
    post_data = request.get_json()
    tech_id = post_data.get('technology_id')
    techs=Technology_Master.query.filter_by(technology_id=tech_id).first()
    try:
        db.session.delete(techs)
        db.session.commit()
        techs=Technology_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        return jsonify({'status': 'fail'})
        return(str(e))

# ||||||||||| OS_TECH_MASTER ||||||||||||||||||||||||||||||||||||||||||||||||||

@app.route("/get_os_master", methods=['GET'])
def get_os_master():
    try:
        techs=OS_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/add_os", methods=['POST'])
def add_os():
    post_data = request.get_json()
    print(post_data)
    technology_id=post_data.get('technology_id')
    OS_technology_name=post_data.get('OS_technology_name')
    OS_tech_dependant_tags=post_data.get('OS_tech_dependant_tags')
    OS_tech_description=post_data.get('OS_tech_description')
    try:
        os_tech_master=OS_Tech_Master(
            technology_id=technology_id,
            OS_technology_name=OS_technology_name,
            OS_tech_dependant_tags=OS_tech_dependant_tags,
            OS_tech_description=OS_tech_description
        )
        db.session.add(os_tech_master)
        db.session.commit()
        techs=OS_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
        #return "OS added to OS_Tech_Master via add_os! OS technology_id={}".format(OS_Tech_Master.technology_id)
    except Exception as e:
        print(str(e))
        return(str(e))

@app.route("/update_os", methods=['PUT'])
def update_os_master():
    post_data = request.get_json()
    OS_technology_name = post_data.get('OS_technology_name')
    OS_tech_dependant_tags=post_data.get('OS_tech_dependant_tags')
    OS_tech_description=post_data.get('OS_tech_description')
    technology_id=post_data.get('technology_id')
    New_OS_name = post_data.get('New_OS_name')
    techs=OS_Tech_Master.query.filter_by(OS_technology_name=OS_technology_name).first()
    try:
        techs.technology_id = technology_id
        techs.OS_technology_name = New_OS_name
        techs.OS_tech_dependant_tags = OS_tech_dependant_tags
        techs.OS_tech_description = OS_tech_description
        db.session.commit()
        techs=OS_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        print(str(e))
        return(str(e))

@app.route("/delete_os", methods=['PUT'])
def delete_os_master():
    post_data = request.get_json()
    os_name = post_data.get('os_name')
    techs=OS_Tech_Master.query.filter_by(OS_technology_name=os_name).first()
    try:
        db.session.delete(techs)
        db.session.commit()
        techs=OS_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        return(str(e))


# ||||||||||| DATA_TECH_MASTER ||||||||||||||||||||||||||||||||||||||||||||||||

@app.route("/get_data_master", methods=['GET'])
def get_data_master():
    try:
        techs=Data_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/add_data", methods=['POST'])
def add_data():
    post_data = request.get_json()
    technology_id=post_data.get('technology_id')
    Data_technology_name=post_data.get('Data_technology_name')
    Data_tech_dependant_tags=post_data.get('Data_tech_dependant_tags')
    Data_tech_description=post_data.get('Data_tech_description')
    try:
        data_tech_master=Data_Tech_Master(
            technology_id=technology_id,
            Data_technology_name=Data_technology_name,
            Data_tech_dependant_tags=Data_tech_dependant_tags,
            Data_tech_description=Data_tech_description
        )
        db.session.add(data_tech_master)
        db.session.commit()
        techs=Data_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        print(str(e))
        return(str(e))

@app.route("/update_data", methods=['PUT'])
def update_data_master():
    post_data = request.get_json()
    Data_technology_name = post_data.get('Data_technology_name')
    New_Data_name = post_data.get('New_Data_technology_name')
    Data_tech_dependant_tags=post_data.get('Data_tech_dependant_tags')
    Data_tech_description=post_data.get('Data_tech_description')
    technology_id=post_data.get('technology_id')
    techs=Data_Tech_Master.query.filter_by(Data_technology_name=Data_technology_name).first()
    try:
        techs.technology_id = technology_id
        techs.Data_technology_name = New_Data_name
        techs.Data_tech_dependant_tags = Data_tech_dependant_tags
        techs.Data_tech_description = Data_tech_description
        db.session.commit()
        techs=Data_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        print(str(e))
        return(str(e))

@app.route("/delete_data", methods=['PUT'])
def delete_data_master():
    post_data = request.get_json()
    data_name = post_data.get('data_name')
    techs=Data_Tech_Master.query.filter_by(Data_technology_name=data_name).first()
    try:
        db.session.delete(techs)
        db.session.commit()
        techs=Data_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        return(str(e))

# ||||||||||| APP_TECH_MASTER |||||||||||||||||||||||||||||||||||||||||||||||||

@app.route("/get_app_master", methods=['GET'])
def get_app_master():
    try:
        techs=App_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

@app.route("/add_app", methods=['POST'])
def add_app():
    post_data = request.get_json()
    technology_id=post_data.get('technology_id')
    App_technology_name=post_data.get('App_technology_name')
    App_tech_dependant_tags=post_data.get('App_tech_dependant_tags')
    App_tech_description=post_data.get('App_tech_description')
    try:
        app_tech_master=App_Tech_Master(
            technology_id=technology_id,
            App_technology_name=App_technology_name,
            App_tech_dependant_tags=App_tech_dependant_tags,
            App_tech_description=App_tech_description
        )
        db.session.add(app_tech_master)
        db.session.commit()
        techs=App_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        print(str(e))
        return(str(e))

@app.route("/update_app", methods=['PUT'])
def update_app_master():
    post_data = request.get_json()
    App_technology_name = post_data.get('App_technology_name')
    New_App_name = post_data.get('New_App_name')
    App_tech_dependant_tags=post_data.get('App_tech_dependant_tags')
    App_tech_description=post_data.get('App_tech_description')
    technology_id=post_data.get('technology_id')
    techs=App_Tech_Master.query.filter_by(App_technology_name=App_technology_name).first()
    try:
        techs.technology_id = technology_id
        techs.App_technology_name = New_App_name
        techs.App_tech_dependant_tags = App_tech_dependant_tags
        techs.App_tech_description = App_tech_description
        db.session.commit()
        techs=App_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        print(str(e))
        return(str(e))

@app.route("/delete_app", methods=['PUT'])
def delete_app_master():
    post_data = request.get_json()
    app_name = post_data.get('app_name')
    techs=App_Tech_Master.query.filter_by(App_technology_name=app_name).first()
    try:
        db.session.delete(techs)
        db.session.commit()
        techs=App_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
        return(str(e))



if __name__ == '__main__':
    app.hello()
