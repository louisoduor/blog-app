from datetime import datetime, date
from typing import List
from enum import Enum

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sort(Enum):
    NEWEST = "newest"
    OLDEST = "oldest"

class TagsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_tags = db.Column(db.Integer)
    tags = db.Column(db.ARRAY(db.String))

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    Access_Token = db.Column(db.String)

class General(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)

class HelpMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    help = db.Column(db.String)

class BlogModel(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    thumbnail = db.Column(db.String)
    content = db.Column(db.String)
    createdon = db.Column(db.DateTime, default=datetime.now)
    tag = db.Column(db.String)
    name = db.Column(db.String)
    authorid = db.Column(db.String)

class BlogData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Total_Blogs = db.Column(db.Integer)
    blogs = db.relationship('BlogModel', backref='blog_data', lazy=True)

class RegisterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    isverified = db.Column(db.Boolean, default=False)
    createdon = db.Column(db.Date, default=date.today)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    dob = db.Column(db.Date)
    profileurl = db.Column(db.String)

class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    isverified = db.Column(db.Boolean, default=False)
    createdon = db.Column(db.Date, default=date.today)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    dob = db.Column(db.Date)
    profileurl = db.Column(db.String)

class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    isverified = db.Column(db.Boolean, default=False)
    createdon = db.Column(db.Date, default=date.today)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    dob = db.Column(db.Date)
    profileurl = db.Column(db.String)

class AuthorList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    authors = db.relationship('AuthorModel', backref='author_list', lazy=True)

class AuthorProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.relationship('ProfileModel', uselist=False, backref='author_profile')
    blogs = db.relationship('BlogData', backref='author_profile', lazy=True)
