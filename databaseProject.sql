CREATE TABLE Type (
	id INT AUTO_INCREMENT,
    name VARCHAR(30) not null,
    typeName INT,
    
	PRIMARY KEY (id)
);

CREATE TABLE Pokemon (
	id INT AUTO_INCREMENT,
    number INT NOT NULL,
    name varchar(40) NOT NULL,
    typeId INT NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (typeId) REFERENCES Type(id) ON UPDATE CASCADE
);

CREATE TABLE Region (
	id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE,
    pokemonId INT NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (pokemonId) REFERENCES Pokemon(id) ON UPDATE CASCADE
);


CREATE TABLE Effective (
	id INT AUTO_INCREMENT,
    weak VARCHAR(30),
    strong VARCHAR (30),
    typeId INT NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (typeId) REFERENCES Type(id) ON UPDATE CASCADE
);

CREATE TABLE hasType(
	id INT AUTO_INCREMENT,
    typeId INT,
    pokemonId INT,
    
    PRIMARY KEY (id),
    FOREIGN KEY (typeId) REFERENCES Type(id),
    FOREIGN KEY (pokemonId) REFERENCES Pokemon(id)
);
CREATE TABLE MyTeam(
	teamId INT AUTO_INCREMENT ,
    pokemonId INT,
    
    PRIMARY KEY(teamId)
);
SELECT * FROM Pokemon;
SELECT * FROM Region;
SELECT * FROM Type;
SELECT * FROM MyTeam;