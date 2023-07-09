import sys
import time
import random

import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/soham/Downloads"




# Event Hanlder Class

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
       print("file has been created:",event.src_path)
    def on_deleted(self, event):
        print("file has been deleted:",event.src_path)
    def on_modified(self, event):
        print ("file has been modified:", event.src_path)
    def on_moved(self, event):
        print ("file has been moved:", event.src_path)
# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    