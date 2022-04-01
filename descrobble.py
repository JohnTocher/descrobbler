""" Empty python script -

    Bases on sample from pylast:
    https://github.com/pylast/pylast

    installed with:

"""

import argparse
import datetime
from pathlib import Path
from fileinput import filename
import pylast

from mylast import lastfm_network
from mylast import lastfm_username
from mylast import track_and_timestamp

OUTPUT_PATH = "C:/Users/John/Sync/HomeSyn/Media/Podcasts/Scrobbles"

def generate_timestamp(time_to_use, stamp_type="default"):
    """ Genrate a text timestamp """

    new_stamp = time_to_use.strftime("%Y%m%d-%H%M%S")

    return new_stamp

def show_last_played(user_args, tracks_to_play=20, save_to_file=False, save_path=""):
    """ Print the last n played tracks to the console
    """

    print(user_args.username + " last played:")
    try:
        recent_tracks = get_recent_tracks(user_args.username, tracks_to_play)
    except pylast.WSError as e:
        print("Error: " + str(e))
    
    if save_to_file:
        if Path(save_path).is_dir:
            file_path = Path(save_path)
        else:
            file_path = Path("output/")
        #//print(f"Output path is: {file_path}")

        time_now = datetime.datetime.now()
        time_stamp = generate_timestamp(time_now, "default")
        line_count = 0
        file_name= file_path / f"{time_stamp}_scrobbles.csv"

        with open(file_name,"wb") as output_file:
            for each_track in recent_tracks:
                track_name = f"{each_track.track}".encode("utf-8","replace").decode("utf-8")
                clean_name = track_name.replace(",", "_")
                this_line  = f"{each_track.playback_date},{clean_name}\n"
                output_file.write(this_line.encode("utf-8"))
                line_count += 1
        
        print(f"Wrote {line_count} lines to file: {file_name}")


def get_recent_tracks(username, number):
    recent_tracks = lastfm_network.get_user(username).get_recent_tracks(limit=number)
    for i, track in enumerate(recent_tracks):
        printable = track_and_timestamp(track)
        print(str(i + 1) + " " + printable)
    return recent_tracks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Show 20 last played tracks",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-u", "--username", help="Last.fm username")
    parser.add_argument(
        "-n",
        "--number",
        default=20,
        type=int,
        help="Number of tracks to show (when no artist given)",
    )
    args = parser.parse_args()

    if not args.username:
        args.username = lastfm_username
    show_last_played(args, tracks_to_play=200, save_to_file=True, save_path=OUTPUT_PATH)
else:
    print("Imported elsewehere")
