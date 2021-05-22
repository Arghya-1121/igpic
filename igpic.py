import instaloader

ig = instaloader.Instaloader()
profile = input("Enter instagram username:")
ig.download_profile(profile, profile_pic_only=True)

