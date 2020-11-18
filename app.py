import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import psycopg2 as psycopg

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
'''
@app.route("/get_tech_master", methods=['GET'])
def get_tech_master():
    try:
        techs=Technology_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))

psycopg2
-create connection, requires db along with user/pass

-cursor, manip tables through cursor

-commit changes

-close connection

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
'''
@app.route("/tech-masters", methods=['GET'])
def get_tech_master_raw():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM "Technology_Master" """)
        records = cur.fetchall()
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    result = []
    for row in records:
        result.append({
        "technology_id" : row[0],
        "technology_name" : row[1],
        "tech_dependant_tags" : row[2],
        "stack_description":row[3]
        })
    conn.commit()
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})
    #return jsonify(result)

@app.route("/tech-masters", methods=['POST'])
def add_tech():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()

    post_data = request.get_json()
    technology_name=post_data.get('technology_name')
    tech_dependant_tags=post_data.get('tech_dependant_tags')
    stack_description=post_data.get('stack_description')
    try:
        cur.execute("""INSERT INTO
        "Technology_Master"(technology_name,tech_dependant_tags,stack_description)
        VALUES('"""+technology_name +"""','"""+tech_dependant_tags+"""','"""+stack_description + """'); """)
        cur.execute("""SELECT * FROM "Technology_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[0],
        "technology_name" : row[1],
        "tech_dependant_tags" : row[2],
        "stack_description":row[3]
        })
    conn.commit()
    conn.close()
    return jsonify({'status': 201, 'data': result, 'message': 'Success.'})

@app.route("/tech-masters", methods=['PUT'])
def update_tech_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()

    post_data = request.get_json()
    tech_id = post_data.get('technology_id')
    technology_name=post_data.get('technology_name')
    tech_dependant_tags=post_data.get('tech_dependant_tags')
    stack_description=post_data.get('stack_description')
    try:
        cur.execute("""UPDATE "Technology_Master"
                        SET technology_name = '""" + technology_name + """', """ +
                            """ tech_dependant_tags = '""" + tech_dependant_tags + """ ', """ +
                            """ stack_description = '""" + stack_description + """'""" +
                            """ WHERE technology_id = """ + str(tech_id) + """;""")

        cur.execute("""SELECT * FROM "Technology_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[0],
        "technology_name" : row[1],
        "tech_dependant_tags" : row[2],
        "stack_description":row[3]
        })

    conn.commit()
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})

@app.route("/tech-master-entries", methods=['PUT'])
def delete_tech_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()

    post_data = request.get_json()
    tech_id = post_data.get('technology_id')
    try:
        cur.execute("""DELETE  FROM "Technology_Master" WHERE technology_id = '""" + str(tech_id) + """';""")
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    cur.execute("""SELECT * FROM "Technology_Master" """)
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[0],
        "technology_name" : row[1],
        "tech_dependant_tags" : row[2],
        "stack_description":row[3]
        })

    conn.commit()
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})

# ||||||||||| OS_TECH_MASTER ||||||||||||||||||||||||||||||||||||||||||||||||||
@app.route("/os-masters", methods=['GET'])
def get_os_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM "OS_Tech_Master" """)
    except Exception as e:
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[1],
        "OS_technology_name" : row[0],
        "OS_tech_dependant_tags" : row[2],
        "OS_tech_description":row[3]
        })

    conn.commit()
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})

@app.route("/os-masters", methods=['POST'])
def add_os():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()

    post_data = request.get_json()
    technology_id=post_data.get('technology_id')
    OS_technology_name=post_data.get('OS_technology_name')
    OS_tech_dependant_tags=post_data.get('OS_tech_dependant_tags')
    OS_tech_description=post_data.get('OS_tech_description')
    try:
        cur.execute("""INSERT INTO
        "OS_Tech_Master"(technology_id,"OS_technology_name","OS_tech_dependant_tags","OS_tech_description")
        VALUES("""+ str(technology_id) + """,'""" + OS_technology_name +"""','"""+ OS_tech_dependant_tags +"""','"""+ OS_tech_description + """'); """)
        cur.execute("""SELECT * FROM "OS_Tech_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[1],
        "OS_technology_name" : row[0],
        "OS_tech_dependant_tags" : row[2],
        "OS_tech_description":row[3]
        })

    conn.commit()
    conn.close()
    return jsonify({'status': 201, 'data': result, 'message': 'Success.'})

@app.route("/os-masters", methods=['PUT'])
def update_os_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()

    post_data = request.get_json()
    OS_technology_name = post_data.get('OS_technology_name')
    OS_tech_dependant_tags=post_data.get('OS_tech_dependant_tags')
    OS_tech_description=post_data.get('OS_tech_description')
    technology_id=post_data.get('technology_id')
    New_OS_name = post_data.get('New_OS_name')
    try:
        cur.execute("""UPDATE "OS_Tech_Master"
                        SET "OS_technology_name" = '""" + New_OS_name + """', """ +
                            """ "OS_tech_dependant_tags" = '""" + OS_tech_dependant_tags + """ ', """ +
                            """ "OS_tech_description" = '""" + OS_tech_description + """', """ +
                            """ technology_id = '""" + str(technology_id) + """' """ +
                            """ WHERE "OS_technology_name" = '""" + OS_technology_name + """';""")

        cur.execute("""SELECT * FROM "OS_Tech_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[1],
        "OS_technology_name" : row[0],
        "OS_tech_dependant_tags" : row[2],
        "OS_tech_description":row[3]
        })

    conn.commit()
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})

