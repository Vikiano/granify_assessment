CREATE TABLE cats (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    favorite_food VARCHAR(255)
);

CREATE TABLE dogs (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    favorite_food VARCHAR(255)
);

INSERT INTO cats (name, age, favorite_food) VALUES ("Whiskers", 8, "tuna");
INSERT INTO cats (name, age, favorite_food) VALUES ("Garfield", 7, "lasagna");
INSERT INTO dogs (name, age, favorite_food) VALUES ("Fido", 3, "beef");
INSERT INTO dogs (name, age, favorite_food) VALUES ("Buddy", 4, "chicken");
