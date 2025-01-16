import logging
import colorlog

# Create a logger
logger = logging.getLogger("CONTENT-GPT-LOGGER")
logger.setLevel(logging.INFO)
# Create a handler for file output
# file_handler = logging.FileHandler('logs/app.log')


# Create a handler for console output
console_handler = logging.StreamHandler()



# Create a formatter with color
formatter = colorlog.ColoredFormatter(
    # '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    '%(log_color)s%(asctime)s p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',

    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

# Attach formatter to handlers
# file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
# logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Test the logger