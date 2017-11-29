# Importing the module
from twython import Twython

#Setting these as variables will make them easier for future edits
app_key = "houCtAHQPOW6zFyvkQ9sEsj43"
app_secret = "NWatkb2pWOPzzqXkQKKyoVmZ6ZcqzeImlJEesYdTGA8Tx3sEg5"
oauth_token = "935926013741207559-FXcXzdYBtfSHH7yHTaXuz1lsn4pmPf4"
oauth_token_secret = "DrKbHPBz9WJSHSH20rtR9k4kGe8ySPly10Ud3Tqmli5Wa"

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

#The obligatory first status update to test
twitter.update_status(status="Hello world.")

status = [
    "Ello mate."
    "Waaazzzuuuuuup!"
    "Waz happenin homies?"
    "My day is poppin."
]

twitter.update_status(status=random.randint(0,4))
