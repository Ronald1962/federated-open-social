#!/usr/bin/env python
# See also: https://www.linux-magazine.com/Issues/2020/231/Social-Skills
import sys

import datetime
import cv2
from optparse import OptionParser
from mastodon import Mastodon


class post:
    def __init__(self, vUser, vPassword):

        self.mastodon = Mastodon(client_id=".secrets")

        self.mastodon.access_token = self.mastodon.log_in(
            username=vUser,
            password=vPassword,
            scopes=["read", "write"],
            to_file=".token",
        )

        self.post_date = None

    def send(self, vToot, vMedia, vVis):
        self.mastodon.status_post(
            vToot, media_ids=vMedia, scheduled_at=self.post_date, visibility=vVis
        )

    def add_Media(self, vMedia):
        return self.mastodon.media_post(vMedia)

    def set_date(self, vDate):
        try:
            self.post_date = datetime.datetime.strptime(vDate, "%b %d %Y %H:%M %Z")
        except:
            self.post_date = None

    def show_scheduled(self):
        print(self.mastodon.scheduled_statuses())


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "-a",
        "--action",
        help='"post", "schedule" or "list"',
        dest="vAction",
        default="list",
    )
    parser.add_option("-u", "--username", help="user's email", dest="vUser")
    parser.add_option("-p", "--password", help="user's password", dest="vPassword")
    parser.add_option("-t", "--toot", help="toot text", dest="vToot")
    parser.add_option(
        "-m",
        "--media",
        help='media ("cam" or image, video, etc.)',
        dest="vMedia",
        default=None,
    )
    parser.add_option(
        "-w",
        "--when",
        help='when to publish toot. Format: "mmm dd YYYY HH:MM Z"',
        dest="vWhen",
        default=None,
    )
    parser.add_option(
        "-v",
        "--visibility",
        help='"public", "unlisted", "private" or "direct"',
        dest="vVis",
        default="public",
    )

    (options, args) = parser.parse_args()

    p = post(options.vUser, options.vPassword)

    mmedia = options.vMedia
    if mmedia != None:
        if mmedia == "cam":
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite("pic.png", image)
            del camera
            mmedia = "pic.png"

        mmedia = p.add_Media(mmedia)

    if options.vAction == "post":
        p.send(options.vToot, mmedia, options.vVis)

    elif options.vAction == "schedule":
        p.set_date(options.vWhen)
        p.send(options.vToot, mmedia, options.vVis)

    else:
        p.show_scheduled()
