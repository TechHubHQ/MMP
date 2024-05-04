-- Table for storing categories of photos
CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Table for storing photos
CREATE TABLE Photos (
    photo_id INTEGER PRIMARY KEY,
    category_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    image_url TEXT NOT NULL,
    upload_date TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Table for storing users
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT,
    phone_number TEXT,
    address TEXT
);

-- Table for storing services offered by the app
CREATE TABLE Services (
    service_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing bookings made by users
CREATE TABLE Bookings (
    booking_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    service_id INTEGER,
    date_booked TEXT NOT NULL,
    date_of_service TEXT,
    location TEXT,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

-- Table for storing reviews/ratings for photos or services
CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    photo_id INTEGER,
    service_id INTEGER,
    rating INTEGER,
    comment TEXT,
    date_posted TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (photo_id) REFERENCES Photos(photo_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);
