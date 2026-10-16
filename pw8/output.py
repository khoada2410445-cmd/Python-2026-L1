import os
import gzip
import pickle
import threading

def compress_and_save(data, filename="students.dat"):
    """
    Background worker task to pickle and compress data.
    Runs silently to avoid breaking the curses UI.
    """
    try:
        with gzip.open(filename, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        pass

def save_data_background(data, filename="students.dat"):
    """
    Spawns and executes compress_and_save in a background thread.
    """
    thread = threading.Thread(
        target=compress_and_save,
        args=(data, filename),
        daemon=True
    )
    thread.start()
    return thread

def load_data(filename="students.dat"):
    """
    Decompresses and loads data from the binary pickle file.
    """
    if not os.path.exists(filename):
        return None

    try:
        with gzip.open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        return None