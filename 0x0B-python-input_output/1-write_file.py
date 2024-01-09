#!/usr/bin/python3
""" Modluel for file Reading"""

def write_file(filename="", text=""):
    """ function for writting to a file
    Args:
        filename (string): the name of file
        text (string): the text to write tio the file
    Exception:
        File not found exception
    Return (bool):Numbe rof character written
    """
    try
        with open(filename, "r", encoding="utf-8") as f:
            return (f.write(text))
    except FileNotFoundError as e:
        return ("File not found")
    except IOError as e:
        return (f"Error: {e}")
