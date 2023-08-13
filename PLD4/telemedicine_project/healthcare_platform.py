#!/usr/bin/python3

from datetime import datetime
from telemedicine_app.telemedicine_classes import TelemedicinePlatform  # Import the TelemedicinePlatform class

if __name__ == "__main__":
    platform = TelemedicinePlatform()
    platform.run()
