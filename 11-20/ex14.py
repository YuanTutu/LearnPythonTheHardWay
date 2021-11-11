from sys import argv

script, user_name = argv
prompt = '> '

print(f"hi {user_name},i'm the {script} script")
print("i'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
you said {likes} about liking me.
you lives in {lives}
you have a {computer}
""")
