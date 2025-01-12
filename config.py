import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7057021367:AAHCu4Pvwi7VgxJhO1EgdhbzrydXnEhmxxk")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29565691"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e093998dbea2e7930d93a5ea14ba8cda")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6204800625"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://harsh03h:harsh03h@cluster0.5jf8f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "RESTRICTION_SAVE_BOT")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
