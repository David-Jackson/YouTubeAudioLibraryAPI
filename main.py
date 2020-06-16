"""
This file processes HAR files saved from
https://www.youtube.com/audiolibrary/music and
https://www.youtube.com/audiolibrary/soundeffects
and outputs a JSON file for each with the track information

To use this script, download your desired HAR files,
place them in the same directory as this script,
and change the har_filenames variable below to match the downloaded filename(s)
"""

import json

har_filenames = ["youtube_sound_library.har", "youtube_music_library.har"]

for filename in har_filenames:
    print(filename, end='')
    har = json.load(open(filename, encoding="utf8"))
    data = json.loads("{\"tracks\": []}")

    for entry in har["log"]["entries"]:
        if "audioswap_ajax?action_get_tracks" in entry["request"]["url"]:
            j = json.loads(entry["response"]["content"]["text"])
            data["tracks"] += j["tracks"]

    output_filename = filename.split(".")[0] + ".json"
    with open(output_filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    print(" -> " + output_filename)
