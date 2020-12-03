from app import app
from flask import render_template, request
from app.models.event_list import events_list, add_new_event
from app.models.event import *

@app.route('/')
def index():
    return render_template("index.html", title="Home", events_list=events_list)


@app.route("/add-event", methods=["POST"])
def add_event():
    event_name = request.form["name"]
    event_description = request.form["description"]
    event_venue = request.form["venue"]
    event_date = request.form["date"]
    event_guests = request.form["guests"]
    new_event = Event(event_name, event_description, event_venue, event_date, event_guests)
    add_new_event(new_event)
    return render_template("index.html",title="Home", events_list=events_list)