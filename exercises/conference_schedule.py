# This program knows about the schedule for a conference that runs over the
# course of a day, with sessions in different tracks in different rooms.  Given
# a room and a time, it can tell you which session starts at that time.
#
# Usage:
#
# $ python conference_schedule.py [room] [time]
#
# For instance:
#
# $ python conference_schedule.py "Main Hall" 13:30
# 

import sys

SCHEDULE = {
    'Main Hall': {
        '10:00': 'Django REST framework',
        '11:00': 'Lessons learned from PHP',
        '12:00': "Tech interviews that don't suck",
        '14:00': 'Taking control of your Bluetooth devices',
        '15:00': "Fast Python? Don't Bother!",
        '16:00': 'Test-Driven Data Analysis',
    },
    'Seminar Room': {
        '10:00': 'Python in my Science Classroom',
        '11:00': 'My journey from wxPython tp PyQt',
        '12:00': 'Easy solutions to hard problems',
        '14:00': 'Taking control of your Bluetooth devices',
        '15:00': "Euler's Key to Cryptography",
        '16:00': 'Build your Microservices with ZeroMQ',
    },
    'Assembly Hall': {
        '10:00': 'Distributed systems from scratch',
        '11:00': 'Python in Medicine: ventilator data',
        '12:00': 'Neurodiversity in Technology',
        '14:00': 'Chat bots: What is AI?',
        '15:00': 'Pygame Zero',
        '16:00': 'The state of PyPy',
    },
}

# print('There are talks scheduled in {} rooms'.format(len(schedule)))

# TODO:
# * Implement the program as described in the comments at the top of the file.
CONFERENCE_START = '10:00'
CONFERENCE_END = '17:00'

def main():
    print(get_conference_information())

def get_conference_information():
    parsed = parser()
    if len(parsed) == 2:
        room, time = parsed
        return get_session(room, time)
    elif len(parsed) == 1:
        talk = parsed[0]
        return get_room_and_time(talk)
    
    return parsed

def round_down_time(time):
    hour, _ = time.split(":")
    return f"{hour}:00"

def parser():
    if len(sys.argv) == 2:
        session_title = sys.argv[1]
        return (session_title,)
    elif len(sys.argv) == 3:
        room = sys.argv[1]
        time = sys.argv[2]
        return room, time
    else:
        return "Usage: \n\npython conference_schedule.py '<room>' '<time>' \nor \npython conference_schedule.py '<title of session>'"
    

def get_session(room_arg, time_arg):
    DEFAULT_SESSION = ""

    time_to_hour = round_down_time(time_arg)

    if time_to_hour == "13:00":
        return f"It's break time"

    if not CONFERENCE_START <= time_arg < CONFERENCE_END:
        return "Please enter a valid time. Conference runs from 10:00 - 16:00"
    
    current_session = SCHEDULE.get(room_arg, {}).get(time_to_hour, DEFAULT_SESSION)
    if current_session == DEFAULT_SESSION:
        return "Enter a valid room name"
    else:
        return f"The current session is '{current_session}'"

def get_room_and_time(talk_arg):
    for room, schedule in SCHEDULE.items():
        for time, talk in schedule.items():
            if talk_arg in talk:
                return f"'{talk}' is happening at {time} in {room}"
    return f"'{talk_arg}' not found"
    

if __name__ == "__main__":
    main()
    



# TODO (extra):
# * Change the program so that that it can tell you what session is running in
#   a room at a given time, even if a session doesn't start at that time.
# * Change the program so that if called with a single argument, the title of a
#   session, it displays the room and the time of the session.
