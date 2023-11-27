from datetime import datetime

def get_event_date(event):
    return datetime.strptime(event.date, '%Y-%m-%d %H:%M:%S')

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        machines.setdefault(event.machine, set())
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].discard(event.user)  
        else:
            print(f"Unknown event type: {event.type}")
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if users:
            print(f"{machine}: {', '.join(users)}")

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# Test Data
events = [
    Event('2023-01-22 08:54:07', 'login', 'workstation1.local', 'charlie'),
    Event('2023-01-15 04:25:50', 'logout', 'workstation2.local', 'alice'),
    Event('2023-01-11 03:33:32', 'logout', 'server1.local', 'charlie'),
    Event('2023-01-17 03:33:43', 'logout', 'server2.local', 'alice'),
    Event('2023-01-14 12:42:34', 'login', 'workstation2.local', 'edward'),
    Event('2023-01-11 01:22:27', 'login', 'workstation1.local', 'bob'),
    Event('2023-01-14 15:46:57', 'login', 'server1.local', 'bob'),
    Event('2023-01-04 15:45:07', 'logout', 'workstation1.local', 'charlie'),
    Event('2023-01-25 16:51:09', 'login', 'server2.local', 'alice'),
    Event('2023-01-17 03:16:25', 'login', 'workstation1.local', 'charlie'),
    Event('2023-01-13 08:51:19', 'logout', 'server2.local', 'diana'),
    Event('2023-01-08 01:28:09', 'login', 'workstation2.local', 'edward'),
    Event('2023-01-27 17:09:05', 'login', 'server2.local', 'edward'),
    Event('2023-01-17 18:32:05', 'logout', 'workstation1.local', 'charlie'),
    Event('2023-01-28 05:15:32', 'logout', 'server2.local', 'alice'),
    Event('2023-01-25 09:35:22', 'logout', 'workstation2.local', 'edward'),
    Event('2023-01-16 18:46:26', 'logout', 'server2.local', 'charlie'),
    Event('2023-01-17 11:45:21', 'logout', 'workstation1.local', 'charlie'),
    Event('2023-01-06 04:25:10', 'logout', 'workstation1.local', 'bob'),
    Event('2023-01-29 03:08:19', 'login', 'workstation1.local', 'diana'),
    Event('2023-01-28 00:58:55', 'logout', 'workstation2.local', 'alice'),
    Event('2023-01-02 05:59:04', 'login', 'server1.local', 'alice'),
    Event('2023-01-09 05:40:06', 'login', 'workstation2.local', 'alice'),
    Event('2023-01-23 11:31:45', 'logout', 'workstation2.local', 'charlie'),
    Event('2023-01-22 00:15:59', 'logout', 'workstation1.local', 'bob'),
    Event('2023-01-29 11:56:28', 'logout', 'server2.local', 'alice'),
    Event('2023-01-07 21:36:13', 'logout', 'server2.local', 'bob'),
    Event('2023-01-07 16:27:04', 'login', 'workstation2.local', 'charlie'),
    Event('2023-01-23 14:33:13', 'logout', 'workstation1.local', 'alice'),
    Event('2023-01-26 12:38:13', 'login', 'workstation2.local', 'edward'),
    Event('2023-01-21 20:32:40', 'logout', 'server1.local', 'alice'),
    Event('2023-01-03 09:17:34', 'logout', 'workstation1.local', 'bob'),
    Event('2023-01-15 00:43:35', 'login', 'server1.local', 'bob'),
    Event('2023-01-05 19:43:35', 'login', 'workstation1.local', 'alice'),
    Event('2023-01-15 15:49:40', 'logout', 'workstation2.local', 'charlie'),
    Event('2023-01-09 14:29:41', 'logout', 'workstation2.local', 'charlie'),
    Event('2023-01-21 15:08:05', 'login', 'server2.local', 'charlie'),
    Event('2023-01-28 02:29:26', 'logout', 'workstation1.local', 'charlie'),
    Event('2023-01-04 20:51:26', 'logout', 'server2.local', 'charlie'),
    Event('2023-01-28 18:39:40', 'logout', 'workstation1.local', 'alice'),
    Event('2023-01-18 15:04:59', 'login', 'server2.local', 'edward'),
    Event('2023-01-07 22:05:15', 'login', 'server1.local', 'bob'),
    Event('2023-01-06 06:01:04', 'logout', 'workstation1.local', 'edward'),
    Event('2023-01-25 01:17:36', 'login', 'workstation1.local', 'bob'),
    Event('2023-01-23 15:55:18', 'login', 'workstation2.local', 'diana'),
    Event('2023-01-15 05:09:12', 'logout', 'workstation1.local', 'bob'),
    Event('2023-01-25 02:09:41', 'logout', 'server1.local', 'alice'),
    Event('2023-01-09 17:01:37', 'logout', 'server2.local', 'charlie'),
    Event('2023-01-11 23:48:25', 'logout', 'server1.local', 'diana'),
    Event('2023-01-28 13:28:25', 'login', 'workstation1.local', 'diana')
]


users = current_users(events)
generate_report(users)
