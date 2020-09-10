from app import db




class Technology_Master(db.Model):
    __tablename__ = 'Technology_Master'

    technology_id = db.Column(db.Integer, primary_key=True)
    technology_name = db.Column(db.String(50), nullable=False)
    tech_dependant_tags = db.Column(db.String(2000))
    stack_description = db.Column(db.String(500))

    def serialize(self):
        return {
            'technology_id': self.technology_id,
            'technology_name': self.technology_name,
            'tech_dependant_tags': self.tech_dependant_tags,
            'stack_description':self.stack_description
        }

class OS_Tech_Master(db.Model):
    __tablename__ = 'OS_Tech_Master'

    OS_technology_name = db.Column(db.String(50), primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('Technology_Master.technology_id'))
    OS_tech_dependant_tags = db.Column(db.String(2000))
    OS_tech_description = db.Column(db.String(500))

    def serialize(self):
        return {
            'technology_id': self.technology_id,
            'OS_technology_name': self.OS_technology_name,
            'OS_tech_dependant_tags': self.OS_tech_dependant_tags,
            'OS_tech_description':self.OS_tech_description
        }

class Data_Tech_Master(db.Model):
    __tablename__ = 'Data_Tech_Master'

    Data_technology_name = db.Column(db.String(50), primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('Technology_Master.technology_id'))
    Data_tech_dependant_tags = db.Column(db.String(2000))
    Data_tech_description = db.Column(db.String(500))

    def serialize(self):
        return {
            'technology_id': self.technology_id,
            'Data_technology_name': self.Data_technology_name,
            'Data_tech_dependant_tags': self.Data_tech_dependant_tags,
            'Data_tech_description':self.Data_tech_description
        }

class App_Tech_Master(db.Model):
    __tablename__ = 'App_Tech_Master'

    App_technology_name = db.Column(db.String(50), primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('Technology_Master.technology_id'))
    App_tech_dependant_tags = db.Column(db.String(2000))
    App_tech_description = db.Column(db.String(500))

    def serialize(self):
        return {
            'technology_id': self.technology_id,
            'App_technology_name': self.App_technology_name,
            'App_tech_dependant_tags': self.App_tech_dependant_tags,
            'App_tech_description':self.App_tech_description
        }
