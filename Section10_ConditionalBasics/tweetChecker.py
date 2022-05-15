tweetLength = len(input("enter your tweet:"))

if tweetLength <= 140:
    print(f"That {tweetLength} chars tweet will work!")
else:
    print(f"Your {tweetLength} tweet is {tweetLength - 140} chars too long")