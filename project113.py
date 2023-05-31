import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

source = "C:/Users/Administrator/Downloads"
destination = "C:/Users/Administrator/Desktop"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey,{event.src.path} has been created!")

    def on_deleted(self,event):
        print(f"Oops! Someone deleted{event.src.path} !")

    def on_modified(self,event):
        print(f"Hey there!, {event.src.path} has been modified")    

    def on_moved(self,event):
        print(f"Someone moved {event.src.path} to {event.dest.path}")

    
                    # Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()