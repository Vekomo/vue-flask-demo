CREATE SCHEMA bschema;

CREATE TABLE bschema.Technology_Master (
  technology_id SERIAL PRIMARY KEY,
  technology_name VARCHAR(50) NOT NULL,
  tech_dependant_tags VARCHAR(2000),
  stack_description VARCHAR(500)
);

CREATE TABLE bschema.OS_Tech_Master (
  OS_technology_name VARCHAR(50) PRIMARY KEY,
  technology_id INTEGER,
  OS_tech_dependent_tags VARCHAR(2000),
  OS_tech_description VARCHAR(500),
  CONSTRAINT fk_technology_id
    FOREIGN KEY(technology_id)
      REFERENCES bschema.Technology_Master(technology_id)
);

CREATE TABLE bschema.Data_Tech_Master (
  Data_technology_name VARCHAR(50) PRIMARY KEY,
  technology_id INTEGER,
  Data_tech_dependent_tags VARCHAR(2000),
  Data_tech_description VARCHAR(500),
  CONSTRAINT fk_technology_id
    FOREIGN KEY(technology_id)
      REFERENCES bschema.Technology_Master(technology_id)
);

CREATE TABLE bschema.App_Tech_Master (
  App_technology_name CHAR(50) PRIMARY KEY,
  technology_id INTEGER,
  App_tech_dependent_tags VARCHAR(2000),
  App_tech_description VARCHAR(500),
  CONSTRAINT fk_technology_id
    FOREIGN KEY(technology_id)
      REFERENCES bschema.Technology_Master(technology_id)
);
