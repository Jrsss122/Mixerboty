from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

api_id = int(getenv("api_id", None))
api_hash = getenv("api_hash", None)
session = getenv("session", "BQFQUu4ASBsj4sp8OieDnX-CsWY3idaJQ_XnPCE-aWzyatWHGJXogEX3D0fELatfyVUMOPY01R58Eb9IrZxREMvkSjFw7XvpV-b1Ar5niZwuBIyVuQ5BgpywDwNqySacBEdK39L6gcF0M4RPkhsmGxuV83ZlAWorZng2CAWXlVVehE-Vfv-TSOaz_JJev9vQXPI1npREjq8N5edqgcI6000uEYnpkHa3Tr46m54GBhwmLG6YfNF5z3V_MPKq3HolhTQalpXsq-Rwhv_dNRcIM2TUm6nmThKb3XepmTkADRSKaHxAJoiJEX-UA6gwlscVcknDmmjR938HrOXj7yhCQe2SesvwkQAAAABvZLCFAA")
bot_token = getenv("bot_token", "7023999606:AAF4hfQDAAgv0-9-H0OWYtE9P2nC0tTuPIU")
db_name = getenv("db_name", None)
mongo_uri = getenv("mongo_uri", "mongodb+srv://muchi:muchi@cluster0.ebmld.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
def_bahasa = getenv("def_bahasa", "toxic")
log_pic = getenv("log_pic", "https://telegra.ph//file/43cec0ae0ded594b55247.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/Jrsss122/Mixerboty",
)
upstream_branch = getenv("upstream_branch", "tes")
git_token = getenv("git_token", None)
alive_pic = getenv("alive_pic", "https://telegra.ph//file/43cec0ae0ded594b55247.jpg")
log_channel = getenv("log_channel", "")
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)
