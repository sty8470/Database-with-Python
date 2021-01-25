
CREATE TABLE Studio (
    studio_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Producer (
    producer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    net_worth DECIMAL(8, 3)
);

CREATE TABLE Genre (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Star (
    star_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    birth_year INT NOT NULL,
    CHECK (birth_year > 1800),
    UNIQUE(name, birth_year)
);

CREATE TABLE Movie (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    length INT,
    studio_id INT NOT NULL,
    producer_id INT NOT NULL,
    UNIQUE(title, year),
    CHECK(year > 1900),
    FOREIGN KEY (studio_id) REFERENCES Studio(studio_id) ON DELETE RESTRICT,
    FOREIGN KEY (producer_id) REFERENCES Producer(producer_id) ON DELETE RESTRICT
);

CREATE TABLE MovieGenre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id) ON DELETE RESTRICT,
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id) ON DELETE RESTRICT
);

CREATE TABLE MovieStar (
    movie_id INT,
    star_id INT,
    PRIMARY KEY (movie_id, star_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id) ON DELETE RESTRICT,
    FOREIGN KEY (star_id) REFERENCES Star(star_id) ON DELETE RESTRICT
);
