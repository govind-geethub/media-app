# Simple Social Media App

A lightweight social media web application built with Python, FastAPI, and Streamlit. It allows users to create accounts, authenticate securely, upload images and videos with captions, and explore posts shared by other users, with media stored on ImageKit and post metadata managed through SQLite.

## ✨ Features
* **User Authentication:** Supports user registration and login with JWT-based authentication.
* **Media Sharing:** Upload images and videos with captions to create posts.
* **Social Feed:** Displays posts with media, captions, author information, and timestamps.
* **Post Management:** Allows users to delete their own posts with backend ownership checks.
* **Cloud Media Storage:** Uses ImageKit to store uploaded media and serve it through URLs.
* **Database Migrations:** Uses Alembic to manage database schema changes while preserving existing records.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Backend:** Python, FastAPI
* **Authentication:** FastAPI Users, JWT
* **Database:** SQLite
* **ORM:** SQLAlchemy (async)
* **Media Storage:** ImageKit
* **Database Migrations:** Alembic
