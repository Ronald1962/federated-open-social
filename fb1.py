#!usr/bin/env python
# Program to mine data from your own facebook account

import json
import facebook


def main():
        token = "EAAOlZAoTdGRkBAKc1UrqZBCEwFNHtDrZBy2ioZBV8G5qkgWI7JqbX3MfED9u9FOWNPHPFXbEmujzolmPZCKSc3kc800wZAfB15nqj9sb6JnlCjzwHYAvuRNW1yNZAoXbU1bZCnzNL3x1zVMsmGZB9fHtcytFvvJJZCUsNhlhbpgVbTRWBL4QZCzZBuZBqJmhgUTKNnR2UTx8nW6CxKzqAXF9elqKlNhUT0zbJjjdP1ct4ZBCKyJQZDZD"
        graph = facebook.GraphAPI(token)
        #fields = ['first_name', 'location{location}','email','link']
        profile = graph.get_object('me',fields='first_name,location,link,email')
        #return desired fields
        print(json.dumps(profile, indent=4))
        # Print friends (Werkt alleen voor vrienden die speciale toestemming gaven).
        friends = graph.get_object('me/friends')
        print(json.dumps(friends, indent=4))

if __name__ == '__main__':
        main()
