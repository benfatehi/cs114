# Importing the module
import random
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

status = [
    "Revenge is an act of passion and Vengeance is an act of justice.",
    "The ultimate ignorance is the rejection of something you know nothing about.",
    "Even if the whole world is telling you to move, it is your duty to plant yourself like a tree, look them in the eye and say, 'No, you move.'",
    "All toasters toast toast.",
    "Never be bullied into silence. Never allow yourself to be made a victim. Accept no one's definition of your life; define yourself. -Harvey Fisher",
    "To the world, you might just be one person, but to one person, you might just be the world.",
    "Whoever kills an innocent life it is as if they have killed all of humanity. -Surat Al-Ma'idah 5:32",
    "We tend to come out of the oven fully cooked.",
    "All men have limits. They learn what their limits are and choose not to exceed them. I ignore mine. -Batman",
    "We stopped checking for monsters under our bed when we realized they were inside of us. -The Joker",
    "Stereotypes are devices for saving a biased person the trouble of learning."
]
#print (status[random.randint(0,10)])
twitter.update_status(status=status[random.randint(0,10)])