@app.route("/os-master-entries", methods=['PUT'])
def delete_os_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()

    post_data = request.get_json()
    os_name = post_data.get('os_name')
    try:
        cur.execute("""DELETE  FROM "OS_Tech_Master" WHERE "OS_technology_name" = '""" + os_name + """';""")

        cur.execute("""SELECT * FROM "OS_Tech_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[1],
        "OS_technology_name" : row[0],
        "OS_tech_dependant_tags" : row[2],
        "OS_tech_description":row[3]
        })

    conn.commit()
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})



# ||||||||||| DATA_TECH_MASTER ||||||||||||||||||||||||||||||||||||||||||||||||
'''
@app.route("/get_data_master", methods=['GET'])
def get_data_master():
    try:
        techs=Data_Tech_Master.query.all()
        return  jsonify([e.serialize() for e in techs])
    except Exception as e:
	    return(str(e))
'''
@app.route("/data-masters", methods=['GET'])
def get_data_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM "Data_Tech_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[1],
        "Data_technology_name" : row[0],
        "Data_tech_dependant_tags" : row[2],
        "Data_tech_description":row[3]
        })
    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})

@app.route("/data-masters", methods=['POST'])
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
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})

    result=Data_Tech_Master.query.all()
    return jsonify({'status': 200, 'data': [e.serialize() for e in result], 'message': 'Success.'})

@app.route("/data-masters", methods=['PUT'])
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
        result=Data_Tech_Master.query.all()
        return jsonify({'status': 200, 'data': [e.serialize() for e in result], 'message': 'Success.'})
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
@app.route("/data-master-entries", methods=['PUT'])
def delete_data_master():
    post_data = request.get_json()
    data_name = post_data.get('data_name')
    techs=Data_Tech_Master.query.filter_by(Data_technology_name=data_name).first()
    try:
        db.session.delete(techs)
        db.session.commit()
        result=Data_Tech_Master.query.all()
        return jsonify({'status': 200, 'data': [e.serialize() for e in result], 'message': 'Success.'})
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})

# ||||||||||| APP_TECH_MASTER |||||||||||||||||||||||||||||||||||||||||||||||||
@app.route("/app-masters", methods=['GET'])
def get_app_master():
    conn = psycopg.connect("dbname=tech_db user=stylo")
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM "App_Tech_Master" """)
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})
    records = cur.fetchall()
    result = []
    for row in records:
        result.append({
        "technology_id" : row[1],
        "App_technology_name" : row[0],
        "App_tech_dependant_tags" : row[2],
        "App_tech_description":row[3]
        })

    conn.close()
    return jsonify({'status': 200, 'data': result, 'message': 'Success.'})

@app.route("/app-masters", methods=['POST'])
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
        result=App_Tech_Master.query.all()
        return jsonify({'status': 201, 'data': [e.serialize() for e in result], 'message': 'Success.'})
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})

@app.route("/app-masters", methods=['PUT'])
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
        result=App_Tech_Master.query.all()
        return jsonify({'status': 200, 'data': [e.serialize() for e in result], 'message': 'Success.'})
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})

@app.route("/app-master-entries", methods=['PUT'])
def delete_app_master():
    post_data = request.get_json()
    app_name = post_data.get('app_name')
    result=App_Tech_Master.query.filter_by(App_technology_name=app_name).first()
    try:
        db.session.delete(result)
        db.session.commit()
        result=App_Tech_Master.query.all()
        return jsonify({'status': 200, 'data': [e.serialize() for e in result], 'message': 'Success.'})
    except Exception as e:
        return jsonify({'status': 500, 'data': [], 'message': 'Failure.'})



if __name__ == '__main__':
    app.hello()
