import time
import aux_funcs
from LevPasha.InstagramAPI import InstagramAPI

delay_seconds = 10

def printUsage():
	print("Usage: \n+ python main.py -u YOUR_USERNAME -p YOUR_PASSWORD -t USERNAME_TARGET")
	return
	
def main():
	try:
		args = aux_funcs.get_args()
		api  = InstagramAPI(args.user, args.password)
		api.login()
		user_id = aux_funcs.get_id(str(args.target))
		try:
			print ("Getting user feed. This may take a long time")
			photos_ids = api.getTotalUserFeed(user_id)
			print ("Done! \n\nLiking all photos")
			for p in photos_ids:
				api.like(p.get("id"))
				time.sleep( delay_seconds )
			print ("Done!")

		except:
			print ("Unable to get user feed. Maybe account is private?")

	except:
		printUsage()
			
if __name__ == "__main__":
    main()
