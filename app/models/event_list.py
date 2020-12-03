from app.models.event import *


event_1 = Event("25-12-2020", "Christmas Market", "200", "Margit Island", "Budapest's famous Chrismtmas event")
event_2 = Event("31-12-2020", "Edinburgh's Hogmanay", "10,000", "The Old Town", "Scotland's annual orgy of drunkeness")

events_list = [event_1, event_2]

def add_new_event(event):
    events_list.append(event)