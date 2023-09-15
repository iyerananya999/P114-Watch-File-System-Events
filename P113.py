import time

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Oops, someone deleted {event.src_path}")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Someone moved {event.src_path} to {event.dest_path}")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()



