class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated
def create_blog(user):
    print(f"{user.name} has a new post")

new_user = User("kester")
new_user.is_logged_in = True
create_blog(new_user)