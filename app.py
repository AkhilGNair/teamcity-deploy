""" Initiate the application."""
import logging
import os
import time
import sched

version = 1.0
host = os.popen("hostname").read().strip()

def initialize():
    """ Configure application settings."""
    logging.basicConfig(
        format="[%(levelname)8s] %(asctime)s: %(message)s",
        level="DEBUG",
        datefmt="%d/%b/%Y:%H:%M:%S %z",
    )

    logging.info(f"Version - {version}")
    logging.info(f"I am a test application logging from {host}")

    return True

initialize()

s = sched.scheduler(time.time, time.sleep)

def log(scheduler, x):
    x = x + 1
    logging.info(f"Slept for {x * 5} seconds - {host}")
    s.enter(5, 1, log, (scheduler, x))

logging.info("Starting logger")
s.enter(5, 1, log, (s, 0))
s.run()

