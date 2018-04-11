# YouTube Audio Library API

A cumulative JSON file of all the tracks from YouTube's [music](https://www.youtube.com/audiolibrary/music) and [sound effects](https://www.youtube.com/audiolibrary/soundeffects) library.

## Data Structure
```
{
  "tracks": [
    {
      "vid": "62fa8c89f5afc555", // id to download .mp3 file 
                                 // (i.e. https://www.youtube.com/audiolibrary_download?vid=62fa8c89f5afc555)
      "len": 3.616, // duration in seconds
      "title": "18V Cordless Drill High Pitch",
      "popularity_percentile": 40,
      "category": "Tools",
      "keywords": [
          "series",
          "trigger pulls",
          "whirring",
          "drilling",
          "construction"
      ],
      "display_category": "Tools",
    }
  ...
  ]
}
```
