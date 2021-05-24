import instaloader

print (' _             _')
print ('(_) __ _ ____ (_) ___')
print ('| |/ _` |  _ \| |/ __|')
print ('| | (_| | |_) | | (__')
print ('|_|\__, | .__/|_|\___|')
print ('   |___/|_|')

ig = instaloader.Instaloader()
profile = input("Enter Instagram username:")
ig.download_profile(profile, profile_pic_only=True)
