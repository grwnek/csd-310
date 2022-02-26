
-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('6875 Castlebrook Dr. Franklin, OH 45005');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Wizard of Oz', 'L. Frank Baum', 'A fantasy novel published in 1900');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald', 'An adventure novel published in 1925');

INSERT INTO book(book_name, author, details)
    VALUES('Frankenstein', 'Mary Shelley', 'A horror fiction novel published in 1818');

INSERT INTO book(book_name, author, details)
    VALUES('The Catcher in the Rye', 'E. Michael Mitchell', 'A fantasy novel published in 1951');

INSERT INTO book(book_name, author, details)
    VALUES('Crime and Punishment', 'Fyodor Dostoevsky', 'A crime fiction novel published in 1866');

INSERT INTO book(book_name, author, details)
    VALUES('Animal Farm', 'George Orwell', 'A political satire novel published in 1945');

INSERT INTO book(book_name, author, details)
    VALUES('Don Quixote', 'Miguel de Cervantes', "A fiction novel published in 1605");

INSERT INTO book(book_name, author, details)
    VALUES('Great Expectations', 'Charles Dickens', 'A fiction novel published in 1861');

INSERT INTO book(book_name, author, details)
    VALUES('To Kill a Mockingbird', 'Harper Lee', 'A Southern Gothic novel published in 1960');
/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Harry', 'Potter');

INSERT INTO user(first_name, last_name)
    VALUES('Hermione', 'Granger');

INSERT INTO user(first_name, last_name)
    VALUES('Ron', 'Weasley');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harry'), 
        (SELECT book_id FROM book WHERE book_name = 'The Great Gatsby')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Hermione'),
        (SELECT book_id FROM book WHERE book_name = 'The Wizard of Oz')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Ron'),
        (SELECT book_id FROM book WHERE book_name = 'Frankenstein')
    );