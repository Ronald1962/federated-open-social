#!/usr/bin/env python

from mastodon import Mastodon

Mastodon.create_app(
     "posttoots",
     api_base_url = "https://mastodon.nl",
     scopes=["read", "write"],
     to_file = ".secrets"
)

mastodon = Mastodon(client_id = ".secrets")

print ("Mastodon version: " + mastodon.retrieve_mastodon_version())
